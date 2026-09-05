---
name: adversarial-research
description: Runs a Phase-0 rumor-mill briefing, a parallel validator / invalidator / domain-collector flight, then a compiler that link-checks and either loops the flight (max 5) or saves an AGENTS.md-marked writeup into hallmarks/, topics/, or compounds/. Use when the user asks to research a hallmark, fill or update a report, check whether a claim is true, investigate a compound, protocol, clinic practice, fad, smear, or rumor, or wants adversarial, steelman, or "is X true" research. Also use when docs-rag search cannot answer the actual question (empty or thin hits) — do not stop on "no supporting data." Repo-ops is not that path.
---

# Adversarial Research

Point this at a subject. Phase 0 briefing → Phase 1 three-agent flight → compiler. The compiler decides process (another flight or save). It does not pick a winner.

Repo law: [AGENTS.md](../../../AGENTS.md). Do not duplicate it. Read it. Obey it.

Prompt templates: [prompts.md](prompts.md). Carrot/bleach gold standard: [examples.md](examples.md).

## Inputs

| Input | Required | Notes |
|---|---|---|
| `subject` | yes | Hallmark, compound, protocol, rumor, claim, or free-text "is X true" |
| `claim` | no | Exact sentence under test if narrower than `subject` |
| `hallmark` | no | `01`–`14` or dir name. If omitted, route from the map below |
| `scope` | no | `full` (default), `mechanism`, `practice`, `rumor` — still run the whole pipeline |

Normalize a `slug`: lowercase, hyphens, no spaces. Example: `hbot`, `rapamycin`. Phase 0 gold standard in [examples.md](examples.md) is still carrots/bleach.

## Route the destination

| Case | Writeup | Sources |
|---|---|---|
| Maps to a hallmark | `hallmarks/NN-short-name/report.md` | `hallmarks/NN-short-name/sources/<emoji>/` |
| Named compound / molecule / intervention SKU | `compounds/<slug>/report.md` | `compounds/<slug>/sources/<emoji>/` |
| New non-molecule topic | `topics/<slug>/report.md` | `topics/<slug>/sources/<emoji>/` |

Hallmark map (from AGENTS.md):

| NN | Dir |
|---|---|
| 01 | `hallmarks/01-genomic-instability/` |
| 02 | `hallmarks/02-telomere-attrition/` |
| 03 | `hallmarks/03-epigenetic-alterations/` |
| 04 | `hallmarks/04-loss-of-proteostasis/` |
| 05 | `hallmarks/05-disabled-macroautophagy/` |
| 06 | `hallmarks/06-deregulated-nutrient-sensing/` |
| 07 | `hallmarks/07-mitochondrial-dysfunction/` |
| 08 | `hallmarks/08-cellular-senescence/` |
| 09 | `hallmarks/09-stem-cell-exhaustion/` |
| 10 | `hallmarks/10-altered-intercellular-communication/` |
| 11 | `hallmarks/11-chronic-inflammation/` |
| 12 | `hallmarks/12-dysbiosis/` |
| 13 | `hallmarks/13-extracellular-matrix-changes/` |
| 14 | `hallmarks/14-psychosocial-isolation/` |

A compound that *touches* a hallmark still lands at `compounds/<slug>/` if the writeup is the molecule. Rapamycin practice → can update `06` *and* land `compounds/rapamycin/`. A rumor, protocol, procedure, or clock-as-product that is not a molecule lands at `topics/<slug>/`. Do not stuff a smear into a hallmark just to have a home. Do not put compounds in `topics/`.

New topic or compound: create the tree, then run:

```bash
bash .cursor/skills/adversarial-research/scripts/init-topic-sources.sh topics/<slug>
bash .cursor/skills/adversarial-research/scripts/init-topic-sources.sh compounds/<slug>
```

That creates `sources/<emoji>/` dirs. File notes there. Marks live in AGENTS.md. Do not copy per-mark READMEs.

How to add a topic (not research one): `topics/<slug>/` (or `compounds/<slug>/`) + this init script + `report.md` + `scripts/index-meta.yaml` + `python3 scripts/build-index.py` + `reindex`. Point at those files. Do not reconstruct the list from an explore pass.

