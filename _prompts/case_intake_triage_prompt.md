# Case Intake Triage Prompt

You are triaging a submitted case for `punitive-damages-research-harness`.

Use only the submitted materials and existing project configuration provided by the user.

Do not search externally.
Do not invent missing information.
Do not decide final inclusion without human review.

Tasks:

1. Check whether the case appears within the current topic scope.
2. Check whether it may duplicate an existing source or case card.
3. Check source reliability.
4. Identify missing information.
5. Mark missing source details as “待核验”.
6. Produce a draft intake review using `_templates/case_intake_review_template.md`.

Allowed output decisions:

- accept recommendation
- reject as out_of_scope recommendation
- duplicate recommendation
- need_verify recommendation

Final intake decision requires human review.
