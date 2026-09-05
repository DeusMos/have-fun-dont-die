---
name: paper-hunter
description: >-
  Resolves hard-to-find papers via Crossref, PubMed, PMC, Unpaywall, OpenAlex,
  Semantic Scholar, and preprint or author-manuscript paths, then uses docs-rag
  to patch related hallmarks/, topics/, and compounds/ reports. Use when a
  citation is paywalled, 403, missing full text, a source note is unfetched,
  the user asks to find a paper, or a research flight cannot fetch a central
  source. Does not use pirate mirrors.
---

# Paper hunter

Find the paper. Identify it. If a legal OA copy exists, read it. Then ask `docs-rag` which writeups that paper actually changes, and patch those — compounds, hallmarks, topics — without wiping them.

Repo law: [AGENTS.md](../../../AGENTS.md). Hunt APIs: [reference.md](reference.md). This is not a research flight. Do not start [adversarial-research](../adversarial-research/SKILL.md) from here. Do not invent a citation.

This repository is not medical advice. Say that once if you touch a biology writeup. Then stop.

## Modes

| Mode | When | Writes `report.md`? |
|---|---|---|
| `resolve-only` | Compiler / flight handoff. LINKCHECK 403 or paywall with empty N/effect. Parent asked only to find the PDF. | No. Hunt packet only. |
| `resolve-and-patch` | User asked to find a paper **and** update related reports. Default for a standalone ask. | Yes. Weave. Do not wipe. |

An active adversarial-research flight owns `report.md`. If you were spawned from that flight, you are `resolve-only` unless the parent said otherwise.

## Task progress

```
- [ ] Session folder exists
- [ ] Citation parsed (DOI / PMID / PMCID / title+year / messy query)
- [ ] resolve.py ran; RESOLVE.json written
- [ ] IDENTITY.md written (or hunt failed visibly)
- [ ] Legal OA PDF/HTML fetched into the session folder when a URL exists
- [ ] RELATED.md from docs-rag + reading the cited report.md files
- [ ] If resolve-and-patch: source notes filed; reports woven; reindex
- [ ] Stop with a hunt summary
```

## Session folder

```
tmp/YYYY-MM-DD_paper-hunter/<slug>/
  RESOLVE.json
  IDENTITY.md
  FULLTEXT.md
  RELATED.md
  HUNT.md
  <slug>.pdf          # only if a legal OA PDF was fetched
```

`<slug>` = first-author-year or a short doi tail. Dump notes here first. Do not cite `tmp/` from `report.md`.

## Resolve

Run the script. Do not reimplement the hops in a one-off shell snippet.

```bash
python3 .cursor/skills/paper-hunter/scripts/resolve.py \
  --doi 10.1038/s41586-022-04618-z \
  --email "$HFDD_UNPAYWALL_EMAIL" \
  --out tmp/YYYY-MM-DD_paper-hunter/<slug>/RESOLVE.json
```

`--pmid`, `--pmcid`, `--title --year`, or `--query "Cagan 2022 Nature crypt"` also work. Unpaywall needs `--email` or `HFDD_UNPAYWALL_EMAIL`. Missing email skips that hop and records the skip. It does not invent an OA URL.

Exit `2` = no bibliographic identity. That is a failed hunt. Say so. Do not guess a paper.

If `oa.status` is `oa-pdf` or `oa-html`, fetch `oa.pdf_url` or `oa.best_url` into the session folder. Those fields are legal OA only — publisher DOI landings, Crossref `link[]`, closed OpenAlex `primary_location`, and Semantic Scholar landing pages do not set them. Confirm it is the same title/DOI before extracting numbers. Then read enough of the paper to fill `N / effect / population / endpoint / duration`. An abstract-only landing page is not a filled source note.

Write `IDENTITY.md`:

```markdown
# Identity
- title:
- authors:
- year:
- venue:
- doi:
- pmid:
- pmcid:
- oa_status:
- best_url:
- pdf_url:
- license:
```

Write `FULLTEXT.md`: `oa-pdf` | `oa-html` | `abstract-only` | `identity-only` plus the local path if you fetched a file.

