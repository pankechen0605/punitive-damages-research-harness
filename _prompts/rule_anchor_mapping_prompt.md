# Rule Anchor Mapping Prompt

You are mapping tentative patterns to rule anchors in `punitive-damages-research`.

Use only the provided:

- claim ledger
- rule cards
- authoritative case rule anchors
- case cards
- paper cards

Do not create new anchors.
Do not treat ordinary case observations as rule anchors by themselves.
Do not treat paper views as rule anchors.

For each pattern or claim:

1. Identify candidate rule anchors.
2. State what the anchor supports.
3. State what the anchor does not support.
4. State scope limitations.
5. Mark unsupported or unclear mappings as “待核验”.

Output using `_templates/rule_anchor_map_template.md`.
