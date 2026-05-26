from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypedDict

from config import REPO_ROOT, PathSafetyError, read_repo_text, safe_resolve


Severity = Literal["error", "warning", "info"]
CardType = Literal["case_card", "rule_card", "paper_card", "auto"]
CARD_TYPES = {"case_card", "rule_card", "paper_card", "auto"}


class ValidationIssue(TypedDict):
    severity: Severity
    message: str
    evidence: str
    suggested_action: str


class LayerBoundaryResult(TypedDict):
    valid: bool
    path: str
    layer: str
    issues: list[ValidationIssue]
    warnings: list[str]
    next_action: str


class DigestCardResult(TypedDict):
    valid: bool
    path: str
    card_type: str
    issues: list[ValidationIssue]
    warnings: list[str]
    next_action: str


class SynthesisClaimsResult(TypedDict):
    valid: bool
    path: str
    issues: list[ValidationIssue]
    warnings: list[str]
    next_action: str


@dataclass(frozen=True)
class Heuristic:
    patterns: tuple[str, ...]
    severity: Severity
    message: str
    suggested_action: str


def _resolve_read_target(target_relative_path: str) -> Path:
    path = Path(target_relative_path)
    if path.is_absolute() or path.anchor or ".." in path.parts:
        raise PathSafetyError(f"Rejected unsafe path: {target_relative_path}")
    if ".git" in path.parts:
        raise PathSafetyError("Rejected .git path.")
    resolved = safe_resolve(target_relative_path)
    if not resolved.is_file():
        raise FileNotFoundError(f"Repository file not found: {target_relative_path}")
    return resolved


def _repo_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _infer_layer(relative_path: str) -> str:
    first = Path(relative_path).parts[0] if Path(relative_path).parts else ""
    if first in {"0_raw", "1_digest", "2_framework", "3_synthesis", "4_output", "_logs"}:
        return first
    return "unknown"


def _excerpt(text: str, pattern: str, limit: int = 90) -> str:
    index = text.find(pattern)
    if index < 0:
        return pattern
    start = max(0, index - 30)
    end = min(len(text), index + len(pattern) + 30)
    return " ".join(text[start:end].split())[:limit]


def _contains_any(text: str, patterns: tuple[str, ...]) -> str | None:
    for pattern in patterns:
        if pattern in text:
            return pattern
    return None


