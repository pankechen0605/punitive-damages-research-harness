# TARA 双案例试跑总结

## 文件索引

- 入口说明：`00_README.md`
- 案例选择：`01_pilot_selection.md`
- 单案阅读顺序：`01_source_atoms.md` → `02_fact_atoms.md` → `03_evidence_atoms.md` → `04_factor_atoms.md` → `05_decision_packets.md` → `06_quality_review.md` → `07_assembly_notes.md`

## 1. TARA 是否能跑通

可以跑通。两个既有案例均能从 case card 和 raw source 拆分为来源卡、事实卡、证据卡、裁判因素卡，并进一步形成判断包、质量审查和组装说明。

本轮跑通的是方法链路，不是最终法律结论：

```text
case card / raw source
→ source atom
→ fact atom
→ evidence atom
→ factor atom
→ decision packet
→ quality review
→ assembly notes
```

## 2. 最有价值的对象

最有价值的是判断包和质量审查。

判断包强制区分：

- 支持事实
- 支持因素
- 支持证据
- 反向证据或限制因素
- 不确定性
- 数据缺口
- allowed claim
- forbidden claim
- next action
- human review status

质量审查则把“能不能进入下一层”从主观感觉变成可检查状态，尤其适合暴露 traceability 和 authority fit 的缺口。

## 3. 暴露的问题

- 现有 case card 已足以支持方法试跑，但仍不能替代逐条原文核验。
- `1_digest/rule_cards` 当前没有可直接引用的 rule card，本轮只能标记 rule card gap 或 pending_backfill。
- 金额计算、倍数表达和固定金额裁量需要更多原文摘录和人工复核。
- factor atoms 与既有 adjudication factor model 可以对齐，但还需要统一字段命名。
- evidence atoms 若只摘少量 raw 定位，适合 pilot；若进入 final synthesis，需要更完整的证据摘录策略。

## 4. PR3 validator 候选字段

PR3 可考虑检查：

- decision packet 是否包含 `allowed_claim` 和 `forbidden_claim`。
- decision packet 是否包含 `uncertainty`、`data_gap`、`next_action` 和 `human_review_status`。
- fact atom 是否绑定 `source_id` 且没有写法律结论。
- evidence atom 是否区分 `supports / limits / refutes`。
- quality review 中 traceability 存在未核验材料时不得为 `pass`。
- source atom 是否明确 `not_usable_for`。
- factor atom 是否写有“不得升格为一般规则”的限制。

## 5. Temu/PDD 迁移启发

惩罚性赔偿项目适合 `case-factor mode`：

```text
case → fact → evidence → factor → decision packet
```

Temu/PDD 双支柱或平台合规项目未来应使用 `compliance-mapping mode`：

```text
source → company fact → rule → issue → decision packet → data gap checklist
```

迁移时可以复用来源卡、事实卡、规则卡、争点卡、证据卡、判断包和质量审查，但不能复用本主题的具体裁判因素、案例结论或赔偿表达。

## 6. Pilot verdict

总体状态：`minor_gap`

原因：

- 方法链路已经跑通。
- 两个案例形成了差异覆盖。
- 判断包和质量审查能有效防止个案观察升级为最终规则。
- 仍存在 rule card gap、部分证据摘录不足和人工复核缺口。

处理：

- PR2 可作为 TARA 样板间进入仓库。
- 不得将本轮判断包作为 final synthesis 使用。
- PR3 再处理 validator、字段约束和迁移指南。
