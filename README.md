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
| [crispr](topics/crispr/report.md) | [report.md](topics/crispr/report.md) | September 3, 2026 | RNA-guided Cas plus host repair (or a fused deaminase/RT) writes a genotype distribution; Casgevy is one ex vivo HSPC product, liver LNP is not whole-body rewrite, and no CRISPR aging RCT was found. |
| [enamel-remineralization-gel](topics/enamel-remineralization-gel/report.md) | [report.md](topics/enamel-remineralization-gel/report.md) | September 3, 2026 | The 2025–2026 enamel-regrowth gel is several SKUs: Hasan 2025 ~10 μm extracted-tooth ELR film (Epinamel, no in-mouth results), chairside P11-4/Curodont (live RCT fight vs fluoride), and consumer nano-HA / CPP-ACP pastes. |
| [salamander-like-regeneration](topics/salamander-like-regeneration/report.md) | [report.md](topics/salamander-like-regeneration/report.md) | September 3, 2026 | 2026 PNAS: conserved SP6/SP8 plus zebrafish-LEN FGF8 AAV partially rescues or speeds mouse P3 digit bone; not a salamander-gene transplant and not whole-limb regeneration. |
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
| [nad](compounds/nad/report.md) | 53-84-9 | [report.md](compounds/nad/report.md) | September 4, 2026 | CID 5892 / CAS 53-84-9; Grant 750 mg IV +398% plasma at 6 h after a 2 h flat; oral NR RCTs miss muscle NAD/OXPHOS; Peach/AgelessRx practice. No healthy-person aging RCT. |
| [fisetin](compounds/fisetin/report.md) | 528-48-3 | [report.md](compounds/fisetin/report.md) | September 3, 2026 | ITP lifespan null; unformulated oral barely appears in plasma; Qualia 1400 mg pulse vs DoNotAge 800 mg daily vs Life Extension 56 mg weekly is an amateur split. |
| [dasatinib](compounds/dasatinib/report.md) | 302962-49-8 | [report.md](compounds/dasatinib/report.md) | September 3, 2026 | D+Q senolytic pilots are n=5–19; continuous CML Sprycel has an established pleural-effusion/PAH harm file; DIY gray-market pulses are forum practice. |
| [quercetin](compounds/quercetin/report.md) | 117-39-5 | [report.md](compounds/quercetin/report.md) | September 3, 2026 | Paired with dasatinib in the 2015 screen and human pilots; CSF undetectable in Gonzales AD; also sold inside Qualia/Life Extension/AMPK stacks. |
| [fucoidan](compounds/fucoidan/report.md) | none | [report.md](compounds/fucoidan/report.md) | September 3, 2026 | DoNotAge SIRT6Activator 800–2400 mg; Gorbunova 2025 preprint is male-mouse lifespan; NCT07500649 GrimAge primary is not mutation burden. |
| [spermidine](compounds/spermidine/report.md) | 124-20-9 | [report.md](compounds/spermidine/report.md) | September 3, 2026 | Autophagy-dependent lifespan in models; SmartAge 0.9 mg memory primary null; 1–2 mg wheat-germ vs 8 mg synthetic is an amateur split. |
| [urolithin-a](compounds/urolithin-a/report.md) | 1143-70-0 | [report.md](compounds/urolithin-a/report.md) | September 3, 2026 | Parkin-axis muscle signature at 500–1000 mg; missed Singh peak power and Liu 6MWT; mitophagy cargo, not general macroautophagy restoration. |
| [resveratrol](compounds/resveratrol/report.md) | 501-36-0 | [report.md](compounds/resveratrol/report.md) | September 3, 2026 | ITP lifespan null; Poulsen/Kjær human metabolic nulls; SIRT1-activator fight; SRT501 myeloma nephrotoxicity is established at that exposure. |
| [berberine](compounds/berberine/report.md) | 2086-83-1 | [report.md](compounds/berberine/report.md) | September 3, 2026 | Sold as AMPK / CR-mimetic (DoNotAge 500 mg, DiBerberine, AMPK Charge+); no compiled lifespan or healthy-aging RCT. |
| [colchicine](compounds/colchicine/report.md) | 64-86-8 | [report.md](compounds/colchicine/report.md) | September 3, 2026 | COLCOT/LoDoCo2 moved CAD events at 0.5 mg; CLEAR SYNERGY was null; clinic inflammaging use and CYP3A4/P-gp vs sirolimus are amateur practice. |
| [semaglutide](compounds/semaglutide/report.md) | 910463-68-2 | [report.md](compounds/semaglutide/report.md) | September 4, 2026 | SELECT 2.4 mg weekly cut MACE HR 0.80 in obesity+CVD; STEP-1-class −14.9% weight; SM-GLP1 RUO ≠ Wegovy. No healthy-person aging RCT. |
| [tirzepatide](compounds/tirzepatide/report.md) | 2023788-19-2 | [report.md](compounds/tirzepatide/report.md) | September 4, 2026 | Zepbound SURMOUNT-1-class 15 mg −20.9% at 72 weeks; AgelessRx XPRIZE names compounded tirzepatide; T-GLP2 RUO ≠ Zepbound. No healthy-person aging RCT. |
| [oxytocin](compounds/oxytocin/report.md) | 50-56-6 | [report.md](compounds/oxytocin/report.md) | September 4, 2026 | CID 439302 / CAS 50-56-6; Pitocin t½ 1–6 min with labeled water-intoxication deaths; Berger IN trait-null; Sikich ASD null; 10 mg RUO ≠ Pitocin. |
| [beta-carotene](compounds/beta-carotene/report.md) | 7235-40-7 | [report.md](compounds/beta-carotene/report.md) | September 3, 2026 | ATBC and CARET raised lung cancer and death in smokers; DNA-protection framing does not survive those trials. |
| [hexarelin](compounds/hexarelin/report.md) | 208251-52-9 | [report.md](compounds/hexarelin/report.md) | September 4, 2026 | Examorelin CID 6918297 / CAS 140703-51-1 + acetate 208251-52-9 / UNII 09QF37C617. Ghigo 1994 routes; Massoud PRL/cortisol. WADA S2.2.4. |
| [5-amino-1mq](compounds/5-amino-1mq/report.md) | 42464-96-0 | [report.md](compounds/5-amino-1mq/report.md) | September 4, 2026 | Cation CID 950107 / iodide CAS 42464-96-0; Neelakantan 2018 + Babula 2024 mouse only (oral F 3.5%); not a peptide; no human RCT. |
| [testagen](compounds/testagen/report.md) | 1026993-38-3 | [report.md](compounds/testagen/report.md) | September 4, 2026 | KEDG tetrapeptide; PubChem CID 404 this flight. Fedoreyeva 2011 HeLa nuclear/CAG binding. No human RCT. RUO 20 mg ≠ testosterone. |
| [pinealon](compounds/pinealon/report.md) | 175175-23-2 | [report.md](compounds/pinealon/report.md) | September 4, 2026 | CID 10273502 / CAS 175175-23-2; EDR tripeptide. Khavinson 2014 cortex-cell serotonin + docking. No UNII. No human RCT. RUO 20 mg ≠ epithalon. |
| [kisspeptin-10](compounds/kisspeptin-10/report.md) | 374675-21-5 | [report.md](compounds/kisspeptin-10/report.md) | September 4, 2026 | CID 25240297 / CAS 374675-21-5 / UNII FS1N52VS3S. George 2011 IV LH 4.1→12.4. Jayasena follicular null. Href CID 16131448 nociceptin. RUO ≠ KP-54. |
| [orforglipron](compounds/orforglipron/report.md) | 2212020-52-3 | [report.md](compounds/orforglipron/report.md) | September 4, 2026 | CID 137319706 / CAS 2212020-52-3; ATTAIN-1 36 mg −11.2% at 72 weeks; Mindful CID 135565576 + C45 formula wrong; SNAC capsule ≠ Lilly tablet. |
| [aniracetam](compounds/aniracetam/report.md) | 72432-10-1 | [report.md](compounds/aniracetam/report.md) | September 4, 2026 | CID 2196 / CAS 72432-10-1 / UNII 5L16LKN964. Senin 1991 N=109 SDAT vs placebo; Parnetti vs piracetam. RUO 750 mg ≠ Ampamet. Not named WADA 2026. |
| [epithalon](compounds/epithalon/report.md) | 307297-39-8 | [report.md](compounds/epithalon/report.md) | September 4, 2026 | CID 219042 / CAS 307297-39-8 AEDG; Khavinson 2003 fibroblasts + Al-dulaimi 2025 ALT-in-cancer; Anisimov 2003 mean LS null; FDA staff no insomnia evidence; no aging RCT. |
| [enclomiphene](compounds/enclomiphene/report.md) | 7599-79-3 | [report.md](compounds/enclomiphene/report.md) | September 4, 2026 | Citrate CID 6420009 / CAS 7599-79-3 / UNII J303A6U9Y6. Kim 2016 ZA-304 TT 445.8 ng/dL, sperm preserved. FDA CRL 2015; EMA EnCyzix refused 2018. RUO 12.5 mg ≠ Androxal. WADA S4.2. |
| [methylcobalamin](compounds/methylcobalamin/report.md) | 13422-55-4 | [report.md](compounds/methylcobalamin/report.md) | September 4, 2026 | CAS 13422-55-4 / UNII BR1SN1JS2W. Sawangjit 2020 15 RCTs RR 1.17 neuropathy. Mindful CID 5460224 is pipecolate ⛔. RUO ≠ Methycobal. |
| [cyanocobalamin](compounds/cyanocobalamin/report.md) | 68-19-9 | [report.md](compounds/cyanocobalamin/report.md) | September 4, 2026 | CID 16058087 / CAS 68-19-9 / UNII P6YC3EG204. USP IM repletion; labeled hypokalemia on intense megaloblastic treatment. RUO 10 mg/10 mL ≠ 1000 µg/mL. |
| [dsip](compounds/dsip/report.md) | 62568-57-4 | [report.md](compounds/dsip/report.md) | September 4, 2026 | CID 68816 / CAS 62568-57-4 / UNII YN28Z5YZ73 emideltide. Schneider vs Bes/Monti 🥼. FDA staff against 503A; PCAC 6–7–1 against. RUO ≠ 1980s IV. |
| [retatrutide](compounds/retatrutide/report.md) | 2381089-83-2 | [report.md](compounds/retatrutide/report.md) | September 4, 2026 | LY3437943 GIP/GLP-1/GCG agonist; CAS 2381089-83-2 on PubChem SID 523601838 (no CID this round). Jastreboff 2023 12 mg −24.2% at 48 weeks; no US label. |
| [mazdutide](compounds/mazdutide/report.md) | 2259884-03-0 | [report.md](compounds/mazdutide/report.md) | September 4, 2026 | CID 167312357 / CAS 2259884-03-0; GLORY-1 6 mg −12.55% at 32 weeks; NMPA weight + T2D 2025; RUO 10 mg ≠ Innovent 4/6 mg; no US label. |
| [cagrilintide](compounds/cagrilintide/report.md) | 1415456-99-3 | [report.md](compounds/cagrilintide/report.md) | September 4, 2026 | CID 171397054 / CAS 1415456-99-3; Lau 2021 4.5 mg −10.8%; REDEFINE 1 CagriSema −20.4%; Mindful CID 433770923 empty; RUO ≠ Novo 2.4 mg. |
| [tesofensine](compounds/tesofensine/report.md) | 402856-42-2 | [report.md](compounds/tesofensine/report.md) | September 4, 2026 | CID 11370864 / CAS 402856-42-2 / UNII BLH9UKX9V1. Astrup 2008 0.5 mg −9.2% at 24 weeks; t½ 234 h. Mindful href CID 11373595 wrong molecule. WADA S6. No US label. |
| [hcg](compounds/hcg/report.md) | 9002-61-3 | [report.md](compounds/hcg/report.md) | September 4, 2026 | CAS 9002-61-3 / UNII 20ED16GHEB, no CID. Pregnyl LH analogue; label kills obesity. Mindful MW 232 ⛔. WADA S2.2.1 males. |
| [l-carnitine](compounds/l-carnitine/report.md) | 541-15-1 | [report.md](compounds/l-carnitine/report.md) | September 4, 2026 | CID 10917 / CAS 541-15-1 / UNII 0G389FZZ9M. Malaguarnera 2007 2 g ×6 mo centenarians; Koeth 2013 TMAO. RUO 600 mg/mL ≠ Carnitor. |
| [ara-290](compounds/ara-290/report.md) | 1208243-50-8 | [report.md](compounds/ara-290/report.md) | September 4, 2026 | CID 91810664 / CAS 1208243-50-8 / UNII 9W5677JKDA. Culver 2017 4 mg CNFA +697 µm²; Dahan/Brines 28-day SFN. WADA S2.1.5 class, not named. RUO ≠ Bachem. |
| [slu-pp-332](compounds/slu-pp-332/report.md) | 303760-60-3 | [report.md](compounds/slu-pp-332/report.md) | September 4, 2026 | CID 5338394 / CAS 303760-60-3. ERR pan-agonist (not ERβ). Billon 2023 mouse IP ~70% longer run; Billon 2024 DIO −12% BW. No human RCT. Not named on WADA 2026. |
| [melanotan-1](compounds/melanotan-1/report.md) | 75921-69-6 | [report.md](compounds/melanotan-1/report.md) | September 4, 2026 | CID 16197727 / CAS 75921-69-6 / UNII QW68W3J66U. Linear 13-mer, not cyclic. Scenesse 16 mg EPP implant; Langendonk US 69.4 vs 40.8 h. RUO 10 mg ≠ implant. |
| [melanotan-2](compounds/melanotan-2/report.md) | 121062-08-6 | [report.md](compounds/melanotan-2/report.md) | September 4, 2026 | CID 92432 / CAS 121062-08-6. Cyclic heptapeptide amide. Dorr 1996 + Wessells 1998 ED. Extra CAS 75921-69-6 is afamelanotide. No US label. RUO ≠ Vyleesi/Scenesse. |
| [thymosin-alpha-1](compounds/thymosin-alpha-1/report.md) | 62304-98-7 | [report.md](compounds/thymosin-alpha-1/report.md) | September 4, 2026 | Thymalfasin CAS 62304-98-7 / CID 16130571. Zadaxin is ex-US HBV 1.6 mg SC BIW, not FDA-approved; TRIIM used rhGH, not this peptide. |
| [glutathione](compounds/glutathione/report.md) | 70-18-8 | [report.md](compounds/glutathione/report.md) | September 4, 2026 | CID 124886 / CAS 70-18-8 / UNII GAN16C9B8O. Richie 2015 oral 1 g +30–35% stores; Allen 2011 4-wk null. Hauser 2009 IV PD UPDRS miss. RUO ≠ Setria. |
| [cerebrolysin](compounds/cerebrolysin/report.md) | 12656-61-0 | [report.md](compounds/cerebrolysin/report.md) | September 4, 2026 | Mixture CAS 12656-61-0, no CID. CASTA N=1070 primary miss; CARS ARAT win. Href SID extra digit. 60 mg RUO ≠ 30 mL EVER. |
| [kpv](compounds/kpv/report.md) | 67727-97-3 | [report.md](compounds/kpv/report.md) | September 4, 2026 | α-MSH(11-13) CID 125672 / CAS 67727-97-3; Dalmasso/Kannengiesser mouse colitis; FDA staff against 503A; Mindful href CID 219062 is a dye. |
| [ss-31](compounds/ss-31/report.md) | 736992-21-5 | [report.md](compounds/ss-31/report.md) | September 4, 2026 | Elamipretide CID 11764719 / CAS 736992-21-5; Forzinity is Barth accelerated approval, not aging; Roshanravan one-dose ATP max; MMPOWER-3 miss. |
| [igf-1-lr3](compounds/igf-1-lr3/report.md) | 946870-92-4 | [report.md](compounds/igf-1-lr3/report.md) | September 4, 2026 | 83-mer Long Arg3-IGF-1 CAS 946870-92-4; PubChem that CAS hits a lipid CID this flight. Increlex is native 70-mer, not this vial. WADA S2.3. |
| [cjc-1295-no-dac](compounds/cjc-1295-no-dac/report.md) | 863288-34-0 | [report.md](compounds/cjc-1295-no-dac/report.md) | September 4, 2026 | Mindful CID 56841945 is the 29-mer (3368 Da). PubChem title CJC-1295 is DAC CID 91971820 (3647 Da); shared CAS 863288-34-0. Teichman is DAC. WADA S2.2.4. |
| [b7-33](compounds/b7-33/report.md) | 1818415-56-3 | [report.md](compounds/b7-33/report.md) | September 4, 2026 | CID 162662592 / CAS 1818415-56-3. Hossain 2016 RXFP1-biased B-chain; Devarakonda 2020 mouse MI 22 vs 45%. No human RCT. Not named WADA 2026. |
| [sermorelin](compounds/sermorelin/report.md) | 86168-78-7 | [report.md](compounds/sermorelin/report.md) | September 4, 2026 | Sermorelin INN CAS 86168-78-7 / CID 16132413. Geref acetate withdrawn (FR 2013 not-safety). Corpas 14-day GH/IGF-1; Vittone nightly DEXA null. |
| [selank](compounds/selank/report.md) | 129954-34-3 | [report.md](compounds/selank/report.md) | September 4, 2026 | CID 11765600 / CAS 129954-34-3 / UNII TS9JR8EP1G. Zozulia 2008 N=62 vs medazepam. Volkova 2016 GABA genes. RUO 10 mg ≠ 0.15% drops. No 503A vote. |
| [tb-500](compounds/tb-500/report.md) | 77591-33-4 | [report.md](compounds/tb-500/report.md) | September 4, 2026 | Mindful table is timbetasin CID 16132341 / CAS 77591-33-4; PubChem/FDA TB-500 is Ac-LKKTETQ 885340-08-9. SEER-1 NK 6/10 vs 1/8 p=0.0656. WADA S2. |
| [semax](compounds/semax/report.md) | 80714-61-0 | [report.md](compounds/semax/report.md) | September 4, 2026 | CID 9811102 / CAS 80714-61-0 / UNII I5FAL2585H. Dolotov 2006 BDNF. Gusev 2018 N=110. Mindful MW 854.99 ≠ 813.9/874.0. FDA staff against 503A; PCAC 8–5–1. |
| [ipamorelin](compounds/ipamorelin/report.md) | 170851-70-4 | [report.md](compounds/ipamorelin/report.md) | September 4, 2026 | CID 9831659 / CAS 170851-70-4 / UNII Y9M3S784Z6. Raun 1998 swine-selective GHS. Beck 2014 POI 25.3 vs 32.6 h p=0.15. WADA S2.2.4. |
| [mots-c](compounds/mots-c/report.md) | 1627580-64-6 | [report.md](compounds/mots-c/report.md) | September 3, 2026 | 16-aa mtDNA peptide; Lee mouse HFD/IR and Reynolds late-life capacity; n=10 endogenous exercise is not a vial RCT; NCT07505745 recruiting for insulin sensitivity. |
| [tesamorelin](compounds/tesamorelin/report.md) | 901758-09-6 | [report.md](compounds/tesamorelin/report.md) | September 4, 2026 | Tesamorelin acetate (CAS 901758-09-6 / CID 44147413); free base 218949-48-5 / CID 16137828. Egrifta HIV-VAT label; TRIIM used rhGH, not this peptide. |
| [pt-141](compounds/pt-141/report.md) | 189691-06-3 | [report.md](compounds/pt-141/report.md) | September 4, 2026 | CID 9941379 / CAS 189691-06-3 / UNII 6Y24O4F92S. Vyleesi 1.75 mg HSDD; FSFI-Desire +0.5/+0.6; SSE null. Nausea 40%. RUO 9 mg ≠ autoinjector. |
| [snap-8](compounds/snap-8/report.md) | 868844-74-0 | [report.md](compounds/snap-8/report.md) | September 4, 2026 | CID 76283482 / CAS 868844-74-0 / UNII 8K14HJF88S. Name SNAP-8 also hits CID 71587832. Lipotec 2010 17-woman imprint. RUO ≠ serum. |
| [bpc-157](compounds/bpc-157/report.md) | 137525-51-0 | [report.md](compounds/bpc-157/report.md) | September 4, 2026 | Pentadecapeptide CID 9941957 / CAS 137525-51-0; acetate 216441-37-1; rodent Sikiric file is not a human RCT; Lee 2021 IA knee phone survey; no aging RCT. |
| [ghk-cu](compounds/ghk-cu/report.md) | 89030-95-5 | [report.md](compounds/ghk-cu/report.md) | September 3, 2026 | Copper complex CID 71587328 / CAS 89030-95-5; Maquart rat wound collagen is not human restore; Miller 2006 topical objective-null; no SubQ aging RCT. |
| [aod-9604](compounds/aod-9604/report.md) | 386264-39-7 | [report.md](compounds/aod-9604/report.md) | September 4, 2026 | CID 71300630 Tyr-hGH 177–191; Mindful CID 16131447 is the wrong isomer; Stier 2013 safety / OPTIONS 2007 miss; WADA S2.2.3; no aging RCT. |
| [ahk-cu](compounds/ahk-cu/report.md) | 682809-81-0 | [report.md](compounds/ahk-cu/report.md) | September 4, 2026 | CID 168431292 / CAS 682809-81-0 (HCl). Storefront 49557-75-7 is free GHK ⛔. Pyo 2007 ex vivo only. Blend-only on REJUV-3X. |
| [jxl-069](compounds/jxl-069/report.md) | 2260696-63-5 | [report.md](compounds/jxl-069/report.md) | September 4, 2026 | CID 137374808 / CAS 2260696-63-5. Mindful 2232594-65-1 PubChem 404. Liu 2021 mouse topical MPC. No human RCT. Blend-only. |
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
