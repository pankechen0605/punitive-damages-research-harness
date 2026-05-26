# Legal Research Harness MCP

This directory contains a local-first MCP server for the punitive damages legal
research harness.

The server exposes repository workflow documents, templates, and prompt files as
read-only MCP resources and prompts. It also provides deterministic status tools
that help MCP clients respect the harness workflow.

## What It Does

- Registers key repository docs, templates, and prompts as read-only resources.
- Wraps existing prompt files as MCP prompts.
- Provides workflow/status tools:
  - `get_project_status`
  - `check_step_prerequisites`
  - `list_harness_assets`
- Resolves all paths relative to the repository root.
- Rejects path traversal and paths outside the repository.

## What It Does Not Do

- It does not write files.
- It does not modify `0_raw` or any other layer.
- It does not execute shell commands.
- It does not make network requests.
- It does not call LLM APIs.
- It does not search the web.
- It does not fabricate cases, statutes, papers, courts, authors, or outcomes.
- It does not generate final legal conclusions.

## Run Locally

Install the official Python MCP SDK in your local environment:

```powershell
pip install mcp
```

Start the server from the repository root:

```powershell
python mcp/server.py
```

The directory is intentionally not a Python package. Run the file path directly
so the local `mcp/` directory does not shadow the official SDK package.

## Connect From An MCP Client

Example local stdio configuration:

```json
{
  "mcpServers": {
    "legal-research-harness": {
      "command": "python",
      "args": ["D:/AI_Project/punitive-damages-research-harness/mcp/server.py"],
      "cwd": "D:/AI_Project/punitive-damages-research-harness"
    }
  }
}
```

Use the same command/args shape in Claude Code or another MCP client that
supports local stdio servers.

## Smoke Check

The smoke script does not require the MCP SDK. It verifies import safety,
registry file existence, status keys, and path traversal rejection:

```powershell
python mcp/smoke_test.py
```

## Safety Boundaries

This PR-MCP-1 server is read-only. It preserves the legal research layer
boundaries:

- `0_raw` remains a clean source-material layer.
- `1_digest` is single-source digestion only.
- `2_framework` designs observation factors and weighting only.
- `3_synthesis` may hold cross-case comparison and synthesis drafts.
- `4_output` is presentation/document adaptation only.

Any uncertain legal content must remain marked as `待核验`. Final legal
conclusions require human legal judgment or explicit human sign-off.
