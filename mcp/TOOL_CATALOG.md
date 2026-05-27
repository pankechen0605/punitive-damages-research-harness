# MCP Tool Catalog

This catalog lists MCP v1 capabilities. Tools are intentionally narrow and local
to this repository.

## Resources

The server exposes selected repository files as read-only resources:

- Workflow and safety docs from `README.md`, `AGENTS.md`, `00_START_HERE.md`,
  and `docs/`.
- Templates from `_templates/`.
- Prompt templates from `_prompts/`.

Allowed effects: read-only access to fixed allowlisted repository files.

Forbidden effects: arbitrary file reads, repo-external reads, writes, web access,
or legal content generation.

## Prompts

- `activate_topic_config`: start a topic configuration workflow.
- `case_digest`: create a single-source case digest draft from provided text.
- `case_review`: review a case digest against the source.
- `rule_anchor_mapping`: map claims to rule anchors for human review.
- `synthesis_draft`: draft synthesis from approved materials.
- `synthesis_review`: review synthesis risks and support.
- `final_document_assembly`: assemble a final document from human-confirmed
  conclusions.

Allowed effects: return prompt text with safety boundaries.

Forbidden effects: web search, source invention, final legal judgment, or
unsupported synthesis.

## Read-Only Tools

### `get_project_status`

Purpose: report whether key repository layers and assets exist.

Inputs: none.

Output shape: `has_topic_config`, layer booleans, `available_templates`,
`available_prompts`, and `warnings`.

Allowed effects: read repository state.

Forbidden effects: writes, content generation, or workflow mutation.

### `check_step_prerequisites`

Purpose: check whether a requested workflow step has likely prerequisites.

Inputs: `target_step`.

Output shape: `allowed`, `missing_prerequisites`, `warnings`,
`suggested_next_action`.

Allowed effects: read-only prerequisite checks.

Forbidden effects: creating files, changing workflow state, or making legal
judgments.

### `list_harness_assets`

Purpose: list docs, templates, prompts, and scripts.

Inputs: none.

Output shape: `docs`, `templates`, `prompts`, `scripts`.

Allowed effects: read-only asset listing.

Forbidden effects: arbitrary discovery outside the repository.

## Controlled Write Tools

### `create_from_template`

Purpose: create a template skeleton in an allowed research layer.

Inputs: `template_name`, `target_layer`, `target_relative_path`, optional
`title`, optional `source_id`, optional `overwrite`.

Output shape: `created`, `path`, `template_used`, `warnings`, `next_action`.

Allowed effects: write template skeletons only under `1_digest/`,
`2_framework/`, `3_synthesis/`, or `4_output/`.

Forbidden effects: writes to `0_raw/`, arbitrary template paths, path traversal,
repo-external writes, legal analysis, or final conclusions.

### `append_workflow_log`

Purpose: append a short structured workflow note.

Inputs: `action`, `target`, `summary`, optional `warnings`.

Output shape: `appended`, `path`, `warnings`.

Allowed effects: append only to `_logs/workflow-log.md`.

Forbidden effects: modifying old entries or writing any other file.

## Validation Tools

### `validate_layer_boundary`

Purpose: flag likely layer-boundary violations.

Inputs: `target_relative_path`.

Output shape: `valid`, `path`, `layer`, `issues`, `warnings`, `next_action`.

Allowed effects: read-only heuristic validation.

Forbidden effects: legal correctness decisions, edits, or auto-repair.

### `validate_digest_card`

Purpose: flag likely digest-card overreach.

Inputs: `target_relative_path`, optional `card_type`.

Output shape: `valid`, `path`, `card_type`, `issues`, `warnings`,
`next_action`.

Allowed effects: read-only checks for case, rule, and paper cards.

Forbidden effects: replacement analysis, source invention, or rule elevation.

### `validate_synthesis_claims`

Purpose: flag likely unsupported or over-elevated synthesis claims.

Inputs: `target_relative_path`.

Output shape: `valid`, `path`, `issues`, `warnings`, `next_action`.

Allowed effects: read-only support and traceability checks.

Forbidden effects: final legal judgment or automatic rewriting.

## Mechanical Extraction Tool

### `run_pdf_to_md`

Purpose: wrap `scripts/pdf_to_md.py` for controlled PDF text extraction.

Inputs: `input_relative_path`, optional `overwrite`, optional `dry_run`.

Output shape: `converted`, `dry_run`, `input_path`, `output_path`,
`script_used`, `warnings`, `next_action`.

Allowed effects: with `dry_run=false`, write mechanical extracted Markdown under
`0_raw/extracted_md/`.

Forbidden effects: modifying original PDFs, summarizing PDFs, creating digest
cards, legal analysis, web access, LLM calls, or arbitrary command execution.
