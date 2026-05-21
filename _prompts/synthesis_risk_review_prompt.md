# Synthesis Risk Review Prompt

You are reviewing a synthesis draft for overclaim risks.

Use only the provided:

- synthesis draft
- claim ledger
- rule anchor map
- evidence manifest

Do not add new conclusions.

Check for:

- overgeneralization;
- unsupported normativity;
- paper views misrepresented as court rules;
- ordinary cases misrepresented as rule anchors;
- missing contrary evidence;
- unclear source tracing;
- excessive language strength;
- missing “待核验” markers.

Output using `_templates/synthesis_risk_review_template.md`.

For each issue, recommend:

- keep
- revise
- downgrade
- reject
- pending human verification

Do not resolve the legal judgment yourself. Human review is required.
