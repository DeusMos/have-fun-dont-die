# Paper hunter — legal ladder

The script [scripts/resolve.py](scripts/resolve.py) walks these hops in order. Run the script. Do not skip to a pirate mirror because a publisher returned 403.

## Hops

| Hop | Needs | What it returns |
|---|---|---|
| Crossref | DOI or bibliographic string | Title, authors, year, venue, DOI, publisher links |
| PubMed eutils | DOI, PMID, or query | PMID, PMCID, journal, article ids |
| Europe PMC | DOI / PMID / PMCID | PMCID, `fullTextUrlList`, PMC HTML + PDF URLs |
| Unpaywall | DOI **and** email | `best_oa_location`, `oa_locations`, license, oa_status |
| OpenAlex | DOI or title | Work record, `best_oa_location`, repository copies |
| Semantic Scholar | DOI or PMID | `openAccessPdf`, external ids |
| bioRxiv / medRxiv | `10.1101/…` or a `*rxiv` DOI | Versioned preprint PDF |

Unpaywall email: `--email` or `HFDD_UNPAYWALL_EMAIL`. Missing email = that hop is skipped and recorded. Other hops still run.

Polite User-Agent: `have-fun-dont-die-paper-hunter/1.0` plus `mailto:` when an email is set.

## After the JSON

If `oa.pdf_url` is set, fetch it. If only `oa.best_url` is set, open that page and look for a publisher PDF, PMC PDF, or author-manuscript PDF on the same host or on `nihms.nih.gov` / `europepmc.org` / a university DSpace URL listed in `oa.locations`.

Then, if still no file, keep digging **on the record you already identified**:

1. PMC author manuscript (`nihms-…`, `PMC…`).
2. Accepted manuscript on the corresponding author’s lab or university page (search author + title + `pdf`).
3. Institutional repository / OSF / figshare / Zenodo already listed by OpenAlex or Unpaywall.
4. A preprint that is the same title + overlapping authors + same figures, not a different paper.
5. Conference abstract or thesis only if it is clearly the same work; mark it for what it is.

A 403 on the publisher DOI is normal. It is not “the paper does not exist.”

## Blocked hosts

`resolve.py` drops URLs whose host is Sci-Hub, LibGen, Anna’s Archive, Z-Library, or a listed mirror. Do not add those URLs by hand. Do not write a fetch script for them.

Identity without OA is still a result: cite the DOI/PMID as paywall-identified. Do not fill N/effect from a remembered PDF.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Identity established. OA may be `none`. |
| 2 | No DOI, PMID, or title+year after all hops. |
| 2 (argparse) | Caller passed no query flags. |

A hop that errors is `ok: false` in `hops`. That is visible failure, not a hidden fallback.

Unit tests (no network). Run from `scripts/`:

```bash
cd .cursor/skills/paper-hunter/scripts && python3 -m unittest test_resolve.py
```

Do not pass the file path to `python3 -m unittest` from the repo root — that treats the path as a module name.

## Manual calls (if the script is the wrong shape)

```bash
# Crossref
curl -sL -A "have-fun-dont-die-paper-hunter/1.0" \
  "https://api.crossref.org/works/10.1038/s41586-022-04618-z"

# Unpaywall
curl -sL "https://api.unpaywall.org/v2/10.1038/s41586-022-04618-z?email=you@example.com"

# Europe PMC
curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41586-022-04618-z&format=json&resultType=core"

# OpenAlex
curl -sL "https://api.openalex.org/works/doi:10.1038/s41586-022-04618-z"
```

Prefer the script. These are for a hop the JSON marked failed and you need the raw error body.
