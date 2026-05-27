from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

from config import REPO_ROOT, PathSafetyError, safe_resolve
from prompts.registry import get_prompt_entries
from resources.registry import get_resource_entries
from schemas import TargetStep
from tools.pdf import run_pdf_to_md
from tools.status import check_step_prerequisites, get_project_status
from tools.validators import validate_digest_card, validate_layer_boundary
from tools.write import append_workflow_log, create_from_template


SMOKE_DIRS = [
    REPO_ROOT / "0_raw" / ".mcp_v1_smoke",
    REPO_ROOT / "1_digest" / ".mcp_v1_smoke",
    REPO_ROOT / "4_output" / ".mcp_v1_smoke",
]
SMOKE_PDF_OUTPUT = REPO_ROOT / "0_raw" / "extracted_md" / "mcp_v1_smoke.md"


def _server_module():
    server_path = Path(__file__).resolve().parent / "server.py"
    spec = importlib.util.spec_from_file_location("harness_mcp_server_v1", server_path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _write_file(layer: str, name: str, content: str) -> str:
    smoke_dir = REPO_ROOT / layer / ".mcp_v1_smoke"
    smoke_dir.mkdir(parents=True, exist_ok=True)
    path = smoke_dir / name
    path.write_text(content, encoding="utf-8")
    return path.relative_to(REPO_ROOT).as_posix()


def _write_pdf() -> str:
    smoke_dir = REPO_ROOT / "0_raw" / ".mcp_v1_smoke"
    smoke_dir.mkdir(parents=True, exist_ok=True)
    path = smoke_dir / "mcp_v1_smoke.pdf"
    path.write_bytes(b"%PDF-1.4\n% v1 smoke placeholder\n")
    return path.relative_to(REPO_ROOT).as_posix()


def test_server_imports() -> None:
    module = _server_module()
    assert hasattr(module, "create_server")


def test_registries_load() -> None:
    assert get_resource_entries()
    assert get_prompt_entries()


def test_status_tools_return_expected_keys() -> None:
    status = get_project_status()
    assert {
        "has_topic_config",
        "has_raw_layer",
        "has_digest_layer",
        "has_framework_layer",
        "has_synthesis_layer",
        "has_output_layer",
        "available_templates",
        "available_prompts",
        "warnings",
    }.issubset(status.keys())

    prerequisites = check_step_prerequisites(TargetStep.DIGEST)
    assert {
        "allowed",
        "missing_prerequisites",
        "warnings",
        "suggested_next_action",
    }.issubset(prerequisites.keys())


def test_create_from_template_safe_area() -> None:
    result = create_from_template(
        template_name="final_doc_template.md",
        target_layer="4_output",
        target_relative_path=".mcp_v1_smoke/final_doc.md",
        overwrite=True,
    )
    assert result["created"] is True
    assert (REPO_ROOT / result["path"]).is_file()


def test_create_from_template_rejections() -> None:
    for target_layer, target_path in [
        ("4_output", str(REPO_ROOT / "4_output" / "blocked.md")),
        ("4_output", "../blocked.md"),
        ("0_raw", "blocked.md"),
    ]:
        try:
            create_from_template(
                template_name="final_doc_template.md",
                target_layer=target_layer,
                target_relative_path=target_path,
            )
        except PathSafetyError:
            continue
        raise AssertionError(f"unsafe template target was not rejected: {target_path}")


def test_append_workflow_log_restore() -> None:
    log_path = safe_resolve("_logs/workflow-log.md")
    original = log_path.read_bytes()
    try:
        result = append_workflow_log(
            action="MCP v1 smoke",
            target="mcp",
            summary="temporary append check",
        )
        assert result["appended"] is True
        assert result["path"] == "_logs/workflow-log.md"
    finally:
        log_path.write_bytes(original)


def test_validators() -> None:
    digest_path = _write_file(
        "1_digest",
        "bad_digest.md",
        "司法实践通常认为，与其他案例相比，可以得出一般规则。",
    )
    boundary = validate_layer_boundary(digest_path)
    card = validate_digest_card(digest_path, "case_card")
    assert boundary["valid"] is False
    assert card["valid"] is False

    try:
        validate_layer_boundary("../README.md")
    except PathSafetyError:
        pass
    else:
        raise AssertionError("validator path traversal was not rejected")


def test_pdf_dry_run_writes_nothing() -> None:
    pdf_path = _write_pdf()
    result = run_pdf_to_md(pdf_path)
    assert result["converted"] is False
    assert result["dry_run"] is True
    assert result["output_path"] == "0_raw/extracted_md/mcp_v1_smoke.md"
    assert not SMOKE_PDF_OUTPUT.exists()


def test_tool_modules_import_together() -> None:
    import tools.pdf  # noqa: F401
    import tools.status  # noqa: F401
    import tools.validators  # noqa: F401
    import tools.write  # noqa: F401


def run() -> None:
    tests = [
        test_server_imports,
        test_registries_load,
        test_status_tools_return_expected_keys,
        test_create_from_template_safe_area,
        test_create_from_template_rejections,
        test_append_workflow_log_restore,
        test_validators,
        test_pdf_dry_run_writes_nothing,
        test_tool_modules_import_together,
    ]
    original_pdf_output = SMOKE_PDF_OUTPUT.read_bytes() if SMOKE_PDF_OUTPUT.exists() else None
    try:
        for test in tests:
            test()
            print(f"ok - {test.__name__}")
    finally:
        for smoke_dir in SMOKE_DIRS:
            if smoke_dir.exists():
                shutil.rmtree(smoke_dir)
        if original_pdf_output is None:
            SMOKE_PDF_OUTPUT.unlink(missing_ok=True)
        else:
            SMOKE_PDF_OUTPUT.write_bytes(original_pdf_output)


if __name__ == "__main__":
    run()
