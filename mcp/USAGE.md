# MCP v1 Integration Guide

This MCP server is a local-first legal research workflow controller for this
repository. It helps MCP clients work inside the repository's fixed material
boundaries and workflow stages.

## What It Is

The server helps clients:

- Read project workflow rules, templates, prompts, and documentation.
- Access fixed prompt templates without searching outside the repository.
- Create template skeleton files in controlled research layers.
- Append short workflow log entries.
- Validate likely layer-boundary and claim-support problems.
- Run mechanical PDF-to-Markdown extraction for PDFs under `0_raw/`.

The server does not:

- Generate final legal conclusions.
- Replace human legal review.
- Search the web.
- Call LLM APIs.
- Fabricate cases, courts, statutes, papers, authors, or outcomes.
- Write AI summaries into `0_raw`.
- Automatically produce final reports.

## Run Locally

Install the official Python MCP SDK:

```powershell
pip install mcp
```

Start the server from the repository root:

```powershell
python mcp/server.py
```

Use this file-path command rather than `python -m mcp.server`; the local
`mcp/` directory is intentionally not a Python package.

## MCP Client Configuration

Replace the `cwd` and `args` path with your local checkout path:

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

## Recommended Flow

1. Run `get_project_status`.
2. Read the relevant resources and prompt wrappers.
3. Use `create_from_template` for a skeleton in an allowed layer.
4. Fill drafts only from user-provided or repository-provided materials.
5. Run `validate_digest_card` or `validate_layer_boundary`.
6. Use `append_workflow_log` for a short workflow note.
7. For PDFs, run `run_pdf_to_md` with `dry_run=true` first.
8. Keep human review before synthesis, final conclusions, or output adaptation.

## Safety Boundaries

- `0_raw` remains the source layer. Extracted Markdown is mechanical and not
  authoritative.
- `1_digest` is single-source digestion only.
- `2_framework` is for observation factors, weighting, derived fields, and
  methodology.
- `3_synthesis` is where cross-source comparison and synthesis happen.
- `4_output` adapts confirmed synthesis for presentation and must not introduce
  new legal conclusions.
- Validators are heuristic review aids, not legal correctness engines.
- Uncertain legal content should remain marked as `待核验`.
