from __future__ import annotations

from dataclasses import dataclass

from config import PROMPT_FILES, exists, read_repo_text


PROMPT_BOUNDARY = """\
Safety boundary:
- Rely only on user-provided materials and repository-provided materials.
- Do not search the web.
- Do not fabricate cases, case numbers, courts, statutes, authors, papers, or outcomes.
- Do not make final legal judgments.
- Mark uncertain legal content as 待核验.
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
