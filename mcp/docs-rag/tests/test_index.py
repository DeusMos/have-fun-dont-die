from __future__ import annotations

from hfdd_docs_rag.corpus import file_sha256
from hfdd_docs_rag.index import ensure_index, load_index
from hfdd_docs_rag.service import RagService


def test_incremental_reindex_picks_up_new_source(fixture_root, embedder, tmp_path) -> None:
    root = _copy_tree(fixture_root, tmp_path)
    index, message = ensure_index(root, embedder)
    assert message == "created"
    first_count = len(index.chunks)

    again, message = ensure_index(root, embedder)
    assert message == "already up to date"
    assert len(again.chunks) == first_count

    new_source = (
        root
        / "hallmarks"
        / "01-genomic-instability"
        / "sources"
        / "📜"
        / "Gorbunova-2025.md"
    )
    new_source.parent.mkdir(parents=True, exist_ok=True)
    new_source.write_text(
        "# Gorbunova 2025 fucoidan SIRT6\nUsed for: male mouse lifespan.\n",
        encoding="utf-8",
    )
    updated, message = ensure_index(root, embedder)
    assert message == "incremental update"
    assert len(updated.chunks) == first_count + 1
    assert any(chunk.path.endswith("Gorbunova-2025.md") for chunk in updated.chunks)
    assert updated.files[new_source.relative_to(root).as_posix()] == file_sha256(new_source)

    loaded = load_index(root)
    assert loaded is not None
    assert len(loaded.chunks) == len(updated.chunks)


def test_status_reports_not_yet_indexed(fixture_root, embedder, tmp_path) -> None:
    root = _copy_tree(fixture_root, tmp_path)
    service = RagService(root=root, embedder=embedder)
    before = service.status()
    assert "not_yet_indexed" in before
    service.reindex()
    after = service.status()
    assert "stale: 0" in after
    assert "not_yet_indexed: 0" in after


def _copy_tree(fixture_root, tmp_path):
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
