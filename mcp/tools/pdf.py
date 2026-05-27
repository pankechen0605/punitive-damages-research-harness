from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, TypedDict

from config import REPO_ROOT, PathSafetyError, safe_resolve


PDF_TO_MD_SCRIPT = "scripts/pdf_to_md.py"
EXTRACTED_MD_DIR = "0_raw/extracted_md"


class PdfToMdResult(TypedDict):
    converted: bool
    dry_run: bool
    input_path: str
    output_path: str
    script_used: str
    warnings: list[str]
    next_action: str


def _resolve_pdf_input(input_relative_path: str) -> Path:
    path = Path(input_relative_path)
    if path.is_absolute() or path.anchor or ".." in path.parts or ".git" in path.parts:
        raise PathSafetyError(f"Rejected unsafe PDF input path: {input_relative_path}")
    if not path.parts or path.parts[0] != "0_raw":
        raise PathSafetyError("PDF input must be under 0_raw/.")
    if path.suffix.lower() != ".pdf":
        raise ValueError("PDF input must end with .pdf.")

    resolved = safe_resolve(input_relative_path)
    if not resolved.is_file():
        raise FileNotFoundError(f"PDF input not found: {input_relative_path}")
    return resolved


def _output_path_for(pdf_path: Path) -> Path:
    output_dir = safe_resolve(EXTRACTED_MD_DIR)
    output_path = (output_dir / f"{pdf_path.stem}.md").resolve()
    try:
        output_path.relative_to(output_dir)
    except ValueError as exc:
        raise PathSafetyError("Resolved Markdown output escaped 0_raw/extracted_md/.") from exc
    if output_path.suffix.lower() != ".md":
        raise PathSafetyError("Resolved Markdown output must end with .md.")
    return output_path


def _load_pdf_to_md_module() -> Any:
    script_path = safe_resolve(PDF_TO_MD_SCRIPT)
    spec = importlib.util.spec_from_file_location("harness_pdf_to_md", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {PDF_TO_MD_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_pdf_to_md(
    input_relative_path: str,
    overwrite: bool = False,
    dry_run: bool = True,
) -> PdfToMdResult:
    pdf_path = _resolve_pdf_input(input_relative_path)
    output_path = _output_path_for(pdf_path)
    warnings = [
        "Extraction preserves machine-readable text only; no summary or legal analysis is generated.",
        "Original PDF is not modified.",
    ]

    if output_path.exists() and not overwrite:
        raise FileExistsError(f"Output already exists and overwrite=false: {output_path}")

    converted = False
    if not dry_run:
        module = _load_pdf_to_md_module()
        markdown = module.extract_pdf_to_md(str(pdf_path))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        converted = True

    return {
        "converted": converted,
        "dry_run": dry_run,
        "input_path": pdf_path.relative_to(REPO_ROOT).as_posix(),
        "output_path": output_path.relative_to(REPO_ROOT).as_posix(),
        "script_used": PDF_TO_MD_SCRIPT,
        "warnings": warnings,
        "next_action": (
            "Run again with dry_run=false after confirming the output path."
            if dry_run
            else "Review extracted Markdown as a machine-readable copy, not as digest or analysis."
        ),
    }
