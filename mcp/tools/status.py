from __future__ import annotations

from config import IMPORTANT_FILES, LAYER_DIRS, REPO_ROOT, is_dir, is_file, safe_resolve
from prompts.registry import get_prompt_entries, missing_prompt_files
from resources.registry import missing_resource_files
from schemas import HarnessAssets, ProjectStatus, StepPrerequisites, TargetStep


def _relative_files(directory: str, pattern: str = "*.md") -> list[str]:
    root = safe_resolve(directory)
    if not root.is_dir():
        return []
    return sorted(
        path.relative_to(REPO_ROOT).as_posix()
        for path in root.rglob(pattern)
        if path.is_file()
    )


def _has_any_non_gitkeep_file(directory: str, pattern: str = "*.md") -> bool:
    root = safe_resolve(directory)
    if not root.is_dir():
        return False
    return any(path.is_file() and path.name != ".gitkeep" for path in root.rglob(pattern))


def _topic_config_exists() -> bool:
    return is_file(IMPORTANT_FILES["root_topic_config"]) or is_file(
        IMPORTANT_FILES["framework_topic_config"]
    )


def _has_factor_model() -> bool:
    return _has_any_non_gitkeep_file("2_framework/adjudication_factors")


def _has_pilot() -> bool:
    return is_dir(IMPORTANT_FILES["pilot"]) and _has_any_non_gitkeep_file(
        IMPORTANT_FILES["pilot"]
    )


def _has_framework_lock() -> bool:
    return is_file(IMPORTANT_FILES["framework_lock"])


def get_project_status() -> ProjectStatus:
    warnings: list[str] = []
    missing_resources = missing_resource_files()
    missing_prompts = missing_prompt_files()

    if missing_resources:
        warnings.append(
            "Some configured MCP resources are missing: "
            + ", ".join(missing_resources)
        )
    if missing_prompts:
        warnings.append(
            "Some configured MCP prompts are missing: " + ", ".join(missing_prompts)
        )
    if not _topic_config_exists():
        warnings.append(
            "No topic config found; run activate_topic_config before framework work."
        )
    if not _has_framework_lock():
        warnings.append("Framework lock file not found; final synthesis may be premature.")

    return {
        "has_topic_config": _topic_config_exists(),
        "has_raw_layer": is_dir(LAYER_DIRS["raw"]),
        "has_digest_layer": is_dir(LAYER_DIRS["digest"]),
        "has_framework_layer": is_dir(LAYER_DIRS["framework"]),
        "has_synthesis_layer": is_dir(LAYER_DIRS["synthesis"]),
        "has_output_layer": is_dir(LAYER_DIRS["output"]),
        "available_templates": sorted(_relative_files("_templates")),
        "available_prompts": sorted(entry.name for entry in get_prompt_entries()),
        "warnings": warnings,
    }


def check_step_prerequisites(target_step: TargetStep) -> StepPrerequisites:
    status = get_project_status()
    missing: list[str] = []
    warnings: list[str] = []

    has_topic = status["has_topic_config"]
    has_raw = status["has_raw_layer"]
    has_digest = status["has_digest_layer"]
    has_framework = status["has_framework_layer"]
    has_synthesis = status["has_synthesis_layer"]
    has_output = status["has_output_layer"]
    has_factor_model = _has_factor_model()
    has_pilot = _has_pilot()
    has_lock = _has_framework_lock()

    if target_step == TargetStep.ACTIVATE_TOPIC_CONFIG:
        if has_topic:
            warnings.append("Topic config already exists; review before replacing it.")
        suggested = "Review the existing topic config or run the activation prompt for a new topic."
    elif target_step == TargetStep.RAW_COLLECTION:
        if not has_topic:
            missing.append("topic_config")
        suggested = "Collect human-approved raw materials under 0_raw without AI summaries."
    elif target_step == TargetStep.DIGEST:
        if not has_topic:
            missing.append("topic_config")
        if not has_raw:
            missing.append("0_raw layer")
        suggested = "Create single-source cards only after raw materials are available."
    elif target_step == TargetStep.FRAMEWORK_DESIGN:
        if not has_topic:
            missing.append("topic_config")
        if not has_digest:
            missing.append("1_digest layer")
        suggested = "Design observation factors and weighting without final legal conclusions."
    elif target_step == TargetStep.PILOT:
        if not has_topic:
            missing.append("topic_config")
        if not has_framework:
            missing.append("2_framework layer")
        if not has_factor_model:
            missing.append("factor_or_weighting_model")
        suggested = "Run a pilot case check and mark uncertain content as \u5f85\u6838\u9a8c."
    elif target_step == TargetStep.FRAMEWORK_LOCK:
        if not has_factor_model:
            missing.append("factor_or_weighting_model")
        if not has_pilot:
            missing.append("pilot_check")
        suggested = "Lock framework v1 only after pilot review confirms fields are usable."
    elif target_step == TargetStep.BATCH_CASE_CARDS:
        if not has_topic:
            missing.append("topic_config")
        if not has_factor_model:
            missing.append("factor_or_weighting_model")
        if not has_pilot:
            missing.append("pilot_check")
        if not has_lock:
            missing.append("framework_v1_lock")
        suggested = "Generate only single-source case cards after framework v1 is locked."
    elif target_step == TargetStep.CROSS_CASE_COMPARISON:
        if not has_lock:
            missing.append("framework_v1_lock")
        if not has_digest:
            missing.append("1_digest layer")
        if not has_synthesis:
            missing.append("3_synthesis layer")
        suggested = "Compare across case cards without upgrading observations into final conclusions."
    elif target_step == TargetStep.FINAL_SYNTHESIS:
        if not has_lock:
            missing.append("framework_v1_lock")
        if not has_synthesis:
            missing.append("3_synthesis layer")
        warnings.append(
            "Final legal conclusions require human legal judgment memo or explicit sign-off."
        )
        suggested = "Prepare synthesis draft, claim ledger, rule anchor map, and risk review for human validation."
    elif target_step == TargetStep.OUTPUT_ADAPTATION:
        if not has_output:
            missing.append("4_output layer")
        warnings.append("Output adaptation must not add, delete, or strengthen synthesis conclusions.")
        suggested = "Adapt only human-confirmed conclusions into presentation or document materials."
    else:
        missing.append("known_target_step")
        suggested = "Choose a supported target step."

    return {
        "allowed": not missing,
        "missing_prerequisites": missing,
        "warnings": warnings,
        "suggested_next_action": suggested,
    }


def list_harness_assets() -> HarnessAssets:
    scripts_root = safe_resolve("scripts")
    scripts = []
    if scripts_root.is_dir():
        scripts = sorted(
            path.relative_to(REPO_ROOT).as_posix()
            for path in scripts_root.rglob("*")
            if path.is_file()
        )

    return {
        "docs": _relative_files("docs"),
        "templates": _relative_files("_templates"),
        "prompts": sorted(entry.path for entry in get_prompt_entries()),
        "scripts": scripts,
    }
