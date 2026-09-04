from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from post_edit_validation import (
    agents_for_buckets,
    build_followup,
    classify,
    handle_record,
    handle_stop,
    is_test_path,
    to_repo_relative,
)


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_classify_skips_tmp_and_secrets() -> None:
    assert classify(Path("tmp/2026-09-03_topic/notes.md")) == set()
    assert classify(Path(".rag/chunks.json")) == set()
    assert classify(Path(".env")) == set()
    assert classify(Path("secrets/credentials.json")) == set()
    assert classify(Path("certs/dev.pem")) == set()


def test_classify_report_and_rules_and_code_paths() -> None:
    assert classify(Path("hallmarks/01-genomic-instability/report.md")) == {"reports"}
    assert classify(Path("topics/example/sources/📚/paper.md")) == {"reports"}
    assert classify(Path("AGENTS.md")) == {"rules"}
    assert classify(Path(".cursor/hooks/post_edit_validation.py")) == {"rules", "code"}
    assert classify(Path("mcp/docs-rag/server.py")) == {"code"}
    assert classify(Path("README.md")) == {"other"}


def test_classify_tests_by_path_convention() -> None:
    assert is_test_path(Path("mcp/docs-rag/tests/test_search.py"))
    assert "tests" in classify(Path("mcp/docs-rag/tests/test_search.py"))
    assert "code" in classify(Path("mcp/docs-rag/tests/test_search.py"))
    assert is_test_path(Path("pkg/foo_test.go"))
    assert is_test_path(Path("web/app.test.ts"))


def test_agents_do_not_stack_reviewer_army() -> None:
    assert agents_for_buckets({"reports"}) == ["rule-validation"]
    assert agents_for_buckets({"tests", "code"}) == ["rule-validation", "test-engineer"]
    assert agents_for_buckets({"code"}) == ["rule-validation", "pr-reviewer"]
    assert agents_for_buckets({"rules", "other"}) == ["rule-validation"]


def test_record_then_stop_emits_rule_validation(repo: Path) -> None:
    target = repo / "compounds" / "nad" / "report.md"
    target.parent.mkdir(parents=True)
    target.write_text("# nad\n", encoding="utf-8")

    recorded = handle_record({"file_path": str(target)}, repo)
    assert recorded == {}

    result = handle_stop({"status": "completed", "loop_count": 0}, repo)
    assert "followup_message" in result
    message = result["followup_message"]
    assert "rule-validation" in message
    assert "compounds/nad/report.md" in message
    assert "pr-reviewer" not in message
    assert "test-engineer" not in message

    replay = handle_stop({"status": "completed", "loop_count": 0}, repo)
    assert replay == {}


def test_stop_skips_aborted_and_same_set_on_loop(repo: Path) -> None:
    hook = repo / ".cursor" / "hooks" / "post-edit-validation.py"
    hook.parent.mkdir(parents=True)
    hook.write_text("print('ok')\n", encoding="utf-8")
    handle_record({"file_path": str(hook)}, repo)

    assert handle_stop({"status": "aborted", "loop_count": 0}, repo) == {}

    first = handle_stop({"status": "completed", "loop_count": 0}, repo)
    assert "followup_message" in first
    assert "pr-reviewer" in first["followup_message"]

    handle_record({"file_path": str(hook)}, repo)
    assert handle_stop({"status": "completed", "loop_count": 1}, repo) == {}


def test_to_repo_relative_rejects_outside(repo: Path) -> None:
    assert to_repo_relative("/etc/passwd", repo) is None
    inside = repo / "AGENTS.md"
    inside.write_text("x\n", encoding="utf-8")
    assert to_repo_relative(str(inside), repo) == Path("AGENTS.md")


def test_stop_requests_again_when_new_paths_appear_on_loop(repo: Path) -> None:
    first = repo / "scripts" / "build-index.py"
    first.parent.mkdir(parents=True)
    first.write_text("print(0)\n", encoding="utf-8")
    second = repo / "README.md"
    second.write_text("# hi\n", encoding="utf-8")

    handle_record({"file_path": str(first)}, repo)
    first_stop = handle_stop({"status": "completed", "loop_count": 0}, repo)
    assert "pr-reviewer" in first_stop["followup_message"]

    handle_record({"file_path": str(second)}, repo)
    second_stop = handle_stop({"status": "completed", "loop_count": 1}, repo)
    assert "rule-validation" in second_stop["followup_message"]
    assert "README.md" in second_stop["followup_message"]
    assert handle_stop({"status": "completed", "loop_count": 2}, repo) == {}


def test_cli_record_and_stop_roundtrip(repo: Path) -> None:
    script = Path(__file__).with_name("post_edit_validation.py")
    target = repo / "hallmarks" / "01-genomic-instability" / "report.md"
    target.parent.mkdir(parents=True)
    target.write_text("x\n", encoding="utf-8")

    record = subprocess.run(
        [sys.executable, str(script), "record"],
        input=json.dumps({"file_path": str(target)}),
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(record.stdout) == {}

    stop = subprocess.run(
        [sys.executable, str(script), "stop"],
        input=json.dumps({"status": "completed", "loop_count": 0}),
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(stop.stdout)
    assert "rule-validation" in payload["followup_message"]
    assert "hallmarks/01-genomic-instability/report.md" in payload["followup_message"]


def test_followup_lists_only_requested_agents() -> None:
    message = build_followup(
        {
            "mcp/docs-rag/tests/test_search.py": {"buckets": ["tests", "code"]},
        }
    )
    assert "test-engineer" in message
    assert "pr-reviewer" not in message
    parsed_ok = json.dumps({"followup_message": message})
    assert "rule-validation" in parsed_ok
