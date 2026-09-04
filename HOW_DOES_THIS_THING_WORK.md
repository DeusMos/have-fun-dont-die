    # How this thing works

This file is the kitchen tour. [README.md](README.md) is the front door. [HOW_TO_ASK_AGENTS_QUESTIONS.MD](HOW_TO_ASK_AGENTS_QUESTIONS.MD) is “how do I ask a question.” [AGENTS.md](AGENTS.md) is the house rules for anyone writing here. This page is “what is actually running when I ask the agent a question.”

You do not need to memorize it. You do not need to run a research swarm to read a report. Open a `report.md`, or ask a question. The rest of this file is here so the machinery is less mysterious.

This repository is not medical advice. It is a sourced information dump. The writeups document. They do not tell you what to take — except ☠︎︎, where stay away is the point.

---

## The short version

This repo is a **notebook plus a small research crew**.

The notebook is the markdown under `hallmarks/`, `topics/`, and `compounds/`. Each assertion in a rewritten page starts with an evidence mark (💯 published-and-settled, 📚 a paper, 🤔 forum practice, and so on). Marks are honesty labels, not a score.

The crew is not a product and not a hosted chatbot. It is instructions that Cursor or Claude Code already know how to follow:

1. **Ask** — search what is already written, read the hits, answer. Done — if the hits actually cover it.
2. **Research** — if you say so, **or** if the ask path cannot answer from filed writeups. Spawn a briefing, then three agents who look at the same claim from different angles, then one compiler who merges them, checks the links, and (when the writeup is ready) saves a report. After at least one flight, the parent answers you from the compiled claims instead of shrugging.

The parent agent in your chat is the stage manager. It does not read every file. It builds a small, relevant pile of context and (when you asked for research) hands copies of that pile to helpers.

---

## What you are looking at

Four piles of stuff, on purpose:

| Pile | Where | Job |
|---|---|---|
| Writeups | `hallmarks/`, `topics/`, `compounds/` | The public notes. This is the corpus. |
| House rules | `AGENTS.md`, `.cursor/rules/`, `template.md` | Voice, marks, where files go. |
| Skills | `.cursor/skills/` (Claude copies live under `.claude/skills/`) | Recipes the agent follows: search, or run a research flight. |
| Local search | `mcp/docs-rag/` + a gitignored `.rag/` index | “What did we already write about this?” |

There is no ChatGPT custom GPT, no website that “asks the repo,” and no cloud vector store. Search stays on your machine. The thinking stays yours. The agents follow directions.

Cheap models are fine for fetching papers. Use a capable one for analysis. Fifty scrapers reading ten papers each will beat one genius who only opened one PDF. That is the whole staffing philosophy.

---

## The two jobs (ask vs research)

The agent is trained, by this repo, to tell these apart.

**Ask** — “what does this repo say about weekly rapamycin and PEARL VAT?”

The agent searches the local index, opens the cited `report.md` / source notes, and answers from those files. If the hits already cover it, it **stops**. It does not launch a three-agent literature flight because you were curious and the notebook already had the answer.

**Research** — “research fisetin,” “update the rapamycin report,” “is X true — write it up,” **or** an ask whose hits are empty or thin for the actual question.

Now it is allowed to go outside the repo: PubMed, preprints, clinic pages, forums. That is the [adversarial-research](.cursor/skills/adversarial-research/) skill. Search still runs first, so the flight starts from what is already filed instead of pretending the folder is empty.

If search cannot answer, the agent must **not** return “no supporting data.” It tells you: “Hey, I don't have all the facts yet. I am going to go do some research. This will take a while. Is that okay?” Then it runs at least one Phase 1 iteration and answers from what the compiler link-checked. A shrug is a failed ask, not a finished one.

If you only wanted an answer and the files already have one, you get the files. If you wanted a new or rewritten page, say “research” or “update the report.” If the notebook is empty on your question, you get research whether you said that word or not.

Repo-ops questions (“how do I add a topic,” “where do files go”) are **not** search and **not** a research flight. Those answers live in this file, `AGENTS.md`, and `topics/README.md`. The search index does not include READMEs or skills on purpose. Empty hits there are expected.

---

## Who is in the room

