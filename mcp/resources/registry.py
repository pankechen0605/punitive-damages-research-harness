from __future__ import annotations

from dataclasses import dataclass

from config import RESOURCE_FILES, exists, read_repo_text


@dataclass(frozen=True)
class ResourceEntry:
    uri: str
    path: str
    title: str
    mime_type: str = "text/markdown"


def _title_for(path: str) -> str:
    return path.replace("\\", "/")


def get_resource_entries() -> list[ResourceEntry]:
    return [
        ResourceEntry(
            uri=f"harness://{path.replace('\\', '/')}",
            path=path,
            title=_title_for(path),
        )
        for path in RESOURCE_FILES
        if exists(path)
    ]


def missing_resource_files() -> list[str]:
    return [path for path in RESOURCE_FILES if not exists(path)]


def read_resource(path: str) -> str:
    return read_repo_text(path)
