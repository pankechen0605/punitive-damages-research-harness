from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


MCP_DIR = Path(__file__).resolve().parent
if str(MCP_DIR) not in sys.path:
    sys.path.insert(0, str(MCP_DIR))

from config import SERVER_NAME
from prompts.registry import get_prompt_entries, render_prompt
from resources.registry import get_resource_entries, read_resource
from schemas import TargetStep
from tools.status import (
    check_step_prerequisites as check_step_prerequisites_impl,
    get_project_status as get_project_status_impl,
    list_harness_assets as list_harness_assets_impl,
)
from tools.write import (
    append_workflow_log as append_workflow_log_impl,
    create_from_template as create_from_template_impl,
)


def _load_fastmcp() -> Any:
    try:
        from mcp.server.fastmcp import FastMCP
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "The official Python MCP SDK is not installed. Install it with "
            "`pip install mcp`, then run `python mcp/server.py`."
        ) from exc
    return FastMCP


def create_server() -> Any:
    FastMCP = _load_fastmcp()
    app = FastMCP(SERVER_NAME)

    for entry in get_resource_entries():

        def make_resource_reader(path: str):
            def resource_reader() -> str:
                return read_resource(path)

            resource_reader.__name__ = (
                "read_" + path.replace("/", "_").replace(".", "_").replace("-", "_")
            )
            return resource_reader

        app.resource(entry.uri)(make_resource_reader(entry.path))

    for entry in get_prompt_entries():

        def make_prompt_renderer(name: str):
            def prompt_renderer() -> str:
                return render_prompt(name)

            prompt_renderer.__name__ = name
            return prompt_renderer

        app.prompt()(make_prompt_renderer(entry.name))

    @app.tool()
    def get_project_status() -> dict[str, Any]:
        """Return deterministic read-only status for the legal research harness."""

        return get_project_status_impl()

    @app.tool()
    def check_step_prerequisites(target_step: TargetStep) -> dict[str, Any]:
        """Check whether a workflow step may proceed under harness guardrails."""

        return check_step_prerequisites_impl(target_step)

    @app.tool()
    def list_harness_assets() -> dict[str, Any]:
        """List repository docs, templates, prompts, and scripts exposed to clients."""

        return list_harness_assets_impl()

    @app.tool()
    def create_from_template(
        template_name: str,
        target_layer: str,
        target_relative_path: str,
        title: str | None = None,
        source_id: str | None = None,
        overwrite: bool = False,
    ) -> dict[str, Any]:
        """Create a controlled template skeleton in an allowed research layer."""

        return create_from_template_impl(
            template_name=template_name,
            target_layer=target_layer,
            target_relative_path=target_relative_path,
            title=title,
            source_id=source_id,
            overwrite=overwrite,
        )

    @app.tool()
    def append_workflow_log(
        action: str,
        target: str,
        summary: str,
        warnings: list[str] | None = None,
    ) -> dict[str, Any]:
        """Append a short structured entry to _logs/workflow-log.md."""

        return append_workflow_log_impl(
            action=action,
            target=target,
            summary=summary,
            warnings=warnings,
        )

    return app


def main() -> None:
    create_server().run()


if __name__ == "__main__":
    main()
