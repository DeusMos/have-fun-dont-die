from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Literal

KNOWN_MARKS = frozenset("💯📚📜🥼🤔🤼⛔🐉☠︎︎")
HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.MULTILINE)
SKIP_FILENAMES = frozenset({"README.md"})
MAX_CHUNK_CHARS = 1800
TARGET_SPLIT_CHARS = 1200

Kind = Literal["report", "source"]


@dataclass(frozen=True)
class Chunk:
    id: str
    path: str
    kind: Kind
    area: str
    mark: str | None
    heading: str
    text: str
    file_hash: str

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> Chunk:
        return Chunk(
            id=data["id"],
            path=data["path"],
            kind=_parse_kind(data["kind"]),
            area=data["area"],
            mark=data.get("mark"),
            heading=data["heading"],
            text=data["text"],
            file_hash=data["file_hash"],
        )


def _parse_kind(value: str) -> Kind:
    if value == "report":
        return "report"
    if value == "source":
        return "source"
    raise ValueError(f"unknown chunk kind: {value!r}")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def iter_corpus_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for tree in ("hallmarks", "topics", "compounds"):
        base = root / tree
        if not base.is_dir():
            continue
        files.extend(_iter_tree(base))
    files.sort()
    return files


def _iter_tree(base: Path) -> Iterable[Path]:
    for path in base.rglob("*.md"):
        if not path.is_file():
            continue
        if path.name in SKIP_FILENAMES:
            continue
        rel_parts = path.relative_to(base).parts
        if not _is_corpus_rel(rel_parts, path.name):
            continue
        yield path


def _is_corpus_rel(rel_parts: tuple[str, ...], name: str) -> bool:
    # <slug>/report.md
    if len(rel_parts) == 2 and name == "report.md":
        return True
    # <slug>/sources/<mark>/<file>.md
    if len(rel_parts) == 4 and rel_parts[1] == "sources":
        return True
    return False


def chunk_file(root: Path, path: Path) -> list[Chunk]:
    rel = path.relative_to(root).as_posix()
    kind, area, mark = _classify(rel)
    digest = file_sha256(path)
    text = path.read_text(encoding="utf-8")
    if kind == "source":
        heading = _source_heading(text, path)
        return [
            Chunk(
                id=f"{rel}#0",
                path=rel,
                kind=kind,
                area=area,
                mark=mark,
                heading=heading,
                text=text.strip(),
                file_hash=digest,
            )
        ]
    return _chunk_report(rel, area, digest, text)


def chunk_corpus(root: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    for path in iter_corpus_files(root):
        chunks.extend(chunk_file(root, path))
    return chunks


def _classify(rel: str) -> tuple[Kind, str, str | None]:
    parts = rel.split("/")
    if len(parts) < 2:
        raise ValueError(f"not a corpus path: {rel}")
    area = "/".join(parts[:2])
    if parts[-1] == "report.md":
        return "report", area, None
    if len(parts) >= 4 and parts[2] == "sources":
        mark = parts[3] if parts[3] in KNOWN_MARKS else None
        return "source", area, mark
    raise ValueError(f"not a corpus path: {rel}")


def _source_heading(text: str, path: Path) -> str:
    for line in text.splitlines():
        stripped = line.strip().lstrip("#").strip()
        if stripped:
            return stripped
    return path.stem


def _chunk_report(rel: str, area: str, digest: str, text: str) -> list[Chunk]:
    sections = _split_headings(text)
    chunks: list[Chunk] = []
    part = 0
    for heading, body in sections:
        for piece in _split_long(body):
            stripped = piece.strip()
            if not stripped:
                continue
            chunks.append(
                Chunk(
                    id=f"{rel}#{part}",
                    path=rel,
                    kind="report",
                    area=area,
                    mark=None,
                    heading=heading,
                    text=stripped,
                    file_hash=digest,
                )
            )
            part += 1
    return chunks


def _split_headings(text: str) -> list[tuple[str, str]]:
    matches = list(HEADING_RE.finditer(text))
    if not matches:
        return [("front matter", text)]

    sections: list[tuple[str, str]] = []
    preamble = text[: matches[0].start()].strip()
    if preamble:
        sections.append(("front matter", preamble))

    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        heading = match.group(2).strip()
        body = text[start:end]
        sections.append((heading, body))
    return sections


def _split_long(body: str) -> list[str]:
    stripped = body.strip()
    if len(stripped) <= MAX_CHUNK_CHARS:
        return [stripped] if stripped else []

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", stripped) if p.strip()]
    if not paragraphs:
        return [stripped]

    pieces: list[str] = []
    current: list[str] = []
    current_len = 0
    for para in paragraphs:
        extra = len(para) + (2 if current else 0)
        if current and current_len + extra > TARGET_SPLIT_CHARS:
            pieces.append("\n\n".join(current))
            current = [para]
            current_len = len(para)
            continue
        current.append(para)
        current_len += extra
    if current:
        pieces.append("\n\n".join(current))
    wrapped: list[str] = []
    for piece in pieces:
        wrapped.extend(_hard_wrap(piece))
    return wrapped


def _hard_wrap(text: str, limit: int = MAX_CHUNK_CHARS) -> list[str]:
    if len(text) <= limit:
        return [text]
    pieces: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + limit, len(text))
        if end < len(text):
            cut = text.rfind(" ", start, end)
            if cut > start:
                end = cut
        piece = text[start:end].strip()
        if piece:
            pieces.append(piece)
        start = end if end > start else start + limit
    return pieces
