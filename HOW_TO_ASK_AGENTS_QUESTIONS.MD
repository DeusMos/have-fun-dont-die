# How to ask agents questions

Hits are what is already written. Corpus is `hallmarks/`, `topics/`, and `compounds/` reports plus filed source notes. Not `tmp/`, not `template.md`. If search cannot answer the actual question, the agent starts research instead of saying “no supporting data” — unless the job is retrieve one paper, in which case it starts [paper-hunter](.cursor/skills/paper-hunter/). How-to-add-a-topic and other repo-ops are not that path — those answers live in [`AGENTS.md`](AGENTS.md). How the agents, search, and context stack fit together: [`HOW_DOES_THIS_THING_WORK.md`](HOW_DOES_THIS_THING_WORK.md). Package notes: [`mcp/docs-rag/README.md`](mcp/docs-rag/README.md).

Ask a real question. Keyword spam is worse than a sentence. If you want a new or rewritten report, say so; that is [adversarial-research](.cursor/skills/adversarial-research/), not search. If you want a specific paper found (and usually the related writeups patched), that is [paper-hunter](.cursor/skills/paper-hunter/) — fetch/patch, not a research flight, not pirate mirrors. To add a topic or compound (tree, sources, catalog, reindex): [AGENTS.md — Adding a topic](AGENTS.md#adding-a-topic-or-compound). What to run after a save: [AGENTS.md — Indexing](AGENTS.md#indexing).

Needs `uv` and Python 3.11+. The index is local (`.rag/`, gitignored). First build downloads `BAAI/bge-small-en-v1.5` and embeds the corpus (~10 min on CPU). Later searches only embed what changed. Do not use a user-level `markdown_rag` server — this repo’s server is `docs-rag`.

## How to use the Cursor skill

1. Open this folder in Cursor.
2. Cursor starts `docs-rag` from [`.cursor/mcp.json`](.cursor/mcp.json). Enable it under Settings → Tools & MCP, then reload if the session does not list it. Root [`.mcp.json`](.mcp.json) is for Claude Code. Ignore any other MCP in the session that is not `docs-rag`.
3. The skill is [`.cursor/skills/docs-rag/`](.cursor/skills/docs-rag/). The always-on rule is [`.cursor/rules/20-docs-rag.mdc`](.cursor/rules/20-docs-rag.mdc). You do not invoke it by name. Ask in chat.
4. The agent should call `search_docs` first, then read the cited `report.md` / source note. If the hits already answer and you did not ask to research, update, or fill a report, it should cite the files and stop.
5. If the hits are empty or thin — they do not answer the actual question — it should **not** shrug with "no supporting data." If the job is retrieve one paper, go to step 7. Otherwise it should say: "Hey, I don't have all the facts yet. I am going to go do some research. This will take a while. Is that okay?" Then it starts [adversarial-research](.cursor/skills/adversarial-research/) for at least one iteration and answers from what that flight compiled. `--mode=ask` cannot write; drop it if you want that path. Repo-ops (how to add a topic, where files go, how this repo works, how to ask) is not this path.
6. To research, update, or fill a report on purpose: [`.cursor/skills/adversarial-research/`](.cursor/skills/adversarial-research/). Say that. Search alone will not write a report.
7. To find one paper (paywalled, 403, unfetched source) and patch the writeups it belongs in: [`.cursor/skills/paper-hunter/`](.cursor/skills/paper-hunter/). Say the citation. That is not a research flight.

If the session does not list `docs-rag`, enable or reload it first. A missing namespace is not permission to skip to the CLI. CLI only if they cannot enable the server this turn:

```bash
mcp/docs-rag/run.sh search "weekly rapamycin PEARL VAT"
mcp/docs-rag/run.sh reindex
mcp/docs-rag/run.sh status
```

## How to use the Claude Code skill

1. Open this folder in Claude Code.
2. Skills are in [`.claude/skills/`](.claude/skills/) (`docs-rag`, `adversarial-research`, `paper-hunter`). Same law as Cursor: [`AGENTS.md`](AGENTS.md).
3. If the session does not already have `docs-rag`, add the project server:

```bash
claude mcp add docs-rag -- bash mcp/docs-rag/run.sh
```

Or enable the `docs-rag` entry from [`.mcp.json`](.mcp.json) (Claude) / [`.cursor/mcp.json`](.cursor/mcp.json) (Cursor) and skip any other server.
4. Ask in chat. You do not invoke the skill by name. Search first, then read the cited `report.md`. If the hits already answer, it should stop. If they do not answer the actual question, it should say it does not have the facts yet, start research, and answer after at least one iteration — not “no supporting data.” Repo-ops is not that path.
5. To research, update, or fill a report on purpose: [`.claude/skills/adversarial-research/`](.claude/skills/adversarial-research/).
6. To find one paper and patch related writeups: [`.claude/skills/paper-hunter/`](.claude/skills/paper-hunter/). Not a research flight. Not pirate mirrors.

If the session does not list `docs-rag`, enable or reload it first. A missing namespace is not permission to skip to the CLI. CLI only if they cannot enable the server this turn:

```bash
mcp/docs-rag/run.sh search "weekly rapamycin PEARL VAT"
```

## How to use the Cursor Agent CLI

Cursor’s `agent` CLI is the same Agent, from a terminal. Not the IDE chat. Official command is `agent`. `cursor agent` is the same binary (`agent --help` prints `Usage: cursor agent`).

1. `cd` to this repo. Workspace defaults to the current working directory. `--workspace <path>` if you are not already in the folder.
2. Auth once: `agent login`. Scripts can use `CURSOR_API_KEY` or `--api-key`.
3. Same law as the Cursor skill: [`.cursor/skills/docs-rag/`](.cursor/skills/docs-rag/), [`.cursor/mcp.json`](.cursor/mcp.json), [`.cursor/rules/20-docs-rag.mdc`](.cursor/rules/20-docs-rag.mdc). Load `docs-rag`, then search. Do not invent.
4. Ask. You do not invoke the skill by name. If search already answers, it should cite and stop. If it cannot, the write pipeline needs default mode (no `--mode=ask`).
5. To research, update, or fill a report on purpose: drop `--mode=ask` and say that. [`.cursor/skills/adversarial-research/`](.cursor/skills/adversarial-research/). Search alone will not write a report.
6. To find one paper and patch related writeups: drop `--mode=ask` and give the citation. [`.cursor/skills/paper-hunter/`](.cursor/skills/paper-hunter/).

Interactive, read-only Q&A (cwd = this repo):

```bash
agent --mode=ask "weekly rapamycin PEARL VAT"
```

`--mode=ask` is read-only. Default (no `--mode`) can edit files and run shell. Use default if you asked for a write, or if you want the agent to research when the notebook cannot answer.

Non-interactive (prints to stdout; for scripts):

```bash
agent -p --mode=ask --trust --approve-mcps "weekly rapamycin PEARL VAT"
```

`-p` / `--print` is non-interactive. It has write and shell tools unless you also pass `--mode=ask`. `--trust` skips the workspace-trust prompt. `--approve-mcps` auto-approves project MCP servers so `docs-rag` can load without a prompt.

If cwd is not the repo:

```bash
agent --workspace /path/to/have-fun-dont-die --mode=ask "weekly rapamycin PEARL VAT"
```

If the session does not list `docs-rag`, enable or reload it first (`--approve-mcps` on `agent` helps). A missing namespace is not permission to skip to the CLI. CLI only if they cannot enable the server this turn:

```bash
mcp/docs-rag/run.sh search "weekly rapamycin PEARL VAT"
```

## GPT-Chat interface purposely left out

There is no ChatGPT custom GPT, no hosted chat UI, and no “ask the repo” product wrapper. Do not add one.

This is a foundation: writeups, marks, a local `docs-rag` index, and agent skills that already know how to search before they invent. It is not a product. Do not ship it as one.

If you want these, just ask Claude code! Don't PR, and please don't fork for just that. We are going to piss Karron off at some point, but let's hope she can't use a CLI.
