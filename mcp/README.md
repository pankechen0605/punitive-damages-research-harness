# Legal Research Harness MCP

This directory contains a local-first MCP server for the punitive damages legal
research harness.

The server exposes repository workflow documents, templates, and prompt files as
MCP resources and prompts. It also provides deterministic status tools,
PR-MCP-2 controlled write tools, PR-MCP-3 heuristic validators, and the
PR-MCP-4 controlled PDF extraction wrapper. PR-MCP-5 closes MCP v1 with usage
documentation, a tool catalog, and an end-to-end smoke test.

## v1 Documentation

- [MCP v1 integration guide](USAGE.md)
- [MCP tool catalog](TOOL_CATALOG.md)
- [MCP v1 completion note](V1_COMPLETION.md)

## What It Does

- Registers key repository docs, templates, and prompts as read-only resources.
- Wraps existing prompt files as MCP prompts.
- Provides workflow/status tools:
  - `get_project_status`
  - `check_step_prerequisites`
  - `list_harness_assets`
- Provides controlled write tools:
  - `create_from_template`
  - `append_workflow_log`
- Provides heuristic validation tools:
  - `validate_layer_boundary`
  - `validate_digest_card`
  - `validate_synthesis_claims`
- Provides controlled extraction tools:
  - `run_pdf_to_md`
- Resolves all paths relative to the repository root.
- Rejects path traversal and paths outside the repository.

## Controlled Writes In PR-MCP-2

`create_from_template` creates template skeleton files only. It uses a fixed
allowlist of existing files under `_templates/` and may write only under:

- `1_digest/`
- `2_framework/`
- `3_synthesis/`
- `4_output/`

`append_workflow_log` appends short structured entries only to
`_logs/workflow-log.md`.

These tools do not generate legal analysis or legal conclusions. They do not
write to `0_raw/`, do not replace human review, and do not expand the research
scope.

## Validation In PR-MCP-3

The validation tools are deterministic keyword and pattern checks. They help
identify likely layer-boundary problems, unsupported synthesis claims, and
digest-card overreach.

Validators are intentionally limited:

- They do not determine legal correctness.
- They do not edit files.
- They do not auto-fix files.
- They do not generate replacement legal analysis.
- They do not replace human review.

False positives are possible. Treat validation output as a review aid for layer
discipline, source traceability, and human-review checkpoints.

## PDF Extraction In PR-MCP-4

`run_pdf_to_md` wraps the existing `scripts/pdf_to_md.py` extractor. It accepts
only relative `.pdf` inputs under `0_raw/` and writes extracted Markdown only
under `0_raw/extracted_md/`.

The tool defaults to `dry_run=true`. It refuses to overwrite existing Markdown
unless `overwrite=true`.

This tool does not modify the original PDF. It does not summarize, interpret,
create digest cards, generate legal analysis, call web services, call LLM APIs,
or execute arbitrary shell commands.

## What It Does Not Do

- It does not modify original PDFs or raw source files.
- It does not execute shell commands.
- It does not make network requests.
- It does not call LLM APIs.
- It does not search the web.
- It does not fabricate cases, statutes, papers, courts, authors, or outcomes.
- It does not generate final legal conclusions.
- It does not provide arbitrary file writes.
- It does not auto-repair research files.
- It does not convert PDFs outside the controlled `0_raw` to `0_raw/extracted_md`
  path.

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

## Smoke Checks

The smoke scripts do not require external services:

```powershell
python mcp/smoke_test.py
python mcp/smoke_v1.py
```

`smoke_test.py` covers individual guardrails. `smoke_v1.py` exercises the MCP v1
surface end to end without creating persistent research artifacts.

## Safety Boundaries

This MCP server preserves the legal research layer boundaries:

- `0_raw` remains a clean source-material layer.
- `1_digest` is single-source digestion only.
- `2_framework` designs observation factors and weighting only.
- `3_synthesis` may hold cross-case comparison and synthesis drafts.
- `4_output` is presentation/document adaptation only.

Any uncertain legal content must remain marked as `待核验`. Final legal
conclusions require human legal judgment or explicit human sign-off.
