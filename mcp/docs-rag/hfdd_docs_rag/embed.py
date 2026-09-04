from __future__ import annotations

import hashlib
import os
import sys
from typing import Protocol

import numpy as np

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
HASH_DIM = 64
DEFAULT_THREADS = 4
DEFAULT_BATCH = 32

# Set before onnxruntime loads; too many threads thrashes a first index.
os.environ.setdefault("OMP_NUM_THREADS", str(DEFAULT_THREADS))
os.environ.setdefault("ORT_NUM_THREADS", str(DEFAULT_THREADS))


class Embedder(Protocol):
    dim: int

    def embed(self, texts: list[str]) -> np.ndarray: ...


class HashEmbedder:
    """Deterministic bag-of-tokens vectors. For tests, not production search."""

    def __init__(self, dim: int = HASH_DIM) -> None:
        self.dim = dim

    def embed(self, texts: list[str]) -> np.ndarray:
        from hfdd_docs_rag.tokenize import tokenize

        matrix = np.zeros((len(texts), self.dim), dtype=np.float32)
        for i, text in enumerate(texts):
            for token in tokenize(text):
                digest = hashlib.sha256(token.encode("utf-8")).digest()
                index = int.from_bytes(digest[:4], "little") % self.dim
                matrix[i, index] += 1.0
            norm = np.linalg.norm(matrix[i])
            if norm > 0:
                matrix[i] /= norm
        return matrix


class FastEmbedder:
    def __init__(self, model_name: str = DEFAULT_MODEL) -> None:
        from fastembed import TextEmbedding

        self._model = TextEmbedding(model_name=model_name, threads=DEFAULT_THREADS)
        self.dim = int(self._model.embedding_size)
        self.batch_size = DEFAULT_BATCH

    def embed(self, texts: list[str]) -> np.ndarray:
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        vectors: list = []
        total = len(texts)
        for start in range(0, total, self.batch_size):
            batch = texts[start : start + self.batch_size]
            vectors.extend(self._model.embed(batch))
            done = min(start + self.batch_size, total)
            print(f"embed {done}/{total}", file=sys.stderr, flush=True)
        return np.asarray(vectors, dtype=np.float32)


def make_embedder() -> Embedder:
    kind = os.environ.get("HFDD_EMBEDDER", "fastembed")
    if kind == "fastembed":
        return FastEmbedder()
    if kind == "hash":
        return HashEmbedder()
    raise ValueError(f"unknown HFDD_EMBEDDER={kind!r} (use fastembed or hash)")
