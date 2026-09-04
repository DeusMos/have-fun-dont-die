#!/usr/bin/env python3
"""Regenerate catalog and section-map blocks from reports + index-meta.yaml.

Heading extraction is markdown format parsing (`##`), not intent classification.
Curated one-liners, status, and cross-cuts live outside generated markers.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META_PATH = ROOT / "scripts" / "index-meta.yaml"
SKIP_SECTION_MAP_TITLES = {"Contents"}
VALID_STATUS = {"rewritten", "legacy template", "no report"}


@dataclass
class ReportInfo:
    h1: str | None = None
    last_updated: str | None = None
    headings: list[str] = field(default_factory=list)


@dataclass
class HallmarkMeta:
    slug: str
    name: str
    status: str
    one_liner: str


@dataclass
class TopicMeta:
    slug: str
    one_liner: str


@dataclass
class CompoundMeta:
    slug: str
    one_liner: str
    cas: list[str]
    aliases: list[str] = field(default_factory=list)
    home_hallmark: str | None = None

    @property
    def primary_cas(self) -> str:
        return self.cas[0]


@dataclass
class IndexMeta:
    adjacency: str
    hallmarks: list[HallmarkMeta]
    topics: list[TopicMeta]
    compounds: list[CompoundMeta]


def github_anchor(title: str) -> str:
    chars: list[str] = []
    for ch in title.strip().lower():
        if ch.isalnum() or ch == "_" or ch == "-":
            chars.append(ch)
        elif ch.isspace():
            chars.append("-")
    return "".join(chars).strip("-")


def _href(link_prefix: str, slug: str) -> str:
    """File-relative path. Empty prefix stays in this tree (`./slug/report.md`)."""
    if link_prefix:
        return f"{link_prefix}{slug}/report.md"
    return f"./{slug}/report.md"


def parse_report(path: Path) -> ReportInfo:
    info = ReportInfo()
    for line in path.read_text(encoding="utf-8").splitlines():
        if info.h1 is None and line.startswith("# ") and not line.startswith("## "):
            info.h1 = line[2:].strip()
            continue
        if line.startswith("**Last updated:**"):
            info.last_updated = line[len("**Last updated:**") :].strip().rstrip("*").strip()
            continue
        if line.startswith("## ") and not line.startswith("### "):
            info.headings.append(line[3:].strip())
    return info


CAS_LITERALS = {"pending", "none", "not assigned"}
CAS_NUMBER_RE = re.compile(r"^\d{2,7}-\d{2}-\d$")
INLINE_LIST_RE = re.compile(r"^\[(.*)\]$")


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _parse_scalar_or_list(value: str) -> str | list[str]:
    stripped = value.strip()
    match = INLINE_LIST_RE.fullmatch(stripped)
    if not match:
        return _unquote(stripped)
    inner = match.group(1).strip()
    if not inner:
        return []
    return [_unquote(part.strip()) for part in inner.split(",") if part.strip()]


def _as_list(value: str | list[str] | None) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    parsed = _parse_scalar_or_list(value)
    if isinstance(parsed, list):
        return parsed
    return [parsed] if parsed else []


def _validate_cas_token(token: str, slug: str) -> None:
    if token in CAS_LITERALS or CAS_NUMBER_RE.fullmatch(token):
        return
    raise SystemExit(f"compound {slug} has invalid cas {token!r}")


def load_meta(path: Path) -> IndexMeta:
    """Load the constrained sidecar YAML. Fail loud on unknown shape."""
    if not path.is_file():
        raise SystemExit(f"missing sidecar: {path}")

    adjacency_parts: list[str] = []
    hallmarks: list[HallmarkMeta] = []
    topics: list[TopicMeta] = []
    compounds: list[CompoundMeta] = []
    section: str | None = None
    current: dict[str, str | list[str]] | None = None
    in_adjacency = False

    def flush_item() -> None:
        nonlocal current
        if current is None:
            return
        if section == "hallmarks":
            for key in ("slug", "name", "status", "one_liner"):
                if key not in current:
                    raise SystemExit(f"hallmark item missing {key}: {current}")
            status = current["status"]
            slug = current["slug"]
            if not isinstance(status, str) or not isinstance(slug, str):
                raise SystemExit(f"hallmark item has non-scalar slug/status: {current}")
            if status not in VALID_STATUS:
                raise SystemExit(f"invalid status {status!r} for {slug}")
            name = current["name"]
            one_liner = current["one_liner"]
            if not isinstance(name, str) or not isinstance(one_liner, str):
                raise SystemExit(f"hallmark item has non-scalar name/one_liner: {current}")
            hallmarks.append(
                HallmarkMeta(
                    slug=slug,
                    name=name,
                    status=status,
                    one_liner=one_liner,
                )
            )
        elif section == "topics":
            for key in ("slug", "one_liner"):
                if key not in current:
                    raise SystemExit(f"topic item missing {key}: {current}")
            slug = current["slug"]
            one_liner = current["one_liner"]
            if not isinstance(slug, str) or not isinstance(one_liner, str):
                raise SystemExit(f"topic item has non-scalar slug/one_liner: {current}")
            topics.append(TopicMeta(slug=slug, one_liner=one_liner))
        elif section == "compounds":
            for key in ("slug", "one_liner", "cas"):
                if key not in current:
                    raise SystemExit(f"compound item missing {key}: {current}")
            slug = current["slug"]
            one_liner = current["one_liner"]
            if not isinstance(slug, str) or not isinstance(one_liner, str):
                raise SystemExit(f"compound item has non-scalar slug/one_liner: {current}")
            cas = _as_list(current["cas"])
            if not cas:
                raise SystemExit(f"compound {slug} has empty cas")
            for token in cas:
                _validate_cas_token(token, slug)
            home = current.get("home_hallmark")
            if home is not None and not isinstance(home, str):
                raise SystemExit(f"compound {slug} has non-scalar home_hallmark")
            compounds.append(
                CompoundMeta(
                    slug=slug,
                    one_liner=one_liner,
                    cas=cas,
                    aliases=_as_list(current.get("aliases")),
                    home_hallmark=home,
                )
            )
        else:
            raise SystemExit(f"list item outside hallmarks/topics/compounds: {current}")
        current = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip().startswith("#") and not in_adjacency:
            continue
        if in_adjacency:
            if raw.startswith("  ") and not raw.startswith("  - "):
                adjacency_parts.append(raw.strip())
                continue
            in_adjacency = False

        if raw.startswith("adjacency:"):
            rest = raw.split(":", 1)[1].strip()
            if rest in {">", ">-", "|", "|-"}:
                in_adjacency = True
            elif rest:
                adjacency_parts.append(_unquote(rest))
            continue

        if raw.startswith("hallmarks:") or raw.startswith("topics:") or raw.startswith(
            "compounds:"
        ):
            flush_item()
            key, rest = raw.split(":", 1)
            section = key
            if rest.strip() in {"", "[]"}:
                continue
            raise SystemExit(f"unexpected inline value for {key}: {raw!r}")

        if raw.startswith("  - "):
            flush_item()
            current = {}
            remainder = raw[4:].strip()
            if remainder and ":" in remainder:
                key, value = remainder.split(":", 1)
                current[key.strip()] = _parse_scalar_or_list(value.strip())
            continue

        if raw.startswith("    ") and current is not None and ":" in raw:
            key, value = raw.strip().split(":", 1)
            current[key.strip()] = _parse_scalar_or_list(value.strip())
            continue

        if raw.strip() == "":
            continue

        raise SystemExit(f"unrecognized sidecar line: {raw!r}")

    flush_item()
    if not hallmarks:
        raise SystemExit("sidecar has no hallmarks")
    return IndexMeta(
        adjacency=" ".join(adjacency_parts).strip(),
        hallmarks=hallmarks,
        topics=topics,
        compounds=compounds,
    )


def report_path(slug: str, kind: str) -> Path:
    return ROOT / kind / slug / "report.md"


def number_from_slug(slug: str) -> str:
    prefix = slug.split("-", 1)[0]
    if not prefix.isdigit():
        raise SystemExit(f"hallmark slug lacks numeric prefix: {slug}")
    return prefix


def hallmarks_catalog_rows(meta: IndexMeta, link_prefix: str) -> str:
    lines = [
        "| # | Hallmark | Report | Status | One-line claim |",
        "|---|---|---|---|---|",
    ]
    for item in meta.hallmarks:
        path = report_path(item.slug, "hallmarks")
        if item.status == "no report":
            if path.is_file():
                raise SystemExit(f"{item.slug} marked no report but {path} exists")
            report_cell = "—"
        else:
            if not path.is_file():
                raise SystemExit(f"{item.slug} status {item.status!r} but missing {path}")
            href = _href(link_prefix, item.slug)
            report_cell = f"[report.md]({href})"
        lines.append(
            f"| {number_from_slug(item.slug)} | {item.name} | {report_cell} | {item.status} | {item.one_liner} |"
        )
    return "\n".join(lines)


def section_maps(meta: IndexMeta) -> str:
    blocks: list[str] = []
    for item in meta.hallmarks:
        path = report_path(item.slug, "hallmarks")
        heading = f"### {number_from_slug(item.slug)} — {item.name} (`{item.status}`)"
        if item.status == "no report":
            blocks.append(f"{heading}\n\nNo `report.md`.")
            continue
        info = parse_report(path)
        updated = info.last_updated or "—"
        lines = [
            heading,
            "",
            f"[report.md]({_href('', item.slug)}) · Last updated: {updated}",
            "",
        ]
        for title in info.headings:
            if title in SKIP_SECTION_MAP_TITLES:
                continue
            anchor = github_anchor(title)
            lines.append(f"- [{title}]({_href('', item.slug)}#{anchor})")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def topics_catalog_rows(meta: IndexMeta, link_prefix: str) -> str:
    lines = [
        "| Slug | Report | Last updated | One-line claim |",
        "|---|---|---|---|",
    ]
    discovered = sorted(p.parent.name for p in (ROOT / "topics").glob("*/report.md"))
    sidecar_slugs = {item.slug for item in meta.topics}
    extra = [slug for slug in discovered if slug not in sidecar_slugs]
    if extra:
        raise SystemExit(f"topics missing from sidecar: {', '.join(extra)}")

    if not meta.topics:
        return "\n".join(lines)

    for item in meta.topics:
        path = report_path(item.slug, "topics")
        if not path.is_file():
            raise SystemExit(f"topic {item.slug} in sidecar but missing {path}")
        info = parse_report(path)
        updated = info.last_updated or "—"
        href = _href(link_prefix, item.slug)
        lines.append(f"| [{item.slug}]({href}) | [report.md]({href}) | {updated} | {item.one_liner} |")
    return "\n".join(lines)


def compounds_catalog_rows(meta: IndexMeta, link_prefix: str) -> str:
    lines = [
        "| Slug | CAS | Report | Last updated | One-line claim |",
        "|---|---|---|---|---|",
    ]
    discovered = sorted(p.parent.name for p in (ROOT / "compounds").glob("*/report.md"))
    sidecar_slugs = {item.slug for item in meta.compounds}
    extra = [slug for slug in discovered if slug not in sidecar_slugs]
    if extra:
        raise SystemExit(f"compounds missing from sidecar: {', '.join(extra)}")

    if not meta.compounds:
        return "\n".join(lines)

    for item in meta.compounds:
        path = report_path(item.slug, "compounds")
        if not path.is_file():
            raise SystemExit(f"compound {item.slug} in sidecar but missing {path}")
        info = parse_report(path)
        updated = info.last_updated or "—"
        href = _href(link_prefix, item.slug)
        lines.append(
            f"| [{item.slug}]({href}) | {item.primary_cas} | [report.md]({href}) | {updated} | {item.one_liner} |"
        )
    return "\n".join(lines)


def compounds_section_maps(meta: IndexMeta) -> str:
    if not meta.compounds:
        return ""
    blocks: list[str] = []
    for item in meta.compounds:
        path = report_path(item.slug, "compounds")
        info = parse_report(path)
        updated = info.last_updated or "—"
        lines = [
            f"### {item.slug}",
            "",
            f"[report.md]({_href('', item.slug)}) · CAS: {item.primary_cas} · Last updated: {updated}",
            "",
        ]
        for title in info.headings:
            if title in SKIP_SECTION_MAP_TITLES:
                continue
            anchor = github_anchor(title)
            lines.append(f"- [{title}]({_href('', item.slug)}#{anchor})")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def replace_block(text: str, name: str, body: str, source: Path) -> str:
    start = f"<!-- BEGIN GENERATED: {name} -->"
    end = "<!-- END GENERATED -->"
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"missing {start} in {source}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"missing {end} after {start} in {source}")
    return text[: i + len(start)] + "\n" + body.rstrip() + "\n" + text[j:]


def write_if_changed(path: Path, text: str) -> None:
    if not path.is_file():
        raise SystemExit(f"missing file to patch: {path}")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    meta = load_meta(META_PATH)

    root_readme = ROOT / "README.md"
    hallmarks_readme = ROOT / "hallmarks" / "README.md"
    topics_readme = ROOT / "topics" / "README.md"
    compounds_readme = ROOT / "compounds" / "README.md"

    root_text = root_readme.read_text(encoding="utf-8")
    root_text = replace_block(
        root_text, "hallmarks-catalog", hallmarks_catalog_rows(meta, "hallmarks/"), root_readme
    )
    root_text = replace_block(
        root_text, "topics-catalog", topics_catalog_rows(meta, "topics/"), root_readme
    )
    root_text = replace_block(
        root_text, "compounds-catalog", compounds_catalog_rows(meta, "compounds/"), root_readme
    )
    write_if_changed(root_readme, root_text)

    hall_text = hallmarks_readme.read_text(encoding="utf-8")
    hall_text = replace_block(
        hall_text, "hallmarks-catalog", hallmarks_catalog_rows(meta, ""), hallmarks_readme
    )
    hall_text = replace_block(
        hall_text, "hallmarks-section-maps", section_maps(meta), hallmarks_readme
    )
    hall_text = replace_block(hall_text, "hallmarks-adjacency", meta.adjacency, hallmarks_readme)
    write_if_changed(hallmarks_readme, hall_text)

    topics_text = topics_readme.read_text(encoding="utf-8")
    topics_text = replace_block(
        topics_text, "topics-catalog", topics_catalog_rows(meta, ""), topics_readme
    )
    write_if_changed(topics_readme, topics_text)

    compounds_text = compounds_readme.read_text(encoding="utf-8")
    compounds_text = replace_block(
        compounds_text, "compounds-catalog", compounds_catalog_rows(meta, ""), compounds_readme
    )
    compounds_text = replace_block(
        compounds_text, "compounds-section-maps", compounds_section_maps(meta), compounds_readme
    )
    write_if_changed(compounds_readme, compounds_text)

    print(f"updated {root_readme.relative_to(ROOT)}")
    print(f"updated {hallmarks_readme.relative_to(ROOT)}")
    print(f"updated {topics_readme.relative_to(ROOT)}")
    print(f"updated {compounds_readme.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
