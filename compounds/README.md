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
| [hexarelin](./hexarelin/report.md) | 208251-52-9 | [report.md](./hexarelin/report.md) | September 3, 2026 | Mindful Research 5 mg research-chem vial; GHRP storefront extract; no compiled aging RCT on this page. |
| [5-amino-1mq](./5-amino-1mq/report.md) | 42464-96-0 | [report.md](./5-amino-1mq/report.md) | September 3, 2026 | Mindful Research 5–50 mg NNMTi powder; storefront extract; no compiled aging RCT on this page. |
| [testagen](./testagen/report.md) | 1026993-38-3 | [report.md](./testagen/report.md) | September 3, 2026 | Mindful Research 20 mg KEDG tetrapeptide; Khavinson-class storefront extract; no compiled aging RCT on this page. |
| [pinealon](./pinealon/report.md) | 175175-23-2 | [report.md](./pinealon/report.md) | September 3, 2026 | Mindful Research 20 mg EDR tripeptide; Khavinson-class storefront extract; no compiled aging RCT on this page. |
| [kisspeptin-10](./kisspeptin-10/report.md) | 374675-21-5 | [report.md](./kisspeptin-10/report.md) | September 3, 2026 | Mindful Research 5 mg KP-10 vial; GnRH-axis storefront extract; no compiled aging RCT on this page. |
| [orforglipron](./orforglipron/report.md) | 2212020-52-3 | [report.md](./orforglipron/report.md) | September 3, 2026 | Mindful Research 1–3 mg oral capsules with SNAC; non-peptide GLP-1 storefront extract; no compiled aging RCT on this page. |
| [aniracetam](./aniracetam/report.md) | 72432-10-1 | [report.md](./aniracetam/report.md) | September 3, 2026 | Mindful Research 750 mg racetam capsules; nootropic storefront extract; no compiled aging RCT on this page. |
| [epithalon](./epithalon/report.md) | 307297-39-8 | [report.md](./epithalon/report.md) | September 3, 2026 | Mindful Research 10 mg vial and 3 mg capsules; telomere-slogan peptide; storefront extract; no compiled aging RCT on this page. |
| [enclomiphene](./enclomiphene/report.md) | 7599-79-3 | [report.md](./enclomiphene/report.md) | September 3, 2026 | Mindful Research 12.5 mg SERM capsules with piperine; storefront extract; no compiled aging RCT on this page. |
| [methylcobalamin](./methylcobalamin/report.md) | 13422-55-4 | [report.md](./methylcobalamin/report.md) | September 3, 2026 | Mindful Research 1.5 mg/mL methyl-B12 ampoule; also 1 mg/mL inside LIPO-C; vitamin SKU, not an aging trial. |
| [cyanocobalamin](./cyanocobalamin/report.md) | 68-19-9 | [report.md](./cyanocobalamin/report.md) | September 3, 2026 | Mindful Research cyanocobalamin 10 mg/10 mL and 0.5 mg ampoule; vitamin SKU, not an aging trial. |
| [dsip](./dsip/report.md) | 62568-57-4 | [report.md](./dsip/report.md) | September 3, 2026 | Mindful Research 5 mg DSIP vial; sleep-slogan peptide; storefront extract; no compiled aging RCT on this page. |
| [retatrutide](./retatrutide/report.md) | 2381089-83-2 | [report.md](./retatrutide/report.md) | September 3, 2026 | Mindful Research RT-GLP3 10–30 mg lists CAS 2381089-83-2; tri-agonist storefront extract; no compiled aging RCT on this page. |
| [mazdutide](./mazdutide/report.md) | 2259884-03-0 | [report.md](./mazdutide/report.md) | September 3, 2026 | Mindful Research 10 mg oxyntomodulin analogue; GLP-1/glucagon storefront extract; no compiled aging RCT on this page. |
| [cagrilintide](./cagrilintide/report.md) | 1415456-99-3 | [report.md](./cagrilintide/report.md) | September 3, 2026 | Mindful Research 5–10 mg amylin analogue; storefront extract; no compiled aging RCT on this page. |
| [tesofensine](./tesofensine/report.md) | 402856-42-2 | [report.md](./tesofensine/report.md) | September 3, 2026 | Mindful Research 500 mcg triple-reuptake capsules; storefront extract; no compiled aging RCT on this page. |
| [hcg](./hcg/report.md) | 9002-61-3 | [report.md](./hcg/report.md) | September 3, 2026 | Mindful Research 5000 IU research-chem vial; LH-analogue storefront extract; no compiled aging RCT on this page. |
| [l-carnitine](./l-carnitine/report.md) | 541-15-1 | [report.md](./l-carnitine/report.md) | September 3, 2026 | Mindful Research 600 mg/mL concentrate and MIC-shot blends; carnitine-shuttle SKU, not an aging trial. |
| [ara-290](./ara-290/report.md) | 1208243-50-8 | [report.md](./ara-290/report.md) | September 3, 2026 | Mindful Research 10 mg EPO-helix-B peptide; storefront extract; no compiled aging RCT on this page. |
| [slu-pp-332](./slu-pp-332/report.md) | 303760-60-3 | [report.md](./slu-pp-332/report.md) | September 3, 2026 | Mindful Research 1000 mcg capsules; exercise-mimetic chatter SKU; storefront extract; no compiled aging RCT on this page. |
| [melanotan-1](./melanotan-1/report.md) | 75921-69-6 | [report.md](./melanotan-1/report.md) | September 3, 2026 | Mindful Research 10 mg MT-1 / afamelanotide; melanocortin storefront extract; no compiled aging RCT on this page. |
| [melanotan-2](./melanotan-2/report.md) | 121062-08-6 | [report.md](./melanotan-2/report.md) | September 3, 2026 | Mindful Research 10 mg MT-2; melanocortin storefront extract; no compiled aging RCT on this page. |
| [thymosin-alpha-1](./thymosin-alpha-1/report.md) | 62304-98-7 | [report.md](./thymosin-alpha-1/report.md) | September 3, 2026 | Mindful Research 10 mg thymalfasin; TRIIM-adjacent storefront extract; no compiled aging RCT on this page. |
| [glutathione](./glutathione/report.md) | 70-18-8 | [report.md](./glutathione/report.md) | September 3, 2026 | Mindful Research 600 mg reduced GSH vial; antioxidant SKU, not an aging trial. |
| [cerebrolysin](./cerebrolysin/report.md) | 12656-61-0 | [report.md](./cerebrolysin/report.md) | September 3, 2026 | Mindful Research 60 mg cerebroprotein hydrolysate; mixture SKU with listed CAS 12656-61-0; no compiled aging RCT on this page. |
| [kpv](./kpv/report.md) | 67727-97-3 | [report.md](./kpv/report.md) | September 3, 2026 | Mindful Research 5–10 mg α-MSH fragment and KLOW blend constituent; storefront extract; no compiled aging RCT on this page. |
| [ss-31](./ss-31/report.md) | 736992-21-5 | [report.md](./ss-31/report.md) | September 3, 2026 | Mindful Research 10–50 mg elamipretide; Forzinity is Barth, not aging; storefront extract plus 07 mention. |
| [igf-1-lr3](./igf-1-lr3/report.md) | 946870-92-4 | [report.md](./igf-1-lr3/report.md) | September 3, 2026 | Mindful Research 0.1–1 mg Long Arg3-IGF-1; storefront extract; no compiled aging RCT on this page. |
| [cjc-1295-no-dac](./cjc-1295-no-dac/report.md) | 863288-34-0 | [report.md](./cjc-1295-no-dac/report.md) | September 3, 2026 | Mindful Research 5 mg Mod GRF (1-29) and 5/5 mg blend with ipamorelin; storefront extract; no compiled aging RCT on this page. |
| [b7-33](./b7-33/report.md) | 1818415-56-3 | [report.md](./b7-33/report.md) | September 3, 2026 | Mindful Research 10 mg relaxin-family single-chain analogue; storefront extract; no compiled aging RCT on this page. |
| [sermorelin](./sermorelin/report.md) | 86168-78-7 | [report.md](./sermorelin/report.md) | September 3, 2026 | Mindful Research 5 mg GHRH 1-29; AgelessRx names nasal sermorelin next to rapamycin; no compiled aging RCT on this page. |
| [selank](./selank/report.md) | 129954-34-3 | [report.md](./selank/report.md) | September 3, 2026 | Mindful Research 10 mg tuftsin analogue; nootropic storefront extract; no compiled aging RCT on this page. |
| [tb-500](./tb-500/report.md) | 77591-33-4 | [report.md](./tb-500/report.md) | September 3, 2026 | Mindful Research 10 mg thymosin β4 and blend constituent; storefront extract; no compiled aging RCT on this page. |
| [semax](./semax/report.md) | 80714-61-0 | [report.md](./semax/report.md) | September 3, 2026 | Mindful Research 10 mg ACTH(4-10) analogue; nootropic storefront extract; no compiled aging RCT on this page. |
| [ipamorelin](./ipamorelin/report.md) | 170851-70-4 | [report.md](./ipamorelin/report.md) | September 3, 2026 | Mindful Research 4 mg GHRP and 5/5 mg blend with CJC no DAC; storefront extract; no compiled aging RCT on this page. |
| [mots-c](./mots-c/report.md) | 1627580-64-6 | [report.md](./mots-c/report.md) | September 3, 2026 | Mindful Research 10–40 mg mtDNA-encoded peptide; Reynolds mouse capacity is not a human restore trial; 07 extract plus storefront SKU. |
| [tesamorelin](./tesamorelin/report.md) | 901758-09-6 | [report.md](./tesamorelin/report.md) | September 3, 2026 | Mindful Research 10 mg GHRH analogue; Egrifta is HIV lipodystrophy; TRIIM-adjacent amateur use; no compiled healthy-aging RCT on this page. |
| [pt-141](./pt-141/report.md) | 189691-06-3 | [report.md](./pt-141/report.md) | September 3, 2026 | Mindful Research 9 mg bremelanotide; labeled HSDD drug sold as research powder; no compiled aging RCT on this page. |
| [snap-8](./snap-8/report.md) | 868844-74-0 | [report.md](./snap-8/report.md) | September 3, 2026 | Mindful Research 9 mg SNAP-25 analogue; cosmetic-peptide storefront extract; no compiled aging RCT on this page. |
| [bpc-157](./bpc-157/report.md) | 137525-51-0 | [report.md](./bpc-157/report.md) | September 3, 2026 | Mindful Research 10 mg vial, capsules, and GLOW/KLOW blends; 12 leaky-gut slogan peptide; storefront extract; no compiled aging RCT on this page. |
| [ghk-cu](./ghk-cu/report.md) | 89030-95-5 | [report.md](./ghk-cu/report.md) | September 3, 2026 | Mindful Research 50–100 mg copper tripeptide plus GLOW/KLOW/REJUV-3X; 13 extract: rat wound collagen is not a human restore trial. |
| [aod-9604](./aod-9604/report.md) | 386264-39-7 | [report.md](./aod-9604/report.md) | September 3, 2026 | Mindful Research 4 mg hGH fragment 176–191; fat-loss storefront extract; no compiled aging RCT on this page. |
| [ahk-cu](./ahk-cu/report.md) | 49557-75-7 | [report.md](./ahk-cu/report.md) | September 3, 2026 | Mindful Research sells AHK-Cu only inside REJUV-3X at 15 mg/mL; no solo vial on the September 3, 2026 pull. |
| [jxl-069](./jxl-069/report.md) | 2232594-65-1 | [report.md](./jxl-069/report.md) | September 3, 2026 | Mindful Research sells JXL-069 only inside REJUV-3X at 0.1 mg/mL; MPC-inhibitor storefront extract; no compiled aging RCT on this page. |
<!-- END GENERATED -->

