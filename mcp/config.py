from __future__ import annotations

from pathlib import Path


SERVER_NAME = "legal-research-harness"
REPO_ROOT = Path(__file__).resolve().parents[1]

RESOURCE_FILES = [
    "README.md",
    "AGENTS.md",
    "00_START_HERE.md",
    "current_topic_config.md",
    "docs/canonical-operating-flow.md",
    "docs/layer-contracts.md",
    "docs/material-routing-rules.md",
    "docs/raw-layer-guide.md",
    "docs/digest-layer-guide.md",
    "docs/framework-layer-guide.md",
    "docs/synthesis-output-guide.md",
    "docs/human-review-checkpoints.md",
    "docs/claim-taxonomy-and-elevation-rules.md",
    "docs/incremental-case-intake-workflow.md",
    "_templates/case_card_template.md",
    "_templates/rule_card_template.md",
    "_templates/paper_card_template.md",
    "_templates/cross_case_comparison_template.md",
    "_templates/final_doc_template.md",
    "_prompts/activate_topic_config_prompt.md",
    "_prompts/mimo_case_digest_prompt.md",
    "_prompts/mimo_case_review_prompt.md",
    "_prompts/rule_anchor_mapping_prompt.md",
    "_prompts/synthesis_draft_prompt.md",
    "_prompts/synthesis_review_prompt.md",
    "_prompts/final_document_assembly_prompt.md",
]

PROMPT_FILES = {
    "activate_topic_config": "_prompts/activate_topic_config_prompt.md",
    "case_digest": "_prompts/mimo_case_digest_prompt.md",
    "case_review": "_prompts/mimo_case_review_prompt.md",
    "rule_anchor_mapping": "_prompts/rule_anchor_mapping_prompt.md",
    "synthesis_draft": "_prompts/synthesis_draft_prompt.md",
    "synthesis_review": "_prompts/synthesis_review_prompt.md",
    "final_document_assembly": "_prompts/final_document_assembly_prompt.md",
}

TEMPLATE_FILES = {
    "case_card_template.md": "_templates/case_card_template.md",
    "rule_card_template.md": "_templates/rule_card_template.md",
    "paper_card_template.md": "_templates/paper_card_template.md",
    "cross_case_comparison_template.md": "_templates/cross_case_comparison_template.md",
    "final_doc_template.md": "_templates/final_doc_template.md",
    "adjudication_factor_model_template.md": "_templates/adjudication_factor_model_template.md",
    "factor_weighting_model_template.md": "_templates/factor_weighting_model_template.md",
    "derived_case_fields_template.md": "_templates/derived_case_fields_template.md",
    "rule_anchor_map_template.md": "_templates/rule_anchor_map_template.md",
    "claim_ledger_template.md": "_templates/claim_ledger_template.md",
    "synthesis_draft_template.md": "_templates/synthesis_draft_template.md",
    "synthesis_evidence_manifest_template.md": "_templates/synthesis_evidence_manifest_template.md",
    "synthesis_risk_review_template.md": "_templates/synthesis_risk_review_template.md",
    "human_legal_judgment_memo_template.md": "_templates/human_legal_judgment_memo_template.md",
    "article_spine_template.md": "_templates/article_spine_template.md",
    "section_blueprint_template.md": "_templates/section_blueprint_template.md",
    "legal_writing_rationale_matrix_template.md": "_templates/legal_writing_rationale_matrix_template.md",
    "normative_backfill_review_template.md": "_templates/normative_backfill_review_template.md",
    "topic_config_template.md": "_templates/topic_config_template.md",
}

ALLOWED_WRITE_LAYERS = {
    "1_digest",
    "2_framework",
    "3_synthesis",
    "4_output",
}

LAYER_DIRS = {
    "raw": "0_raw",
    "digest": "1_digest",
    "framework": "2_framework",
    "synthesis": "3_synthesis",
    "output": "4_output",
}

IMPORTANT_FILES = {
    "root_topic_config": "current_topic_config.md",
    "framework_topic_config": "2_framework/field_design/current_topic_config.md",
    "pilot": "2_framework/pilot",
    "framework_lock": "2_framework/framework_v1_lock.md",
}


class PathSafetyError(ValueError):
    """Raised when a requested path would escape the repository root."""


def safe_resolve(relative_path: str) -> Path:
    path = Path(relative_path)
    if path.is_absolute() or path.anchor or ".." in path.parts:
        raise PathSafetyError(f"Rejected unsafe path: {relative_path}")

    resolved = (REPO_ROOT / path).resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise PathSafetyError(f"Rejected path outside repository: {relative_path}") from exc
    return resolved


def read_repo_text(relative_path: str) -> str:
    path = safe_resolve(relative_path)
    if not path.is_file():
        raise FileNotFoundError(f"Repository file not found: {relative_path}")
    return path.read_text(encoding="utf-8")


def exists(relative_path: str) -> bool:
    return safe_resolve(relative_path).exists()


def is_dir(relative_path: str) -> bool:
    return safe_resolve(relative_path).is_dir()


def is_file(relative_path: str) -> bool:
    return safe_resolve(relative_path).is_file()
