#!/usr/bin/env python3
"""Record afterFileEdit paths; on stop, request validation agents via followup_message.

Cursor hooks cannot spawn Task/subagents. This script only queues paths and,
on a completed agent turn, prints a stop-hook followup for the parent to launch
the named agents. Path prefix and filename convention only — no prompt text,
no content classification.
"""

from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path
from typing import Any

STATE_VERSION = 1
STATE_RELATIVE = Path(".cursor") / "hooks" / "state" / "post-edit-validation.json"

SKIP_PREFIXES = (
    Path("tmp"),
    Path(".rag"),
    Path(".git"),
    Path(".cursor") / "hooks" / "state",
)
REPORT_PREFIXES = (Path("hallmarks"), Path("topics"), Path("compounds"))
RULE_PREFIXES = (
    Path("AGENTS.md"),
    Path("template.md"),
    Path("HOW_TO_ASK_AGENTS_QUESTIONS.MD"),
    Path(".cursor"),
    Path(".claude"),
)
CODE_PREFIXES = (Path("mcp"), Path("scripts"))
CODE_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".go"}
SECRET_NAMES = {".env", ".envrc", "credentials.json"}
MAX_STOP_LOOP = 2

logger = logging.getLogger("post-edit-validation")


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[post-edit-validation] %(levelname)s %(message)s",
        stream=sys.stderr,
    )


def repo_root() -> Path:
    return Path.cwd()


def state_path(root: Path) -> Path:
    return root / STATE_RELATIVE


def empty_state() -> dict[str, Any]:
    return {
        "version": STATE_VERSION,
        "files": {},
        "last_followup_files": [],
    }


def load_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return empty_state()
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or raw.get("version") != STATE_VERSION:
        raise ValueError(f"unsupported hook state at {path}")
    files = raw.get("files")
    last = raw.get("last_followup_files")
    if not isinstance(files, dict):
        raise ValueError(f"hook state files must be an object: {path}")
    if not isinstance(last, list):
        raise ValueError(f"hook state last_followup_files must be a list: {path}")
    return {
        "version": STATE_VERSION,
        "files": files,
        "last_followup_files": [str(item) for item in last],
    }


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def emit(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False))
    sys.stdout.write("\n")


def to_repo_relative(file_path: str, root: Path) -> Path | None:
    candidate = Path(file_path)
    resolved = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()
    root_resolved = root.resolve()
    try:
        return resolved.relative_to(root_resolved)
    except ValueError:
        return None


def is_under(relative: Path, prefix: Path) -> bool:
    return relative == prefix or relative.is_relative_to(prefix)


def is_secret_path(relative: Path) -> bool:
    name = relative.name
    if name in SECRET_NAMES or name.startswith(".env."):
        return True
    return relative.suffix == ".pem"


def is_test_path(relative: Path) -> bool:
    if "tests" in relative.parts or "test" in relative.parts:
        return True
    name = relative.name
    if name.startswith("test_") and name.endswith(".py"):
        return True
    if name.endswith("_test.py"):
        return True
    if name.endswith(".test.ts") or name.endswith(".test.tsx") or name.endswith(".test.js"):
        return True
    return name.endswith("_test.go")


def classify(relative: Path) -> set[str]:
    """Return path buckets. Empty set means skip (do not queue)."""
    if any(is_under(relative, prefix) for prefix in SKIP_PREFIXES):
        return set()
    if is_secret_path(relative):
        return set()

    buckets: set[str] = set()
    if any(is_under(relative, prefix) for prefix in REPORT_PREFIXES):
        buckets.add("reports")
    if any(is_under(relative, prefix) for prefix in RULE_PREFIXES):
        buckets.add("rules")
    if is_test_path(relative):
        buckets.add("tests")
    if any(is_under(relative, prefix) for prefix in CODE_PREFIXES) or relative.suffix in CODE_SUFFIXES:
        buckets.add("code")
    if not buckets:
        buckets.add("other")
    return buckets


