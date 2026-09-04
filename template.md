# Template

Section skeleton only. Voice, marks, and source rules: [AGENTS.md](AGENTS.md).

Do not fill this file. Do not copy a finished writeup back into it. Destination is `hallmarks/NN-short-name/report.md`, `topics/<slug>/report.md`, or `compounds/<slug>/report.md`.

One not-medical-advice paragraph per document, then stop:

This repository is not medical advice. It is a sourced information dump for people who already experiment on themselves.

Every asserting sentence starts with an evidence mark. Titles, headers, and bare citations do not.

---

## Hallmark or topic

Topics use the same sections as hallmarks. Title a hallmark `# The Hallmarks of Aging: <Name>`. Title a topic `# Topic: <Name>`.

```markdown
# The Hallmarks of Aging: <Name>

**Hallmark:** <name>
**Evidence cutoff:** <Month D, YYYY>
**Last updated:** <Month D, YYYY>

This repository is not medical advice. It is a sourced information dump for people who already experiment on themselves.

## Contents

- [The claim and the slogan](#the-claim-and-the-slogan)
- [What the words mean](#what-the-words-mean)
- [Mechanism](#mechanism)
- [Animal data](#animal-data)
- [Human data](#human-data)
- [Measurement](#measurement)
- [What clinics and self-experimenters are doing](#what-clinics-and-self-experimenters-are-doing)
- [Speculative](#speculative)
- [Named compounds](#named-compounds)
- [Adjacent hallmarks](#adjacent-hallmarks)
- [What is actually on the table](#what-is-actually-on-the-table)

## The claim and the slogan

The scientific claim under test. The slogan in the wild. Nearby true facts vs the product. Commercial conflict as a clause.

## What the words mean

Terms, what they are not, clinic English vs the paper.

## Mechanism

How the biology works. Nulls and counter-mechanisms stay here.

## Animal data

Model, N, dose, duration, endpoint, effect size. Nulls and harms in the same section.

## Human data

Population, N, endpoint, effect size. A biomarker move is not a healthspan result. Nulls and harms stay here.

## Measurement

What assays exist, what they actually score, what clinics sell as a score.

## What clinics and self-experimenters are doing

Observed practice, not instructions. Dose, source, who sells it. Practice can be 🤔 when efficacy is null or 🐉.

## Speculative

Required. Mark 🐉 or 🤔 and move on.

## Named compounds

Per-molecule dossiers extracted from this report. Not a recommendation. Only compounds this page actually uses. Catalog: [compounds/README.md](compounds/README.md).

- [<slug>](../../compounds/<slug>/report.md) — why it is on this page

## Adjacent hallmarks

Links and the actual coupling, not a taxonomy dump.

## What is actually on the table

What is known, what is a fight, what people are buying, what is still a guess. No action ladder.
```

---

## Compound

Title `# Compound: <Name>`. CAS is a first-class field. Rules: [compounds/README.md](compounds/README.md).

```markdown
# Compound: <Name>

**CAS:** <number | pending | none>
**Evidence cutoff:** <Month D, YYYY>
**Last updated:** <Month D, YYYY>

This repository is not medical advice. It is a sourced information dump for people who already experiment on themselves.

## Contents

- [Identity](#identity)
- [The claim and the slogan](#the-claim-and-the-slogan)
- [Mechanism](#mechanism)
- [Pharmacokinetics / pharmacodynamics](#pharmacokinetics--pharmacodynamics)
- [Animal data](#animal-data)
- [Human data — aging, off-label, and geroscience](#human-data--aging-off-label-and-geroscience)
- [Toxicity and hazards](#toxicity-and-hazards)
- [Interactions](#interactions)
- [Formulations and source quality](#formulations-and-source-quality)
- [Observed practice](#observed-practice)
- [Fights](#fights)
- [Legal / access status](#legal--access-status)
- [Related hallmarks](#related-hallmarks)
- [Related compounds](#related-compounds)
- [Open questions](#open-questions)
- [What is actually on the table](#what-is-actually-on-the-table)

## Identity

Home hallmark. Aliases. Related molecules that already have their own dir.

## The claim and the slogan

What is sold vs what the papers measured.

## Mechanism

Target, pathway, what the molecule is not.

## Pharmacokinetics / pharmacodynamics

Half-life, bioavailability, CYP, tissue. Do not invent a table.

## Animal data

Model, N, dose, duration, endpoint, effect size. Nulls stay here.

## Human data — aging, off-label, and geroscience

Aging / off-label / geroscience first. Approved-indication data only when it bears on the aging claim. Nulls stay here.

## Toxicity and hazards

Established harm is ☠︎︎. Boxed warnings, known toxicities.

## Interactions

Documented interactions, not a sermon.

## Formulations and source quality

What is sold, what the trial used, gray-market vs pharmacy.

## Observed practice

Practice is not efficacy. Doses are observed, not instructions.

## Fights

Paper fight → 🥼. Amateur fight → 🤼.

## Legal / access status

Rx, supplement, compounded, research chemical. Not a recommendation.

## Related hallmarks

Links.

## Related compounds

- [<slug>](../<slug>/report.md) — why it is adjacent

## Open questions

What is still unknown.

## What is actually on the table

No action ladder.
```

---

## Compounds

Existing molecule pages. Link these from Named compounds / Related compounds. Do not invent a slug that has no dir. Full catalog: [compounds/README.md](compounds/README.md).

- [rapamycin](compounds/rapamycin/report.md)
- [everolimus](compounds/everolimus/report.md)
- [rtb101](compounds/rtb101/report.md)
- [metformin](compounds/metformin/report.md)
- [nicotinamide-riboside](compounds/nicotinamide-riboside/report.md)
- [nicotinamide-mononucleotide](compounds/nicotinamide-mononucleotide/report.md)
- [nad](compounds/nad/report.md)
- [fisetin](compounds/fisetin/report.md)
- [dasatinib](compounds/dasatinib/report.md)
- [quercetin](compounds/quercetin/report.md)
- [fucoidan](compounds/fucoidan/report.md)
- [spermidine](compounds/spermidine/report.md)
- [urolithin-a](compounds/urolithin-a/report.md)
- [resveratrol](compounds/resveratrol/report.md)
- [berberine](compounds/berberine/report.md)
- [colchicine](compounds/colchicine/report.md)
- [semaglutide](compounds/semaglutide/report.md)
- [tirzepatide](compounds/tirzepatide/report.md)
- [oxytocin](compounds/oxytocin/report.md)
- [beta-carotene](compounds/beta-carotene/report.md)