```text
You
 └─ Cursor chat, Cursor `agent` CLI, or Claude Code
     └─ Parent agent  (the one you are talking to)
         ├─ Always-on rules + AGENTS.md + matching skills
         ├─ docs-rag MCP  →  search / reindex / status
         ├─ Tools: read files, fetch URLs, run shell, write markdown
         │
         ├─ Ask path: search → read hits → answer you → stop
         │    (if hits are empty/thin: do not shrug — go to Research)
         │
         ├─ Research path (you asked, or ask could not answer):
         │    tell you it will take a while
         │    Phase 0 briefing
         │    three Task subagents in parallel
         │      validator / invalidator / domain collector
         │    one compiler (sequential)
         │    answer you if compiled claims are enough
         │    maybe another flight (cap 5)
         │    save report + sources + catalogs + reindex
         │
         └─ After some edits, a hook may ask the parent
            to spawn rule-validation (a reviewer, not a writer)
```

You talk to **one** agent. That agent may hire helpers. The helpers do not see your whole chat history. They get a written packet: the house rules, a briefing, and a job.

That is how context is built. Not by stuffing the entire repo into one prompt.

---

## How context is built

This is the part that looks like magic and is actually a stack of small, boring files.

### 1. You open this folder

Cursor and Claude Code treat the workspace as the project. Skills, rules, and `AGENTS.md` are discovered from disk. You do not paste a system prompt.

### 2. House rules load without you asking

- **`AGENTS.md`** — voice, evidence marks, source rules, layout, indexing. Writers (human or model) obey this file. Existing reports that predate it lose; this file wins.
- **`.cursor/rules/20-docs-rag.mdc`** — always on. Before answering a question: search first, then read the hit, then stop if it answers. If it does not, and this is not repo-ops, tell you research is starting and run the flight.
- Other always-on user/workspace rules (safety, tmp artifacts, no keyword-intent classifiers, and so on) sit in your Cursor rules. They apply here too.

The parent agent therefore starts every question with “look it up here” rather than answering from memory.

### 3. Skills show up when they match

A skill is a `SKILL.md` with a name and a description. The agent does **not** need you to type `/docs-rag`. You ask a normal question. If the description matches, it reads the skill and follows it.

| Skill | When it fires | What it does |
|---|---|---|
| [docs-rag](.cursor/skills/docs-rag/) | “What does the repo say,” a question that may already be filed, or after a save | Search, maybe reindex. Hand off to research if the hits cannot answer. |
| [adversarial-research](.cursor/skills/adversarial-research/) | You asked to research, update, fill a report, or search could not answer the question | The Phase 0 → three-agent → compiler pipeline. |

Claude Code uses the copies under `.claude/skills/`. Same law, same prompts.

### 4. Search is a local MCP, not a vibe

Cursor starts `docs-rag` from [`.cursor/mcp.json`](.cursor/mcp.json). Claude Code uses [`.mcp.json`](.mcp.json). Both launch the same process:

```text
bash mcp/docs-rag/run.sh
```

That process exposes three tools to the agent:

| Tool | Everyday meaning |
|---|---|
| `search_docs` | “Find the chunks that match this question.” |
| `reindex` | “The files changed; update the index.” |
| `corpus_status` | “What is indexed, and is anything stale?” |

Load `docs-rag` first (enable / reload if the session does not list it). CLI (`mcp/docs-rag/run.sh search "…"`) is last resort, not the default when the namespace is missing. Do not point a user-level `markdown_rag` server at this repo — that one shares a collection with other vaults.

### 5. The index is a map, not the book

On first real build, the server downloads a small embedding model (`BAAI/bge-small-en-v1.5`) and embeds the corpus into `.rag/` at the repo root. That folder is gitignored. Nothing is uploaded to a hosted vector store. First build can take about ten minutes on CPU. Later searches only embed files that changed.

What gets indexed:

- `hallmarks/*/report.md`, `topics/*/report.md`, `compounds/*/report.md`
- Filed source notes under `sources/<mark>/` (the emoji folder that matches the claim)

What does **not** get indexed (on purpose):

- `tmp/` scratch
- `template.md`
- source-dir `README.md` files
- this file, `AGENTS.md`, catalog READMEs, skills

A file that is not in that list is invisible to `search_docs`. That is why a new report also needs a reindex, and why notes left in `tmp/` never become “the repo said.”

Search itself is hybrid: keyword (BM25) plus embedding similarity, fused. You can filter by `kind` (report vs source), `area` (`compounds/rapamycin`), or `mark` (📚 only). Default is eight chunks. The agent is supposed to **read the cited file** before quoting it. Hits are pointers, not a license to invent a citation.

### 6. The parent still has to open files

Search returns short chunks (roughly 1–2k characters, split on headings). The agent then uses the ordinary Read tool on `report.md` or the source note. Context for an **ask** is:

1. Your question
2. The always-on rules and the docs-rag skill
3. A handful of search hits
4. The full text of the one or two files it decided to open

It does not load all fourteen hallmarks. That is why the README says: do not memorize it; do not read every file.

