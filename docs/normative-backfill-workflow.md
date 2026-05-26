# Normative Backfill Workflow

本文说明当 case cards、claim ledger 或 rule anchor map 暴露出规范依据不足时，如何从案例线索回填 laws 层和 rule cards。

Normative backfill 不是流程失败。它是法律研究中正常的发现机制：先读案例，发现法院反复引用或依赖的法条、司法解释、规范性文件，再回到规范材料层补齐底本。

但 case card 中出现的法条名称或条号只能作为 backfill clue，不能直接作为 rule anchor。

## 触发条件

出现以下情况时，必须启动 normative backfill：

- case card 中反复出现某个法条、司法解释或规范性文件，但 `0_raw/laws` 中没有对应原文。
- claim ledger 中某个 claim 需要规范依据，但 rule card 不足。
- rule anchor map 中出现 `anchor gap` 或 `pending verification`。
- risk review 标记了“规范依据不足”“来源错配”或“论文观点替代法院规则”。
- article spine 或 writing rationale matrix 需要某个规范背景，但现有 rule cards 无法支撑。

## Backfill 原则

1. case card 只能提供线索，不能直接提供 rule anchor。
2. 规范材料必须回到 `0_raw/laws` 保存原文或忠实摘录。
3. 不确定名称、条号、版本、生效时间或来源时，标记“待核验”。
4. 回填后的规范材料必须生成或更新 `1_digest/rule_cards`。
5. rule card 之后应更新 `2_framework/normative_map` 或对应的 framework notes。
6. `3_synthesis/rule_anchor_map` 必须标记该 anchor 是 `initial_intake` 还是 `backfilled`。
7. 如果无法找到规范原文，只能保留为 `backfill clue pending verification`，不得进入 final legal conclusion。

## 标准流程

```text
backfill clue detected
→ normative backfill review
→ locate authoritative law source
→ preserve source in 0_raw/laws
→ update source-index
→ generate or update rule card
→ update normative map / framework notes
→ rerun rule anchor mapping
→ rerun risk review if claim strength changes
→ continue article spine / human legal judgment lock
```

## 允许来源

| Source Type | Raw Location | Can Become Rule Anchor? | Notes |
|---|---|---|---|
| 法律条文原文 | `0_raw/laws/statutes/` | yes | 需记录名称、条号、版本或来源。 |
| 司法解释原文 | `0_raw/laws/judicial_interpretations/` | yes | 需记录发布机关、生效状态和条文范围。 |
| 规范性文件原文 | `0_raw/laws/normative_documents/` | conditional | 需说明效力层级和适用范围。 |
| 权威案例裁判要点 | `0_raw/authoritative_cases/` + `1_digest/rule_cards/*.rule-anchor.md` | conditional | 只限原文已有裁判要点、典型意义或指导意义。 |
| 普通案例中的法条引用 | `1_digest/case_cards/` | no | 只能作为 backfill clue。 |
| 论文观点 | `1_digest/paper_cards/` | no | 只能作为 scholarly interpretation。 |

## Backfill Review Template

建议使用 `_templates/normative_backfill_review_template.md` 记录每次回填。

每个 review 至少回答：

- 触发来源是什么？
- case card 或 claim 里出现了什么规范线索？
- 是否已经找到规范原文？
- 原文放入 `0_raw/laws` 哪个位置？
- 是否已经更新 `source-index.md`？
- 是否已经生成或更新 rule card？
- 是否需要更新 normative map？
- rule anchor map 中的状态如何变化？

## 与第 9 步的关系

在第 9 步中，normative backfill 是暂停点，不是绕行通道。

如果 `9.3 Rule Anchor Mapping` 发现规范锚点不足，应暂停后续 `article spine` 和 `human legal judgment lock`，先完成 backfill。否则该 claim 只能保留为 observation 或 pending verification。

如果 `9.5 Article Spine Confirmation` 发现某个主线依赖尚未补齐的规范依据，应降低主线强度，或把相关部分放入待核验，不得为了文章完整性直接补写规范结论。

## 完成标准

- backfill clue 已登记。
- 规范原文已入 `0_raw/laws`，或明确标记未找到且待核验。
- `0_raw/metadata/source-index.md` 已更新。
- rule card 已生成或更新。
- normative map 或 framework notes 已说明影响。
- rule anchor map 已重新标记支持范围和 human validation status。
- risk review 已复核是否仍有过度概括风险。

## 常见错误

- 把 case card 中的法条引用直接当作规范原文。
- 只补条号，不补规范全文或来源。
- 回填后不更新 source-index。
- 回填后不生成 rule card。
- 用普通案例中的法院说理替代司法解释或法律条文。
- 为了让文章主线更完整，临时补写无法回溯的规范结论。
