# Post-edit validation hooks

Project hooks. Cursor loads [`.cursor/hooks.json`](../hooks.json) in a trusted workspace and on cloud agents. User-level `~/.cursor/hooks.json` is a different file; this repo does not use it.

## Limitation

Cursor hooks **cannot spawn Task/subagents**. `afterFileEdit` has no `followup_message` and no agent-invoke field. The supported way to request agent work is a `stop` hook that returns `followup_message`, which Cursor submits as the next user message. The parent agent then launches the named subagent(s). Same pattern as the continual-learning plugin.

## Events

| Event | Script | What it does |
|---|---|---|
| `afterFileEdit` | `python3 .cursor/hooks/post_edit_validation.py record` | Reads `{file_path, edits}` from stdin. Classifies the path (prefix / filename convention only). Records relevant repo-relative paths under `.cursor/hooks/state/` (gitignored). Does not run an LLM and does not read the user prompt. |
| `stop` | `python3 .cursor/hooks/post_edit_validation.py stop` | If the agent turn `completed` and the queue is non-empty, returns `{followup_message}` asking the parent to launch `rule-validation`, plus `test-engineer` and/or `pr-reviewer` when those path buckets are present. `loop_limit` is 2 so a fix-up recheck can run once. |

Tab completions use `afterTabFileEdit`, which this repo does not hook. One agent keystroke / Tab accept must not launch reviewers.

## Path buckets (not intent)

The script never inspects file contents or the user message. It only looks at the repo-relative path:

- skip: `tmp/`, `.rag/`, `.git/`, hook state, known secret filenames (`.env`, `*.pem`, `credentials.json`)
- reports: `hallmarks/`, `topics/`, `compounds/`
- rules: `AGENTS.md`, `template.md`, `.cursor/`, `.claude/`, `HOW_TO_ASK_AGENTS_QUESTIONS.MD`
- tests: a `tests`/`test` path segment, or `test_*.py` / `*_test.py` / `*.test.ts` filename convention
- code: `mcp/`, `scripts/`, or `*.py` / `*.ts` / `*.tsx` / `*.js` / `*.jsx` / `*.go`
- other: anything else in the repo (still gets `rule-validation`)

Agents requested on stop:

- always, if anything was recorded: `rule-validation`
- if any path is in **tests**: also `test-engineer`
- if any path is in **code** and none is in **tests**: also `pr-reviewer`

`security-review`, `bugbot`, and `thermo-nuclear-code-quality-review` are not auto-requested.

## Enable

1. Trust this workspace when Cursor asks.
2. Confirm the hooks appear under **Cursor Settings → Hooks**. Cursor reloads `hooks.json` on save; restart Cursor if they do not show.
3. First run may prompt to allow the hook command (`python3 .cursor/hooks/post_edit_validation.py`).
4. Cloud agents pick up project hooks only (not `~/.cursor/hooks.json`).

Hook script tests (path classification and stdin JSON protocol):

```bash
uv run --with pytest pytest .cursor/hooks/test_post_edit_validation.py
```

Manual review without waiting for `stop`:

```
Use the rule-validation subagent on the current diff.
```

## State and artifacts

- Queue: `.cursor/hooks/state/post-edit-validation.json` (gitignored, created on first edit)
- Review writeups: `./tmp/YYYY-MM-DD_rule-validation/` (gitignored)

No secrets in this directory. The scripts read stdin JSON from Cursor and write paths plus a follow-up string.
