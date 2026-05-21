# Repo Architecture Review

## Purpose

This review checks whether the public `punitive-damages-research-harness` repository consistently describes the same reusable legal research workflow across README, AGENTS, docs, templates, and prompts.

This is a documentation-only architecture review. It does not add legal conclusions, legal materials, cases, statutes, papers, authors, or court views.

## Source-of-Truth Files

| Role | File |
|---|---|
| Agent rules | `AGENTS.md` |
| User-facing overview | `README.md` |
| Canonical workflow | `docs/canonical-operating-flow.md` |
| Layer contracts | `docs/layer-contracts.md` |
| Synthesis/output boundary | `docs/synthesis-output-guide.md` |
| Step 9 human review workflow | `docs/synthesis-human-review-workflow.md` |
| Claim taxonomy | `docs/claim-taxonomy-and-elevation-rules.md` |
| Synthesis templates | `_templates/synthesis_*`, `_templates/claim_ledger_template.md`, `_templates/rule_anchor_map_template.md`, `_templates/human_legal_judgment_memo_template.md`, `_templates/final_doc_template.md` |
| Synthesis prompts | `_prompts/synthesis_*`, `_prompts/rule_anchor_mapping_prompt.md`, `_prompts/final_document_assembly_prompt.md` |

## Consistency Audit Table

| Checked Area | Finding | Minimal Fix |
|---|---|---|
| README workflow numbering | README used a 9-step flow and collapsed horizontal comparison with rule summary. | Updated README to the 10-step canonical workflow. |
| AGENTS rules | AGENTS described synthesis and output but collapsed “horizontal comparison and rule summary” in the default flow. | Updated AGENTS default flow to separate Step 8, Step 9, and Step 10. |
| `docs/canonical-operating-flow.md` | The file had correct substance but used 0-9 section numbering, making Step 8/9/10 ambiguous. | Renumbered sections to the 10-step canonical workflow and clarified Step 9 vs Step 10. |
| `docs/layer-contracts.md` | 3_synthesis owned comparison and summary, but human sign-off and output non-modification needed to be explicit. | Added human-in-the-loop final conclusion condition and output prohibition against strengthening/weakening conclusions. |
| `docs/synthesis-output-guide.md` | Boundary was mostly correct but did not explicitly say output cannot soften conclusions. | Added explicit “synthesis decides; output presents” boundary including no strengthening, softening, inventing, or rewriting. |
| `docs/synthesis-human-review-workflow.md` | No issue found. It already documents Step 9 as human-in-the-loop. | No change. |
| `docs/claim-taxonomy-and-elevation-rules.md` | No issue found. It distinguishes observation, tentative pattern, rule anchor, and final legal conclusion. | No change. |
| Synthesis templates | `final_doc_template.md` contained legacy PPT-oriented structure. Other synthesis templates were aligned. | Updated `final_doc_template.md` to final synthesis report structure with human sign-off and traceability. |
| Synthesis prompts | `synthesis_review_prompt.md` used older “pre material” review language. Other prompts were aligned. | Updated `synthesis_review_prompt.md` to check Step 9 claim taxonomy, human sign-off, and output-contamination risks. |

## Checked Areas

### README Workflow Numbering

README now separates:

1. activate topic config
2. `0_raw` collect materials
3. `1_digest` single-source digestion
4. `2_framework` design adjudication factors and weighting model
5. pilot run
6. framework v1 lock
7. batch case cards
8. `3_synthesis/cross_case_comparison` horizontal comparison
9. `3_synthesis/rule_summary + final_doc` human-in-the-loop rule summary / final document
10. `4_output` presentation adaptation

### AGENTS Rules

AGENTS now directs agents to treat Step 9 as synthesis and Step 10 as output adaptation only.

### Canonical Operating Flow

The canonical flow now uses the same 10-step sequence and keeps Step 8, Step 9, and Step 10 distinct.

### Layer Contracts

`3_synthesis` owns cross-case comparison, rule summary, and final analytical document. `4_output` owns presentation adaptation only.

### Synthesis / Output Boundary

`4_output` cannot create, strengthen, soften, or modify synthesis-layer conclusions.

### Step 9 Human Review

Step 9 remains AI-assisted but human-validated. Final legal conclusions require human sign-off.

### Templates and Prompts

Templates and prompts now align around:

- use only provided materials;
- distinguish case observation / tentative pattern / rule anchor / final legal conclusion;
- mark uncertainty as “待核验”;
- no final legal conclusion without human sign-off;
- no output-layer strengthening of synthesis-layer conclusions.

## Recommended Minimal Fixes Completed

- Updated README workflow to 10 steps.
- Updated AGENTS default workflow.
- Renumbered canonical operating flow.
- Clarified layer contracts.
- Clarified synthesis/output boundary.
- Updated `final_doc_template.md`.
- Updated `synthesis_review_prompt.md`.

## Remaining Notes

- No substantive legal content was added.
- No new cases, statutes, papers, court views, or legal conclusions were created.
- Future changes should keep Step 9 inside `3_synthesis` and Step 10 inside `4_output`.