### 7. Research helpers get a packet, not your chat

When the parent spawns Task subagents, each one starts fresh. It does **not** inherit the conversation. The parent copies the role prompt from [prompts.md](.cursor/skills/adversarial-research/prompts.md) and fills in paths:

- `{AGENTS}` — absolute path to `AGENTS.md` (they are told to read it)
- `{BRIEFING}` — `tmp/YYYY-MM-DD_<slug>/BRIEFING.md`
- `{UPDATE}` — only on round 2+, what is still unanswered
- `{SESSION}`, `{STAGING}`, `{FINDINGS}` — where that role is allowed to write

Plus the shared rules block: marks, cite or do not speak, do not write `report.md`, do not “win” by being louder.

That packet **is** their context. The briefing exists so the three of them share the same claim, the same definition traps, and the same “this slogan is not the paper” warnings — without the parent pasting a novel into each prompt.

Working notes live under `tmp/YYYY-MM-DD_<slug>/` (gitignored). Dump there first. Do not “finish” a report from memory. Do not cite `tmp/` from a public `report.md`.

### 8. After a save, two indexes get a refresh

Saving a page is not enough for the next session to find it.

| Index | Command | What it updates |
|---|---|---|
| Catalog (front-door tables) | `python3 scripts/build-index.py` | The `BEGIN GENERATED` blocks in the READMEs |
| RAG (`search_docs`) | MCP `reindex` or `mcp/docs-rag/run.sh reindex` | `.rag/` embeddings |

A new topic or compound also needs a row in `scripts/index-meta.yaml`. The catalog script fails closed if a `report.md` has no sidecar. Do not hand-edit the generated tables.

---

## How agents are spawned

Nobody walks around the repo spawning daemons. “Spawn” here means: the parent agent starts another model call with a narrower job.

### You usually do not name them

Ask in chat. The parent picks the skill. For research it launches helpers with Cursor’s Task / subagent mechanism (Claude Code has the same idea). You will see extra agents appear in the UI with names like validator or compiler. That is expected. They write files under `tmp/` and then stop.

### The research flight is three-at-once, then one

Phase 0 (briefing) is the parent or a single helper. It must exist **before** the flight.

Phase 1 is **three Task calls in one message**, same briefing, different mandates. They write three separate findings files so they cannot clobber each other. The parent waits for all three. Then it sends **one** compiler prompt. The compiler does not re-search the literature from scratch. It compiles, link-checks, and decides whether another flight is needed.

Cap is **5** Phase 1 flights unless you set a lower number. After the fifth compiler pass, it saves and flags leftover gaps. Loops are for missing sides of a fight or dead citations, not for prettier prose.

### Hooks can request a reviewer after you edit

Cursor project hooks live in [`.cursor/hooks.json`](.cursor/hooks.json). They cannot spawn Task agents by themselves. The pattern is gentler than it sounds:

1. You (or the parent) edit a file.
2. `afterFileEdit` records the **path** (not the meaning of your sentence) into a small gitignored queue.
3. When the turn finishes, the `stop` hook may return a follow-up message: “please launch rule-validation on these paths.”
4. The parent then starts the [rule-validation](.cursor/agents/rule-validation.md) subagent.

Tab completions do not launch reviewers. `tmp/` and `.rag/` are ignored. Biology reports get a rules check. Test files can also request a test-engineer; other code can request a pr-reviewer. Security-review and bugbot are **not** auto-fired.

Trust the workspace when Cursor asks, or the hooks stay off. Details: [`.cursor/hooks/README.md`](.cursor/hooks/README.md).

### Cursor Agent CLI is the same agent

`agent --mode=ask "weekly rapamycin PEARL VAT"` is the parent in a terminal, read-only. Drop `--mode=ask` if you asked it to write, or if search cannot answer and you want the research flight. Same skills, same MCP, same law. See [HOW_TO_ASK_AGENTS_QUESTIONS.MD](HOW_TO_ASK_AGENTS_QUESTIONS.MD).

---

## What each role actually does

Think of a newsroom, not a tribunal. Nobody is assigned to “win.”

### Parent (the one in your chat)

Stage manager. Reads your ask. Searches the repo. Decides ask-vs-research (research if you asked, or if search cannot answer). If it is pivoting from a thin ask, it tells you it does not have the facts yet and that research will take a while. Creates `tmp/YYYY-MM-DD_<slug>/`. Writes or delegates Phase 0. Launches the three, waits, launches the compiler, answers you if the compiled claims are enough, maybe loops, then makes sure the catalogs and `.rag/` got updated. Talks to you in normal language. Never ends a question the notebook cannot answer with “no supporting data.” Repo-ops is the exception.