## Session folder

```
tmp/YYYY-MM-DD_<slug>/
  BRIEFING.md
  UPDATE.r{N}.md                 # only if compiler loops; N is the next flight
  FINDINGS.validator.r{N}.md
  FINDINGS.invalidator.r{N}.md
  FINDINGS.domain.r{N}.md
  DRAFT.md
  LINKCHECK.md
  DECISION.md
  staging/validator/r{N}/<emoji>/
  staging/invalidator/r{N}/<emoji>/
  staging/domain/r{N}/<emoji>/
```

Dump notes here first. Do not "finish" a report from memory. Default `{N}` starts at 1. Cap: **5** Phase 1 flights unless the user sets a lower number.

## Pipeline

```
Task progress:
- [ ] Session folder exists
- [ ] Phase 0 BRIEFING.md written (no verdict)
- [ ] Destination chosen (hallmark and/or compounds/<slug>/ and/or topics/<slug>/)
- [ ] Sources tree present
- [ ] Phase 1: three flight agents in parallel (BRIEFING + UPDATE.r{N} if any)
- [ ] Three FINDINGS.*.r{N}.md exist
- [ ] Compiler: DRAFT.md + LINKCHECK.md + DECISION.md
- [ ] If LINKCHECK has `http-403-needs-rescue` or a central `paywall-identified` row missing N/effect: **parent** launches paper-hunter `resolve-only` (compiler does not nest-spawn)
- [ ] If another_round and N < cap → write UPDATE.r{N+1}.md, increment N, repeat Phase 1
- [ ] If no, or N == cap → save report.md + sources/<emoji>/
- [ ] `scripts/index-meta.yaml` rewritten for this subject; `python3 scripts/build-index.py`
- [ ] `mcp/docs-rag/run.sh reindex` (or MCP `reindex`)
```

Do not return until every box is checked. Do not return after Phase 0, after launching Phase 1, or with "compiler starts after they file findings." That is not done. One subject per run.

### Thin-ask trigger

If this flight started because `search_docs` could not answer the actual question (empty or thin hits, not repo-ops), the parent already told the user: "Hey, I don't have all the facts yet. I am going to go do some research. This will take a while. Is that okay?" That is a real flight, not a briefing-only detour.

- Complete Phase 0 + **at least one** Phase 1 + compiler before talking to the user again about the answer.
- After that compiler pass, read `DECISION.md`. If `question_answerable_now` is yes, the parent answers the original question from the compiled, link-checked claims **now**. Then continue save or loop per the compiler.
- If `question_answerable_now` is no, loop per the decision rubric (cap 5). Do not return "no supporting data." Answer from the draft, or say what is still unknown with marks.
- Do not skip Phase 1 because Phase 0 found nothing in-repo. That is why the flight exists.

### Phase 0 — rumor mill (not a decision)

Orchestrator (or one subagent) only. **Before** the flight.

Job: gather context so the flight is not framed-stupid. Search the slogan, the controversy, the marketing, the political smear, the definition trap. Do **not** decide true/false. Do **not** validate or invalidate. Do **not** write `report.md`. Do **not** skip the flight because the rumor looks dumb.

**Repo first.** Load MCP `docs-rag`, then call `search_docs` on the subject and the claim. CLI (`mcp/docs-rag/run.sh search "…"`) only if they cannot enable the server this turn. Put the hits in `already_in_repo`. If the user asked a question and did **not** ask to research, update, or fill a report, and the hits answer that question, cite the files and stop — do not start Phase 1. If they asked to research or update, or this run is a thin-ask trigger (search already failed to answer), the flight still runs; the hits are starting context, not a verdict. Do not abort after Phase 0 because `already_in_repo` is empty.

Checklist (every item, even if the answer is "none found"):

1. Claim as asked
2. Claim as used in the wild
3. Nearby true facts that get laundered into the claim
4. Who is pushing it
5. Incentive
6. Date / fad cycle
7. Definition traps (asked-meaning vs technical meaning)
8. Framing hazards for the validator (what "hits" will look like that are not the claim)

