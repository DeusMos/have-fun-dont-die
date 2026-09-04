# compounds/

Hallmark extracts, not researched dossiers. Hallmark reports own the biology; this tree owns identity, PK, animal vs human, nulls, toxicity, observed practice, and source quality. A full adversarial-research rewrite has not been run on these pages.

```
compounds/<slug>/report.md
compounds/<slug>/sources/<emoji>/
```

`<slug>` is lowercase hyphenated (`rapamycin`, not `Rapamycin` or `sirolimus`). Create the sources tree with:

```bash
bash .cursor/skills/adversarial-research/scripts/init-topic-sources.sh compounds/<slug>
```

A compound writeup does **not** land in `topics/`. Topics stay for non-molecule subjects. Marks, voice, and source rules are in `AGENTS.md`.

Ask what is already written with MCP `docs-rag` (`.cursor/skills/docs-rag/`). Research a molecule with `.cursor/skills/adversarial-research/` (Claude: `.claude/skills/adversarial-research/`).

## Slug and CAS rules

- Canonical name = the name this scene actually searches (`rapamycin`, not `sirolimus`; `fisetin`, not the IUPAC).
- INN, brand, and research codes go in Identity and in [`scripts/index-meta.yaml`](../scripts/index-meta.yaml) `aliases`.
- One dir per distinct chemical. Salts/esters that people treat as the same drug share a dir and **one primary CAS**. Distinct molecules get their own dir (`everolimus`, `rtb101`).
- Combo stacks (D+Q) do not get a second full dossier; each molecule owns a dir.
- No numeric prefix. Hallmark `NN-` is hallmark taxonomy.
- **CAS** is a first-class field on every report. Sidecar `cas:` is required once a dir exists: a registry number, a YAML list (first = primary), `pending`, or `none`.
- Live pages source CAS from a public listing. Use `CAS: pending` only until that listing is cited. Never guess.
- Biologics, live probiotics, fecal products, plasma, blends, or a class/cluster page: `CAS: none` or `not assigned` plus a one-line why.

## Catalog

Generated table (`python3 scripts/build-index.py`). Do not hand-edit the generated block. One-liners and `cas:` go in [`scripts/index-meta.yaml`](../scripts/index-meta.yaml).