### Phase 0 — rumor mill (briefing only)

Gathers **frame**, not a verdict.

It searches this repo first (`already_in_repo`). Then it looks at how the slogan is used in the wild: who is pushing it, what nearby true fact gets laundered into the claim, what words mean two different things, what a naive “yes” search will hit that is not the claim.

It writes `BRIEFING.md` with a fixed schema. It is **forbidden** to say the claim is true or false, to skip the flight because the rumor looks dumb, or to tell the validator who should win. “This circulates as marketing” is frame. It is not the result.

Gold-standard tone lives in [examples.md](.cursor/skills/adversarial-research/examples.md) (carrots / bleach). Phase 0 still runs even when the slogan is silly. That is how you avoid a confident wrong page.

### Validator

Makes the strongest **honest** case that the steelmanned claim is true. Positive trials, supporting mechanisms, practice that matches the *actual* claim. Must treat the briefing’s framing hazards as binding: a nearby true fact is not a hit. Writes `FINDINGS.validator.r{N}.md` and stages source notes under `staging/validator/`. Stops. Does not write the public report.

### Invalidator

Attacks the **same** claim. Nulls, failed replications, harms, definition games, conflicts of interest. Strawmanning a weaker slogan while the real claim stands is a miss. “No perfect human RCT yet” is not disproof — the marks 📜, 🤔, and 🐉 exist so the repo can still write. Writes `FINDINGS.invalidator.r{N}.md`. Stops.

### Domain collector

Maps the field. Does not prosecute and does not steelman. Canonical reviews, what the assay actually measures, what clinics and forums are doing, adjacent hallmarks, live paper fights vs amateur fights. Graded on covering the briefing’s must-watch list (brands, protocols, who-is-pushing). Writes `FINDINGS.domain.r{N}.md` plus a landscape block. Stops.

### Compiler

One agent, after the three files exist. Merges Phase 0 + both sides + the map into `DRAFT.md`. Both sides stay. No tidy winner. Every asserting sentence gets a mark. Practice is not efficacy.

Then it **tests every link** (fetch or HEAD the URL / DOI / PMID) into `LINKCHECK.md`. Dead or invented citations drop. A 403 / “open this in a browser” is not treated as fake — it tries DOI or PubMed before giving up.

Then it writes `DECISION.md`: another round, or save. That decision is about **process** (did we miss a side, a must-watch clinic, a dead central paper), not about whether the claim is true.

On save it copies surviving notes into `sources/<emoji>/`, writes `report.md` using [template.md](template.md) as **headings only**, updates `scripts/index-meta.yaml`, runs `build-index.py`, and reindexes search.

### Rule-validation (after edits, optional)

A reviewer. Reads the diff against `AGENTS.md` and the matching rule families. Writes findings under `tmp/YYYY-MM-DD_rule-validation/` if something is actually wrong. Does not silently rewrite your page. Does not reindex. You can also ask for it by name: “use the rule-validation subagent on the current diff.”

---

## A research run, step by step

Suppose you say: “Research whether weekly rapamycin restores nutrient sensing in healthy adults. Update the report.”

1. **Parent searches** `docs-rag` for the subject. Hits go into the briefing as `already_in_repo`. Because you asked to research, the flight still runs.
2. **Destination is chosen.** A molecule writeup lands at `compounds/rapamycin/`. The hallmark it touches (`06-deregulated-nutrient-sensing`) can be updated too. A rumor that is not a molecule would go to `topics/<slug>/`. A hallmark rewrite stays in `hallmarks/NN-short-name/`.
3. **Session folder** `tmp/YYYY-MM-DD_rapamycin/` is created if needed. Sources tree is created with `init-topic-sources.sh` if the dir is new (copies the per-mark README folders).
4. **Phase 0** writes `BRIEFING.md`: claim as asked vs as used in the wild, definition traps, who sells the capsule, what “restore” will falsely match.
5. **Phase 1** launches validator, invalidator, and domain collector together. Each reads `AGENTS.md` + the briefing. Each writes only its own findings + staging notes.
6. **Compiler** builds `DRAFT.md`, `LINKCHECK.md`, `DECISION.md`.
7. If the draft deleted the practice map the old report already had, or one side of a 🥼 fight is missing, the compiler writes `UPDATE.r2.md` and the parent runs Phase 1 again. Same briefing, extra hunt list. Max five times.
8. **Save:** `compounds/rapamycin/report.md` (weave, do not wipe) and matching `sources/📚/…`, `sources/🤔/…`, and so on. File a note in the folder that matches the mark on the sentence.
9. **Sidecar + catalogs + reindex.** The next ask can find the new sentences.

