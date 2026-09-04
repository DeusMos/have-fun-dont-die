from __future__ import annotations

from fastmcp import FastMCP
from pydantic import Field

from hfdd_docs_rag.service import RagService

mcp = FastMCP(
    "hfdd-docs-rag",
    instructions=(
        "Search have-fun-dont-die writeups. Corpus is hallmarks/*/report.md, "
        "topics/*/report.md, compounds/*/report.md, and filed source notes "
        "under sources/<mark>/. "
        "Call search_docs before answering a biology / longevity / practice "
        "question from this repo. Hits are what is already written, not a "
        "reason to invent citations. After saving a report or source note, "
        "call reindex."
    ),
)

_service = RagService()


@mcp.tool(
    name="search_docs",
    description=(
        "Semantic + keyword search over hallmarks/, topics/, and compounds/ "
        "reports and source notes. Use before re-researching a claim that may already be written."
    ),
    tags={"search", "rag"},
)
def search_docs(
    query: str = Field(description="Natural-language question or topic"),
    k: int = Field(8, description="Number of chunks to return"),
    kind: str = Field("all", description="all | report | source"),
    area: str = Field(
        "",
        description="Optional prefix such as hallmarks/01-genomic-instability, topics/rapamycin, or compounds/rapamycin",
    ),
    mark: str = Field("", description="Optional evidence-mark filter for source notes, e.g. 📚"),
) -> str:
    return _service.search(query=query, k=k, kind=kind, area=area, mark=mark)


@mcp.tool(
    name="reindex",
    description="Rebuild or incrementally update the docs-rag index after reports or sources change.",
    tags={"index"},
)
def reindex(
    force: bool = Field(False, description="If true, rebuild the whole index"),
) -> str:
    return _service.reindex(force=force)


@mcp.tool(
    name="corpus_status",
    description="Show what is indexed and whether the on-disk corpus is stale.",
    tags={"status"},
)
def corpus_status() -> str:
    return _service.status()


def run() -> None:
    mcp.run(transport="stdio")