<!-- BEGIN GENERATED: compounds-catalog -->
| Slug | CAS | Report | Last updated | One-line claim |
|---|---|---|---|---|
| [rapamycin](./rapamycin/report.md) | 53123-88-9 | [report.md](./rapamycin/report.md) | September 3, 2026 | ITP lifespan hit in mice; PEARL VAT null and RAPA-EX-01 chair-stand miss at weekly geroscience doses; transplant daily sirolimus has boxed infection/pneumonitis. |
| [everolimus](./everolimus/report.md) | 159351-69-6 | [report.md](./everolimus/report.md) | September 3, 2026 | Mannick Phase 2 vaccine-titer and infection-surrogate signals; not a lifespan or disability-free-survival result. |
| [rtb101](./rtb101/report.md) | 915019-65-7 | [report.md](./rtb101/report.md) | September 3, 2026 | Phase 3 winter respiratory-illness null in adults ≥65; the indication was dropped. |
| [metformin](./metformin/report.md) | 1115-70-4 | [report.md](./metformin/report.md) | September 3, 2026 | DPP indicated diabetes delay; ITP lifespan null; TAME not launched; Konopka vs Pilmark is a live exercise-adaptation fight. |
| [nicotinamide-riboside](./nicotinamide-riboside/report.md) | 1341-23-7 | [report.md](./nicotinamide-riboside/report.md) | September 3, 2026 | Raises blood NAD; ITP lifespan null; Dollerup clamp and muscle-respiration nulls; Elysium Basis is the storefront pair with pterostilbene. |
| [nicotinamide-mononucleotide](./nicotinamide-mononucleotide/report.md) | 1094-61-7 | [report.md](./nicotinamide-mononucleotide/report.md) | September 3, 2026 | Yoshino 2021 muscle insulin-sensitivity move in prediabetes; DoNotAge 500–1000 mg storefront; not sirtuin restoration. |
| [nad](./nad/report.md) | 53-84-9 | [report.md](./nad/report.md) | September 3, 2026 | Peach IV 100–1000 mg and AgelessRx nasal 30 mg are practice; IV vs oral vs nasal is an amateur split; blood NAD is target engagement, not genome or mito restoration. |
| [fisetin](./fisetin/report.md) | 528-48-3 | [report.md](./fisetin/report.md) | September 3, 2026 | ITP lifespan null; unformulated oral barely appears in plasma; Qualia 1400 mg pulse vs DoNotAge 800 mg daily vs Life Extension 56 mg weekly is an amateur split. |
| [dasatinib](./dasatinib/report.md) | 302962-49-8 | [report.md](./dasatinib/report.md) | September 3, 2026 | D+Q senolytic pilots are n=5–19; continuous CML Sprycel has an established pleural-effusion/PAH harm file; DIY gray-market pulses are forum practice. |
| [quercetin](./quercetin/report.md) | 117-39-5 | [report.md](./quercetin/report.md) | September 3, 2026 | Paired with dasatinib in the 2015 screen and human pilots; CSF undetectable in Gonzales AD; also sold inside Qualia/Life Extension/AMPK stacks. |
| [fucoidan](./fucoidan/report.md) | none | [report.md](./fucoidan/report.md) | September 3, 2026 | DoNotAge SIRT6Activator 800–2400 mg; Gorbunova 2025 preprint is male-mouse lifespan; NCT07500649 GrimAge primary is not mutation burden. |
| [spermidine](./spermidine/report.md) | 124-20-9 | [report.md](./spermidine/report.md) | September 3, 2026 | Autophagy-dependent lifespan in models; SmartAge 0.9 mg memory primary null; 1–2 mg wheat-germ vs 8 mg synthetic is an amateur split. |
| [urolithin-a](./urolithin-a/report.md) | 1143-70-0 | [report.md](./urolithin-a/report.md) | September 3, 2026 | Parkin-axis muscle signature at 500–1000 mg; missed Singh peak power and Liu 6MWT; mitophagy cargo, not general macroautophagy restoration. |
| [resveratrol](./resveratrol/report.md) | 501-36-0 | [report.md](./resveratrol/report.md) | September 3, 2026 | ITP lifespan null; Poulsen/Kjær human metabolic nulls; SIRT1-activator fight; SRT501 myeloma nephrotoxicity is established at that exposure. |
| [berberine](./berberine/report.md) | 2086-83-1 | [report.md](./berberine/report.md) | September 3, 2026 | Sold as AMPK / CR-mimetic (DoNotAge 500 mg, DiBerberine, AMPK Charge+); no compiled lifespan or healthy-aging RCT. |
| [colchicine](./colchicine/report.md) | 64-86-8 | [report.md](./colchicine/report.md) | September 3, 2026 | COLCOT/LoDoCo2 moved CAD events at 0.5 mg; CLEAR SYNERGY was null; clinic inflammaging use and CYP3A4/P-gp vs sirolimus are amateur practice. |
| [semaglutide](./semaglutide/report.md) | 910463-68-2 | [report.md](./semaglutide/report.md) | September 3, 2026 | SELECT cut MACE in obesity plus established CVD; relabeling that as nutrient-sensing restoration for healthy buyers is a definition swap. |
| [tirzepatide](./tirzepatide/report.md) | 2023788-19-2 | [report.md](./tirzepatide/report.md) | September 3, 2026 | Named on AgelessRx XPRIZE-finals copy next to weekly rapamycin; no healthy-person aging RCT. |
| [oxytocin](./oxytocin/report.md) | 50-56-6 | [report.md](./oxytocin/report.md) | September 3, 2026 | Pitocin is obstetric injectable; compounded IN/troche is the longevity SKU; Berger trait-loneliness null; Sikich ASD social-functioning null. |
| [beta-carotene](./beta-carotene/report.md) | 7235-40-7 | [report.md](./beta-carotene/report.md) | September 3, 2026 | ATBC and CARET raised lung cancer and death in smokers; DNA-protection framing does not survive those trials. |
<!-- END GENERATED -->

## Class groupings

Hand-maintained. Not extra dirs. Class/cluster pages are not used in v1; each distinct chemical owns a dir.

