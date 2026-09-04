# have-fun-dont-die

## What this is

This repo is an **agentic research workflow** — a jumping-off point for an **agent**, not a textbook — demonstrated by a deep dive on the hallmarks of aging and prolonging healthy life. The name is have-fun-dont-die.

Any research topic is welcome. Political and PC filler is not: no equity sermons, access lectures, stigma language, identity politics, or “societal implications” filler. Biology, evidence, practice, uncertainty.

Do not memorize it. Do not read every file — most writeups are shorthand.

Ask it questions. Have it research to answer them. How: [HOW_TO_ASK_AGENTS_QUESTIONS.MD](HOW_TO_ASK_AGENTS_QUESTIONS.MD).

Sourced dump of aging biology, tactics people are actually running, and the speculative edge — ideas the institutional apparatus will not go first on. We document. We do not recommend — except ☠︎︎, where we say stay away.

It makes mistakes. When the miss is the repo or the agent config, `/self-improve` so the same failure does not recur. Please PR improvement one at a time, provide an example of it failing and then it succeeding after, so we can share the improvements!

Use the most capable model you can for **analysis**. Cheap agents work for **scraping**. Fifty Composer agents reading ten papers each will beat Fable reading one.

LLMs do not think. They follow directions. The thinking is yours.

## About the author & why I made this.

I always suspected we could be a lot further toward agelessness if that were actually the assignment. It is not. Institutional science would rather do nothing than be wrong in public. They will get there. My people are on a timer.

I do not treat “natural causes” as an answer. It is a filing category for machinery that failed in named ways, after which everyone writes a review article and goes to lunch. I wanted the other ending. Not a wellness brand. Not a graceful decline. The people I love, still here, still sharp.

I went to university for molecular biology to eliminate tooth decay. That sentence is already a personality test. Cavities were the tutorial: one tissue, one ecology, a rot you can actually corner. I intended to keep going. Then I stayed for a self-imposed fifth year of a triple bachelor’s in biology, botany, and chemistry — cringe, better than a tattoo, worse than a plan. Three stacks. One motive. Smart people do dumb things. Get over it.

School found out why I wanted all three. I was trying to stack enough mechanism to make my loved ones immortal. They were not charmed. There is a particular silence that arrives when you say the quiet part to people whose job is to keep it quiet. How dare I treat the course catalog like a spellbook. Meetings were had. Concern was expressed. I was invited to want a smaller, more employable thing.

So I dropped out and switched to software design. Same problem, different compiler. The wet lab wanted permission and a ten-year aims page. I wanted an apparatus that works at night.

Then a beautiful woman knocked on my dorm room door. I fell in love before I had a protocol for it. The ordinary campaign started going suspiciously well. 😉 👶👶👶

The timer got a number when my mom died at 60 of God knows what. Not a named disease. Not a paper you can cite. Just gone. Sixty is not a finished run. I need a lot more clock than that. The papers came back off the shelf.

I herd agentic swarms for a living now. Of course I built one for this. Automate the reading. Automate the sourcing. Keep the thinking. I mean the motto: laziness is nothing but the relentless pursuit of efficiency.

This is the briefing I am leaving on the table. Sourced notes, evidence marks, agents you can point at the literature the journals will get to in 2048. For people who want that knowledge and do not already know how to stand up the apparatus.



## Not medical advice

This repository is not medical advice, a protocol, or a clinic. It is a sourced dump of what is known, what is guessed, and what people are actually running — for anyone who wants the details.

You do not have to be mid-experiment to read it. Self-experimenters are welcome. So is anyone who wants the primary papers, the nulls, the harms, and the forum protocols in one place, marked for how thin they are.

We document. We do not recommend — except ☠︎︎. A dose in these files is observed practice, not an instruction. You decide. If the mark is established harm, stay away.

## How to read a mark

Every assertion in a rewritten report starts with one of these. Titles, headers, and bare citations do not. Full marking rules: [AGENTS.md](AGENTS.md).