You can watch the `tmp/` folder while this happens. That is the paper trail. It is not the published page.

---

## What a finished page looks like

[template.md](template.md) is a skeleton. Nobody writes a filled report into it.

Hallmarks and topics share sections: claim vs slogan, definitions, mechanism, animal, human, measurement, what clinics are doing, speculative (required), named compounds, adjacent hallmarks, what is actually on the table.

Compounds add identity (including CAS), PK, toxicity, interactions, formulations, observed practice, fights, legal/access status.

Every asserting sentence starts with one mark. Titles and headers do not. Mixed grades get split into two sentences. One not-medical-advice paragraph at the top, then never again in that file. Nulls and harms sit in the same section as the positive claims. Doses are observed practice with a source, not instructions.

The emoji folders under `sources/` match the mark on the claim. A 📚 sentence is backed by a note in `sources/📚/`. Do not invent source files to decorate an empty folder.

---

## The two indexes again (because this trips people)

```text
report.md  +  sources/<mark>/*.md
        │
        ├── scripts/index-meta.yaml  +  build-index.py
        │     → tables in README.md, hallmarks/README.md, …
        │     → humans browsing GitHub
        │
        └── mcp/docs-rag  reindex
              → .rag/  (local, gitignored)
              → search_docs
              → agents answering questions
```

They do not watch each other. A beautiful report that skipped `reindex` is invisible in chat. A reindex that skipped `index-meta.yaml` + `build-index.py` is invisible on the front door.

| You changed | Catalog? | RAG? |
|---|---|---|
| New topic or compound (`report.md` + sidecar) | yes | yes |
| Hallmark rewrite (status / one-liner / headings) | yes | yes |
| Body of an existing `report.md` only | no | yes |
| A source note | no | yes |
| `index-meta.yaml` only | yes | no |
| Notes in `tmp/` | neither | neither |

---

## File map (the useful corners)

```text
have-fun-dont-die/
  README.md                         front door + generated catalogs
  ABOUT.md                          why this exists (not corpus)
  AGENTS.md                         law for writers
  HOW_TO_ASK_AGENTS_QUESTIONS.MD    Cursor / CLI / Claude how-to-ask
  HOW_DOES_THIS_THING_WORK.md       this file
  template.md                       headings only
  hallmarks/NN-short-name/report.md + sources/<mark>/
  topics/<slug>/                    same shape; non-molecules
  compounds/<slug>/                 same shape; molecules
  scripts/build-index.py            catalog tables
  scripts/index-meta.yaml           one-liners, CAS, status
  mcp/docs-rag/                     local search server + CLI
  .rag/                             generated index (gitignored)
  tmp/YYYY-MM-DD_<slug>/            scratch for a flight (gitignored)
  .cursor/skills/docs-rag/
  .cursor/skills/adversarial-research/   SKILL.md, prompts.md, examples.md
  .cursor/agents/rule-validation.md
  .cursor/rules/20-docs-rag.mdc
  .cursor/hooks.json                post-edit path recorder + stop follow-up
  .cursor/mcp.json                  Cursor starts docs-rag
  .mcp.json                         Claude Code starts docs-rag
  .claude/skills/                   Claude Code copies of the same skills
```

`topics/` is empty until someone researches a non-molecule subject. `compounds/` pages began as extracts from the hallmark reports; a full adversarial flight has not been run on every one of them. The catalogs say so.

---

## What this is not

- Not a doctor, not a protocol, not a store.
- Not a hosted “ask the repo” app. Please do not add one. The foundation is the writeups, the marks, the local index, and the skills.
- Not a requirement that you run agents at all. The markdown is readable by itself.
- Not a promise that the agents are right. They follow directions and they miss. When the miss is the repo or the agent config, `/self-improve` (or the self-improve skill) so the same failure does not recur. PRs that fix one failure, with an example of it failing and then succeeding, are the useful kind.

---

## If you only remember four things

1. **Ask** searches the notebook. **Research** writes new pages — when you ask for it, or when the notebook cannot answer.
2. Context is a **small pile**: rules + a search + the files the search pointed at. Helpers get a **briefing packet**, not your whole chat.
3. Three research agents argue the same claim from different jobs. A compiler merges them and checks links. Nobody is supposed to tidy away a fight.
4. After a save, run **both** indexes that apply, or the next session cannot find the work.

How to actually type the question: [HOW_TO_ASK_AGENTS_QUESTIONS.MD](HOW_TO_ASK_AGENTS_QUESTIONS.MD).
