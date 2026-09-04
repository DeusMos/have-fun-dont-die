from __future__ import annotations

from pathlib import Path

from hfdd_docs_rag.corpus import Kind, file_sha256, iter_corpus_files
from hfdd_docs_rag.embed import Embedder, make_embedder
from hfdd_docs_rag.format import format_hits, format_reindex, format_status
from hfdd_docs_rag.index import ensure_index, load_index
from hfdd_docs_rag.paths import find_repo_root
from hfdd_docs_rag.search import hybrid_search


class RagService:
    def __init__(self, root: Path | None = None, embedder: Embedder | None = None) -> None:
        self.root = root or find_repo_root()
        self._embedder = embedder

    @property
    def embedder(self) -> Embedder:
        if self._embedder is None:
            self._embedder = make_embedder()
        return self._embedder

    def search(
        self,
        query: str,
        k: int = 8,
        kind: str = "all",
        area: str = "",
        mark: str = "",
    ) -> str:
        if not query.strip():
            raise ValueError("query is empty")
        if k < 1:
            raise ValueError("k must be >= 1")
        index, _status = ensure_index(self.root, self.embedder)
        query_vector = self.embedder.embed([query])[0]
        hits = hybrid_search(
            query=query,
            chunks=index.chunks,
            vectors=index.vectors,
            query_vector=query_vector,
            k=k,
            kind=_parse_kind_filter(kind),
            area=area.strip() or None,
            mark=mark.strip() or None,
        )
        return format_hits(hits)

    def reindex(self, force: bool = False) -> str:
        index, message = ensure_index(self.root, self.embedder, force=force)
        return format_reindex(message, index.chunks, index.dim)

    def status(self) -> str:
        wanted = {
            path.relative_to(self.root).as_posix(): file_sha256(path)
            for path in iter_corpus_files(self.root)
        }
        current = load_index(self.root)
        if current is None:
            return format_status(
                root=str(self.root),
                file_count=0,
                chunk_count=0,
                dim=0,
                stale=[],
                missing=[],
                extra=sorted(wanted),
            )
        stale = sorted(
            rel for rel, digest in wanted.items() if current.files.get(rel) not in (None, digest)
        )
        extra = sorted(rel for rel in wanted if rel not in current.files)
        missing = sorted(rel for rel in current.files if rel not in wanted)
        return format_status(
            root=str(self.root),
            file_count=len(current.files),
            chunk_count=len(current.chunks),
            dim=current.dim,
            stale=stale,
            missing=missing,
            extra=extra,
        )


def _parse_kind_filter(value: str) -> Kind | None:
    if value in ("", "all"):
        return None
    if value == "report":
        return "report"
    if value == "source":
        return "source"
    raise ValueError("kind must be all, report, or source")
