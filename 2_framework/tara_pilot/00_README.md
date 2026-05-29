# TARA 双案例试跑

## 定位

本目录用于验证“可追溯法律研究组装框架 v0.1”是否能应用于既有案例卡。它不是新一轮实体研究成果，也不是最终横向规则总结。

本轮只选取两个已经完成 digest / pilot 的案例：

- `PD-PILOT-001-zhang-32-illegal-mining`
- `PD-PILOT-002-chen-guizhou-cultural-relic`

## 试跑链路

```text
既有 case card / raw source
→ source atom
→ fact atom
→ evidence atom
→ factor atom
→ decision packet
→ quality review
→ assembly notes
```

## 阅读顺序

每个 pilot case 的推荐阅读顺序为：

```text
01_source_atoms
→ 02_fact_atoms
→ 03_evidence_atoms
→ 04_factor_atoms
→ 05_decision_packets
→ 06_quality_review
→ 07_assembly_notes
```

## 使用边界

- 本目录中的判断包均为方法论 pilot 材料。
- 本目录不得作为 final synthesis 或最终法律结论使用。
- 所有法律判断仍需人工复核。
- 未回查到原文或未完成 rule card 的内容必须保留“待核验”或“需补材料”。

## PR2 不做

- 不修改 `0_raw`。
- 不重写已有 case cards。
- 不做全量案例迁移。
- 不新增最终法律结论。
- 不修改 MCP 或 scripts。
- 不迁移 Temu/PDD 主题。
