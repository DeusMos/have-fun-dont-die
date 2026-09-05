#!/usr/bin/env python3
"""Resolve a citation to bibliographic identity and legal OA locations.

Hops: Crossref, PubMed, Europe PMC, Unpaywall, OpenAlex, Semantic Scholar,
bioRxiv / medRxiv. Pirate-mirror hosts are rejected if an API returns them.

Usage:
  python3 resolve.py --doi 10.1038/s41586-022-04618-z
  python3 resolve.py --pmid 18065594
  python3 resolve.py --title "Annual somatic mutation rate" --year 2022
  python3 resolve.py --query "Cagan 2022 Nature intestinal crypt mutation"

Unpaywall needs an email: --email or HFDD_UNPAYWALL_EMAIL. Missing email
skips that hop and records the skip. It does not invent an OA URL.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

TIMEOUT_SEC = 20
SCRIPT_NAME = "have-fun-dont-die-paper-hunter/1.0"
CROSSREF = "https://api.crossref.org/works"
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
EUROPE_PMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UNPAYWALL = "https://api.unpaywall.org/v2"
OPENALEX = "https://api.openalex.org/works"
SEMANTIC_SCHOLAR = "https://api.semanticscholar.org/graph/v1/paper"
BIORXIV = "https://api.biorxiv.org/details"

# Hostname suffixes / exact hosts. URL-host validation, not intent classification.
BLOCKED_HOST_SUFFIXES = (
    "sci-hub.se",
    "sci-hub.st",
    "sci-hub.ru",
    "sci-hub.box",
    "sci-hub.red",
    "sci-hub.ee",
    "sci-hub.ren",
    "libgen.is",
    "libgen.li",
    "libgen.rs",
    "libgen.st",
    "library.lol",
    "libgen.gs",
    "annas-archive.org",
    "annas-archive.se",
    "z-library.sk",
    "z-lib.fm",
    "1lib.sk",
)

DOI_RE = re.compile(
    r"10\.\d{4,9}/[-._;()/:A-Z0-9]+",
    re.IGNORECASE,
)
PMID_RE = re.compile(r"^\d{1,9}$")

log = logging.getLogger("paper-hunter")


@dataclass
class Hop:
    name: str
    ok: bool
    note: str


@dataclass
class Identity:
    title: str | None = None
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    venue: str | None = None
    doi: str | None = None
    pmid: str | None = None
    pmcid: str | None = None
    type: str | None = None


@dataclass
class Location:
    url: str
    kind: str
    source: str
    license: str | None = None
    is_pdf: bool = False
    is_oa: bool = False


@dataclass
class Result:
    query: dict[str, Any]
    identity: Identity
    oa: dict[str, Any]
    hops: list[Hop] = field(default_factory=list)

    def to_json(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "identity": asdict(self.identity),
            "oa": self.oa,
            "hops": [asdict(h) for h in self.hops],
        }


def normalize_doi(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text, flags=re.IGNORECASE)
    text = text.removeprefix("doi:")
    return text.strip().rstrip(".").lower()


def extract_doi(text: str) -> str | None:
    match = DOI_RE.search(text)
    if match is None:
        return None
    return normalize_doi(match.group(0))


def host_of(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return (parsed.hostname or "").lower()


def is_blocked_host(url: str) -> bool:
    host = host_of(url)
    if not host:
        return False
    for suffix in BLOCKED_HOST_SUFFIXES:
        if host == suffix or host.endswith("." + suffix):
            return True
    if host.startswith("sci-hub.") or host.endswith(".sci-hub.se"):
        return True
    return False


def is_pdf_url(url: str) -> bool:
    path = urllib.parse.urlparse(url).path.lower()
    return path.endswith(".pdf") or path.endswith("/pdf") or path.endswith("/pdf/") or "/pdf/" in path


def user_agent(email: str | None) -> str:
    if email:
        return f"{SCRIPT_NAME} (mailto:{email})"
    return SCRIPT_NAME


def http_json(
    url: str,
    email: str | None,
    extra_headers: dict[str, str] | None = None,
) -> Any:
    headers = {
        "User-Agent": user_agent(email),
        "Accept": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SEC) as response:
            status = getattr(response, "status", 200)
            if status >= 400:
                raise urllib.error.HTTPError(
                    url, status, f"HTTP {status}", response.headers, None
                )
            raw = response.read()
    except urllib.error.HTTPError:
        raise
    except urllib.error.URLError as exc:
        raise urllib.error.URLError(f"{url}: {exc.reason}") from exc
    if not raw:
        raise ValueError(f"{url}: empty body")
    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{url}: not JSON ({exc})") from exc


def add_location(
    locations: list[Location],
    url: str,
    kind: str,
    source: str,
    license_name: str | None = None,
    is_oa: bool = False,
) -> None:
    if not url or not url.startswith("http"):
        return
    if is_blocked_host(url):
        log.info("dropped blocked host: %s", url)
        return
    for existing in locations:
        if existing.url == url:
            return
    locations.append(
        Location(
            url=url,
            kind=kind,
            source=source,
            license=license_name,
            is_pdf=is_pdf_url(url),
            is_oa=is_oa,
        )
    )


def merge_identity(identity: Identity, incoming: Identity) -> None:
    if incoming.title and not identity.title:
        identity.title = incoming.title
    if incoming.year and not identity.year:
        identity.year = incoming.year
    if incoming.venue and not identity.venue:
        identity.venue = incoming.venue
    if incoming.doi and not identity.doi:
        identity.doi = incoming.doi
    if incoming.pmid and not identity.pmid:
        identity.pmid = incoming.pmid
    if incoming.pmcid and not identity.pmcid:
        identity.pmcid = incoming.pmcid
    if incoming.type and not identity.type:
        identity.type = incoming.type
    if incoming.authors and not identity.authors:
        identity.authors = incoming.authors


def authors_from_crossref(message: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for author in message.get("author") or []:
        given = author.get("given") or ""
        family = author.get("family") or ""
        name = f"{given} {family}".strip()
        if name:
            out.append(name)
    return out


def hop_crossref(identity: Identity, locations: list[Location], email: str | None, hops: list[Hop], query_title: str | None) -> None:
    doi = identity.doi
    try:
        if doi:
            payload = http_json(f"{CROSSREF}/{urllib.parse.quote(doi)}", email)
        elif query_title:
            params = urllib.parse.urlencode(
                {"query.bibliographic": query_title, "rows": 3}
            )
            payload = http_json(f"{CROSSREF}?{params}", email)
        else:
            hops.append(Hop("crossref", False, "no DOI or title"))
            return
        items = []
        message = payload.get("message") or {}
        if "DOI" in message:
            items = [message]
        else:
            items = message.get("items") or []
        if not items:
            hops.append(Hop("crossref", False, "no items"))
            return
        first = items[0]
        merge_identity(
            identity,
            Identity(
                title=(first.get("title") or [None])[0],
                authors=authors_from_crossref(first),
                year=_year_from_date_parts(first.get("issued") or first.get("published")),
                venue=(first.get("container-title") or [None])[0],
                doi=normalize_doi(first["DOI"]) if first.get("DOI") else None,
                type=first.get("type"),
            ),
        )
        for link in first.get("link") or []:
            add_location(
                locations,
                link.get("URL") or "",
                "publisher",
                "crossref",
                None,
            )
        hops.append(Hop("crossref", True, identity.doi or "ok"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("crossref", False, str(exc)))


def _year_from_date_parts(blob: Any) -> int | None:
    if not isinstance(blob, dict):
        return None
    parts = blob.get("date-parts")
    if not parts or not parts[0]:
        return None
    try:
        return int(parts[0][0])
    except (TypeError, ValueError, IndexError):
        return None


def hop_pubmed(identity: Identity, email: str | None, hops: list[Hop], extra_query: str | None) -> None:
    try:
        if identity.pmid:
            pmid = identity.pmid
        else:
            term_parts: list[str] = []
            if identity.doi:
                term_parts.append(f"{identity.doi}[doi]")
            elif extra_query:
                term_parts.append(extra_query)
            else:
                hops.append(Hop("pubmed", False, "no DOI, PMID, or query"))
                return
            params = urllib.parse.urlencode(
                {
                    "db": "pubmed",
                    "retmode": "json",
                    "retmax": 3,
                    "term": " ".join(term_parts),
                }
            )
            search = http_json(f"{PUBMED_ESEARCH}?{params}", email)
            ids = ((search.get("esearchresult") or {}).get("idlist")) or []
            if not ids:
                hops.append(Hop("pubmed", False, "no hits"))
                return
            pmid = str(ids[0])
        params = urllib.parse.urlencode(
            {"db": "pubmed", "retmode": "json", "id": pmid}
        )
        summary = http_json(f"{PUBMED_ESUMMARY}?{params}", email)
        rec = (summary.get("result") or {}).get(pmid) or {}
        article_ids = rec.get("articleids") or []
        doi = identity.doi
        pmcid = identity.pmcid
        for item in article_ids:
            if item.get("idtype") == "doi" and item.get("value"):
                doi = normalize_doi(item["value"])
            if item.get("idtype") == "pmcid" and item.get("value"):
                pmcid = item["value"]
        authors = [
            a.get("name")
            for a in (rec.get("authors") or [])
            if a.get("name")
        ]
        year = None
        pubdate = rec.get("pubdate") or rec.get("epubdate") or ""
        if pubdate[:4].isdigit():
            year = int(pubdate[:4])
        merge_identity(
            identity,
            Identity(
                title=rec.get("title"),
                authors=authors,
                year=year,
                venue=rec.get("fulljournalname") or rec.get("source"),
                doi=doi,
                pmid=pmid,
                pmcid=pmcid,
            ),
        )
        hops.append(Hop("pubmed", True, f"pmid={pmid}"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("pubmed", False, str(exc)))


_EUROPE_PMC_OA_AVAIL = frozenset({"open access", "free", "oa", "f"})
_EUROPE_PMC_CLOSED_AVAIL = frozenset(
    {"subscription required", "subscription", "closed", "restricted", "s"}
)


def europe_pmc_fulltext_is_oa(availability: str | None, document_style: str | None) -> bool:
    """Europe PMC fullTextUrl is OA unless it is a DOI landing or closed availability."""
    if (document_style or "").lower() == "doi":
        return False
    avail = (availability or "").strip().lower()
    if avail in _EUROPE_PMC_CLOSED_AVAIL:
        return False
    if not avail or avail in _EUROPE_PMC_OA_AVAIL:
        return True
    return False


def hop_europe_pmc(identity: Identity, locations: list[Location], email: str | None, hops: list[Hop]) -> None:
    clauses: list[str] = []
    if identity.doi:
        clauses.append(f'DOI:"{identity.doi}"')
    if identity.pmid:
        clauses.append(f"EXT_ID:{identity.pmid}")
    if identity.pmcid:
        clauses.append(identity.pmcid)
    if not clauses:
        hops.append(Hop("europe_pmc", False, "no DOI/PMID/PMCID"))
        return
    try:
        params = urllib.parse.urlencode(
            {
                "query": " OR ".join(clauses),
                "format": "json",
                "resultType": "core",
                "pageSize": 3,
            }
        )
        payload = http_json(f"{EUROPE_PMC}?{params}", email)
        results = ((payload.get("resultList") or {}).get("result")) or []
        if not results:
            hops.append(Hop("europe_pmc", False, "no hits"))
            return
        first = results[0]
        pmcid = first.get("pmcid")
        merge_identity(
            identity,
            Identity(
                title=first.get("title"),
                year=int(first["pubYear"]) if str(first.get("pubYear") or "").isdigit() else None,
                venue=first.get("journalTitle"),
                doi=normalize_doi(first["doi"]) if first.get("doi") else None,
                pmid=str(first["pmid"]) if first.get("pmid") else None,
                pmcid=pmcid,
            ),
        )
        if pmcid:
            add_location(
                locations,
                f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/",
                "pmc",
                "europe_pmc",
                is_oa=True,
            )
            add_location(
                locations,
                f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/",
                "pmc-pdf",
                "europe_pmc",
                is_oa=True,
            )
        for url_item in (first.get("fullTextUrlList") or {}).get("fullTextUrl") or []:
            style = (url_item.get("documentStyle") or "fulltext").lower()
            availability = url_item.get("availability") or url_item.get("availabilityCode")
            add_location(
                locations,
                url_item.get("url") or "",
                style,
                "europe_pmc",
                url_item.get("availability"),
                is_oa=europe_pmc_fulltext_is_oa(availability, style),
            )
        hops.append(Hop("europe_pmc", True, pmcid or identity.doi or "ok"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("europe_pmc", False, str(exc)))


def hop_unpaywall(identity: Identity, locations: list[Location], email: str | None, hops: list[Hop]) -> None:
    if not identity.doi:
        hops.append(Hop("unpaywall", False, "no DOI"))
        return
    if not email:
        hops.append(Hop("unpaywall", False, "skipped: no --email or HFDD_UNPAYWALL_EMAIL"))
        return
    try:
        url = f"{UNPAYWALL}/{urllib.parse.quote(identity.doi)}?{urllib.parse.urlencode({'email': email})}"
        payload = http_json(url, email)
        best = payload.get("best_oa_location") or {}
        add_location(
            locations,
            best.get("url_for_pdf") or best.get("url") or "",
            "unpaywall-best",
            "unpaywall",
            best.get("license"),
            is_oa=True,
        )
        for loc in payload.get("oa_locations") or []:
            add_location(
                locations,
                loc.get("url_for_pdf") or loc.get("url") or "",
                loc.get("host_type") or "oa",
                "unpaywall",
                loc.get("license"),
                is_oa=True,
            )
        hops.append(
            Hop(
                "unpaywall",
                True,
                payload.get("oa_status") or ("oa" if payload.get("is_oa") else "closed"),
            )
        )
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("unpaywall", False, str(exc)))


def hop_openalex(identity: Identity, locations: list[Location], email: str | None, hops: list[Hop], query_title: str | None) -> None:
    try:
        if identity.doi:
            url = f"{OPENALEX}/doi:{urllib.parse.quote(identity.doi)}"
            if email:
                url += f"?{urllib.parse.urlencode({'mailto': email})}"
            payload = http_json(url, email)
        elif query_title:
            params = {"search": query_title, "per-page": 3}
            if email:
                params["mailto"] = email
            payload_list = http_json(f"{OPENALEX}?{urllib.parse.urlencode(params)}", email)
            results = payload_list.get("results") or []
            if not results:
                hops.append(Hop("openalex", False, "no hits"))
                return
            payload = results[0]
        else:
            hops.append(Hop("openalex", False, "no DOI or title"))
            return
        ids = payload.get("ids") or {}
        doi = None
        if ids.get("doi"):
            doi = extract_doi(ids["doi"])
        authors = []
        for authorship in payload.get("authorships") or []:
            author = authorship.get("author") or {}
            if author.get("display_name"):
                authors.append(author["display_name"])
        merge_identity(
            identity,
            Identity(
                title=payload.get("title") or payload.get("display_name"),
                authors=authors,
                year=payload.get("publication_year"),
                venue=((payload.get("primary_location") or {}).get("source") or {}).get("display_name"),
                doi=doi,
                pmid=_openalex_pmid(ids.get("pmid")),
                type=payload.get("type"),
            ),
        )
        best_oa = payload.get("best_oa_location")
        if best_oa:
            add_location(
                locations,
                best_oa.get("pdf_url") or best_oa.get("landing_page_url") or "",
                "openalex",
                "openalex",
                best_oa.get("license"),
                is_oa=True,
            )
        primary = payload.get("primary_location") or {}
        if primary:
            primary_is_oa = bool(primary.get("is_oa"))
            add_location(
                locations,
                primary.get("pdf_url") or primary.get("landing_page_url") or "",
                "openalex" if primary_is_oa else "landing",
                "openalex",
                primary.get("license"),
                is_oa=primary_is_oa,
            )
        hops.append(Hop("openalex", True, identity.doi or "ok"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("openalex", False, str(exc)))


def _openalex_pmid(pmid_url: str | None) -> str | None:
    if not pmid_url:
        return None
    tail = pmid_url.rstrip("/").rsplit("/", 1)[-1]
    if tail.isdigit():
        return tail
    return None


def hop_semantic_scholar(identity: Identity, locations: list[Location], email: str | None, hops: list[Hop]) -> None:
    paper_id = None
    if identity.doi:
        paper_id = f"DOI:{identity.doi}"
    elif identity.pmid:
        paper_id = f"PMID:{identity.pmid}"
    if not paper_id:
        hops.append(Hop("semantic_scholar", False, "no DOI or PMID"))
        return
    try:
        fields = "title,year,authors,externalIds,openAccessPdf,abstract,url,venue"
        url = f"{SEMANTIC_SCHOLAR}/{urllib.parse.quote(paper_id, safe=':')}?fields={fields}"
        payload = http_json(url, email)
        ext = payload.get("externalIds") or {}
        authors = [a.get("name") for a in (payload.get("authors") or []) if a.get("name")]
        merge_identity(
            identity,
            Identity(
                title=payload.get("title"),
                authors=authors,
                year=payload.get("year"),
                venue=payload.get("venue"),
                doi=normalize_doi(ext["DOI"]) if ext.get("DOI") else None,
                pmid=str(ext["PubMed"]) if ext.get("PubMed") else None,
                pmcid=ext.get("PubMedCentral"),
            ),
        )
        oa_pdf = payload.get("openAccessPdf") or {}
        add_location(
            locations,
            oa_pdf.get("url") or "",
            "oa-pdf",
            "semantic_scholar",
            is_oa=True,
        )
        add_location(
            locations,
            payload.get("url") or "",
            "landing",
            "semantic_scholar",
        )
        hops.append(Hop("semantic_scholar", True, identity.doi or "ok"))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("semantic_scholar", False, str(exc)))


def hop_preprint_servers(identity: Identity, locations: list[Location], email: str | None, hops: list[Hop]) -> None:
    if not identity.doi:
        hops.append(Hop("preprint", False, "no DOI"))
        return
    doi = identity.doi
    server = None
    if "biorxiv" in doi or doi.startswith("10.1101/"):
        server = "biorxiv"
    if "medrxiv" in doi:
        server = "medrxiv"
    if server is None:
        hops.append(Hop("preprint", False, "DOI is not a bioRxiv/medRxiv id"))
        return
    try:
        payload = http_json(f"{BIORXIV}/{server}/{urllib.parse.quote(doi)}/na/json", email)
        collection = payload.get("collection") or []
        if not collection:
            hops.append(Hop("preprint", False, "no collection"))
            return
        latest = collection[-1]
        merge_identity(
            identity,
            Identity(
                title=latest.get("title"),
                year=int(str(latest.get("date") or "")[:4]) if str(latest.get("date") or "")[:4].isdigit() else None,
                venue=server,
                doi=normalize_doi(latest["doi"]) if latest.get("doi") else doi,
                type="preprint",
            ),
        )
        version = latest.get("version") or "1"
        add_location(
            locations,
            f"https://www.{server}.org/content/{doi}v{version}.full.pdf",
            "preprint-pdf",
            server,
            is_oa=True,
        )
        hops.append(Hop("preprint", True, server))
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError) as exc:
        hops.append(Hop("preprint", False, str(exc)))


def pick_best(locations: list[Location]) -> dict[str, Any]:
    oa_locs = [loc for loc in locations if loc.is_oa]
    pdfs = [loc for loc in oa_locs if loc.is_pdf]
    html = [loc for loc in oa_locs if not loc.is_pdf]
    best_pdf = pdfs[0] if pdfs else None
    best_html = html[0] if html else None
    best = best_pdf or best_html
    status = "none"
    if best_pdf:
        status = "oa-pdf"
    elif best_html:
        status = "oa-html"
    return {
        "status": status,
        "best_url": best.url if best else None,
        "pdf_url": best_pdf.url if best_pdf else None,
        "license": best.license if best else None,
        "locations": [asdict(loc) for loc in locations],
    }


def has_identity(identity: Identity) -> bool:
    return bool(identity.doi or identity.pmid or (identity.title and identity.year))


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--doi")
    parser.add_argument("--pmid")
    parser.add_argument("--pmcid")
    parser.add_argument("--title")
    parser.add_argument("--year", type=int)
    parser.add_argument("--query", help="Free bibliographic string")
    parser.add_argument(
        "--email",
        default=os.environ.get("HFDD_UNPAYWALL_EMAIL"),
        help="Contact email for Unpaywall / polite pools (or HFDD_UNPAYWALL_EMAIL)",
    )
    parser.add_argument(
        "--out",
        help="Write JSON here as well as stdout",
    )
    return parser


def seed_identity(args: argparse.Namespace) -> tuple[Identity, str | None]:
    identity = Identity(
        title=args.title,
        year=args.year,
        doi=normalize_doi(args.doi) if args.doi else None,
        pmid=args.pmid,
        pmcid=args.pmcid,
    )
    extra = args.query
    if extra:
        found = extract_doi(extra)
        if found and not identity.doi:
            identity.doi = found
        if PMID_RE.match(extra.strip()) and not identity.pmid:
            identity.pmid = extra.strip()
        if extra.lower().startswith("pmc") and not identity.pmcid:
            identity.pmcid = extra.strip()
    if identity.doi is None and args.title:
        found = extract_doi(args.title)
        if found:
            identity.doi = found
    return identity, extra


def resolve(args: argparse.Namespace) -> Result:
    identity, extra = seed_identity(args)
    query_title = args.title or extra
    locations: list[Location] = []
    hops: list[Hop] = []
    email = args.email

    hop_crossref(identity, locations, email, hops, query_title)
    hop_pubmed(identity, email, hops, extra or args.title)
    hop_europe_pmc(identity, locations, email, hops)
    hop_unpaywall(identity, locations, email, hops)
    hop_openalex(identity, locations, email, hops, query_title)
    hop_semantic_scholar(identity, locations, email, hops)
    hop_preprint_servers(identity, locations, email, hops)

    return Result(
        query={
            "doi": args.doi,
            "pmid": args.pmid,
            "pmcid": args.pmcid,
            "title": args.title,
            "year": args.year,
            "query": args.query,
        },
        identity=identity,
        oa=pick_best(locations),
        hops=hops,
    )


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = build_arg_parser().parse_args(argv)
    if not any([args.doi, args.pmid, args.pmcid, args.title, args.query]):
        build_arg_parser().error("need --doi, --pmid, --pmcid, --title, or --query")
    result = resolve(args)
    blob = json.dumps(result.to_json(), indent=2, ensure_ascii=False)
    print(blob)
    if args.out:
        Path(args.out).write_text(blob + "\n", encoding="utf-8")
    if not has_identity(result.identity):
        log.error("no bibliographic identity (DOI, PMID, or title+year)")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
