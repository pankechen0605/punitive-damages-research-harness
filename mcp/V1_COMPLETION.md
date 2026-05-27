# MCP v1 Completion Note

MCP v1 is the first stable local integration surface for this legal research
harness.

## Included

- Read-only context exposure for fixed repository docs, templates, and prompts.
- Prompt wrappers with repository safety boundaries.
- Controlled template skeleton creation.
- Workflow log append support.
- Heuristic layer and claim validation.
- PDF-to-Markdown extraction wrapper with dry-run-first behavior.
- Smoke tests and usage documentation.

## Intentionally Excluded

- Automatic legal conclusion generation.
- Autonomous case search.
- Automatic final report generation.
- Web search.
- LLM API calls.
- Writing to `0_raw` except mechanical extracted Markdown under
  `0_raw/extracted_md/`.
- Replacement of human review.

## v1 Operating Rule

MCP v1 helps clients stay inside the harness workflow. It is not an autonomous
research agent and does not decide legal correctness.
