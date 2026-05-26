from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import TypedDict

from config import (
    ALLOWED_WRITE_LAYERS,
    REPO_ROOT,
    TEMPLATE_FILES,
    PathSafetyError,
    read_repo_text,
    safe_resolve,
)


WORKFLOW_LOG_PATH = "_logs/workflow-log.md"
FORBIDDEN_TOP_LEVELS = {"0_raw", ".git"}


class CreateFromTemplateResult(TypedDict):
    created: bool
    path: str
    template_used: str
    warnings: list[str]
    next_action: str


class AppendWorkflowLogResult(TypedDict):
    appended: bool
    path: str
    warnings: list[str]


def _normalize_template_name(template_name: str) -> str:
    name = template_name.strip().replace("\\", "/")
    if "/" in name or name not in TEMPLATE_FILES:
        allowed = ", ".join(sorted(TEMPLATE_FILES))
        raise ValueError(f"Template is not allowed: {template_name}. Allowed: {allowed}")
    return name


def _resolve_write_target(target_layer: str, target_relative_path: str) -> Path:
    if target_layer not in ALLOWED_WRITE_LAYERS:
        allowed = ", ".join(sorted(ALLOWED_WRITE_LAYERS))
        raise PathSafetyError(f"Target layer is not writable: {target_layer}. Allowed: {allowed}")

    relative = Path(target_relative_path)
    if relative.is_absolute() or relative.anchor or ".." in relative.parts:
        raise PathSafetyError(f"Rejected unsafe target path: {target_relative_path}")
    if not relative.parts:
        raise PathSafetyError("Target path must name a file inside the target layer.")
    if relative.parts[0] in FORBIDDEN_TOP_LEVELS:
        raise PathSafetyError(f"Rejected forbidden target path: {target_relative_path}")

    layer_root = safe_resolve(target_layer)
    target = (layer_root / relative).resolve()
    try:
        target.relative_to(layer_root)
    except ValueError as exc:
        raise PathSafetyError(f"Rejected target outside layer: {target_relative_path}") from exc
    try:
        target.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise PathSafetyError(f"Rejected target outside repository: {target_relative_path}") from exc
    return target


def _render_template_skeleton(template_text: str, title: str | None, source_id: str | None) -> str:
    rendered = template_text
    if title is not None:
        rendered = rendered.replace("{{title}}", title)
        rendered = rendered.replace("{{topic_name}}", title)
    if source_id is not None:
        rendered = rendered.replace("{{source_id}}", source_id)
    return rendered


def create_from_template(
    template_name: str,
    target_layer: str,
    target_relative_path: str,
    title: str | None = None,
    source_id: str | None = None,
    overwrite: bool = False,
) -> CreateFromTemplateResult:
    template_key = _normalize_template_name(template_name)
    template_path = TEMPLATE_FILES[template_key]
    target = _resolve_write_target(target_layer, target_relative_path)

    warnings: list[str] = [
        "Created from a template skeleton only; no legal analysis was generated.",
        "Human review is still required before using this file as research output.",
    ]

    if target.exists() and not overwrite:
        raise FileExistsError(f"Target already exists and overwrite=false: {target}")

    template_text = read_repo_text(template_path)
    content = _render_template_skeleton(template_text, title, source_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

    return {
        "created": True,
        "path": target.relative_to(REPO_ROOT).as_posix(),
        "template_used": template_path,
        "warnings": warnings,
        "next_action": "Review and fill the skeleton using only approved source materials.",
    }


def append_workflow_log(
    action: str,
    target: str,
    summary: str,
    warnings: list[str] | None = None,
) -> AppendWorkflowLogResult:
    log_path = safe_resolve(WORKFLOW_LOG_PATH)
    if not log_path.is_file():
        raise FileNotFoundError(f"Workflow log not found: {WORKFLOW_LOG_PATH}")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    warning_text = "; ".join(warnings or [])
    note = summary if not warning_text else f"{summary} Warnings: {warning_text}"
    entry = f"| {timestamp} | {action} | {target} | MCP controlled write | {note} |\n"
    with log_path.open("a", encoding="utf-8", newline="") as file:
        file.write(entry)

    return {
        "appended": True,
        "path": WORKFLOW_LOG_PATH,
        "warnings": warnings or [],
    }
