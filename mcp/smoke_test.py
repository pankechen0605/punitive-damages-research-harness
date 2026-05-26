from __future__ import annotations

import importlib.util
from pathlib import Path

from config import PathSafetyError, safe_resolve
from resources.registry import get_resource_entries, missing_resource_files
from tools.status import get_project_status


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


def test_path_traversal_rejected() -> None:
    try:
        safe_resolve("../README.md")
    except PathSafetyError:
        return
    raise AssertionError("path traversal was not rejected")


def run() -> None:
    tests = [
        test_server_imports,
        test_resource_registry_files_exist,
        test_project_status_keys,
        test_path_traversal_rejected,
    ]
    for test in tests:
        test()
        print(f"ok - {test.__name__}")


if __name__ == "__main__":
    run()
