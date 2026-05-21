# Synthesis Delta Review Prompt

You are comparing a newly verified case card against existing synthesis.

Use only:

- the new verified case card;
- existing cross-case comparison;
- existing claim ledger, if provided;
- existing rule summary / final_doc, if provided;
- current factor model and weighting model.

Do not rewrite final conclusions.
Do not add legal conclusions.
Do not update output-layer documents.

Tasks:

1. Identify affected comparison fields.
2. Identify affected claims.
3. State whether the new case supports, contradicts, or does not affect existing synthesis.
4. Classify impact as:
   - no impact
   - minor supplement
   - contrary evidence
   - framework gap
5. Preserve scope limitations.
6. Mark uncertainty as “待核验”.
7. Require human decision before any synthesis update.

Output using `_templates/synthesis_delta_review_template.md`.