Write `BRIEFING.md` with this schema. No evidence-mark emojis in the briefing — it is meta-context, not the writeup. Phase 0 may say "this circulates as a smear / fad / marketing frame." That is frame, not a research conclusion.

```markdown
# Phase 0 briefing

- subject:
- slug:
- destination: hallmarks/NN-short-name/ | compounds/<slug>/ | topics/<slug>/
- already_in_repo:
  - query:
    hits:
      - path:
        heading:
        note:
- claim_as_asked:
- claim_as_used_in_the_wild:
- nearby_true_facts_that_get_laundered:
  - fact:
    how_laundered:
- who_is_pushing:
  - actor:
    incentive:
- date_fad_cycle:
- definition_traps:
  - word:
    asked_meaning:
    technical_meaning:
- framing_hazards_for_validator:
  - hit_that_is_not_the_claim:
    why_not_the_claim:
- venues_that_will_lie_by_omission:
- what_the_words_actually_mean:
- political_smear_or_marketing: none | smear | fad | slogan | bait-and-switch
  one_line_meta:
- must_not_treat_as_settled:
- flight_still_runs: true
```

Filled gold standard: [examples.md](examples.md) (carrots / bleach).

Phase 0 is **forbidden** to: issue a verdict; write "so it is false"; mark the claim ⛔ or 📚 as if researched; skip or shrink the flight; tell the three agents who should win.

### Phase 1 — three agents, parallel

`BRIEFING.md` must exist first. Then launch **three Task/subagents in one message**. Same briefing. Wait for all three FINDINGS files. Then run Compiler. Do not return after launch. On round 2+ they also read `UPDATE.r{N}.md`. Asymmetric mandates. They cannot win by being louder.

| Role | Job | Search bias |
|---|---|---|
| Validator | Steelman and hunt confirmation | Positive trials, supporting mechanisms, practice that matches the *real* claim |
| Invalidator | Hunt failure of that same claim | Nulls, failed replications, harms, definition games, conflicts |
| Domain collector | Map the field. Cover every Phase 0 must-watch / `who_is_pushing` / clinic-tourism item. Adjacent-hallmark side quests are extra, not a substitute. | Reviews, measurement, clinic/biohacker practice, adjacent hallmarks, 🥼 vs 🤼 |

Copy the role blocks from [prompts.md](prompts.md). Fill `{SESSION}`, `{BRIEFING}`, `{UPDATE}`, `{ROUND}`, `{STAGING}`, `{FINDINGS}`.

Each agent:

- Reads AGENTS.md, `BRIEFING.md`, and `UPDATE.r{N}.md` if it exists
- Treats `framing_hazards_for_validator` as binding
- Writes **only** `FINDINGS.<role>.r{N}.md` plus files under `staging/<role>/r{N}/`
- Stops. No `report.md`. No shared `FINDINGS.md` (parallel appends race)

Reuse from collective-collaborative-deep-dive: one shared problem, role-split, per-role files. Do **not** reuse its plan-approval, Jira, consensus-to-act, or review-gate.

### Compiler — after each Phase 1

One agent, sequential. Does **not** re-search from scratch. Copy the compiler block from [prompts.md](prompts.md).

Reads: `BRIEFING.md` + all `FINDINGS.*.r*.md` + staged notes + prior `DRAFT.md` if any.

Does four jobs:

1. **Compile** those files into `{SESSION}/DRAFT.md`. Both sides present. Phase 0 framing in the draft. No tidy winner.
2. **Review and update** so the draft follows AGENTS.md (marks, sources, voice, one not-medical-advice paragraph, ☠︎︎ vs ⛔, 🥼 vs 🤼, 📜 vs 📚).
3. **Test every source link** (fetch or HEAD the URL, DOI, PMID). Write `{SESSION}/LINKCHECK.md`. Dead, 404, invented, or paywall-only-without-identity (cannot resolve title/authors) → drop or flag the citation. The claim is removed or downgraded. No hallucinated leftovers. HTTP 403 / need-a-browser is **not** invented or dead — resolve via DOI, PMID, or Crossref before drop. Do not drop on the first 403. Do not classify a 403 as `paywall-no-identity`. Mark those rows `http-403-needs-rescue`. A paywall that already has title/authors/DOI or PMID is `paywall-identified`.
4. **Decide process**, not truth. Write `{SESSION}/DECISION.md`. Include whether the user’s original question is answerable from this round. Then either loop Phase 1 or save. The parent answers the user now if `question_answerable_now` is yes — do not wait for a save to do that.

