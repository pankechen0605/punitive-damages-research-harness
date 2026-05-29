# Quality Review：PD-PILOT-001 张某山等 32 人非法采矿案

## 质量审查结论

总体状态：`minor_gap`

本案可以作为 TARA 方法试跑样本，但不能进入 final synthesis。主要原因是：已能形成 atoms 和 decision packets，但原文证据摘录、金额计算、规则卡和人工复核仍不完整。

## 1. traceability

状态：`major_gap`

原因：

- 已绑定 case card 和 raw source。
- 已登记少量 raw 定位。
- 但金额、分担比例、评估方法和故意认定完整说理仍未逐条摘录核验。

处理：

- 允许作为方法试跑。
- 不允许作为 final legal conclusion。

## 2. authority_fit

状态：`major_gap`

原因：

- 本案来源角色为 ordinary_case / judgment。
- `1_digest/rule_cards` 当前没有可引用规则卡。
- 规则线索只能作为 pending_backfill，不能作为 rule anchor。

处理：进入 synthesis 前必须补 rule card 或明确保留为 observation。

## 3. boundary_safety

状态：`pass`

原因：

- 判断包明确区分 allowed_claim 和 forbidden_claim。
- 未将个案观察升格为一般裁判规则。
- 明确写明本案不得作为 final synthesis。

## 4. issue_coverage

状态：`minor_gap`

原因：

- 已覆盖主观故意、损害后果、赔偿基数、赔偿表达和刑民交叉。
- 被告抗辩、评估方法和全部责任分配仍缺。

## 5. counter_evidence_awareness

状态：`minor_gap`

原因：

- 每个 decision packet 均列出限制因素。
- 但反向证据主要表现为缺口，而非完整反向材料。

## 6. reusability

状态：`pass`

原因：

- atoms 和 packets 均使用可迁移字段。
- 本案具体结论未写入模板。

## 7. human_review_readiness

状态：`pass`

原因：

- 每个判断包都列出 data_gap、next_action 和 human_review_status。
- 人工可以快速识别应补原文、规则卡和金额计算材料。

## Pilot verdict

本案适合保留为 TARA pilot。进入后续横向比较时，只能使用已标明边界的观察字段；进入最终规则总结前，必须补原文摘录、rule card 和人工复核。
