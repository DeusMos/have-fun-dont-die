from __future__ import annotations

import os
from pathlib import Path

INDEX_DIRNAME = ".rag"
MANIFEST_NAME = "manifest.json"
CHUNKS_NAME = "chunks.json"
VECTORS_NAME = "vectors.npy"


def find_repo_root(start: Path | None = None) -> Path:
    env = os.environ.get("HFDD_ROOT")
    if env:
        root = Path(env).expanduser().resolve()
        if not _looks_like_root(root):
            raise RuntimeError(
                f"HFDD_ROOT={env} is not a have-fun-dont-die root "
                "(need AGENTS.md and hallmarks/)"
            )
        return root

    here = (start or Path(__file__)).resolve()
    candidates = [here] if here.is_dir() else [here.parent]
    candidates.extend(here.parents)
    for path in candidates:
        if _looks_like_root(path):
            return path
    raise RuntimeError(
        "Could not find have-fun-dont-die root (AGENTS.md + hallmarks/). "
        "Set HFDD_ROOT or run from the repo."
    )


def index_dir(root: Path) -> Path:
    return root / INDEX_DIRNAME


def _looks_like_root(path: Path) -> bool:
    return (path / "AGENTS.md").is_file() and (path / "hallmarks").is_dir()
