from __future__ import annotations

from dataclasses import dataclass

from config import PROMPT_FILES, exists, read_repo_text


PROMPT_BOUNDARY = """\
Safety boundary:
- Rely only on user-provided materials and repository-provided materials.
- Preserve the harness layer boundaries: 0_raw is source-only, 1_digest is single-source digestion,
  2_framework is factor and weighting design, 3_synthesis is cross-case comparison and synthesis,
  and 4_output is presentation adaptation only.
- Do not search the web.
- Do not fabricate cases, case numbers, courts, statutes, authors, papers, or outcomes.
- Do not make final legal judgments.
- Mark uncertain legal content as \u5f85\u6838\u9a8c.
"""


@dataclass(frozen=True)
class PromptEntry:
    name: str
    path: str


def get_prompt_entries() -> list[PromptEntry]:
    return [
        PromptEntry(name=name, path=path)
        for name, path in PROMPT_FILES.items()
        if exists(path)
    ]


def missing_prompt_files() -> list[str]:
    return [path for path in PROMPT_FILES.values() if not exists(path)]


def render_prompt(name: str) -> str:
    if name not in PROMPT_FILES:
        raise KeyError(f"Unknown prompt: {name}")
    prompt_text = read_repo_text(PROMPT_FILES[name])
    return f"{PROMPT_BOUNDARY}\n---\n\n{prompt_text}"
