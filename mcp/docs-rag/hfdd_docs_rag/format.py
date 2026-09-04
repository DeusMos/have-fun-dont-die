from __future__ import annotations

from hfdd_docs_rag.corpus import Chunk
from hfdd_docs_rag.search import Hit


def format_hits(hits: list[Hit]) -> str:
    if not hits:
        return "No hits."
    blocks = []
    for i, hit in enumerate(hits, start=1):
        blocks.append(format_hit(i, hit))
    return "\n\n---\n\n".join(blocks)


def format_hit(n: int, hit: Hit) -> str:
    chunk = hit.chunk
    ranks = []
    if hit.bm25_rank is not None:
        ranks.append(f"bm25={hit.bm25_rank}")
    if hit.dense_rank is not None:
        ranks.append(f"dense={hit.dense_rank}")
    rank_s = f" {' '.join(ranks)}" if ranks else ""
    return (
        f"[{n}] {chunk.path} § {chunk.heading}\n"
        f"kind={chunk.kind} area={chunk.area} mark={chunk.mark or '—'} "
        f"score={hit.score:.4f}{rank_s}\n\n"
        f"{chunk.text}"
    )


def format_status(
    root: str,
    file_count: int,
    chunk_count: int,
    dim: int,
    stale: list[str],
    missing: list[str],
    extra: list[str],
) -> str:
    lines = [
        f"root: {root}",
        f"files: {file_count}",
        f"chunks: {chunk_count}",
        f"dim: {dim}",
        f"stale: {len(stale)}",
        f"missing_from_disk: {len(missing)}",
        f"not_yet_indexed: {len(extra)}",
    ]
    for label, paths in (
        ("stale", stale),
        ("missing_from_disk", missing),
        ("not_yet_indexed", extra),
    ):
        if paths:
            lines.append(f"{label}:")
            lines.extend(f"  {path}" for path in paths[:20])
            if len(paths) > 20:
                lines.append(f"  … {len(paths) - 20} more")
    return "\n".join(lines)


def format_reindex(message: str, chunks: list[Chunk], dim: int) -> str:
    areas = sorted({chunk.area for chunk in chunks})
    return (
        f"{message}\n"
        f"chunks: {len(chunks)}\n"
        f"files: {len({chunk.path for chunk in chunks})}\n"
        f"dim: {dim}\n"
        f"areas: {', '.join(areas) if areas else '—'}"
    )
