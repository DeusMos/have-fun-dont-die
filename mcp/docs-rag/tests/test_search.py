from __future__ import annotations

from hfdd_docs_rag.index import build_index
from hfdd_docs_rag.search import hybrid_search
from hfdd_docs_rag.service import RagService


def test_search_finds_cagan_and_fucoidan(fixture_root, embedder, tmp_path) -> None:
    root = _copy_fixture(fixture_root, tmp_path)
    index = build_index(root, embedder)
    query_vector = embedder.embed(["Cagan intestinal crypt mutation rate lifespan"])[0]
    hits = hybrid_search(
        query="Cagan intestinal crypt mutation rate lifespan",
        chunks=index.chunks,
        vectors=index.vectors,
        query_vector=query_vector,
        k=5,
    )
    assert hits
    texts = " ".join(hit.chunk.text for hit in hits)
    paths = " ".join(hit.chunk.path for hit in hits)
    assert "Cagan" in texts or "Cagan" in paths


def test_kind_and_area_filters(fixture_root, embedder, tmp_path) -> None:
    root = _copy_fixture(fixture_root, tmp_path)
    service = RagService(root=root, embedder=embedder)
    source_hits = service.search("Cagan SBS lifespan", k=5, kind="source")
    assert "Cagan-2022.md" in source_hits
    assert "report.md" not in source_hits

    topic_hits = service.search("sirolimus weekly dose", k=5, area="topics/rapamycin")
    assert "topics/rapamycin/report.md" in topic_hits
    assert "01-genomic-instability" not in topic_hits

    compound_hits = service.search("sirolimus weekly dose", k=5, area="compounds/rapamycin")
    assert "compounds/rapamycin/report.md" in compound_hits
    assert "topics/rapamycin" not in compound_hits
    assert "01-genomic-instability" not in compound_hits


def test_empty_query_raises(fixture_root, embedder, tmp_path) -> None:
    root = _copy_fixture(fixture_root, tmp_path)
    service = RagService(root=root, embedder=embedder)
    try:
        service.search("   ")
    except ValueError as exc:
        assert "empty" in str(exc)
    else:
        raise AssertionError("expected ValueError for empty query")


def _copy_fixture(fixture_root, tmp_path):
    dest = tmp_path / "repo"
    dest.mkdir()
    for src in fixture_root.rglob("*"):
        rel = src.relative_to(fixture_root)
        target = dest / rel
        if src.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(src.read_bytes())
    return dest