| Mark | Meaning | Use when |
|---|---|---|
| 💯 | Settled. Known and not contested. | Textbook-grade facts. Not a single paper. Not a hot fight. Rare. |
| 📚 | Published and peer-reviewed. | A real paper or review supports the statement, and that specific finding is not currently in a serious fight. |
| 📜 | Preprint. Posted, not peer-reviewed. | bioRxiv, medRxiv, arXiv, and the like. |
| 🥼 | Papers in a live fight. | Research literature disagrees. Cite both sides. |
| 🤔 | Forum / clinic / newsletter practice; mechanistically coherent; not known false. | Forums, clinics, newsletters, podcasts, self-experiments. |
| 🤼 | Amateur / biohacker fight. | Forum posts, Discord, blogs, clinic marketing — not research papers. |
| ⛔ | Suspect. Does not make sense. | Circulating but implausible, inconsistent, or already contradicted. |
| ☠︎︎ | Sure, meaningful harm. | Established that this hurts people in a real way. This is the only time we give advice "STAY THE FUCK AWAY"|
| 🐉 | Here be dragons. Wild speculation. | Forward-looking or mechanistic leaps with little or no direct evidence. |

## Start here

Six entry paths. Not a recommendation ladder.

- [How this works](HOW_DOES_THIS_THING_WORK.md) — agents, search, how context is built
- [How to ask](HOW_TO_ASK_AGENTS_QUESTIONS.MD) — Cursor, Cursor Agent CLI, or Claude Code
- [By hallmark](#hallmarks-catalog)
- [By compound](#compounds-catalog)
- [By tactic people are running](#by-tactic-assay-and-protocol) — NAD, rapamycin, senolytics, CHIP panels, clocks, fucoidan, plasma/HBOT, antioxidants
- [By live fight](#by-live-fight) — literature and amateur
- [By known harm or suspect claim](#by-known-harm-or-suspect-claim)

## Hallmarks catalog

Catalogs are generated (`python3 scripts/build-index.py`). Do not hand-edit the generated blocks.

<!-- BEGIN GENERATED: hallmarks-catalog -->
| # | Hallmark | Report | Status | One-line claim |
|---|---|---|---|---|
| 01 | Genomic instability | [report.md](hallmarks/01-genomic-instability/report.md) | rewritten | DNA lesions, misrepair, chromosomal/mtDNA change, and selected clones accumulate with age; whether ordinary SNV burden is the master clock is a live paper fight. |
| 02 | Telomere attrition | [report.md](hallmarks/02-telomere-attrition/report.md) | rewritten | Telomeres shorten with age and can cause tissue failure at Mendelian extremes; ordinary LTL as a master clock, and lengthening as geroprotection, is a live fight. |
| 03 | Epigenetic alterations | [report.md](hallmarks/03-epigenetic-alterations/report.md) | rewritten | Methylation and chromatin drift with age and later clocks predict death; whether epigenetic information loss is the driver, and clock moves as rejuvenation, is a live fight. |
| 04 | Loss of proteostasis | [report.md](hallmarks/04-loss-of-proteostasis/report.md) | rewritten | Chaperones, UPS, and solubility fail with age and named proteinopathies are causal; a general cleanup score-and-restore product is not a completed human result. |
| 05 | Disabled macroautophagy | [report.md](hallmarks/05-disabled-macroautophagy/report.md) | rewritten | Macroautophagy is a causal lifespan knob in mice; ordinary human flux is not uniformly down, and the 16-hour / spermidine / Mitopure cleanup product is not a completed restoration result. |
| 06 | Deregulated nutrient sensing | [report.md](hallmarks/06-deregulated-nutrient-sensing/report.md) | rewritten | IIS/mTOR/AMPK/sirtuin tone is a causal lifespan knob in animals; weekly rapamycin / metformin-for-the-healthy / NAD stacks are not a completed human restoration result. |
| 07 | Mitochondrial dysfunction | [report.md](hallmarks/07-mitochondrial-dysfunction/report.md) | rewritten | Capacity, clonal mtDNA deletions, and quality control fail with age in tissue-specific ways; Mitopure/NAD/MitoQ/Forzinity/MOTS-c are not a completed human restore result. |
| 08 | Cellular senescence | [report.md](hallmarks/08-cellular-senescence/report.md) | rewritten | p16-high/senescent populations can be causal in mice; human senolytics are n=5–14 pilots plus OA/ITP nulls; Qualia/D+Q/fisetin SKUs are not a completed restore result. |
| 09 | Stem-cell exhaustion | [report.md](hallmarks/09-stem-cell-exhaustion/report.md) | rewritten | Useful regenerative capacity falls with age in tissue-specific ways (HSC function/clonality, MuSC, ISC/HFSC); refill IVs, STEMREGEN, and young plasma are not a completed restore result. |
| 10 | Altered intercellular communication | [report.md](hallmarks/10-altered-intercellular-communication/report.md) | rewritten | Endocrine/neural/EV/SASP-as-signal and circulating factors change with age; young plasma, TPE, and exosome IVs are not a completed human restore result. |
| 11 | Chronic inflammation | [report.md](hallmarks/11-chronic-inflammation/report.md) | rewritten | Sterile low-grade inflammatory tone rises with age and CANTOS moved MACE; hsCRP dashboards, curcumin/SPM stacks, and off-label colchicine/canakinumab/JAKi are not a completed human restore result. |
| 12 | Dysbiosis | [report.md](hallmarks/12-dysbiosis/report.md) | rewritten | Gut communities and functions change with age and mouse transfers can move permeability and progeria lifespan; Viome/Akkermansia/FMT stacks are not a completed human restore result. |
| 13 | Extracellular matrix changes | [report.md](hallmarks/13-extracellular-matrix-changes/report.md) | rewritten | Long-lived collagen accumulates AGEs and stiffness predicts events; collagen/GHK-Cu/AGE-Reader/alagebrium stacks are not a completed human restore result. |
| 14 | Psychosocial isolation | [report.md](hallmarks/14-psychosocial-isolation/report.md) | rewritten | Isolation and loneliness associate with death, CVD, and dementia; residual isolation vs loneliness-NS is a live fight; UCLA-as-CRP, Oxipops, and AI companions are not a completed restore result. |
<!-- END GENERATED -->

## Topics catalog

The tree exists; there are no writeups yet. Layout: [topics/README.md](topics/README.md).

<!-- BEGIN GENERATED: topics-catalog -->
| Slug | Report | Last updated | One-line claim |
|---|---|---|---|
<!-- END GENERATED -->

## Compounds catalog

Hallmark extracts, not researched dossiers. Layout: [compounds/README.md](compounds/README.md).

<!-- BEGIN GENERATED: compounds-catalog -->
| Slug | CAS | Report | Last updated | One-line claim |
|---|---|---|---|---|
| [rapamycin](compounds/rapamycin/report.md) | 53123-88-9 | [report.md](compounds/rapamycin/report.md) | September 3, 2026 | ITP lifespan hit in mice; PEARL VAT null and RAPA-EX-01 chair-stand miss at weekly geroscience doses; transplant daily sirolimus has boxed infection/pneumonitis. |
| [everolimus](compounds/everolimus/report.md) | 159351-69-6 | [report.md](compounds/everolimus/report.md) | September 3, 2026 | Mannick Phase 2 vaccine-titer and infection-surrogate signals; not a lifespan or disability-free-survival result. |
| [rtb101](compounds/rtb101/report.md) | 915019-65-7 | [report.md](compounds/rtb101/report.md) | September 3, 2026 | Phase 3 winter respiratory-illness null in adults ≥65; the indication was dropped. |
| [metformin](compounds/metformin/report.md) | 1115-70-4 | [report.md](compounds/metformin/report.md) | September 3, 2026 | DPP indicated diabetes delay; ITP lifespan null; TAME not launched; Konopka vs Pilmark is a live exercise-adaptation fight. |
| [nicotinamide-riboside](compounds/nicotinamide-riboside/report.md) | 1341-23-7 | [report.md](compounds/nicotinamide-riboside/report.md) | September 3, 2026 | Raises blood NAD; ITP lifespan null; Dollerup clamp and muscle-respiration nulls; Elysium Basis is the storefront pair with pterostilbene. |
| [nicotinamide-mononucleotide](compounds/nicotinamide-mononucleotide/report.md) | 1094-61-7 | [report.md](compounds/nicotinamide-mononucleotide/report.md) | September 3, 2026 | Yoshino 2021 muscle insulin-sensitivity move in prediabetes; DoNotAge 500–1000 mg storefront; not sirtuin restoration. |
| [nad](compounds/nad/report.md) | 53-84-9 | [report.md](compounds/nad/report.md) | September 3, 2026 | Peach IV 100–1000 mg and AgelessRx nasal 30 mg are practice; IV vs oral vs nasal is an amateur split; blood NAD is target engagement, not genome or mito restoration. |
| [fisetin](compounds/fisetin/report.md) | 528-48-3 | [report.md](compounds/fisetin/report.md) | September 3, 2026 | ITP lifespan null; unformulated oral barely appears in plasma; Qualia 1400 mg pulse vs DoNotAge 800 mg daily vs Life Extension 56 mg weekly is an amateur split. |
| [dasatinib](compounds/dasatinib/report.md) | 302962-49-8 | [report.md](compounds/dasatinib/report.md) | September 3, 2026 | D+Q senolytic pilots are n=5–19; continuous CML Sprycel has an established pleural-effusion/PAH harm file; DIY gray-market pulses are forum practice. |
| [quercetin](compounds/quercetin/report.md) | 117-39-5 | [report.md](compounds/quercetin/report.md) | September 3, 2026 | Paired with dasatinib in the 2015 screen and human pilots; CSF undetectable in Gonzales AD; also sold inside Qualia/Life Extension/AMPK stacks. |
| [fucoidan](compounds/fucoidan/report.md) | none | [report.md](compounds/fucoidan/report.md) | September 3, 2026 | DoNotAge SIRT6Activator 800–2400 mg; Gorbunova 2025 preprint is male-mouse lifespan; NCT07500649 GrimAge primary is not mutation burden. |
| [spermidine](compounds/spermidine/report.md) | 124-20-9 | [report.md](compounds/spermidine/report.md) | September 3, 2026 | Autophagy-dependent lifespan in models; SmartAge 0.9 mg memory primary null; 1–2 mg wheat-germ vs 8 mg synthetic is an amateur split. |
| [urolithin-a](compounds/urolithin-a/report.md) | 1143-70-0 | [report.md](compounds/urolithin-a/report.md) | September 3, 2026 | Parkin-axis muscle signature at 500–1000 mg; missed Singh peak power and Liu 6MWT; mitophagy cargo, not general macroautophagy restoration. |
| [resveratrol](compounds/resveratrol/report.md) | 501-36-0 | [report.md](compounds/resveratrol/report.md) | September 3, 2026 | ITP lifespan null; Poulsen/Kjær human metabolic nulls; SIRT1-activator fight; SRT501 myeloma nephrotoxicity is established at that exposure. |
| [berberine](compounds/berberine/report.md) | 2086-83-1 | [report.md](compounds/berberine/report.md) | September 3, 2026 | Sold as AMPK / CR-mimetic (DoNotAge 500 mg, DiBerberine, AMPK Charge+); no compiled lifespan or healthy-aging RCT. |
| [colchicine](compounds/colchicine/report.md) | 64-86-8 | [report.md](compounds/colchicine/report.md) | September 3, 2026 | COLCOT/LoDoCo2 moved CAD events at 0.5 mg; CLEAR SYNERGY was null; clinic inflammaging use and CYP3A4/P-gp vs sirolimus are amateur practice. |
| [semaglutide](compounds/semaglutide/report.md) | 910463-68-2 | [report.md](compounds/semaglutide/report.md) | September 3, 2026 | SELECT cut MACE in obesity plus established CVD; relabeling that as nutrient-sensing restoration for healthy buyers is a definition swap. |
| [tirzepatide](compounds/tirzepatide/report.md) | 2023788-19-2 | [report.md](compounds/tirzepatide/report.md) | September 3, 2026 | Named on AgelessRx XPRIZE-finals copy next to weekly rapamycin; no healthy-person aging RCT. |
| [oxytocin](compounds/oxytocin/report.md) | 50-56-6 | [report.md](compounds/oxytocin/report.md) | September 3, 2026 | Pitocin is obstetric injectable; compounded IN/troche is the longevity SKU; Berger trait-loneliness null; Sikich ASD social-functioning null. |
| [beta-carotene](compounds/beta-carotene/report.md) | 7235-40-7 | [report.md](compounds/beta-carotene/report.md) | September 3, 2026 | ATBC and CARET raised lung cancer and death in smokers; DNA-protection framing does not survive those trials. |
<!-- END GENERATED -->

## By tactic, assay, and protocol

Observed practice, not advice. Rows are “this subject appears here.” No efficacy verdict.

- **NAD / NR / NMN** — [nad](compounds/nad/report.md); [nicotinamide-riboside](compounds/nicotinamide-riboside/report.md); [nicotinamide-mononucleotide](compounds/nicotinamide-mononucleotide/report.md); [01 Human data](hallmarks/01-genomic-instability/report.md#human-data) (sold as DNA repair; Martens NAD+ rise is target engagement, not genome restoration); [01 clinics](hallmarks/01-genomic-instability/report.md#what-clinics-and-self-experimenters-are-doing); [06](hallmarks/06-deregulated-nutrient-sensing/report.md)
- **Rapamycin / sirolimus / grapefruit** — [rapamycin](compounds/rapamycin/report.md); [everolimus](compounds/everolimus/report.md); [rtb101](compounds/rtb101/report.md); [01 clinics](hallmarks/01-genomic-instability/report.md#what-clinics-and-self-experimenters-are-doing) (PK fight parked here); [06](hallmarks/06-deregulated-nutrient-sensing/report.md); [08](hallmarks/08-cellular-senescence/report.md); [11](hallmarks/11-chronic-inflammation/report.md)
- **Senolytics (D+Q, fisetin)** — [dasatinib](compounds/dasatinib/report.md); [quercetin](compounds/quercetin/report.md); [fisetin](compounds/fisetin/report.md); [08](hallmarks/08-cellular-senescence/report.md); [11](hallmarks/11-chronic-inflammation/report.md); [13](hallmarks/13-extracellular-matrix-changes/report.md)
- **CHIP / mosaic NGS panels** — [01 clinics](hallmarks/01-genomic-instability/report.md#what-clinics-and-self-experimenters-are-doing); [09](hallmarks/09-stem-cell-exhaustion/report.md); [11](hallmarks/11-chronic-inflammation/report.md)
- **Methylation clocks / GrimAge** — [01 Measurement](hallmarks/01-genomic-instability/report.md#measurement); [03](hallmarks/03-epigenetic-alterations/report.md)
- **Fucoidan / SIRT6 capsules** — [fucoidan](compounds/fucoidan/report.md); [01 clinics](hallmarks/01-genomic-instability/report.md#what-clinics-and-self-experimenters-are-doing)
- **Young plasma / HBOT** — [01 Human data](hallmarks/01-genomic-instability/report.md#human-data); [01 clinics](hallmarks/01-genomic-instability/report.md#what-clinics-and-self-experimenters-are-doing)
- **Urine 8-OHdG / comet / micronucleus** — [01 Measurement](hallmarks/01-genomic-instability/report.md#measurement)
- **High-dose antioxidant / beta-carotene “DNA protection”** — [beta-carotene](compounds/beta-carotene/report.md); [01 Human data](hallmarks/01-genomic-instability/report.md#human-data) (harm record)
- **Metformin** — [metformin](compounds/metformin/report.md); [06](hallmarks/06-deregulated-nutrient-sensing/report.md)
- **Spermidine** — [spermidine](compounds/spermidine/report.md); [05](hallmarks/05-disabled-macroautophagy/report.md)
- **Urolithin A** — [urolithin-a](compounds/urolithin-a/report.md); [07](hallmarks/07-mitochondrial-dysfunction/report.md)
- **Resveratrol / berberine** — [resveratrol](compounds/resveratrol/report.md); [berberine](compounds/berberine/report.md); [06](hallmarks/06-deregulated-nutrient-sensing/report.md)
- **Colchicine** — [colchicine](compounds/colchicine/report.md); [11](hallmarks/11-chronic-inflammation/report.md)
- **Semaglutide / tirzepatide** — [semaglutide](compounds/semaglutide/report.md); [tirzepatide](compounds/tirzepatide/report.md); [06](hallmarks/06-deregulated-nutrient-sensing/report.md)
- **Oxytocin** — [oxytocin](compounds/oxytocin/report.md); [14](hallmarks/14-psychosocial-isolation/report.md)

## By live fight

- **Ordinary SNV burden vs persistent lesions / transcription stress vs selected clones** — [01](hallmarks/01-genomic-instability/report.md#what-is-actually-on-the-table) (🥼 papers in a fight)
- **Repair-defect progeria as a low-dose version of ordinary aging** — [01](hallmarks/01-genomic-instability/report.md#what-is-actually-on-the-table)
- **Weekly longevity sirolimus dose and grapefruit boosting** — [rapamycin](compounds/rapamycin/report.md); [01 clinics](hallmarks/01-genomic-instability/report.md#what-clinics-and-self-experimenters-are-doing); [06](hallmarks/06-deregulated-nutrient-sensing/report.md) (🤼 amateur fight)

## By known harm or suspect claim

- **ATBC / CARET / SELECT / Cochrane antioxidant mortality** — [beta-carotene](compounds/beta-carotene/report.md); [01 Human data](hallmarks/01-genomic-instability/report.md#human-data)
- **Hallmark-listing-as-proof and clock-move-as-lesion-clearance** — [01 claim](hallmarks/01-genomic-instability/report.md#the-claim-and-the-slogan); [01 Measurement](hallmarks/01-genomic-instability/report.md#measurement) (⛔)

## Repo map

- [`hallmarks/`](hallmarks/) — one dir per hallmark; writeup is `report.md`
- [`topics/`](topics/) — non-molecule writeups, same shape
- [`compounds/`](compounds/) — per-molecule extracts from the hallmark reports, same shape
- `sources/<mark>/` — filed notes matching the mark on the claim
- [`scripts/build-index.py`](scripts/build-index.py) — regenerates catalog / section-map blocks from reports + [`scripts/index-meta.yaml`](scripts/index-meta.yaml)
- [`mcp/docs-rag/`](mcp/docs-rag/) — local search MCP + CLI over the writeups
- `tmp/` — scratch; gitignored; not indexed
- [`HOW_DOES_THIS_THING_WORK.md`](HOW_DOES_THIS_THING_WORK.md) — kitchen tour: agents, spawn, context
- [`HOW_TO_ASK_AGENTS_QUESTIONS.MD`](HOW_TO_ASK_AGENTS_QUESTIONS.MD) — Cursor / Cursor Agent CLI / Claude Code ask path
- [`ABOUT.md`](ABOUT.md) — why this exists
- [`AGENTS.md`](AGENTS.md) — voice, marks, layout; [adding a topic or compound](AGENTS.md#adding-a-topic-or-compound)
- [`LICENSE`](LICENSE) — MIT
- [`template.md`](template.md) — section skeleton only
