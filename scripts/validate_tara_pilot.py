#!/usr/bin/env python3
"""Validate TARA pilot structure and review gates.

This script checks workflow quality only. It does not evaluate legal accuracy,
does not call an LLM, and does not modify files.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


REQUIRED_CASE_FILES = [
    "01_source_atoms.md",
    "02_fact_atoms.md",
    "03_evidence_atoms.md",
    "04_factor_atoms.md",
    "05_decision_packets.md",
    "06_quality_review.md",
    "07_assembly_notes.md",
]

DECISION_FIELD_GROUPS = {
    "decision_id": ["decision_id", "判断编号"],
    "issue": ["对应争点"],
    "preliminary_judgment": ["初步判断"],
    "supporting_facts": ["supporting_facts", "支持事实"],
    "supporting_factors": ["supporting_factors", "支持因素"],
    "supporting_evidence": ["supporting_evidence", "支持证据"],
    "counter_evidence_or_limits": [
        "counter_evidence_or_limits",
        "反向证据",
        "限制因素",
    ],
    "uncertainty": ["uncertainty", "不确定性"],
    "data_gap": ["data_gap", "数据缺口"],
    "allowed_claim": ["allowed_claim", "允许表述"],
    "forbidden_claim": ["forbidden_claim", "禁止表述"],
    "next_action": ["next_action", "下一步动作"],
    "human_review_status": ["human_review_status", "人工复核状态"],
}

QUALITY_FIELD_GROUPS = {
    "traceability": ["traceability", "可追溯性"],
    "authority_fit": ["authority_fit", "权威匹配"],
    "boundary_safety": ["boundary_safety", "边界安全"],
    "issue_coverage": ["issue_coverage", "问题覆盖"],
    "counter_evidence_awareness": ["counter_evidence_awareness", "反向材料意识"],
    "reusability": ["reusability", "可复用性"],
    "human_review_readiness": ["human_review_readiness", "人工复核友好"],
}

QUALITY_STATUS_TERMS = ["pass", "minor_gap", "major_gap", "blocked"]

RISK_TERMS = [
    "必然",
    "显然",
    "确定",
    "一定",
    "已经证明",
    "足以证明",
    "当然适用",
    "直接推出",
    "无需进一步核验",
    "最终结论",
]

PENDING_TERMS = [
    "待核验",
    "需回查原文",
    "待补原文摘录",
    "当前仅基于",
    "尚未回查",
]


@dataclass
class CaseReport:
    name: str
    structure_ok: bool = True
    missing_files: list[str] = field(default_factory=list)
    decision_ok: bool = True
    missing_decision_fields: list[str] = field(default_factory=list)
    quality_ok: bool = True
    missing_quality_fields: list[str] = field(default_factory=list)
    quality_status_ok: bool = True
    risk_hits: list[str] = field(default_factory=list)
    pending_hits: list[str] = field(default_factory=list)

    @property
    def has_failures(self) -> bool:
        return not (
            self.structure_ok
            and self.decision_ok
            and self.quality_ok
            and self.quality_status_ok
        )

    @property
    def has_warnings(self) -> bool:
        return bool(self.risk_hits or self.pending_hits)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def contains_any(text: str, terms: Iterable[str]) -> bool:
    text_lower = text.lower()
    return any(term.lower() in text_lower for term in terms)


def find_missing_fields(text: str, field_groups: dict[str, list[str]]) -> list[str]:
    return [
        field_name
        for field_name, terms in field_groups.items()
        if not contains_any(text, terms)
    ]


def collect_term_hits(case_dir: Path, terms: list[str]) -> list[str]:
    hits: list[str] = []
    for path in sorted(case_dir.glob("*.md")):
        text = read_text(path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for term in terms:
                if term in line:
                    hits.append(f"{path.name}:{line_number}: {term}")
    return hits


def validate_case(case_dir: Path) -> CaseReport:
    report = CaseReport(name=case_dir.name)

    for file_name in REQUIRED_CASE_FILES:
        if not (case_dir / file_name).is_file():
            report.structure_ok = False
            report.missing_files.append(file_name)

    decision_path = case_dir / "05_decision_packets.md"
    if decision_path.is_file():
        decision_text = read_text(decision_path)
        report.missing_decision_fields = find_missing_fields(
            decision_text, DECISION_FIELD_GROUPS
        )
        report.decision_ok = not report.missing_decision_fields
    else:
        report.decision_ok = False
        report.missing_decision_fields = list(DECISION_FIELD_GROUPS)

    quality_path = case_dir / "06_quality_review.md"
    if quality_path.is_file():
        quality_text = read_text(quality_path)
        report.missing_quality_fields = find_missing_fields(
            quality_text, QUALITY_FIELD_GROUPS
        )
        report.quality_ok = not report.missing_quality_fields
        report.quality_status_ok = contains_any(quality_text, QUALITY_STATUS_TERMS)
    else:
        report.quality_ok = False
        report.quality_status_ok = False
        report.missing_quality_fields = list(QUALITY_FIELD_GROUPS)

    report.risk_hits = collect_term_hits(case_dir, RISK_TERMS)
    report.pending_hits = collect_term_hits(case_dir, PENDING_TERMS)
    return report


def discover_cases(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and path.name.startswith("PD-PILOT-"))


def print_case_report(report: CaseReport) -> None:
    print(report.name)
    print(f"- Structure: {'PASS' if report.structure_ok else 'FAIL'}")
    if report.missing_files:
        for file_name in report.missing_files:
            print(f"  - missing: {file_name}")

    print(f"- Decision packet required fields: {'PASS' if report.decision_ok else 'FAIL'}")
    if report.missing_decision_fields:
        for field_name in report.missing_decision_fields:
            print(f"  - missing field: {field_name}")

    quality_status = "PASS" if report.quality_ok and report.quality_status_ok else "FAIL"
    print(f"- Quality review: {quality_status}")
    if report.missing_quality_fields:
        for field_name in report.missing_quality_fields:
            print(f"  - missing quality item: {field_name}")
    if not report.quality_status_ok:
        print("  - missing quality status marker: pass / minor_gap / major_gap / blocked")

    if report.risk_hits:
        print("- Risk terms: WARNING")
        for hit in report.risk_hits:
            print(f"  - {hit}")
    else:
        print("- Risk terms: PASS")

    if report.pending_hits:
        print("- Pending verification markers: WARNING")
        for hit in report.pending_hits:
            print(f"  - {hit}")
    else:
        print("- Pending verification markers: PASS")

    print()


def overall_verdict(reports: list[CaseReport]) -> str:
    if not reports or any(report.has_failures for report in reports):
        return "FAIL"
    if any(report.has_warnings for report in reports):
        return "PASS_WITH_WARNINGS"
    return "PASS"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate TARA pilot files.")
    parser.add_argument(
        "--root",
        default="2_framework/tara_pilot",
        help="TARA pilot root directory. Defaults to 2_framework/tara_pilot.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    cases = discover_cases(root)
    reports = [validate_case(case_dir) for case_dir in cases]
    verdict = overall_verdict(reports)

    print("TARA Pilot Validation Report")
    print()
    print(f"Root: {root}")
    print(f"Checked cases: {len(reports)}")
    print()

    if not root.exists():
        print(f"FAIL: root directory does not exist: {root}")
    elif not reports:
        print("FAIL: no PD-PILOT-* case directories found.")
    else:
        for report in reports:
            print_case_report(report)

    print(f"Overall verdict: {verdict}")
    return 1 if verdict == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