- **mTOR / rapalogs** — [rapamycin](./rapamycin/report.md), [everolimus](./everolimus/report.md), [rtb101](./rtb101/report.md)
- **NAD cluster** — [nad](./nad/report.md), [nicotinamide-riboside](./nicotinamide-riboside/report.md), [nicotinamide-mononucleotide](./nicotinamide-mononucleotide/report.md)
- **Senolytics** — [dasatinib](./dasatinib/report.md), [quercetin](./quercetin/report.md), [fisetin](./fisetin/report.md)
- **GLP-1 / incretins** — [semaglutide](./semaglutide/report.md), [tirzepatide](./tirzepatide/report.md)
- **Cleanup / mitophagy slogans** — [spermidine](./spermidine/report.md), [urolithin-a](./urolithin-a/report.md)
- **Other Tier A** — [metformin](./metformin/report.md), [fucoidan](./fucoidan/report.md), [colchicine](./colchicine/report.md), [resveratrol](./resveratrol/report.md), [berberine](./berberine/report.md), [oxytocin](./oxytocin/report.md), [beta-carotene](./beta-carotene/report.md)

## Section maps

Generated from `##` headings except Contents.

<!-- BEGIN GENERATED: compounds-section-maps -->
### rapamycin

[report.md](./rapamycin/report.md) · CAS: 53123-88-9 · Last updated: September 3, 2026

