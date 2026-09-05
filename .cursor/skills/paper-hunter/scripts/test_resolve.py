#!/usr/bin/env python3
"""Unit tests for paper-hunter resolve helpers. No network.

Run from this directory: python3 -m unittest test_resolve.py
Do not run as python3 -m unittest .cursor/skills/.../test_resolve.py
(that treats the path as a module name).
"""

from __future__ import annotations

import unittest

from resolve import (
    add_location,
    europe_pmc_fulltext_is_oa,
    extract_doi,
    has_identity,
    Identity,
    is_blocked_host,
    is_pdf_url,
    normalize_doi,
    pick_best,
    Location,
)


class NormalizeDoiTests(unittest.TestCase):
    def test_strips_resolver_prefix(self) -> None:
        self.assertEqual(
            normalize_doi("https://doi.org/10.1038/s41586-022-04618-z"),
            "10.1038/s41586-022-04618-z",
        )

    def test_strips_doi_colon_and_case(self) -> None:
        self.assertEqual(
            normalize_doi("doi:10.1093/AJCN/86.6.1738."),
            "10.1093/ajcn/86.6.1738",
        )

    def test_extract_from_prose(self) -> None:
        self.assertEqual(
            extract_doi("see DOI 10.1038/s41586-022-04618-z in Nature"),
            "10.1038/s41586-022-04618-z",
        )

    def test_extract_none(self) -> None:
        self.assertIsNone(extract_doi("PMID 18065594 only"))


class BlockedHostTests(unittest.TestCase):
    def test_scihub_dropped(self) -> None:
        self.assertTrue(is_blocked_host("https://sci-hub.se/10.1038/s41586-022-04618-z"))

    def test_libgen_dropped(self) -> None:
        self.assertTrue(is_blocked_host("http://library.lol/main/abc"))

    def test_annas_dropped(self) -> None:
        self.assertTrue(is_blocked_host("https://annas-archive.org/md5/abc"))

    def test_pmc_kept(self) -> None:
        self.assertFalse(
            is_blocked_host("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC123/")
        )

    def test_unpaywall_repo_kept(self) -> None:
        self.assertFalse(
            is_blocked_host("https://europepmc.org/articles/PMC123?pdf=render")
        )


class PdfUrlTests(unittest.TestCase):
    def test_pdf_suffix(self) -> None:
        self.assertTrue(is_pdf_url("https://www.biorxiv.org/content/10.1101/x.full.pdf"))

    def test_pmc_pdf_path(self) -> None:
        self.assertTrue(
            is_pdf_url("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1/pdf/")
        )

    def test_html_landing(self) -> None:
        self.assertFalse(is_pdf_url("https://doi.org/10.1038/s41586-022-04618-z"))

    def test_pdfium_path_is_not_pdf(self) -> None:
        self.assertFalse(is_pdf_url("https://example.org/pdfium/viewer"))


class IdentityAndPickTests(unittest.TestCase):
    def test_has_identity_doi(self) -> None:
        self.assertTrue(has_identity(Identity(doi="10.1/abc")))

    def test_has_identity_title_year(self) -> None:
        self.assertTrue(has_identity(Identity(title="A study", year=2022)))

    def test_no_identity(self) -> None:
        self.assertFalse(has_identity(Identity(title="A study")))

    def test_pick_prefers_pdf(self) -> None:
        locations = [
            Location(
                "https://example.org/abs",
                "html",
                "unpaywall",
                is_pdf=False,
                is_oa=True,
            ),
            Location(
                "https://example.org/p.pdf",
                "pdf",
                "unpaywall",
                is_pdf=True,
                is_oa=True,
            ),
        ]
        picked = pick_best(locations)
        self.assertEqual(picked["status"], "oa-pdf")
        self.assertEqual(picked["pdf_url"], "https://example.org/p.pdf")

    def test_publisher_only_status_none(self) -> None:
        locations: list[Location] = []
        add_location(
            locations,
            "https://www.nature.com/articles/s41586-022-04618-z",
            "publisher",
            "crossref",
        )
        add_location(
            locations,
            "https://www.nature.com/articles/s41586-022-04618-z.pdf",
            "publisher",
            "crossref",
        )
        add_location(
            locations,
            "https://www.semanticscholar.org/paper/abc",
            "landing",
            "semantic_scholar",
        )
        add_location(
            locations,
            "https://openalex.org/works/W1",
            "landing",
            "openalex",
        )
        picked = pick_best(locations)
        self.assertEqual(picked["status"], "none")
        self.assertIsNone(picked["best_url"])
        self.assertIsNone(picked["pdf_url"])
        self.assertIsNone(picked["license"])
        self.assertEqual(len(picked["locations"]), 4)
        self.assertFalse(any(loc.is_oa for loc in locations))

    def test_landing_only_status_none(self) -> None:
        locations = [
            Location(
                "https://www.semanticscholar.org/paper/abc",
                "landing",
                "semantic_scholar",
                is_oa=False,
            ),
        ]
        picked = pick_best(locations)
        self.assertEqual(picked["status"], "none")
        self.assertIsNone(picked["best_url"])
        self.assertIsNone(picked["pdf_url"])

    def test_html_only_real_oa(self) -> None:
        locations: list[Location] = []
        add_location(
            locations,
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC123/",
            "pmc",
            "europe_pmc",
            is_oa=True,
        )
        picked = pick_best(locations)
        self.assertEqual(picked["status"], "oa-html")
        self.assertEqual(
            picked["best_url"],
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC123/",
        )
        self.assertIsNone(picked["pdf_url"])

    def test_empty_locations_none(self) -> None:
        picked = pick_best([])
        self.assertEqual(picked["status"], "none")
        self.assertIsNone(picked["best_url"])
        self.assertIsNone(picked["pdf_url"])
        self.assertEqual(picked["locations"], [])

    def test_publisher_does_not_override_real_oa(self) -> None:
        locations: list[Location] = []
        add_location(
            locations,
            "https://doi.org/10.1038/s41586-022-04618-z",
            "publisher",
            "crossref",
        )
        add_location(
            locations,
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1/pdf/",
            "pmc-pdf",
            "europe_pmc",
            is_oa=True,
        )
        picked = pick_best(locations)
        self.assertEqual(picked["status"], "oa-pdf")
        self.assertEqual(
            picked["pdf_url"],
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1/pdf/",
        )
        self.assertEqual(len(picked["locations"]), 2)


class EuropePmcFulltextTests(unittest.TestCase):
    def test_open_html_is_oa(self) -> None:
        self.assertTrue(europe_pmc_fulltext_is_oa("Open access", "html"))

    def test_doi_landing_is_not_oa(self) -> None:
        self.assertFalse(europe_pmc_fulltext_is_oa("Open access", "doi"))

    def test_subscription_is_not_oa(self) -> None:
        self.assertFalse(europe_pmc_fulltext_is_oa("Subscription required", "pdf"))


if __name__ == "__main__":
    unittest.main()
