---
name: docs-rag
description: Search already-written hallmarks/, topics/, and compounds/ reports via the built-in docs-rag MCP. Use when the user asks what the repo says, asks a question that may already be filed, or after a report is saved and the index needs a refresh. If search cannot answer the actual question (empty or thin hits), hand off to adversarial-research — do not stop on "no supporting data." Repo-ops is not that path.
---

# Docs RAG

Repo law: [AGENTS.md](../../../AGENTS.md). This skill is retrieval first. If retrieval cannot answer the actual question, hand off to [adversarial-research](../adversarial-research/SKILL.md). Do not stop on "no supporting data."

## Tools

MCP server name: `docs-rag`. Do not use the user-level `markdown_rag` MCP here — it shares one Milvus collection with other vaults.

| Tool | When |
|---|---|
| `search_docs` | Default. Natural-language query. |
| `reindex` | After saving `report.md` or a source note. `force=true` only if the index is broken. |
| `corpus_status` | Check stale/missing files. |

## Load first

Do this before any search, including the CLI.

1. Discover the `docs-rag` namespace and inspect `search_docs`. Cursor starts this server from [`.cursor/mcp.json`](../../../.cursor/mcp.json). Root [`.mcp.json`](../../../.mcp.json) is Claude Code only.
2. If `namespaceStatus` is `needsAuth`, authenticate, then discover again.
3. If the namespace is missing or not ready: ask the user to enable `docs-rag` (Settings → Tools & MCP) or reload MCP servers, then discover again. A missing namespace is not permission to skip to the CLI.
4. Call `search_docs`. After a save, call `reindex`.
5. CLI only if they cannot enable the server this turn and still want an answer:

```bash
mcp/docs-rag/run.sh search "SIRT6 fucoidan mouse lifespan"
mcp/docs-rag/run.sh reindex
mcp/docs-rag/run.sh status
```

Use `-k 12` for breadth. Do not pass `--k` — the CLI reads that as `--kind`.

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
- Judge whether the hits answer the **actual question**. Off-topic chunks, a related molecule, or a heading match are thin. Do not decide that by keyword counting. Do not classify the question as biology vs not.
- Empty/thin hits that do not answer the actual question: do **not** answer with "no supporting data," "the repo does not cover this," or a shrug. That reply is useless. Tell the user exactly: "Hey, I don't have all the facts yet. I am going to go do some research. This will take a while. Is that okay?" Then start [adversarial-research](../adversarial-research/SKILL.md) in the same turn for **at least one** Phase 1 iteration (Phase 0 + three-agent flight + compiler). Do not wait for a second "yes" unless they already declined. After that compiler pass, evaluate: if compiled, link-checked claims answer the question, answer now. If not, follow the compiler loop (cap 5). Never return a bare no-data line after a flight.
- `--mode=ask` (or any read-only session) cannot write the flight. Same sentence, then tell them to drop `--mode=ask` / use default mode. Do not invent an answer from memory.
- Repo-ops (how to add a topic, where files go, how this repo works, how to ask) is not corpus (READMEs and skills are not indexed). Point at `topics/README.md`, `.cursor/skills/adversarial-research/` (`init-topic-sources.sh` + `scripts/index-meta.yaml` + `build-index.py`), and `AGENTS.md`. Empty hits there are expected. Do not start a research flight.
- Do not treat `tmp/` as corpus.
- After a save, `reindex`. Catalog vs RAG, corpus paths, and when to skip `build-index.py`: [AGENTS.md — Indexing](../../../AGENTS.md#indexing).

Package notes: [mcp/docs-rag/README.md](../../../mcp/docs-rag/README.md).