- [Identity](./rapamycin/report.md#identity)
- [The claim and the slogan](./rapamycin/report.md#the-claim-and-the-slogan)
- [Mechanism](./rapamycin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./rapamycin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./rapamycin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./rapamycin/report.md#human-data--aging-off-label-and-geroscience)
- [Toxicity and hazards](./rapamycin/report.md#toxicity-and-hazards)
- [Interactions](./rapamycin/report.md#interactions)
- [Formulations and source quality](./rapamycin/report.md#formulations-and-source-quality)
- [Observed practice](./rapamycin/report.md#observed-practice)
- [Fights](./rapamycin/report.md#fights)
- [Legal / access status](./rapamycin/report.md#legal--access-status)
- [Related hallmarks](./rapamycin/report.md#related-hallmarks)
- [Related compounds](./rapamycin/report.md#related-compounds)
- [Open questions](./rapamycin/report.md#open-questions)
- [What is actually on the table](./rapamycin/report.md#what-is-actually-on-the-table)

### everolimus

[report.md](./everolimus/report.md) · CAS: 159351-69-6 · Last updated: September 3, 2026

- [Identity](./everolimus/report.md#identity)
- [The claim and the slogan](./everolimus/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./everolimus/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — aging, off-label, and geroscience](./everolimus/report.md#human-data--aging-off-label-and-geroscience)
- [Legal / access status](./everolimus/report.md#legal--access-status)
- [Related hallmarks](./everolimus/report.md#related-hallmarks)
- [Related compounds](./everolimus/report.md#related-compounds)
- [Open questions](./everolimus/report.md#open-questions)
- [What is actually on the table](./everolimus/report.md#what-is-actually-on-the-table)

### rtb101

[report.md](./rtb101/report.md) · CAS: 915019-65-7 · Last updated: September 3, 2026

- [Identity](./rtb101/report.md#identity)
- [The claim and the slogan](./rtb101/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./rtb101/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — aging, off-label, and geroscience](./rtb101/report.md#human-data--aging-off-label-and-geroscience)
- [Nulls, failures, and replication](./rtb101/report.md#nulls-failures-and-replication)
- [Legal / access status](./rtb101/report.md#legal--access-status)
- [Related hallmarks](./rtb101/report.md#related-hallmarks)
- [Related compounds](./rtb101/report.md#related-compounds)
- [Open questions](./rtb101/report.md#open-questions)
- [What is actually on the table](./rtb101/report.md#what-is-actually-on-the-table)

### metformin

[report.md](./metformin/report.md) · CAS: 1115-70-4 · Last updated: September 3, 2026

- [Identity](./metformin/report.md#identity)
- [The claim and the slogan](./metformin/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./metformin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./metformin/report.md#animal-data)
- [Human data — labeled / indicated use](./metformin/report.md#human-data--labeled--indicated-use)
- [Human data — aging, off-label, and geroscience](./metformin/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./metformin/report.md#observed-practice)
- [Fights](./metformin/report.md#fights)
- [Legal / access status](./metformin/report.md#legal--access-status)
- [Related hallmarks](./metformin/report.md#related-hallmarks)
- [Related compounds](./metformin/report.md#related-compounds)
- [Open questions](./metformin/report.md#open-questions)
- [What is actually on the table](./metformin/report.md#what-is-actually-on-the-table)

### nicotinamide-riboside

[report.md](./nicotinamide-riboside/report.md) · CAS: 1341-23-7 · Last updated: September 3, 2026

- [Identity](./nicotinamide-riboside/report.md#identity)
- [The claim and the slogan](./nicotinamide-riboside/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./nicotinamide-riboside/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./nicotinamide-riboside/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./nicotinamide-riboside/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./nicotinamide-riboside/report.md#observed-practice)
- [Fights](./nicotinamide-riboside/report.md#fights)
- [Legal / access status](./nicotinamide-riboside/report.md#legal--access-status)
- [Related hallmarks](./nicotinamide-riboside/report.md#related-hallmarks)
- [Related compounds](./nicotinamide-riboside/report.md#related-compounds)
- [Open questions](./nicotinamide-riboside/report.md#open-questions)
- [What is actually on the table](./nicotinamide-riboside/report.md#what-is-actually-on-the-table)

### nicotinamide-mononucleotide

[report.md](./nicotinamide-mononucleotide/report.md) · CAS: 1094-61-7 · Last updated: September 3, 2026

- [Identity](./nicotinamide-mononucleotide/report.md#identity)
- [The claim and the slogan](./nicotinamide-mononucleotide/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./nicotinamide-mononucleotide/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — aging, off-label, and geroscience](./nicotinamide-mononucleotide/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./nicotinamide-mononucleotide/report.md#observed-practice)
- [Legal / access status](./nicotinamide-mononucleotide/report.md#legal--access-status)
- [Related hallmarks](./nicotinamide-mononucleotide/report.md#related-hallmarks)
- [Related compounds](./nicotinamide-mononucleotide/report.md#related-compounds)
- [Open questions](./nicotinamide-mononucleotide/report.md#open-questions)
- [What is actually on the table](./nicotinamide-mononucleotide/report.md#what-is-actually-on-the-table)

### nad

[report.md](./nad/report.md) · CAS: 53-84-9 · Last updated: September 3, 2026

- [Identity](./nad/report.md#identity)
- [The claim and the slogan](./nad/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./nad/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — aging, off-label, and geroscience](./nad/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./nad/report.md#observed-practice)
- [Fights](./nad/report.md#fights)
- [Legal / access status](./nad/report.md#legal--access-status)
- [Related hallmarks](./nad/report.md#related-hallmarks)
- [Related compounds](./nad/report.md#related-compounds)
- [Open questions](./nad/report.md#open-questions)
- [What is actually on the table](./nad/report.md#what-is-actually-on-the-table)

### fisetin

[report.md](./fisetin/report.md) · CAS: 528-48-3 · Last updated: September 3, 2026

- [Identity](./fisetin/report.md#identity)
- [The claim and the slogan](./fisetin/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./fisetin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./fisetin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./fisetin/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./fisetin/report.md#observed-practice)
- [Fights](./fisetin/report.md#fights)
- [Legal / access status](./fisetin/report.md#legal--access-status)
- [Related hallmarks](./fisetin/report.md#related-hallmarks)
- [Related compounds](./fisetin/report.md#related-compounds)
- [Open questions](./fisetin/report.md#open-questions)
- [What is actually on the table](./fisetin/report.md#what-is-actually-on-the-table)

### dasatinib

[report.md](./dasatinib/report.md) · CAS: 302962-49-8 · Last updated: September 3, 2026

- [Identity](./dasatinib/report.md#identity)
- [The claim and the slogan](./dasatinib/report.md#the-claim-and-the-slogan)
- [Mechanism](./dasatinib/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./dasatinib/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./dasatinib/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./dasatinib/report.md#human-data--aging-off-label-and-geroscience)
- [Toxicity and hazards](./dasatinib/report.md#toxicity-and-hazards)
- [Observed practice](./dasatinib/report.md#observed-practice)
- [Fights](./dasatinib/report.md#fights)
- [Legal / access status](./dasatinib/report.md#legal--access-status)
- [Related hallmarks](./dasatinib/report.md#related-hallmarks)
- [Related compounds](./dasatinib/report.md#related-compounds)
- [Open questions](./dasatinib/report.md#open-questions)
- [What is actually on the table](./dasatinib/report.md#what-is-actually-on-the-table)

### quercetin

[report.md](./quercetin/report.md) · CAS: 117-39-5 · Last updated: September 3, 2026

- [Identity](./quercetin/report.md#identity)
- [The claim and the slogan](./quercetin/report.md#the-claim-and-the-slogan)
- [Mechanism](./quercetin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./quercetin/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — aging, off-label, and geroscience](./quercetin/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./quercetin/report.md#observed-practice)
- [Fights](./quercetin/report.md#fights)
- [Legal / access status](./quercetin/report.md#legal--access-status)
- [Related hallmarks](./quercetin/report.md#related-hallmarks)
- [Related compounds](./quercetin/report.md#related-compounds)
- [Open questions](./quercetin/report.md#open-questions)
- [What is actually on the table](./quercetin/report.md#what-is-actually-on-the-table)

### fucoidan

[report.md](./fucoidan/report.md) · CAS: none · Last updated: September 3, 2026

- [Identity](./fucoidan/report.md#identity)
- [The claim and the slogan](./fucoidan/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./fucoidan/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./fucoidan/report.md#animal-data)
- [Observed practice](./fucoidan/report.md#observed-practice)
- [Legal / access status](./fucoidan/report.md#legal--access-status)
- [Related hallmarks](./fucoidan/report.md#related-hallmarks)
- [Related compounds](./fucoidan/report.md#related-compounds)
- [Open questions](./fucoidan/report.md#open-questions)
- [What is actually on the table](./fucoidan/report.md#what-is-actually-on-the-table)

### spermidine

[report.md](./spermidine/report.md) · CAS: 124-20-9 · Last updated: September 3, 2026

- [Identity](./spermidine/report.md#identity)
- [The claim and the slogan](./spermidine/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./spermidine/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./spermidine/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./spermidine/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./spermidine/report.md#observed-practice)
- [Fights](./spermidine/report.md#fights)
- [Legal / access status](./spermidine/report.md#legal--access-status)
- [Related hallmarks](./spermidine/report.md#related-hallmarks)
- [Related compounds](./spermidine/report.md#related-compounds)
- [Open questions](./spermidine/report.md#open-questions)
- [What is actually on the table](./spermidine/report.md#what-is-actually-on-the-table)

### urolithin-a

[report.md](./urolithin-a/report.md) · CAS: 1143-70-0 · Last updated: September 3, 2026

- [Identity](./urolithin-a/report.md#identity)
- [The claim and the slogan](./urolithin-a/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./urolithin-a/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./urolithin-a/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./urolithin-a/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./urolithin-a/report.md#observed-practice)
- [Fights](./urolithin-a/report.md#fights)
- [Legal / access status](./urolithin-a/report.md#legal--access-status)
- [Related hallmarks](./urolithin-a/report.md#related-hallmarks)
- [Related compounds](./urolithin-a/report.md#related-compounds)
- [Open questions](./urolithin-a/report.md#open-questions)
- [What is actually on the table](./urolithin-a/report.md#what-is-actually-on-the-table)

### resveratrol

[report.md](./resveratrol/report.md) · CAS: 501-36-0 · Last updated: September 3, 2026

- [Identity](./resveratrol/report.md#identity)
- [The claim and the slogan](./resveratrol/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./resveratrol/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./resveratrol/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./resveratrol/report.md#human-data--aging-off-label-and-geroscience)
- [Toxicity and hazards](./resveratrol/report.md#toxicity-and-hazards)
- [Observed practice](./resveratrol/report.md#observed-practice)
- [Fights](./resveratrol/report.md#fights)
- [Legal / access status](./resveratrol/report.md#legal--access-status)
- [Related hallmarks](./resveratrol/report.md#related-hallmarks)
- [Related compounds](./resveratrol/report.md#related-compounds)
- [Open questions](./resveratrol/report.md#open-questions)
- [What is actually on the table](./resveratrol/report.md#what-is-actually-on-the-table)

### berberine

[report.md](./berberine/report.md) · CAS: 2086-83-1 · Last updated: September 3, 2026

- [Identity](./berberine/report.md#identity)
- [The claim and the slogan](./berberine/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./berberine/report.md#pharmacokinetics--pharmacodynamics)
- [Observed practice](./berberine/report.md#observed-practice)
- [Legal / access status](./berberine/report.md#legal--access-status)
- [Related hallmarks](./berberine/report.md#related-hallmarks)
- [Related compounds](./berberine/report.md#related-compounds)
- [Open questions](./berberine/report.md#open-questions)
- [What is actually on the table](./berberine/report.md#what-is-actually-on-the-table)

### colchicine

[report.md](./colchicine/report.md) · CAS: 64-86-8 · Last updated: September 3, 2026

- [Identity](./colchicine/report.md#identity)
- [The claim and the slogan](./colchicine/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./colchicine/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — labeled / indicated use](./colchicine/report.md#human-data--labeled--indicated-use)
- [Observed practice](./colchicine/report.md#observed-practice)
- [Interactions](./colchicine/report.md#interactions)
- [Fights](./colchicine/report.md#fights)
- [Legal / access status](./colchicine/report.md#legal--access-status)
- [Related hallmarks](./colchicine/report.md#related-hallmarks)
- [Related compounds](./colchicine/report.md#related-compounds)
- [Open questions](./colchicine/report.md#open-questions)
- [What is actually on the table](./colchicine/report.md#what-is-actually-on-the-table)

### semaglutide

[report.md](./semaglutide/report.md) · CAS: 910463-68-2 · Last updated: September 3, 2026

- [Identity](./semaglutide/report.md#identity)
- [The claim and the slogan](./semaglutide/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./semaglutide/report.md#pharmacokinetics--pharmacodynamics)
- [Human data — labeled / indicated use](./semaglutide/report.md#human-data--labeled--indicated-use)
- [Legal / access status](./semaglutide/report.md#legal--access-status)
- [Related hallmarks](./semaglutide/report.md#related-hallmarks)
- [Related compounds](./semaglutide/report.md#related-compounds)
- [Open questions](./semaglutide/report.md#open-questions)
- [What is actually on the table](./semaglutide/report.md#what-is-actually-on-the-table)

### tirzepatide

[report.md](./tirzepatide/report.md) · CAS: 2023788-19-2 · Last updated: September 3, 2026

- [Identity](./tirzepatide/report.md#identity)
- [The claim and the slogan](./tirzepatide/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./tirzepatide/report.md#pharmacokinetics--pharmacodynamics)
- [Observed practice](./tirzepatide/report.md#observed-practice)
- [Legal / access status](./tirzepatide/report.md#legal--access-status)
- [Related hallmarks](./tirzepatide/report.md#related-hallmarks)
- [Related compounds](./tirzepatide/report.md#related-compounds)
- [Open questions](./tirzepatide/report.md#open-questions)
- [What is actually on the table](./tirzepatide/report.md#what-is-actually-on-the-table)

### oxytocin

[report.md](./oxytocin/report.md) · CAS: 50-56-6 · Last updated: September 3, 2026

- [Identity](./oxytocin/report.md#identity)
- [The claim and the slogan](./oxytocin/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./oxytocin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./oxytocin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./oxytocin/report.md#human-data--aging-off-label-and-geroscience)
- [Observed practice](./oxytocin/report.md#observed-practice)
- [Fights](./oxytocin/report.md#fights)
- [Legal / access status](./oxytocin/report.md#legal--access-status)
- [Related hallmarks](./oxytocin/report.md#related-hallmarks)
- [Related compounds](./oxytocin/report.md#related-compounds)
- [Open questions](./oxytocin/report.md#open-questions)
- [What is actually on the table](./oxytocin/report.md#what-is-actually-on-the-table)

### beta-carotene

[report.md](./beta-carotene/report.md) · CAS: 7235-40-7 · Last updated: September 3, 2026

- [Identity](./beta-carotene/report.md#identity)
- [The claim and the slogan](./beta-carotene/report.md#the-claim-and-the-slogan)
- [Pharmacokinetics / pharmacodynamics](./beta-carotene/report.md#pharmacokinetics--pharmacodynamics)
- [Toxicity and hazards](./beta-carotene/report.md#toxicity-and-hazards)
- [Legal / access status](./beta-carotene/report.md#legal--access-status)
- [Related hallmarks](./beta-carotene/report.md#related-hallmarks)
- [Related compounds](./beta-carotene/report.md#related-compounds)
- [Open questions](./beta-carotene/report.md#open-questions)
- [What is actually on the table](./beta-carotene/report.md#what-is-actually-on-the-table)
<!-- END GENERATED -->
