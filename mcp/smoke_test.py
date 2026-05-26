from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

from config import PathSafetyError, REPO_ROOT, TEMPLATE_FILES, safe_resolve
from resources.registry import get_resource_entries, missing_resource_files
from schemas import TargetStep
from tools.status import check_step_prerequisites, get_project_status
from tools.validators import (
    _validate_text_for_layer,
    validate_digest_card,
    validate_layer_boundary,
    validate_synthesis_claims,
)
from tools.write import append_workflow_log, create_from_template


SMOKE_DIRS = [
    REPO_ROOT / "1_digest" / ".mcp_smoke",
    REPO_ROOT / "3_synthesis" / ".mcp_smoke",
    REPO_ROOT / "4_output" / ".mcp_smoke",
]


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


def test_git_path_rejected() -> None:
    try:
        safe_resolve(".git/config")
    except PathSafetyError:
        return
    raise AssertionError(".git path was not rejected")


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


def _write_smoke_file(layer: str, name: str, content: str) -> str:
    smoke_dir = REPO_ROOT / layer / ".mcp_smoke"
    smoke_dir.mkdir(parents=True, exist_ok=True)
    path = smoke_dir / name
    path.write_text(content, encoding="utf-8")
    return path.relative_to(REPO_ROOT).as_posix()


def test_validate_layer_boundary_rejects_absolute_path() -> None:
    try:
        validate_layer_boundary(str(REPO_ROOT / "README.md"))
    except PathSafetyError:
        return
    raise AssertionError("absolute validation path was not rejected")


def test_validate_layer_boundary_rejects_path_traversal() -> None:
    try:
        validate_layer_boundary("../README.md")
    except PathSafetyError:
        return
    raise AssertionError("path traversal validation path was not rejected")


def test_validate_layer_boundary_rejects_outside_repo() -> None:
    try:
        validate_layer_boundary("..\\outside.md")
    except PathSafetyError:
        return
    raise AssertionError("repo-external validation path was not rejected")


def test_validate_layer_boundary_flags_raw_pollution() -> None:
    issues = _validate_text_for_layer("综合来看，本案说明如下。待核验。", "0_raw")
    assert any(issue["severity"] == "error" for issue in issues)


def test_validate_layer_boundary_flags_digest_synthesis_language() -> None:
    target = _write_smoke_file(
        "1_digest",
        "digest_boundary.md",
        "司法实践通常认为，与其他案例相比，可以得出一般规则。",
    )
    result = validate_layer_boundary(target)
    assert result["layer"] == "1_digest"
    assert result["valid"] is False


def test_validate_digest_card_flags_case_generalization() -> None:
    target = _write_smoke_file(
        "1_digest",
        "case_card.md",
        "case_id: CC-SMOKE\n规则是法院一般应当认定，可以得出一般规则。",
    )
    result = validate_digest_card(target, "case_card")
    assert result["valid"] is False
    assert result["card_type"] == "case_card"


def test_validate_digest_card_flags_paper_opinion_as_rule() -> None:
    target = _write_smoke_file(
        "1_digest",
        "paper_card.md",
        "paper_id: PC-SMOKE\n作者认为法院规则是可以直接适用。",
    )
    result = validate_digest_card(target, "paper_card")
    assert result["valid"] is False
    assert result["card_type"] == "paper_card"


def test_validate_digest_card_flags_rule_missing_source_anchor() -> None:
    target = _write_smoke_file(
        "1_digest",
        "rule_card.md",
        "规则内容：一律支持惩罚性赔偿。",
    )
    result = validate_digest_card(target, "rule_card")
    assert result["valid"] is False
    assert any(issue["severity"] == "error" for issue in result["issues"])


def test_validate_synthesis_claims_flags_unsupported_broad_claim() -> None:
    target = _write_smoke_file(
        "3_synthesis",
        "synthesis_claim.md",
        "司法实践通常认为裁判规则是已经形成规则。",
    )
    result = validate_synthesis_claims(target)
    assert result["valid"] is False


def test_validate_synthesis_claims_flags_single_case_general_rule() -> None:
    target = _write_smoke_file(
        "3_synthesis",
        "single_case_claim.md",
        "仅凭本案可以得出一般规则。",
    )
    result = validate_synthesis_claims(target)
    assert result["valid"] is False


def test_validate_synthesis_claims_flags_strong_language() -> None:
    target = _write_smoke_file(
        "3_synthesis",
        "strong_language.md",
        "该责任必然成立，一律支持，均应适用。",
    )
    result = validate_synthesis_claims(target)
    assert result["valid"] is False


def run() -> None:
    tests = [
        test_server_imports,
        test_resource_registry_files_exist,
        test_template_allowlist_files_exist,
        test_project_status_keys,
        test_check_step_prerequisites_keys,
        test_path_traversal_rejected,
        test_git_path_rejected,
        test_create_from_template_allowed_layer,
        test_create_from_template_rejects_0_raw,
        test_create_from_template_rejects_path_traversal,
        test_create_from_template_rejects_absolute_path,
        test_create_from_template_refuses_overwrite_by_default,
        test_append_workflow_log_fixed_path,
        test_validate_layer_boundary_rejects_absolute_path,
        test_validate_layer_boundary_rejects_path_traversal,
        test_validate_layer_boundary_rejects_outside_repo,
        test_validate_layer_boundary_flags_raw_pollution,
        test_validate_layer_boundary_flags_digest_synthesis_language,
        test_validate_digest_card_flags_case_generalization,
        test_validate_digest_card_flags_paper_opinion_as_rule,
        test_validate_digest_card_flags_rule_missing_source_anchor,
        test_validate_synthesis_claims_flags_unsupported_broad_claim,
        test_validate_synthesis_claims_flags_single_case_general_rule,
        test_validate_synthesis_claims_flags_strong_language,
    ]
    try:
        for test in tests:
            test()
            print(f"ok - {test.__name__}")
    finally:
        for smoke_dir in SMOKE_DIRS:
            if smoke_dir.exists():
                shutil.rmtree(smoke_dir)


if __name__ == "__main__":
    run()
