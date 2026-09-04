---
name: docs-rag
description: Search already-written hallmarks/, topics/, and compounds/ reports via the built-in docs-rag MCP. Use when the user asks what the repo says, asks a biology/longevity/practice question that may already be filed, or after a report is saved and the index needs a refresh.
---

# Docs RAG

Repo law: [AGENTS.md](../../../AGENTS.md). This skill is retrieval, not new research.

## Tools

MCP server name: `docs-rag`. Do not use the user-level `markdown_rag` MCP here — it shares one Milvus collection with other vaults.

| Tool | When |
|---|---|
| `search_docs` | Default. Natural-language query. |
| `reindex` | After saving `report.md` or a source note. `force=true` only if the index is broken. |
| `corpus_status` | Check stale/missing files. |

If the MCP is not loaded in this session, use the CLI:

```bash
mcp/docs-rag/run.sh search "SIRT6 fucoidan mouse lifespan"
mcp/docs-rag/run.sh reindex
mcp/docs-rag/run.sh status
```

## search_docs arguments

- `query`: a real question or topic phrase, not keyword spam
- `k`: default 8; raise to 12 when you need breadth
- `kind`: `all` (default), `report`, or `source`
- `area`: `hallmarks/01-genomic-instability`, `topics/rapamycin`, or `compounds/rapamycin`
- `mark`: evidence-mark filter for source notes only (`📚`, `🤔`, …)

`search_docs` incrementally updates the index if files changed.

## Rules

- Search first. Then read the cited file if you will quote or update it.
- If the hits already answer and the user did not ask to research, update, or fill a report, cite the files and stop.
- Hits are the current writeup. They are not a verdict and not a reason to skip a research run the user asked for.
- Empty/thin hits on the actual question → say so. Then either read the obvious `report.md` or start adversarial-research if they asked to research/update.
- How to add a topic / how this repo works is not corpus (READMEs and skills are not indexed). Point at `topics/README.md`, `.cursor/skills/adversarial-research/` (`init-topic-sources.sh` + `scripts/index-meta.yaml` + `build-index.py`), and `AGENTS.md`. Do not start a research flight.
- Do not treat `tmp/` as corpus.
- After a save, `reindex`. Catalog vs RAG, corpus paths, and when to skip `build-index.py`: [AGENTS.md — Indexing](../../../AGENTS.md#indexing).

Package notes: [mcp/docs-rag/README.md](../../../mcp/docs-rag/README.md).
