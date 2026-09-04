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
| [crispr](./crispr/report.md) | [report.md](./crispr/report.md) | September 3, 2026 | RNA-guided Cas plus host repair (or a fused deaminase/RT) writes a genotype distribution; Casgevy is one ex vivo HSPC product, liver LNP is not whole-body rewrite, and no CRISPR aging RCT was found. |
| [enamel-remineralization-gel](./enamel-remineralization-gel/report.md) | [report.md](./enamel-remineralization-gel/report.md) | September 3, 2026 | The 2025–2026 enamel-regrowth gel is several SKUs: Hasan 2025 ~10 μm extracted-tooth ELR film (Epinamel, no in-mouth results), chairside P11-4/Curodont (live RCT fight vs fluoride), and consumer nano-HA / CPP-ACP pastes. |
| [salamander-like-regeneration](./salamander-like-regeneration/report.md) | [report.md](./salamander-like-regeneration/report.md) | September 3, 2026 | 2026 PNAS: conserved SP6/SP8 plus zebrafish-LEN FGF8 AAV partially rescues or speeds mouse P3 digit bone; not a salamander-gene transplant and not whole-limb regeneration. |
<!-- END GENERATED -->
