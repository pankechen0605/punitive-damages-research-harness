from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

from config import PathSafetyError, REPO_ROOT, TEMPLATE_FILES, safe_resolve
from resources.registry import get_resource_entries, missing_resource_files
from schemas import TargetStep
from tools.status import check_step_prerequisites, get_project_status
from tools.write import append_workflow_log, create_from_template


SMOKE_DIR = REPO_ROOT / "4_output" / ".mcp_smoke"


def test_server_imports() -> None:
    server_path = Path(__file__).resolve().parent / "server.py"
    spec = importlib.util.spec_from_file_location("harness_mcp_server", server_path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    assert hasattr(module, "create_server")


def test_resource_registry_files_exist() -> None:
    assert missing_resource_files() == []
    assert get_resource_entries()


def test_template_allowlist_files_exist() -> None:
    assert TEMPLATE_FILES
    for template_path in TEMPLATE_FILES.values():
        assert (REPO_ROOT / template_path).is_file()


def test_project_status_keys() -> None:
    status = get_project_status()
    expected = {
        "has_topic_config",
        "has_raw_layer",
        "has_digest_layer",
        "has_framework_layer",
        "has_synthesis_layer",
        "has_output_layer",
        "available_templates",
        "available_prompts",
        "warnings",
    }
    assert expected.issubset(status.keys())


def test_check_step_prerequisites_keys() -> None:
    result = check_step_prerequisites(TargetStep.DIGEST)
    expected = {
        "allowed",
        "missing_prerequisites",
        "warnings",
        "suggested_next_action",
    }
    assert expected.issubset(result.keys())


def test_path_traversal_rejected() -> None:
    try:
        safe_resolve("../README.md")
    except PathSafetyError:
        return
    raise AssertionError("path traversal was not rejected")


def test_create_from_template_allowed_layer() -> None:
    result = create_from_template(
        template_name="final_doc_template.md",
        target_layer="4_output",
        target_relative_path=".mcp_smoke/final_doc.md",
        title="Smoke Test",
        overwrite=True,
    )
    created = REPO_ROOT / result["path"]
    assert result["created"] is True
    assert result["template_used"] == "_templates/final_doc_template.md"
    assert created.is_file()


def test_create_from_template_rejects_0_raw() -> None:
    try:
        create_from_template(
            template_name="case_card_template.md",
            target_layer="0_raw",
            target_relative_path="blocked.md",
        )
    except PathSafetyError:
        return
    raise AssertionError("0_raw write was not rejected")


def test_create_from_template_rejects_path_traversal() -> None:
    try:
        create_from_template(
            template_name="final_doc_template.md",
            target_layer="4_output",
            target_relative_path="../blocked.md",
        )
    except PathSafetyError:
        return
    raise AssertionError("path traversal write was not rejected")


def test_create_from_template_rejects_absolute_path() -> None:
    try:
        create_from_template(
            template_name="final_doc_template.md",
            target_layer="4_output",
            target_relative_path=str(REPO_ROOT / "4_output" / "absolute.md"),
        )
    except PathSafetyError:
        return
    raise AssertionError("absolute target path was not rejected")


def test_create_from_template_refuses_overwrite_by_default() -> None:
    create_from_template(
        template_name="final_doc_template.md",
        target_layer="4_output",
        target_relative_path=".mcp_smoke/no_overwrite.md",
        overwrite=True,
    )
    try:
        create_from_template(
            template_name="final_doc_template.md",
            target_layer="4_output",
            target_relative_path=".mcp_smoke/no_overwrite.md",
        )
    except FileExistsError:
        return
    raise AssertionError("overwrite=false did not refuse existing target")


def test_append_workflow_log_fixed_path() -> None:
    log_path = safe_resolve("_logs/workflow-log.md")
    original = log_path.read_bytes() if log_path.exists() else None
    try:
        result = append_workflow_log(
            action="MCP smoke test",
            target="mcp",
            summary="append_workflow_log fixed-path smoke check",
        )
        assert result["appended"] is True
        assert result["path"] == "_logs/workflow-log.md"
        assert log_path.read_bytes().endswith(
            b"append_workflow_log fixed-path smoke check |\n"
        )
    finally:
        if original is None:
            log_path.unlink(missing_ok=True)
        else:
            log_path.write_bytes(original)


def run() -> None:
    tests = [
        test_server_imports,
        test_resource_registry_files_exist,
        test_template_allowlist_files_exist,
        test_project_status_keys,
        test_check_step_prerequisites_keys,
        test_path_traversal_rejected,
        test_create_from_template_allowed_layer,
        test_create_from_template_rejects_0_raw,
        test_create_from_template_rejects_path_traversal,
        test_create_from_template_rejects_absolute_path,
        test_create_from_template_refuses_overwrite_by_default,
        test_append_workflow_log_fixed_path,
    ]
    try:
        for test in tests:
            test()
            print(f"ok - {test.__name__}")
    finally:
        if SMOKE_DIR.exists():
            shutil.rmtree(SMOKE_DIR)


if __name__ == "__main__":
    run()