Write `HUNT.md` as a table: hop | ok | note. Copy from `RESOLVE.json` hops. Do not hide a failed hop.

## What you will not do

- Do not fetch or link Sci-Hub, LibGen, Anna’s Archive, Z-Library, or any other pirate mirror. Persistence is the legal ladder in [reference.md](reference.md).
- Do not paste substantial copyrighted text into a report. Numbers, methods, and a short cited claim are the job.
- Do not invent a DOI, PMID, or paper.
- Do not drop a 403 on first contact. Resolve identity via DOI / PMID / Crossref, then this ladder.
- Do not start a new `topics/` or `compounds/` page. Hand that to adversarial-research.
- Do not spawn nested paper-hunters.
- Do not use user-level `markdown_rag`.

A paywall-identified paper (title + authors + DOI or PMID live) may stay as a citation. You still cannot fill `N / effect / …` from memory. If the abstract states those fields, use the abstract and say so on the card.

## RAG: what needs updating

After identity exists. Same load-first rule as [docs-rag](../docs-rag/SKILL.md).

1. Load MCP `docs-rag`. Inspect `search_docs`. CLI only if they cannot enable the server this turn.
2. Search at least twice, `k=12`:
   - title + first author + year
   - DOI and/or the molecule / mechanism / hallmark the paper is actually about
3. Read the cited `report.md` / source notes. Hits are pointers.
4. Judge whether this paper changes a claim, fills an unfetched note, adds a missing fight side, or is off-topic. Do not decide that by counting keywords.
5. Write `RELATED.md`:

```markdown
# Related writeups
- query:
  hits:
    - path:
      heading:
      belongs: yes | no
      why:
      proposed_edit:
```

`belongs: no` is a valid result. Do not patch those files.

## Patch (resolve-and-patch only)

For each `belongs: yes` row:

1. Weave the new fact into the existing section. Do not wipe. Do not restore `template.md` sermons.
2. Mark the asserting sentence. One paper is 📚. Preprint is 📜. Live paper fight is 🥼 (both sides). Do not upgrade a mark because the PDF was hard to get.
3. File a source note under that writeup’s `sources/<emoji>/` matching the mark on **that** sentence. Name: `Author-Year-short-slug.md`.
4. Same-mark dedup: search note **bodies** in that dir for the same DOI, PMID, or URL. If one exists, keep it and update the card. Do not add a second slug for the same ID in that dir.
5. Cross-mark sibling: same URL backing a different mark in another sentence is a second card in the other mark dir.
6. Every filed card fills `N / effect / population / endpoint / duration` from the fetched paper (or from the abstract, labeled as such). A gloss that restates the claim is not filed.

Card shape (existing house style):

```markdown
# FirstAuthor et al., Venue Year
https://doi.org/10.xxxx/yyyy
PMID nnn
Used for: <the marked claim this card backs>
Mark: 📚
N / effect / population / endpoint / duration: …
Conflict if any: …
```

Then:

- `reindex` (MCP or `mcp/docs-rag/run.sh reindex`).
- `python3 scripts/build-index.py` only if you changed sidecar fields or `##` headings. Body-only and source-note edits do not need the catalog.

`--mode=ask` cannot write. Same sentence as docs-rag: drop `--mode=ask`.

## Flight handoff (resolve-only)

Parent reads `LINKCHECK.md`. For each `http-403-needs-rescue` or a central `paywall-identified` row that still lacks N/effect, spawn this agent (`subagent_type: "paper-hunter"`) with the citation and the research session path. You write the hunt packet into that session (or into `tmp/YYYY-MM-DD_paper-hunter/<slug>/`). You do not save `report.md`. The compiler or the next flight uses `IDENTITY.md` / `FULLTEXT.md`.

## Output to the parent

- One-line result: found OA / identity-only / failed.
- DOI, PMID, best legal URL.
- Paths in `RELATED.md` you patched, or “resolve-only; no report edit.”
- Hops that failed, if identity or OA is missing.
