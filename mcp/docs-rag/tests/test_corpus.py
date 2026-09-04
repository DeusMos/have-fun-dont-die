from __future__ import annotations

from hfdd_docs_rag.corpus import MAX_CHUNK_CHARS, chunk_corpus, chunk_file, iter_corpus_files


def test_iter_skips_tmp_template_and_readmes(fixture_root) -> None:
    rels = [path.relative_to(fixture_root).as_posix() for path in iter_corpus_files(fixture_root)]
    assert "hallmarks/01-genomic-instability/report.md" in rels
    assert "hallmarks/01-genomic-instability/sources/📚/Cagan-2022.md" in rels
    assert "topics/rapamycin/report.md" in rels
    assert "compounds/rapamycin/report.md" in rels
    assert "compounds/rapamycin/sources/🤔/weekly-sirolimus.md" in rels
    assert "tmp/scratch.md" not in rels
    assert "template.md" not in rels
    assert "AGENTS.md" not in rels
    assert not any(path.endswith("README.md") for path in rels)


def test_report_chunks_split_on_headings(fixture_root) -> None:
    chunks = chunk_corpus(fixture_root)
    report = [c for c in chunks if c.path.endswith("01-genomic-instability/report.md")]
    headings = {c.heading for c in report}
    assert "Animal data" in headings
    assert "What clinics and self-experimenters are doing" in headings
    animal = next(c for c in report if c.heading == "Animal data")
    assert "Cagan" in animal.text
    assert animal.kind == "report"
    assert animal.area == "hallmarks/01-genomic-instability"
    assert animal.mark is None


def test_compound_report_area(fixture_root) -> None:
    chunks = chunk_corpus(fixture_root)
    report = [c for c in chunks if c.path.endswith("compounds/rapamycin/report.md")]
    assert report
    assert all(c.kind == "report" for c in report)
    assert all(c.area == "compounds/rapamycin" for c in report)
    assert all(c.mark is None for c in report)
    headings = {c.heading for c in report}
    assert "Observed practice" in headings


def test_source_chunk_keeps_mark(fixture_root) -> None:
    chunks = chunk_corpus(fixture_root)
    source = next(c for c in chunks if c.path.endswith("Cagan-2022.md"))
    assert source.kind == "source"
    assert source.mark == "📚"
    assert source.area == "hallmarks/01-genomic-instability"
    assert "SBS rate" in source.text


def test_long_paragraph_is_hard_wrapped(tmp_path) -> None:
    root = tmp_path / "repo"
    report = root / "hallmarks" / "01-genomic-instability" / "report.md"
    report.parent.mkdir(parents=True)
    (root / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
    body = "word " * 2000
    report.write_text(f"# Title\n\n## Mechanism\n\n{body}\n", encoding="utf-8")
    chunks = chunk_file(root, report)
    assert len(chunks) > 1
    assert all(len(chunk.text) <= MAX_CHUNK_CHARS for chunk in chunks)
