from __future__ import annotations

import re

# Format tokens only: keep compound IDs like 8-ohdg, sirt6, nct07500649.
TOKEN_RE = re.compile(r"[a-z0-9]+(?:[-+][a-z0-9]+)*", re.IGNORECASE)


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN_RE.finditer(text)]