def _apply_heuristics(text: str, heuristics: list[Heuristic]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for heuristic in heuristics:
        matched = _contains_any(text, heuristic.patterns)
        if matched is None:
            continue
        issues.append(
            {
                "severity": heuristic.severity,
                "message": heuristic.message,
                "evidence": _excerpt(text, matched),
                "suggested_action": heuristic.suggested_action,
            }
        )
    return issues


def _has_reference(text: str, prefixes: tuple[str, ...]) -> bool:
    return any(prefix in text for prefix in prefixes)


def _has_any_issue(issues: list[ValidationIssue]) -> bool:
    return any(issue["severity"] in {"error", "warning"} for issue in issues)


RAW_HEURISTICS = [
    Heuristic(
        ("AI生成", "AI 生成", "模型总结", "自动摘要", "摘要如下"),
        "error",
        "0_raw appears to contain AI-generated or processed summary markers.",
        "Keep 0_raw limited to original source material or faithful machine-readable copies.",
    ),
    Heuristic(
        ("分析", "本案说明", "裁判规则", "横向比较", "综合来看", "本文认为"),
        "error",
        "0_raw appears to contain analysis, digest, or synthesis language.",
        "Move analysis to the proper digest, framework, or synthesis layer.",
    ),
    Heuristic(
        ("待核验",),
        "warning",
        "0_raw contains 待核验, which may indicate processed content.",
        "Verify this is part of the original source rather than an AI annotation.",
    ),
    Heuristic(
        ("source_id:", "case_id:", "rule_id:", "## 本案观察", "## 横向比较"),
        "warning",
        "0_raw resembles a structured digest or synthesis template.",
        "Store structured cards outside 0_raw.",
    ),
]

DIGEST_HEURISTICS = [
    Heuristic(
        ("与其他案例相比", "横向比较", "跨案例", "综合来看"),
        "error",
        "1_digest appears to contain cross-case or synthesis language.",
        "Keep digest cards limited to a single source.",
    ),
    Heuristic(
        ("司法实践通常认为", "法院一般认为", "规则是", "裁判规则是"),
        "warning",
        "1_digest appears to make a broad legal generalization.",
        "Limit the statement to the source or move synthesis to 3_synthesis.",
    ),
    Heuristic(
        ("本文认为", "最终结论", "可以得出一般规则"),
        "warning",
        "1_digest appears to contain final-report or general-rule language.",
        "Mark uncertainty or defer rule elevation to synthesis and human review.",
    ),
]

FRAMEWORK_HEURISTICS = [
    Heuristic(
        ("最终法律结论", "法院规则是", "应当认定", "已经形成规则"),
        "warning",
        "2_framework appears to contain final legal conclusions.",
        "Keep framework files focused on observation factors, weighting, and methodology.",
    ),
    Heuristic(
        ("本案应认定", "本案构成", "直接适用"),
        "warning",
        "2_framework appears to make case-specific determinations as results.",
        "Move determinations to the appropriate digest or synthesis layer with sources.",
    ),
    Heuristic(
        ("综上，", "本文认为", "最终可写为"),
        "info",
        "2_framework may contain output-ready prose.",
        "Ensure this remains methodology rather than final document text.",
    ),
]

SYNTHESIS_HEURISTICS = [
    Heuristic(
        ("必然", "显然", "当然", "一律", "均应"),
        "warning",
        "3_synthesis uses strong determinative language.",
        "Qualify the claim and ensure source support is visible.",
    ),
    Heuristic(
        ("法院规则是", "已经形成规则", "可以直接适用"),
        "warning",
        "3_synthesis appears to elevate a claim into a rule.",
        "Add rule anchors and human validation status before treating it as a legal conclusion.",
    ),
    Heuristic(
        ("学者认为法院规则", "论文认为法院规则", "学界观点即裁判规则"),
        "error",
        "Paper or academic opinion appears to be treated as a court rule.",
        "Separate scholarly interpretation from court rule anchors.",
    ),
    Heuristic(
        ("仅凭本案", "单一案例", "可以得出一般规则"),
        "warning",
        "A few-case or single-case observation may be elevated into doctrine.",
        "Keep the claim tentative unless supported by cross-case evidence and rule anchors.",
    ),
]

OUTPUT_HEURISTICS = [
    Heuristic(
        ("新增分析", "本案应认定", "新规则", "裁判规则是", "法院规则是"),
        "warning",
        "4_output appears to introduce substantive legal analysis or rule claims.",
        "Trace this content back to 3_synthesis or remove it from output adaptation.",
    ),
    Heuristic(
        ("与其他案例相比", "可以得出一般规则", "司法实践通常认为"),
        "warning",
        "4_output appears to add new comparison or synthesis language.",
        "Keep output files limited to adapting human-confirmed synthesis.",
    ),
]

CASE_CARD_HEURISTICS = [
    Heuristic(
        ("司法实践通常", "法院一般", "规则是", "可以得出一般规则"),
        "warning",
        "Case card appears to make a broad legal conclusion beyond the case.",
        "Limit the statement to this case or mark it for synthesis review.",
    ),
    Heuristic(
        ("应当认定", "与其他案例相比", "横向比较"),
        "warning",
        "Case card appears to compare cases or state a general determination.",
        "Keep case cards single-source and avoid cross-case conclusions.",
    ),
]

RULE_CARD_HEURISTICS = [
    Heuristic(
        ("学者认为", "论文认为", "作者认为"),
        "warning",
        "Rule card may mix academic opinions into rule anchors.",
        "Separate scholarly interpretation from statute, interpretation, guiding case, or typical case anchors.",
    ),
    Heuristic(
        ("一律", "均应", "必然"),
        "warning",
        "Rule card uses broad rule language that may need authority-level support.",
        "Add authority level and precise source scope.",
    ),
]

PAPER_CARD_HEURISTICS = [
    Heuristic(
        ("法院规则是", "裁判规则是", "可以直接适用"),
        "error",
        "Paper card appears to present author opinion as a court rule.",
        "Keep paper claims framed as scholarly interpretation only.",
    ),
    Heuristic(
        ("由此可得规则", "一般规则是"),
        "warning",
        "Paper card may elevate academic analysis directly into doctrine.",
        "Route rule claims through rule anchors and synthesis validation.",
    ),
]

SYNTHESIS_CLAIM_HEURISTICS = [
    Heuristic(
        ("司法实践通常认为", "法院一般认为"),
        "warning",
        "Broad synthesis language appears without guaranteed visible multi-case support.",
        "Confirm multiple case references or mark the claim as 待核验.",
    ),
    Heuristic(
        ("裁判规则是", "法院规则是"),
        "warning",
        "Rule language appears in synthesis and may need a rule anchor.",
        "Add rule_id, statute, judicial interpretation, guiding case, or human validation status.",
    ),
    Heuristic(
        ("学界认为",),
        "info",
        "Scholarly claim should have visible paper references.",
        "Confirm paper_id or source references are present.",
    ),
    Heuristic(
        ("必然", "显然", "一律", "均应"),
        "warning",
        "Strong synthesis language may overstate support.",
        "Qualify the claim or add source traceability.",
    ),
    Heuristic(
        ("已经形成规则", "可以直接适用"),
        "warning",
        "Synthesis may be making a final legal conclusion.",
        "Keep final legal conclusions human-reviewed and source anchored.",
    ),
    Heuristic(
        ("单一案例", "仅凭本案", "可以得出一般规则"),
        "warning",
        "Single-case observation may be elevated into a general claim.",
        "Downgrade to tentative pattern unless supported across sources.",
    ),
    Heuristic(
        ("计算得出", "倍数为", "比例为"),
        "info",
        "Numerical conclusion should be traceable to calculation or source evidence.",
        "Confirm calculation basis or source references are visible.",
    ),
]


def _source_reference_warning(text: str, layer: str) -> list[ValidationIssue]:
    broad_terms = ("司法实践通常认为", "法院一般认为", "裁判规则是", "法院规则是")
    references = ("source_id", "case_id", "rule_id", "paper_id", "CC-", "RC-", "PC-")
    if layer == "3_synthesis" and _contains_any(text, broad_terms) and not _has_reference(text, references):
        return [
            {
                "severity": "warning",
                "message": "Broad synthesis claim lacks visible source or rule references.",
                "evidence": _excerpt(text, _contains_any(text, broad_terms) or broad_terms[0]),
                "suggested_action": "Add source_id, case_id, rule_id, paper_id, or mark the claim as 待核验.",
            }
        ]
    return []


def _validate_text_for_layer(text: str, layer: str) -> list[ValidationIssue]:
    heuristics_by_layer = {
        "0_raw": RAW_HEURISTICS,
        "1_digest": DIGEST_HEURISTICS,
        "2_framework": FRAMEWORK_HEURISTICS,
        "3_synthesis": SYNTHESIS_HEURISTICS,
        "4_output": OUTPUT_HEURISTICS,
    }
    issues = _apply_heuristics(text, heuristics_by_layer.get(layer, []))
    issues.extend(_source_reference_warning(text, layer))
    return issues


def validate_layer_boundary(target_relative_path: str) -> LayerBoundaryResult:
    path = _resolve_read_target(target_relative_path)
    repo_path = _repo_path(path)
    layer = _infer_layer(repo_path)
    text = read_repo_text(repo_path)
    warnings: list[str] = []

    issues = _validate_text_for_layer(text, layer)

    if layer == "unknown":
        warnings.append("Path is outside recognized harness layers.")
    if layer == "_logs":
        warnings.append("Workflow logs are checked only for path safety in PR-MCP-3.")

    return {
        "valid": not _has_any_issue(issues),
        "path": repo_path,
        "layer": layer,
        "issues": issues,
        "warnings": warnings,
        "next_action": (
            "Review flagged passages; validators are heuristic and do not decide legal correctness."
            if issues
            else "No likely layer-boundary issue detected by deterministic heuristics."
        ),
    }


def _infer_card_type(repo_path: str, text: str, card_type: CardType) -> str:
    if card_type != "auto":
        return card_type
    if "case_cards" in repo_path or "case_id" in text or "本案观察" in text:
        return "case_card"
    if "rule_cards" in repo_path or "rule_id" in text or "authority" in text.lower():
        return "rule_card"
    if "paper_cards" in repo_path or "paper_id" in text or "作者" in text:
        return "paper_card"
    return "auto"


def validate_digest_card(target_relative_path: str, card_type: CardType = "auto") -> DigestCardResult:
    if card_type not in CARD_TYPES:
        raise ValueError("card_type must be one of: auto, case_card, rule_card, paper_card")
    path = _resolve_read_target(target_relative_path)
    repo_path = _repo_path(path)
    text = read_repo_text(repo_path)
    resolved_type = _infer_card_type(repo_path, text, card_type)
    warnings: list[str] = []
    issues: list[ValidationIssue] = []

    if not repo_path.startswith("1_digest/"):
        warnings.append("Digest-card validator is intended primarily for files under 1_digest/.")

    if resolved_type == "case_card":
        issues.extend(_apply_heuristics(text, CASE_CARD_HEURISTICS))
        if not _has_reference(text, ("source_id", "case_id", "案号", "案件名称", "CC-")):
            issues.append(
                {
                    "severity": "warning",
                    "message": "Case card may be missing source_id or case identifier.",
                    "evidence": "",
                    "suggested_action": "Add source_id, case_id, case name, or case number.",
                }
            )
        if "本案观察" not in text and "规则结论" in text:
            issues.append(
                {
                    "severity": "warning",
                    "message": "Case card may not distinguish case observation from rule conclusion.",
                    "evidence": _excerpt(text, "规则结论"),
                    "suggested_action": "Keep case observation separate from any rule conclusion.",
                }
            )
    elif resolved_type == "rule_card":
        issues.extend(_apply_heuristics(text, RULE_CARD_HEURISTICS))
        if not _has_reference(text, ("source_id", "rule_id", "法条", "司法解释", "指导性案例", "典型案例", "RC-")):
            issues.append(
                {
                    "severity": "error",
                    "message": "Rule card may be missing legal basis or source anchor.",
                    "evidence": "",
                    "suggested_action": "Add statute, judicial interpretation, guiding case, typical case, or source reference.",
                }
            )
        if not _has_reference(text, ("效力层级", "authority_level", "authority level", "法律", "司法解释")):
            issues.append(
                {
                    "severity": "warning",
                    "message": "Rule card may be missing authority level.",
                    "evidence": "",
                    "suggested_action": "Record the authority level and applicable scope.",
                }
            )
    elif resolved_type == "paper_card":
        issues.extend(_apply_heuristics(text, PAPER_CARD_HEURISTICS))
        if not _has_reference(text, ("author", "作者", "paper_id", "PC-", "来源", "source_id")):
            issues.append(
                {
                    "severity": "warning",
                    "message": "Paper card may be missing author or source information.",
                    "evidence": "",
                    "suggested_action": "Add author, publication/source, paper_id, or source_id.",
                }
            )
        if "论证" not in text and "证据" not in text and "argument" not in text.lower():
            issues.append(
                {
                    "severity": "info",
                    "message": "Paper card may not distinguish argument from evidence.",
                    "evidence": "",
                    "suggested_action": "Separate author argument, evidence, and limits.",
                }
            )
    else:
        warnings.append("Unable to infer card type; pass card_type explicitly for stricter checks.")

    return {
        "valid": not _has_any_issue(issues),
        "path": repo_path,
        "card_type": resolved_type,
        "issues": issues,
        "warnings": warnings,
        "next_action": (
            "Review flagged passages without generating replacement legal analysis."
            if issues
            else "No likely digest-card issue detected by deterministic heuristics."
        ),
    }


def validate_synthesis_claims(target_relative_path: str) -> SynthesisClaimsResult:
    path = _resolve_read_target(target_relative_path)
    repo_path = _repo_path(path)
    text = read_repo_text(repo_path)
    warnings: list[str] = []

    if not repo_path.startswith("3_synthesis/"):
        warnings.append("Synthesis validator is intended primarily for files under 3_synthesis/.")

    issues = _apply_heuristics(text, SYNTHESIS_CLAIM_HEURISTICS)
    issues.extend(_source_reference_warning(text, "3_synthesis"))

    if _contains_any(text, ("裁判规则是", "法院规则是")) and not _has_reference(text, ("rule_id", "RC-", "法条", "司法解释")):
        issues.append(
            {
                "severity": "warning",
                "message": "Rule claim lacks visible rule anchor.",
                "evidence": _excerpt(text, _contains_any(text, ("裁判规则是", "法院规则是")) or "裁判规则是"),
                "suggested_action": "Add a rule anchor or downgrade the claim to a tentative pattern.",
            }
        )
    if _contains_any(text, ("司法实践通常认为", "法院一般认为")) and not _has_reference(text, ("case_id", "CC-", "source_id")):
        issues.append(
            {
                "severity": "warning",
                "message": "Broad practice claim lacks visible case support.",
                "evidence": _excerpt(text, _contains_any(text, ("司法实践通常认为", "法院一般认为")) or "司法实践通常认为"),
                "suggested_action": "Add multiple case references or mark the claim as 待核验.",
            }
        )

    return {
        "valid": not _has_any_issue(issues),
        "path": repo_path,
        "issues": issues,
        "warnings": warnings,
        "next_action": (
            "Check source traceability and human-review status for flagged claims."
            if issues
            else "No likely unsupported synthesis claim detected by deterministic heuristics."
        ),
    }