After `LINKCHECK.md` exists, the **parent** (not the compiler) launches [paper-hunter](../paper-hunter/SKILL.md) in `resolve-only` for each `http-403-needs-rescue` row and for a central `paywall-identified` citation that still lacks N/effect. The compiler does not nest-spawn. Hunt packet lands in the research session or `tmp/YYYY-MM-DD_paper-hunter/<slug>/`. The compiler or the next flight uses `IDENTITY.md` / `FULLTEXT.md`. Do not drop on the first 403.

```markdown
# DECISION
- another_round: yes | no
- reason: <which YES rubric line fired, or "none of the YES lines; polish-only leftovers">
- question_answerable_now: yes | no
- answer_from_this_round: <marked, cited sentences the parent can give the user> | not yet
- briefing_was_wrong_about_meta: no | yes
- gaps_if_saving_at_cap:
```

`question_answerable_now` is about the user’s question, not about whether the public `report.md` is finished. Yes means the parent must answer now. No means loop if the rubric says so; do not dump “no supporting data.”

#### Decision rubric

Phase 0 **must-watch** = `who_is_pushing` actors + `framing_hazards_for_validator` rows + any clinic, protocol, brand, or practice name the briefing already listed. If an existing `{REPORT}` has a practice/protocol section, that map is must-watch too.

Another round is warranted when any of these are true:

- The user’s actual question is still not answerable from compiled, link-checked claims
- A central citation is dead and the claim matters
- Validator and invalidator talked past different definitions (Phase 0 trap was missed)
- A 🥼/🤼 fight is missing one side
- Sources were not filed / marks are missing on a material statement
- Existing report (or Phase 0 must-watch list) had a practice/protocol map that this draft deleted, stubbed ("not re-fetched"), or did not re-source — that is a loop, not polish
- A Phase 0 must-watch item has no filed source and no `HAZARD SKIPPED` / explicit coverage in the draft
- Domain collector (or the draft) never touched a Phase 0 must-watch topic

Another round is **not** warranted for: polish, more papers that will not change the answer, or a prettier narrative. Shrinking a rewrite is **not** a reason to skip a loop if the shrink dropped practice that Phase 0 or the prior report already had.

The compiler does not pick a winner to look tidy.

**Yes** → write `UPDATE.r{N+1}.md`. Orchestrator restarts Phase 1. Agents read Phase 0 + the update packet. Do **not** re-run Phase 0 unless the compiler finds the briefing was wrong about the meta (smear / fad / definition). Then rewrite `BRIEFING.md` and say so in the update packet.

**No** → compile the final report and save it (see Save).

**Cap: 5** Phase 1 flights unless the user sets a lower number. After the 5th compiler pass, save. Flag remaining gaps in the report. Do not loop.

#### Update-packet schema

```markdown
# UPDATE r{N}

- round_launching:
- prior_rounds:
- still_unanswered:
  - question:
    who_hunts: validator | invalidator | domain
- dead_links_that_matter:
  - citation:
    claim_it_supported:
    replacement_needed:
- framing_traps_that_bit:
- definition_mismatch:
  - validator_used:
    invalidator_used:
    use_this:
- missing_fight_side: 🥼 | 🤼 | none
- missing_marks_or_unfiled_sources:
- do_not_relitigate:
- briefing_rewrite: no | yes + why
- flight_still_runs: true
```

#### Draft / save rules