def agents_for_buckets(all_buckets: set[str]) -> list[str]:
    agents = ["rule-validation"]
    if "tests" in all_buckets:
        agents.append("test-engineer")
    elif "code" in all_buckets:
        agents.append("pr-reviewer")
    return agents


def build_followup(files: dict[str, Any]) -> str:
    lines = [
        "Post-edit validation is required for this turn.",
        "Cursor hooks cannot spawn Task/subagents; this message is the stop-hook follow-up.",
        "Launch the listed Task subagent(s) now. Do not skip. Do not start unrelated work.",
        "",
        "Changed files (path-scoped; not an intent classification):",
    ]
    all_buckets: set[str] = set()
    for rel in sorted(files):
        entry = files[rel]
        buckets = entry.get("buckets", [])
        if isinstance(buckets, list):
            all_buckets.update(str(item) for item in buckets)
            bucket_text = ",".join(str(item) for item in buckets)
        else:
            bucket_text = "other"
            all_buckets.add("other")
        lines.append(f"- {rel} ({bucket_text})")

    agents = agents_for_buckets(all_buckets)
    lines.extend(["", "Invoke in parallel via the Task tool:"])
    for index, agent in enumerate(agents, start=1):
        lines.append(
            f"{index}. subagent_type: {agent!r} — pass the file list above "
            f"as ### Changed files. Review only; do not implement a new feature."
        )
    lines.extend(
        [
            "",
            "Do not auto-launch security-review, bugbot, or "
            "thermo-nuclear-code-quality-review.",
            "rule-validation may write findings under ./tmp/YYYY-MM-DD_rule-validation/.",
            "After the subagent(s) return, summarize pass/needs-work to the user.",
        ]
    )
    return "\n".join(lines)


def handle_record(payload: dict[str, Any], root: Path) -> dict[str, Any]:
    file_path = payload.get("file_path")
    if not isinstance(file_path, str) or not file_path:
        logger.info("record skipped: missing file_path")
        return {}
    relative = to_repo_relative(file_path, root)
    if relative is None:
        logger.info("record skipped: outside repo (%s)", file_path)
        return {}
    buckets = classify(relative)
    if not buckets:
        logger.info("record skipped: %s", relative.as_posix())
        return {}
    path = state_path(root)
    state = load_state(path)
    rel_key = relative.as_posix()
    state["files"][rel_key] = {
        "buckets": sorted(buckets),
        "recorded_at_ms": int(time.time() * 1000),
    }
    save_state(path, state)
    logger.info("recorded %s buckets=%s", rel_key, sorted(buckets))
    return {}


def handle_stop(payload: dict[str, Any], root: Path) -> dict[str, Any]:
    status = payload.get("status")
    loop_count = payload.get("loop_count", 0)
    if status != "completed":
        logger.info("stop skipped: status=%s", status)
        return {}
    if not isinstance(loop_count, int) or loop_count < 0:
        raise ValueError(f"invalid loop_count: {loop_count!r}")
    if loop_count >= MAX_STOP_LOOP:
        logger.info("stop skipped: loop_count=%s", loop_count)
        return {}

    path = state_path(root)
    state = load_state(path)
    files = state["files"]
    if not files:
        logger.info("stop skipped: empty queue")
        return {}

    queued = sorted(files)
    last = sorted(str(item) for item in state["last_followup_files"])
    if loop_count > 0 and queued == last:
        logger.info("stop skipped: same file set already requested")
        return {}

    message = build_followup(files)
    state["last_followup_files"] = queued
    state["files"] = {}
    save_state(path, state)
    logger.info("stop followup for %s files agents implied", len(queued))
    return {"followup_message": message}


def read_stdin_json() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise ValueError("hook stdin must be a JSON object")
    return parsed


def main(argv: list[str]) -> int:
    configure_logging()
    if len(argv) != 2 or argv[1] not in {"record", "stop"}:
        raise SystemExit("usage: post_edit_validation.py record|stop")
    action = argv[1]
    payload = read_stdin_json()
    root = repo_root()
    if action == "record":
        emit(handle_record(payload, root))
        return 0
    emit(handle_stop(payload, root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
