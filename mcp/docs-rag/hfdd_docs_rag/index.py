from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from hfdd_docs_rag.corpus import Chunk, chunk_file, file_sha256, iter_corpus_files
from hfdd_docs_rag.embed import Embedder
from hfdd_docs_rag.paths import CHUNKS_NAME, MANIFEST_NAME, VECTORS_NAME, index_dir


@dataclass
class Index:
    root: Path
    chunks: list[Chunk]
    vectors: np.ndarray
    files: dict[str, str]

    @property
    def dim(self) -> int:
        if self.vectors.size == 0:
            return 0
        return int(self.vectors.shape[1])


def load_index(root: Path) -> Index | None:
    store = index_dir(root)
    manifest_path = store / MANIFEST_NAME
    chunks_path = store / CHUNKS_NAME
    vectors_path = store / VECTORS_NAME
    if not (manifest_path.is_file() and chunks_path.is_file() and vectors_path.is_file()):
        return None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    raw_chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
    chunks = [Chunk.from_dict(item) for item in raw_chunks]
    vectors = np.load(vectors_path)
    if vectors.shape[0] != len(chunks):
        raise RuntimeError(
            f"index broken under {store}: {vectors.shape[0]} vectors vs {len(chunks)} chunks"
        )
    return Index(
        root=root,
        chunks=chunks,
        vectors=vectors,
        files=manifest.get("files", {}),
    )


def save_index(index: Index) -> Path:
    store = index_dir(index.root)
    store.mkdir(parents=True, exist_ok=True)
    manifest = {
        "files": index.files,
        "chunk_count": len(index.chunks),
        "dim": index.dim,
    }
    (store / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (store / CHUNKS_NAME).write_text(
        json.dumps([chunk.to_dict() for chunk in index.chunks], ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    np.save(store / VECTORS_NAME, index.vectors)
    return store


def build_index(root: Path, embedder: Embedder) -> Index:
    chunks: list[Chunk] = []
    files: dict[str, str] = {}
    for path in iter_corpus_files(root):
        file_chunks = chunk_file(root, path)
        rel = path.relative_to(root).as_posix()
        files[rel] = file_sha256(path)
        chunks.extend(file_chunks)
    vectors = _embed_chunks(embedder, chunks)
    index = Index(root=root, chunks=chunks, vectors=vectors, files=files)
    save_index(index)
    return index


def ensure_index(root: Path, embedder: Embedder, force: bool = False) -> tuple[Index, str]:
    if force:
        return build_index(root, embedder), "full rebuild"

    current = load_index(root)
    wanted = {path.relative_to(root).as_posix(): file_sha256(path) for path in iter_corpus_files(root)}
    if current is None:
        return build_index(root, embedder), "created"
    if current.files == wanted and current.vectors.shape[0] == len(current.chunks):
        return current, "already up to date"
    return _incremental(root, embedder, current, wanted), "incremental update"


def _incremental(
    root: Path,
    embedder: Embedder,
    current: Index,
    wanted: dict[str, str],
) -> Index:
    keep_chunks: list[Chunk] = []
    keep_vectors: list[np.ndarray] = []
    for chunk, vector in zip(current.chunks, current.vectors, strict=True):
        if current.files.get(chunk.path) == wanted.get(chunk.path):
            keep_chunks.append(chunk)
            keep_vectors.append(vector)

    new_chunks: list[Chunk] = []
    for rel, digest in wanted.items():
        if current.files.get(rel) == digest:
            continue
        new_chunks.extend(chunk_file(root, root / rel))

    if keep_vectors:
        base = np.stack(keep_vectors, axis=0)
    else:
        base = np.zeros((0, embedder.dim), dtype=np.float32)
    added = _embed_chunks(embedder, new_chunks)
    if added.size and base.size and added.shape[1] != base.shape[1]:
        raise RuntimeError(
            f"embedder dim {added.shape[1]} does not match index dim {base.shape[1]}; "
            "reindex with force=true"
        )
    if added.size == 0:
        vectors = base
    elif base.size == 0:
        vectors = added
    else:
        vectors = np.concatenate([base, added], axis=0)

    index = Index(
        root=root,
        chunks=keep_chunks + new_chunks,
        vectors=vectors,
        files=wanted,
    )
    save_index(index)
    return index


def _embed_chunks(embedder: Embedder, chunks: list[Chunk]) -> np.ndarray:
    if not chunks:
        return np.zeros((0, embedder.dim), dtype=np.float32)
    texts = [f"{chunk.heading}\n{chunk.text}" for chunk in chunks]
    return embedder.embed(texts)