- Every asserting sentence starts with exactly one of: 💯 📚 📜 🥼 🤔 🤼 ⛔ 🐉 ☠︎︎
- Titles, headers, and bare citations do not get marks
- Mixed grades → split the sentence
- Phase 0 framing near the top, after the single not-medical-advice paragraph
- Validator and invalidator land in the **same** sections (mechanism, animal, human, practice)
- Paper-vs-paper fight → 🥼, both sides. Amateur fight → 🤼, never for papers
- Practice ≠ efficacy. Clinic/forum doses are 🤔
- No lifestyle sermons. No recommend for/against. No action ladder. No "talk to your doctor"
- Doses are observed practice, with a source and a mark
- Dead or invented citations: drop the claim
- Updating an existing report: weave; do not wipe; do not restore `template.md` sermons. A stub or "not re-fetched this round" in place of a prior practice map is a wipe — loop, do not save
- 💯 is textbook-uncontested only. A consensus or famous review (López-Otín included) is 📚, not a 💯 parking lot
- New report: `template.md` is section skeleton only; voice is AGENTS.md. Never write a filled report into `template.md`.
- Speculative section is required. Mark 🐉 or 🤔 and move on

#### Save

Only when `another_round` is no, or the cap is hit.

1. File sources:
   1. Copy surviving staged sources into the destination `sources/<emoji>/` by how the **claim** is marked in `report.md`. Name: `Author-Year-short-slug.ext`.
   2. Same-mark dedup: before adding a note, search **note bodies** in that same `sources/<emoji>/` for the same DOI, PMID, or URL (not the filename). If one is already there, keep that file. Do not add a second slug for the same ID in that dir.
   3. Cross-mark sibling: if the same URL also backs a claim with a different mark, that is a second card in the other mark dir. `Used for` and `Mark` on each card match that dir only. Do not copy a mixed card across dirs. Do not skip the second card because the first exists.
   Each copied or rescue-written note must fill `N / effect / population / endpoint / duration` from the fetched paper (n or "n not reported", population/strain, comparator, endpoint, duration, effect). A gloss that only restates the claim is not filed.
2. Write `report.md`:

| Case | Writeup | Sources |
|---|---|---|
| Existing hallmark | `hallmarks/NN-short-name/report.md` | that hallmark’s `sources/<emoji>/` |
| Compound | `compounds/<slug>/report.md` | `compounds/<slug>/sources/<emoji>/` (create the tree if needed) |
| New topic | `topics/<slug>/report.md` | `topics/<slug>/sources/<emoji>/` (create the tree if needed) |

Working notes stay in `tmp/YYYY-MM-DD_<slug>/`. Do not delete them. Do not cite `tmp/` or other gitignored paths from `report.md`.

Then, still before returning:

3. Rewrite `scripts/index-meta.yaml` status + one_liner for this subject. Run `python3 scripts/build-index.py`. Do not hand-edit README `BEGIN GENERATED` blocks.
4. Reindex: `mcp/docs-rag/run.sh reindex` (or MCP `reindex`).

## Hard constraints (AGENTS.md)

- We document. We do not recommend for or against — except ☠︎︎, where stay-away is required.
- Hallucinations are not tolerated. Fetch the paper.
- 💯 is expensive. Textbook-grade, uncontested. One paper is 📚. A famous or consensus review is 📚, not 💯. A preprint is 📜. Live literature fight is 🥼.
- ☠︎︎ is sure meaningful harm, not Prop-65 theater. ⛔ is suspect / does not make sense.
- "What people are doing" can be 🤔 when efficacy is null or 🐉.
- Commercial conflict gets a clause ("X sells the capsule"), not a sermon.

## Additional resources

- [prompts.md](prompts.md) — Phase 0, Phase 1, and compiler prompts
- [examples.md](examples.md) — carrots/bleach briefing (Phase 0 gold standard)
- [AGENTS.md](../../../AGENTS.md) — marks, voice, source rules
- [docs-rag](../docs-rag/SKILL.md) — search already-written reports before a new flight
- [paper-hunter](../paper-hunter/SKILL.md) — parent-launched `resolve-only` for LINKCHECK 403 / central paywall missing N/effect
- `template.md` — heading skeleton only