## Class groupings

Hand-maintained. Not extra dirs. Class/cluster pages are not used in v1; each distinct chemical owns a dir.

- **mTOR / rapalogs** — [rapamycin](./rapamycin/report.md), [everolimus](./everolimus/report.md), [rtb101](./rtb101/report.md)
- **NAD cluster** — [nad](./nad/report.md), [nicotinamide-riboside](./nicotinamide-riboside/report.md), [nicotinamide-mononucleotide](./nicotinamide-mononucleotide/report.md)
- **Senolytics** — [dasatinib](./dasatinib/report.md), [quercetin](./quercetin/report.md), [fisetin](./fisetin/report.md)
- **GLP-1 / incretins** — [semaglutide](./semaglutide/report.md), [tirzepatide](./tirzepatide/report.md), [retatrutide](./retatrutide/report.md), [mazdutide](./mazdutide/report.md), [cagrilintide](./cagrilintide/report.md), [orforglipron](./orforglipron/report.md)
- **GH axis** — [tesamorelin](./tesamorelin/report.md), [sermorelin](./sermorelin/report.md), [ipamorelin](./ipamorelin/report.md), [cjc-1295-no-dac](./cjc-1295-no-dac/report.md), [hexarelin](./hexarelin/report.md), [igf-1-lr3](./igf-1-lr3/report.md)
- **Repair / ECM slogans** — [bpc-157](./bpc-157/report.md), [tb-500](./tb-500/report.md), [ghk-cu](./ghk-cu/report.md), [kpv](./kpv/report.md)
- **Mito peptides** — [mots-c](./mots-c/report.md), [ss-31](./ss-31/report.md)
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
- [Observed practice](./semaglutide/report.md#observed-practice)
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

### hexarelin

[report.md](./hexarelin/report.md) · CAS: 208251-52-9 · Last updated: September 3, 2026

- [Identity](./hexarelin/report.md#identity)
- [The claim and the slogan](./hexarelin/report.md#the-claim-and-the-slogan)
- [Mechanism](./hexarelin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./hexarelin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./hexarelin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./hexarelin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./hexarelin/report.md#formulations-and-source-quality)
- [Observed practice](./hexarelin/report.md#observed-practice)
- [Legal / access status](./hexarelin/report.md#legal--access-status)
- [Related hallmarks](./hexarelin/report.md#related-hallmarks)
- [Related compounds](./hexarelin/report.md#related-compounds)
- [Open questions](./hexarelin/report.md#open-questions)
- [What is actually on the table](./hexarelin/report.md#what-is-actually-on-the-table)

### 5-amino-1mq

[report.md](./5-amino-1mq/report.md) · CAS: 42464-96-0 · Last updated: September 3, 2026

- [Identity](./5-amino-1mq/report.md#identity)
- [The claim and the slogan](./5-amino-1mq/report.md#the-claim-and-the-slogan)
- [Mechanism](./5-amino-1mq/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./5-amino-1mq/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./5-amino-1mq/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./5-amino-1mq/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./5-amino-1mq/report.md#formulations-and-source-quality)
- [Observed practice](./5-amino-1mq/report.md#observed-practice)
- [Legal / access status](./5-amino-1mq/report.md#legal--access-status)
- [Related hallmarks](./5-amino-1mq/report.md#related-hallmarks)
- [Related compounds](./5-amino-1mq/report.md#related-compounds)
- [Open questions](./5-amino-1mq/report.md#open-questions)
- [What is actually on the table](./5-amino-1mq/report.md#what-is-actually-on-the-table)

### testagen

[report.md](./testagen/report.md) · CAS: 1026993-38-3 · Last updated: September 3, 2026

- [Identity](./testagen/report.md#identity)
- [The claim and the slogan](./testagen/report.md#the-claim-and-the-slogan)
- [Mechanism](./testagen/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./testagen/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./testagen/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./testagen/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./testagen/report.md#formulations-and-source-quality)
- [Observed practice](./testagen/report.md#observed-practice)
- [Legal / access status](./testagen/report.md#legal--access-status)
- [Related hallmarks](./testagen/report.md#related-hallmarks)
- [Related compounds](./testagen/report.md#related-compounds)
- [Open questions](./testagen/report.md#open-questions)
- [What is actually on the table](./testagen/report.md#what-is-actually-on-the-table)

### pinealon

[report.md](./pinealon/report.md) · CAS: 175175-23-2 · Last updated: September 3, 2026

- [Identity](./pinealon/report.md#identity)
- [The claim and the slogan](./pinealon/report.md#the-claim-and-the-slogan)
- [Mechanism](./pinealon/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./pinealon/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./pinealon/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./pinealon/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./pinealon/report.md#formulations-and-source-quality)
- [Observed practice](./pinealon/report.md#observed-practice)
- [Legal / access status](./pinealon/report.md#legal--access-status)
- [Related hallmarks](./pinealon/report.md#related-hallmarks)
- [Related compounds](./pinealon/report.md#related-compounds)
- [Open questions](./pinealon/report.md#open-questions)
- [What is actually on the table](./pinealon/report.md#what-is-actually-on-the-table)

### kisspeptin-10

[report.md](./kisspeptin-10/report.md) · CAS: 374675-21-5 · Last updated: September 3, 2026

- [Identity](./kisspeptin-10/report.md#identity)
- [The claim and the slogan](./kisspeptin-10/report.md#the-claim-and-the-slogan)
- [Mechanism](./kisspeptin-10/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./kisspeptin-10/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./kisspeptin-10/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./kisspeptin-10/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./kisspeptin-10/report.md#formulations-and-source-quality)
- [Observed practice](./kisspeptin-10/report.md#observed-practice)
- [Legal / access status](./kisspeptin-10/report.md#legal--access-status)
- [Related hallmarks](./kisspeptin-10/report.md#related-hallmarks)
- [Related compounds](./kisspeptin-10/report.md#related-compounds)
- [Open questions](./kisspeptin-10/report.md#open-questions)
- [What is actually on the table](./kisspeptin-10/report.md#what-is-actually-on-the-table)

### orforglipron

[report.md](./orforglipron/report.md) · CAS: 2212020-52-3 · Last updated: September 3, 2026

- [Identity](./orforglipron/report.md#identity)
- [The claim and the slogan](./orforglipron/report.md#the-claim-and-the-slogan)
- [Mechanism](./orforglipron/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./orforglipron/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./orforglipron/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./orforglipron/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./orforglipron/report.md#formulations-and-source-quality)
- [Observed practice](./orforglipron/report.md#observed-practice)
- [Legal / access status](./orforglipron/report.md#legal--access-status)
- [Related hallmarks](./orforglipron/report.md#related-hallmarks)
- [Related compounds](./orforglipron/report.md#related-compounds)
- [Open questions](./orforglipron/report.md#open-questions)
- [What is actually on the table](./orforglipron/report.md#what-is-actually-on-the-table)

### aniracetam

[report.md](./aniracetam/report.md) · CAS: 72432-10-1 · Last updated: September 3, 2026

- [Identity](./aniracetam/report.md#identity)
- [The claim and the slogan](./aniracetam/report.md#the-claim-and-the-slogan)
- [Mechanism](./aniracetam/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./aniracetam/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./aniracetam/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./aniracetam/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./aniracetam/report.md#formulations-and-source-quality)
- [Observed practice](./aniracetam/report.md#observed-practice)
- [Legal / access status](./aniracetam/report.md#legal--access-status)
- [Related hallmarks](./aniracetam/report.md#related-hallmarks)
- [Related compounds](./aniracetam/report.md#related-compounds)
- [Open questions](./aniracetam/report.md#open-questions)
- [What is actually on the table](./aniracetam/report.md#what-is-actually-on-the-table)

### epithalon

[report.md](./epithalon/report.md) · CAS: 307297-39-8 · Last updated: September 3, 2026

- [Identity](./epithalon/report.md#identity)
- [The claim and the slogan](./epithalon/report.md#the-claim-and-the-slogan)
- [Mechanism](./epithalon/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./epithalon/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./epithalon/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./epithalon/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./epithalon/report.md#formulations-and-source-quality)
- [Observed practice](./epithalon/report.md#observed-practice)
- [Legal / access status](./epithalon/report.md#legal--access-status)
- [Related hallmarks](./epithalon/report.md#related-hallmarks)
- [Related compounds](./epithalon/report.md#related-compounds)
- [Open questions](./epithalon/report.md#open-questions)
- [What is actually on the table](./epithalon/report.md#what-is-actually-on-the-table)

### enclomiphene

[report.md](./enclomiphene/report.md) · CAS: 7599-79-3 · Last updated: September 3, 2026

- [Identity](./enclomiphene/report.md#identity)
- [The claim and the slogan](./enclomiphene/report.md#the-claim-and-the-slogan)
- [Mechanism](./enclomiphene/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./enclomiphene/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./enclomiphene/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./enclomiphene/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./enclomiphene/report.md#formulations-and-source-quality)
- [Observed practice](./enclomiphene/report.md#observed-practice)
- [Legal / access status](./enclomiphene/report.md#legal--access-status)
- [Related hallmarks](./enclomiphene/report.md#related-hallmarks)
- [Related compounds](./enclomiphene/report.md#related-compounds)
- [Open questions](./enclomiphene/report.md#open-questions)
- [What is actually on the table](./enclomiphene/report.md#what-is-actually-on-the-table)

### methylcobalamin

[report.md](./methylcobalamin/report.md) · CAS: 13422-55-4 · Last updated: September 3, 2026

- [Identity](./methylcobalamin/report.md#identity)
- [The claim and the slogan](./methylcobalamin/report.md#the-claim-and-the-slogan)
- [Mechanism](./methylcobalamin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./methylcobalamin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./methylcobalamin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./methylcobalamin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./methylcobalamin/report.md#formulations-and-source-quality)
- [Observed practice](./methylcobalamin/report.md#observed-practice)
- [Legal / access status](./methylcobalamin/report.md#legal--access-status)
- [Related hallmarks](./methylcobalamin/report.md#related-hallmarks)
- [Related compounds](./methylcobalamin/report.md#related-compounds)
- [Open questions](./methylcobalamin/report.md#open-questions)
- [What is actually on the table](./methylcobalamin/report.md#what-is-actually-on-the-table)

### cyanocobalamin

[report.md](./cyanocobalamin/report.md) · CAS: 68-19-9 · Last updated: September 3, 2026

- [Identity](./cyanocobalamin/report.md#identity)
- [The claim and the slogan](./cyanocobalamin/report.md#the-claim-and-the-slogan)
- [Mechanism](./cyanocobalamin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./cyanocobalamin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./cyanocobalamin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./cyanocobalamin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./cyanocobalamin/report.md#formulations-and-source-quality)
- [Observed practice](./cyanocobalamin/report.md#observed-practice)
- [Legal / access status](./cyanocobalamin/report.md#legal--access-status)
- [Related hallmarks](./cyanocobalamin/report.md#related-hallmarks)
- [Related compounds](./cyanocobalamin/report.md#related-compounds)
- [Open questions](./cyanocobalamin/report.md#open-questions)
- [What is actually on the table](./cyanocobalamin/report.md#what-is-actually-on-the-table)

### dsip

[report.md](./dsip/report.md) · CAS: 62568-57-4 · Last updated: September 3, 2026

- [Identity](./dsip/report.md#identity)
- [The claim and the slogan](./dsip/report.md#the-claim-and-the-slogan)
- [Mechanism](./dsip/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./dsip/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./dsip/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./dsip/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./dsip/report.md#formulations-and-source-quality)
- [Observed practice](./dsip/report.md#observed-practice)
- [Legal / access status](./dsip/report.md#legal--access-status)
- [Related hallmarks](./dsip/report.md#related-hallmarks)
- [Related compounds](./dsip/report.md#related-compounds)
- [Open questions](./dsip/report.md#open-questions)
- [What is actually on the table](./dsip/report.md#what-is-actually-on-the-table)

### retatrutide

[report.md](./retatrutide/report.md) · CAS: 2381089-83-2 · Last updated: September 3, 2026

- [Identity](./retatrutide/report.md#identity)
- [The claim and the slogan](./retatrutide/report.md#the-claim-and-the-slogan)
- [Mechanism](./retatrutide/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./retatrutide/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./retatrutide/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./retatrutide/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./retatrutide/report.md#formulations-and-source-quality)
- [Observed practice](./retatrutide/report.md#observed-practice)
- [Legal / access status](./retatrutide/report.md#legal--access-status)
- [Related hallmarks](./retatrutide/report.md#related-hallmarks)
- [Related compounds](./retatrutide/report.md#related-compounds)
- [Open questions](./retatrutide/report.md#open-questions)
- [What is actually on the table](./retatrutide/report.md#what-is-actually-on-the-table)

### mazdutide

[report.md](./mazdutide/report.md) · CAS: 2259884-03-0 · Last updated: September 3, 2026

- [Identity](./mazdutide/report.md#identity)
- [The claim and the slogan](./mazdutide/report.md#the-claim-and-the-slogan)
- [Mechanism](./mazdutide/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./mazdutide/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./mazdutide/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./mazdutide/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./mazdutide/report.md#formulations-and-source-quality)
- [Observed practice](./mazdutide/report.md#observed-practice)
- [Legal / access status](./mazdutide/report.md#legal--access-status)
- [Related hallmarks](./mazdutide/report.md#related-hallmarks)
- [Related compounds](./mazdutide/report.md#related-compounds)
- [Open questions](./mazdutide/report.md#open-questions)
- [What is actually on the table](./mazdutide/report.md#what-is-actually-on-the-table)

### cagrilintide

[report.md](./cagrilintide/report.md) · CAS: 1415456-99-3 · Last updated: September 3, 2026

- [Identity](./cagrilintide/report.md#identity)
- [The claim and the slogan](./cagrilintide/report.md#the-claim-and-the-slogan)
- [Mechanism](./cagrilintide/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./cagrilintide/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./cagrilintide/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./cagrilintide/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./cagrilintide/report.md#formulations-and-source-quality)
- [Observed practice](./cagrilintide/report.md#observed-practice)
- [Legal / access status](./cagrilintide/report.md#legal--access-status)
- [Related hallmarks](./cagrilintide/report.md#related-hallmarks)
- [Related compounds](./cagrilintide/report.md#related-compounds)
- [Open questions](./cagrilintide/report.md#open-questions)
- [What is actually on the table](./cagrilintide/report.md#what-is-actually-on-the-table)

### tesofensine

[report.md](./tesofensine/report.md) · CAS: 402856-42-2 · Last updated: September 3, 2026

- [Identity](./tesofensine/report.md#identity)
- [The claim and the slogan](./tesofensine/report.md#the-claim-and-the-slogan)
- [Mechanism](./tesofensine/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./tesofensine/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./tesofensine/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./tesofensine/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./tesofensine/report.md#formulations-and-source-quality)
- [Observed practice](./tesofensine/report.md#observed-practice)
- [Legal / access status](./tesofensine/report.md#legal--access-status)
- [Related hallmarks](./tesofensine/report.md#related-hallmarks)
- [Related compounds](./tesofensine/report.md#related-compounds)
- [Open questions](./tesofensine/report.md#open-questions)
- [What is actually on the table](./tesofensine/report.md#what-is-actually-on-the-table)

### hcg

[report.md](./hcg/report.md) · CAS: 9002-61-3 · Last updated: September 3, 2026

- [Identity](./hcg/report.md#identity)
- [The claim and the slogan](./hcg/report.md#the-claim-and-the-slogan)
- [Mechanism](./hcg/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./hcg/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./hcg/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./hcg/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./hcg/report.md#formulations-and-source-quality)
- [Observed practice](./hcg/report.md#observed-practice)
- [Legal / access status](./hcg/report.md#legal--access-status)
- [Related hallmarks](./hcg/report.md#related-hallmarks)
- [Related compounds](./hcg/report.md#related-compounds)
- [Open questions](./hcg/report.md#open-questions)
- [What is actually on the table](./hcg/report.md#what-is-actually-on-the-table)

### l-carnitine

[report.md](./l-carnitine/report.md) · CAS: 541-15-1 · Last updated: September 3, 2026

- [Identity](./l-carnitine/report.md#identity)
- [The claim and the slogan](./l-carnitine/report.md#the-claim-and-the-slogan)
- [Mechanism](./l-carnitine/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./l-carnitine/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./l-carnitine/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./l-carnitine/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./l-carnitine/report.md#formulations-and-source-quality)
- [Observed practice](./l-carnitine/report.md#observed-practice)
- [Legal / access status](./l-carnitine/report.md#legal--access-status)
- [Related hallmarks](./l-carnitine/report.md#related-hallmarks)
- [Related compounds](./l-carnitine/report.md#related-compounds)
- [Open questions](./l-carnitine/report.md#open-questions)
- [What is actually on the table](./l-carnitine/report.md#what-is-actually-on-the-table)

### ara-290

[report.md](./ara-290/report.md) · CAS: 1208243-50-8 · Last updated: September 3, 2026

- [Identity](./ara-290/report.md#identity)
- [The claim and the slogan](./ara-290/report.md#the-claim-and-the-slogan)
- [Mechanism](./ara-290/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./ara-290/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./ara-290/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./ara-290/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./ara-290/report.md#formulations-and-source-quality)
- [Observed practice](./ara-290/report.md#observed-practice)
- [Legal / access status](./ara-290/report.md#legal--access-status)
- [Related hallmarks](./ara-290/report.md#related-hallmarks)
- [Related compounds](./ara-290/report.md#related-compounds)
- [Open questions](./ara-290/report.md#open-questions)
- [What is actually on the table](./ara-290/report.md#what-is-actually-on-the-table)

### slu-pp-332

[report.md](./slu-pp-332/report.md) · CAS: 303760-60-3 · Last updated: September 3, 2026

- [Identity](./slu-pp-332/report.md#identity)
- [The claim and the slogan](./slu-pp-332/report.md#the-claim-and-the-slogan)
- [Mechanism](./slu-pp-332/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./slu-pp-332/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./slu-pp-332/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./slu-pp-332/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./slu-pp-332/report.md#formulations-and-source-quality)
- [Observed practice](./slu-pp-332/report.md#observed-practice)
- [Legal / access status](./slu-pp-332/report.md#legal--access-status)
- [Related hallmarks](./slu-pp-332/report.md#related-hallmarks)
- [Related compounds](./slu-pp-332/report.md#related-compounds)
- [Open questions](./slu-pp-332/report.md#open-questions)
- [What is actually on the table](./slu-pp-332/report.md#what-is-actually-on-the-table)

### melanotan-1

[report.md](./melanotan-1/report.md) · CAS: 75921-69-6 · Last updated: September 3, 2026

- [Identity](./melanotan-1/report.md#identity)
- [The claim and the slogan](./melanotan-1/report.md#the-claim-and-the-slogan)
- [Mechanism](./melanotan-1/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./melanotan-1/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./melanotan-1/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./melanotan-1/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./melanotan-1/report.md#formulations-and-source-quality)
- [Observed practice](./melanotan-1/report.md#observed-practice)
- [Legal / access status](./melanotan-1/report.md#legal--access-status)
- [Related hallmarks](./melanotan-1/report.md#related-hallmarks)
- [Related compounds](./melanotan-1/report.md#related-compounds)
- [Open questions](./melanotan-1/report.md#open-questions)
- [What is actually on the table](./melanotan-1/report.md#what-is-actually-on-the-table)

### melanotan-2

[report.md](./melanotan-2/report.md) · CAS: 121062-08-6 · Last updated: September 3, 2026

- [Identity](./melanotan-2/report.md#identity)
- [The claim and the slogan](./melanotan-2/report.md#the-claim-and-the-slogan)
- [Mechanism](./melanotan-2/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./melanotan-2/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./melanotan-2/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./melanotan-2/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./melanotan-2/report.md#formulations-and-source-quality)
- [Observed practice](./melanotan-2/report.md#observed-practice)
- [Legal / access status](./melanotan-2/report.md#legal--access-status)
- [Related hallmarks](./melanotan-2/report.md#related-hallmarks)
- [Related compounds](./melanotan-2/report.md#related-compounds)
- [Open questions](./melanotan-2/report.md#open-questions)
- [What is actually on the table](./melanotan-2/report.md#what-is-actually-on-the-table)

### thymosin-alpha-1

[report.md](./thymosin-alpha-1/report.md) · CAS: 62304-98-7 · Last updated: September 3, 2026

- [Identity](./thymosin-alpha-1/report.md#identity)
- [The claim and the slogan](./thymosin-alpha-1/report.md#the-claim-and-the-slogan)
- [Mechanism](./thymosin-alpha-1/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./thymosin-alpha-1/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./thymosin-alpha-1/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./thymosin-alpha-1/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./thymosin-alpha-1/report.md#formulations-and-source-quality)
- [Observed practice](./thymosin-alpha-1/report.md#observed-practice)
- [Legal / access status](./thymosin-alpha-1/report.md#legal--access-status)
- [Related hallmarks](./thymosin-alpha-1/report.md#related-hallmarks)
- [Related compounds](./thymosin-alpha-1/report.md#related-compounds)
- [Open questions](./thymosin-alpha-1/report.md#open-questions)
- [What is actually on the table](./thymosin-alpha-1/report.md#what-is-actually-on-the-table)

### glutathione

[report.md](./glutathione/report.md) · CAS: 70-18-8 · Last updated: September 3, 2026

- [Identity](./glutathione/report.md#identity)
- [The claim and the slogan](./glutathione/report.md#the-claim-and-the-slogan)
- [Mechanism](./glutathione/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./glutathione/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./glutathione/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./glutathione/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./glutathione/report.md#formulations-and-source-quality)
- [Observed practice](./glutathione/report.md#observed-practice)
- [Legal / access status](./glutathione/report.md#legal--access-status)
- [Related hallmarks](./glutathione/report.md#related-hallmarks)
- [Related compounds](./glutathione/report.md#related-compounds)
- [Open questions](./glutathione/report.md#open-questions)
- [What is actually on the table](./glutathione/report.md#what-is-actually-on-the-table)

### cerebrolysin

[report.md](./cerebrolysin/report.md) · CAS: 12656-61-0 · Last updated: September 3, 2026

- [Identity](./cerebrolysin/report.md#identity)
- [The claim and the slogan](./cerebrolysin/report.md#the-claim-and-the-slogan)
- [Mechanism](./cerebrolysin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./cerebrolysin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./cerebrolysin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./cerebrolysin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./cerebrolysin/report.md#formulations-and-source-quality)
- [Observed practice](./cerebrolysin/report.md#observed-practice)
- [Legal / access status](./cerebrolysin/report.md#legal--access-status)
- [Related hallmarks](./cerebrolysin/report.md#related-hallmarks)
- [Related compounds](./cerebrolysin/report.md#related-compounds)
- [Open questions](./cerebrolysin/report.md#open-questions)
- [What is actually on the table](./cerebrolysin/report.md#what-is-actually-on-the-table)

### kpv

[report.md](./kpv/report.md) · CAS: 67727-97-3 · Last updated: September 3, 2026

- [Identity](./kpv/report.md#identity)
- [The claim and the slogan](./kpv/report.md#the-claim-and-the-slogan)
- [Mechanism](./kpv/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./kpv/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./kpv/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./kpv/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./kpv/report.md#formulations-and-source-quality)
- [Observed practice](./kpv/report.md#observed-practice)
- [Legal / access status](./kpv/report.md#legal--access-status)
- [Related hallmarks](./kpv/report.md#related-hallmarks)
- [Related compounds](./kpv/report.md#related-compounds)
- [Open questions](./kpv/report.md#open-questions)
- [What is actually on the table](./kpv/report.md#what-is-actually-on-the-table)

### ss-31

[report.md](./ss-31/report.md) · CAS: 736992-21-5 · Last updated: September 3, 2026

- [Identity](./ss-31/report.md#identity)
- [The claim and the slogan](./ss-31/report.md#the-claim-and-the-slogan)
- [Mechanism](./ss-31/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./ss-31/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./ss-31/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./ss-31/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./ss-31/report.md#formulations-and-source-quality)
- [Observed practice](./ss-31/report.md#observed-practice)
- [Legal / access status](./ss-31/report.md#legal--access-status)
- [Related hallmarks](./ss-31/report.md#related-hallmarks)
- [Related compounds](./ss-31/report.md#related-compounds)
- [Open questions](./ss-31/report.md#open-questions)
- [What is actually on the table](./ss-31/report.md#what-is-actually-on-the-table)

### igf-1-lr3

[report.md](./igf-1-lr3/report.md) · CAS: 946870-92-4 · Last updated: September 3, 2026

- [Identity](./igf-1-lr3/report.md#identity)
- [The claim and the slogan](./igf-1-lr3/report.md#the-claim-and-the-slogan)
- [Mechanism](./igf-1-lr3/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./igf-1-lr3/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./igf-1-lr3/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./igf-1-lr3/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./igf-1-lr3/report.md#formulations-and-source-quality)
- [Observed practice](./igf-1-lr3/report.md#observed-practice)
- [Legal / access status](./igf-1-lr3/report.md#legal--access-status)
- [Related hallmarks](./igf-1-lr3/report.md#related-hallmarks)
- [Related compounds](./igf-1-lr3/report.md#related-compounds)
- [Open questions](./igf-1-lr3/report.md#open-questions)
- [What is actually on the table](./igf-1-lr3/report.md#what-is-actually-on-the-table)

### cjc-1295-no-dac

[report.md](./cjc-1295-no-dac/report.md) · CAS: 863288-34-0 · Last updated: September 3, 2026

- [Identity](./cjc-1295-no-dac/report.md#identity)
- [The claim and the slogan](./cjc-1295-no-dac/report.md#the-claim-and-the-slogan)
- [Mechanism](./cjc-1295-no-dac/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./cjc-1295-no-dac/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./cjc-1295-no-dac/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./cjc-1295-no-dac/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./cjc-1295-no-dac/report.md#formulations-and-source-quality)
- [Observed practice](./cjc-1295-no-dac/report.md#observed-practice)
- [Legal / access status](./cjc-1295-no-dac/report.md#legal--access-status)
- [Related hallmarks](./cjc-1295-no-dac/report.md#related-hallmarks)
- [Related compounds](./cjc-1295-no-dac/report.md#related-compounds)
- [Open questions](./cjc-1295-no-dac/report.md#open-questions)
- [What is actually on the table](./cjc-1295-no-dac/report.md#what-is-actually-on-the-table)

### b7-33

[report.md](./b7-33/report.md) · CAS: 1818415-56-3 · Last updated: September 3, 2026

- [Identity](./b7-33/report.md#identity)
- [The claim and the slogan](./b7-33/report.md#the-claim-and-the-slogan)
- [Mechanism](./b7-33/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./b7-33/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./b7-33/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./b7-33/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./b7-33/report.md#formulations-and-source-quality)
- [Observed practice](./b7-33/report.md#observed-practice)
- [Legal / access status](./b7-33/report.md#legal--access-status)
- [Related hallmarks](./b7-33/report.md#related-hallmarks)
- [Related compounds](./b7-33/report.md#related-compounds)
- [Open questions](./b7-33/report.md#open-questions)
- [What is actually on the table](./b7-33/report.md#what-is-actually-on-the-table)

### sermorelin

[report.md](./sermorelin/report.md) · CAS: 86168-78-7 · Last updated: September 3, 2026

- [Identity](./sermorelin/report.md#identity)
- [The claim and the slogan](./sermorelin/report.md#the-claim-and-the-slogan)
- [Mechanism](./sermorelin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./sermorelin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./sermorelin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./sermorelin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./sermorelin/report.md#formulations-and-source-quality)
- [Observed practice](./sermorelin/report.md#observed-practice)
- [Legal / access status](./sermorelin/report.md#legal--access-status)
- [Related hallmarks](./sermorelin/report.md#related-hallmarks)
- [Related compounds](./sermorelin/report.md#related-compounds)
- [Open questions](./sermorelin/report.md#open-questions)
- [What is actually on the table](./sermorelin/report.md#what-is-actually-on-the-table)

### selank

[report.md](./selank/report.md) · CAS: 129954-34-3 · Last updated: September 3, 2026

- [Identity](./selank/report.md#identity)
- [The claim and the slogan](./selank/report.md#the-claim-and-the-slogan)
- [Mechanism](./selank/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./selank/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./selank/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./selank/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./selank/report.md#formulations-and-source-quality)
- [Observed practice](./selank/report.md#observed-practice)
- [Legal / access status](./selank/report.md#legal--access-status)
- [Related hallmarks](./selank/report.md#related-hallmarks)
- [Related compounds](./selank/report.md#related-compounds)
- [Open questions](./selank/report.md#open-questions)
- [What is actually on the table](./selank/report.md#what-is-actually-on-the-table)

### tb-500

[report.md](./tb-500/report.md) · CAS: 77591-33-4 · Last updated: September 3, 2026

- [Identity](./tb-500/report.md#identity)
- [The claim and the slogan](./tb-500/report.md#the-claim-and-the-slogan)
- [Mechanism](./tb-500/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./tb-500/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./tb-500/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./tb-500/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./tb-500/report.md#formulations-and-source-quality)
- [Observed practice](./tb-500/report.md#observed-practice)
- [Legal / access status](./tb-500/report.md#legal--access-status)
- [Related hallmarks](./tb-500/report.md#related-hallmarks)
- [Related compounds](./tb-500/report.md#related-compounds)
- [Open questions](./tb-500/report.md#open-questions)
- [What is actually on the table](./tb-500/report.md#what-is-actually-on-the-table)

### semax

[report.md](./semax/report.md) · CAS: 80714-61-0 · Last updated: September 3, 2026

- [Identity](./semax/report.md#identity)
- [The claim and the slogan](./semax/report.md#the-claim-and-the-slogan)
- [Mechanism](./semax/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./semax/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./semax/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./semax/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./semax/report.md#formulations-and-source-quality)
- [Observed practice](./semax/report.md#observed-practice)
- [Legal / access status](./semax/report.md#legal--access-status)
- [Related hallmarks](./semax/report.md#related-hallmarks)
- [Related compounds](./semax/report.md#related-compounds)
- [Open questions](./semax/report.md#open-questions)
- [What is actually on the table](./semax/report.md#what-is-actually-on-the-table)

### ipamorelin

[report.md](./ipamorelin/report.md) · CAS: 170851-70-4 · Last updated: September 3, 2026

- [Identity](./ipamorelin/report.md#identity)
- [The claim and the slogan](./ipamorelin/report.md#the-claim-and-the-slogan)
- [Mechanism](./ipamorelin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./ipamorelin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./ipamorelin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./ipamorelin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./ipamorelin/report.md#formulations-and-source-quality)
- [Observed practice](./ipamorelin/report.md#observed-practice)
- [Legal / access status](./ipamorelin/report.md#legal--access-status)
- [Related hallmarks](./ipamorelin/report.md#related-hallmarks)
- [Related compounds](./ipamorelin/report.md#related-compounds)
- [Open questions](./ipamorelin/report.md#open-questions)
- [What is actually on the table](./ipamorelin/report.md#what-is-actually-on-the-table)

### mots-c

[report.md](./mots-c/report.md) · CAS: 1627580-64-6 · Last updated: September 3, 2026

- [Identity](./mots-c/report.md#identity)
- [The claim and the slogan](./mots-c/report.md#the-claim-and-the-slogan)
- [Mechanism](./mots-c/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./mots-c/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./mots-c/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./mots-c/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./mots-c/report.md#formulations-and-source-quality)
- [Observed practice](./mots-c/report.md#observed-practice)
- [Legal / access status](./mots-c/report.md#legal--access-status)
- [Related hallmarks](./mots-c/report.md#related-hallmarks)
- [Related compounds](./mots-c/report.md#related-compounds)
- [Open questions](./mots-c/report.md#open-questions)
- [What is actually on the table](./mots-c/report.md#what-is-actually-on-the-table)

### tesamorelin

[report.md](./tesamorelin/report.md) · CAS: 901758-09-6 · Last updated: September 3, 2026

- [Identity](./tesamorelin/report.md#identity)
- [The claim and the slogan](./tesamorelin/report.md#the-claim-and-the-slogan)
- [Mechanism](./tesamorelin/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./tesamorelin/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./tesamorelin/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./tesamorelin/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./tesamorelin/report.md#formulations-and-source-quality)
- [Observed practice](./tesamorelin/report.md#observed-practice)
- [Legal / access status](./tesamorelin/report.md#legal--access-status)
- [Related hallmarks](./tesamorelin/report.md#related-hallmarks)
- [Related compounds](./tesamorelin/report.md#related-compounds)
- [Open questions](./tesamorelin/report.md#open-questions)
- [What is actually on the table](./tesamorelin/report.md#what-is-actually-on-the-table)

### pt-141

[report.md](./pt-141/report.md) · CAS: 189691-06-3 · Last updated: September 3, 2026

- [Identity](./pt-141/report.md#identity)
- [The claim and the slogan](./pt-141/report.md#the-claim-and-the-slogan)
- [Mechanism](./pt-141/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./pt-141/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./pt-141/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./pt-141/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./pt-141/report.md#formulations-and-source-quality)
- [Observed practice](./pt-141/report.md#observed-practice)
- [Legal / access status](./pt-141/report.md#legal--access-status)
- [Related hallmarks](./pt-141/report.md#related-hallmarks)
- [Related compounds](./pt-141/report.md#related-compounds)
- [Open questions](./pt-141/report.md#open-questions)
- [What is actually on the table](./pt-141/report.md#what-is-actually-on-the-table)

### snap-8

[report.md](./snap-8/report.md) · CAS: 868844-74-0 · Last updated: September 3, 2026

- [Identity](./snap-8/report.md#identity)
- [The claim and the slogan](./snap-8/report.md#the-claim-and-the-slogan)
- [Mechanism](./snap-8/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./snap-8/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./snap-8/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./snap-8/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./snap-8/report.md#formulations-and-source-quality)
- [Observed practice](./snap-8/report.md#observed-practice)
- [Legal / access status](./snap-8/report.md#legal--access-status)
- [Related hallmarks](./snap-8/report.md#related-hallmarks)
- [Related compounds](./snap-8/report.md#related-compounds)
- [Open questions](./snap-8/report.md#open-questions)
- [What is actually on the table](./snap-8/report.md#what-is-actually-on-the-table)

### bpc-157

[report.md](./bpc-157/report.md) · CAS: 137525-51-0 · Last updated: September 3, 2026

- [Identity](./bpc-157/report.md#identity)
- [The claim and the slogan](./bpc-157/report.md#the-claim-and-the-slogan)
- [Mechanism](./bpc-157/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./bpc-157/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./bpc-157/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./bpc-157/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./bpc-157/report.md#formulations-and-source-quality)
- [Observed practice](./bpc-157/report.md#observed-practice)
- [Legal / access status](./bpc-157/report.md#legal--access-status)
- [Related hallmarks](./bpc-157/report.md#related-hallmarks)
- [Related compounds](./bpc-157/report.md#related-compounds)
- [Open questions](./bpc-157/report.md#open-questions)
- [What is actually on the table](./bpc-157/report.md#what-is-actually-on-the-table)

### ghk-cu

[report.md](./ghk-cu/report.md) · CAS: 89030-95-5 · Last updated: September 3, 2026

- [Identity](./ghk-cu/report.md#identity)
- [The claim and the slogan](./ghk-cu/report.md#the-claim-and-the-slogan)
- [Mechanism](./ghk-cu/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./ghk-cu/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./ghk-cu/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./ghk-cu/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./ghk-cu/report.md#formulations-and-source-quality)
- [Observed practice](./ghk-cu/report.md#observed-practice)
- [Legal / access status](./ghk-cu/report.md#legal--access-status)
- [Related hallmarks](./ghk-cu/report.md#related-hallmarks)
- [Related compounds](./ghk-cu/report.md#related-compounds)
- [Open questions](./ghk-cu/report.md#open-questions)
- [What is actually on the table](./ghk-cu/report.md#what-is-actually-on-the-table)

### aod-9604

[report.md](./aod-9604/report.md) · CAS: 386264-39-7 · Last updated: September 3, 2026

- [Identity](./aod-9604/report.md#identity)
- [The claim and the slogan](./aod-9604/report.md#the-claim-and-the-slogan)
- [Mechanism](./aod-9604/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./aod-9604/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./aod-9604/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./aod-9604/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./aod-9604/report.md#formulations-and-source-quality)
- [Observed practice](./aod-9604/report.md#observed-practice)
- [Legal / access status](./aod-9604/report.md#legal--access-status)
- [Related hallmarks](./aod-9604/report.md#related-hallmarks)
- [Related compounds](./aod-9604/report.md#related-compounds)
- [Open questions](./aod-9604/report.md#open-questions)
- [What is actually on the table](./aod-9604/report.md#what-is-actually-on-the-table)

### ahk-cu

[report.md](./ahk-cu/report.md) · CAS: 49557-75-7 · Last updated: September 3, 2026

- [Identity](./ahk-cu/report.md#identity)
- [The claim and the slogan](./ahk-cu/report.md#the-claim-and-the-slogan)
- [Mechanism](./ahk-cu/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./ahk-cu/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./ahk-cu/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./ahk-cu/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./ahk-cu/report.md#formulations-and-source-quality)
- [Observed practice](./ahk-cu/report.md#observed-practice)
- [Legal / access status](./ahk-cu/report.md#legal--access-status)
- [Related hallmarks](./ahk-cu/report.md#related-hallmarks)
- [Related compounds](./ahk-cu/report.md#related-compounds)
- [Open questions](./ahk-cu/report.md#open-questions)
- [What is actually on the table](./ahk-cu/report.md#what-is-actually-on-the-table)

### jxl-069

[report.md](./jxl-069/report.md) · CAS: 2232594-65-1 · Last updated: September 3, 2026

- [Identity](./jxl-069/report.md#identity)
- [The claim and the slogan](./jxl-069/report.md#the-claim-and-the-slogan)
- [Mechanism](./jxl-069/report.md#mechanism)
- [Pharmacokinetics / pharmacodynamics](./jxl-069/report.md#pharmacokinetics--pharmacodynamics)
- [Animal data](./jxl-069/report.md#animal-data)
- [Human data — aging, off-label, and geroscience](./jxl-069/report.md#human-data--aging-off-label-and-geroscience)
- [Formulations and source quality](./jxl-069/report.md#formulations-and-source-quality)
- [Observed practice](./jxl-069/report.md#observed-practice)
- [Legal / access status](./jxl-069/report.md#legal--access-status)
- [Related hallmarks](./jxl-069/report.md#related-hallmarks)
- [Related compounds](./jxl-069/report.md#related-compounds)
- [Open questions](./jxl-069/report.md#open-questions)
- [What is actually on the table](./jxl-069/report.md#what-is-actually-on-the-table)
<!-- END GENERATED -->
