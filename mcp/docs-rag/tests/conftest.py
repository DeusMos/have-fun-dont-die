from __future__ import annotations

from pathlib import Path

import pytest

from hfdd_docs_rag.embed import HashEmbedder

FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "repo"


@pytest.fixture
def embedder() -> HashEmbedder:
    return HashEmbedder(dim=32)


@pytest.fixture
def fixture_root() -> Path:
    return FIXTURE_ROOT
