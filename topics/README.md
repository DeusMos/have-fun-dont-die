# topics/

First-class writeups that are not one of the 14 hallmarks and are not a named molecule. Same shape as `hallmarks/NN-short-name/`. A compound lands at `compounds/<slug>/`, not here.

```
topics/<slug>/report.md
topics/<slug>/sources/<emoji>/
```

`<slug>` is lowercase hyphenated (`hbot`, `chip-panels`). Create the sources tree with:

```bash
bash .cursor/skills/adversarial-research/scripts/init-topic-sources.sh topics/<slug>
```

Ask what is already written with MCP `docs-rag` (`.cursor/skills/docs-rag/`). Research a subject with `.cursor/skills/adversarial-research/` (Claude: `.claude/skills/adversarial-research/`). Marks, voice, and source rules are in `AGENTS.md`.

## Catalog

Generated table (`python3 scripts/build-index.py`). Do not hand-edit the generated block. One-liners go in [`scripts/index-meta.yaml`](../scripts/index-meta.yaml).

<!-- BEGIN GENERATED: topics-catalog -->
| Slug | Report | Last updated | One-line claim |
|---|---|---|---|
<!-- END GENERATED -->
