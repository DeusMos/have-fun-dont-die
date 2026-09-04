# docs-rag

Built-in MCP + CLI over this repo’s `hallmarks/`, `topics/`, and `compounds/` writeups.

Agents call `search_docs` instead of redoing research that is already filed. The index is local (`.rag/` at the repo root). Nothing is sent to a hosted vector store.

## Corpus

Indexed:

- `hallmarks/*/report.md`
- `topics/*/report.md`
- `compounds/*/report.md`
- `hallmarks/*/sources/<mark>/*.md`, `topics/*/sources/<mark>/*.md`, and `compounds/*/sources/<mark>/*.md`

Not indexed: `tmp/`, `template.md`, source `README.md` files, skills, AGENTS.md.

## Tools

| Tool | Job |
|---|---|
| `search_docs` | Hybrid BM25 + embedding search. Filters: `kind` (`all` / `report` / `source`), `area`, `mark`. |
| `reindex` | Incremental update, or `force=true` for a full rebuild. |
| `corpus_status` | What is indexed and whether files changed. |

`search_docs` incrementally updates the index if reports or sources changed.

## CLI

```bash
mcp/docs-rag/run.sh status
mcp/docs-rag/run.sh reindex
mcp/docs-rag/run.sh search "SIRT6 fucoidan mouse lifespan"
```

Needs `uv`. First production index downloads `BAAI/bge-small-en-v1.5` via fastembed and embeds every chunk (about ten minutes on CPU for the current corpus). Later `search` / incremental `reindex` only embeds what changed.

`HFDD_EMBEDDER=hash` is a test double. Do not use it for real search.

## Cursor

Cursor starts this server from `.cursor/mcp.json`. Claude Code uses the root `.mcp.json`. After adding or changing either, enable `docs-rag` (Settings → Tools & MCP) and reload so the session sees it.
