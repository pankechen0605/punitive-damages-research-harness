# Synthesis Human Review Workflow

第 9 步不是“AI 自动总结规则”，而是：

```text
AI-assisted synthesis, human-validated legal conclusion workflow
```

AI 可以辅助归纳、提示风险、整理证据链；人负责判断哪些内容能被提升为法律结论。

## 目的

第 9 步的目标是把已经完成的 case cards、rule cards、paper cards、framework v1 和横向比较结果，转化为可审查、可回溯、可降级的 synthesis 产物。

它不是完全自动化的规则生成步骤。

AI 的定位是：

```text
synthesis assistant
```

不是：

```text
legal conclusion author
```

## AI 可以做什么

- 从 case cards / rule cards / paper cards 中抽取共同因素。
- 生成横向比较草稿。
- 生成 case observations。
- 生成 tentative patterns，并标记样本范围。
- 生成 claim ledger / proposition list。
- 检查来源链条。
- 标记过度概括风险。
- 提示反向材料或缺失材料。
- 生成最终文档结构草稿。

## 人必须判断什么

- 某个观察是否能上升为裁判规律。
- 普通案例是否具有代表性。
- 不同法院、不同层级案例的研究权重。
- 论文观点是否只能作为学术解释。
- 某个 rule anchor 是否足以支撑结论。
- 反例是否足以削弱初步结论。
- 最终法律结论的表述强度。
- 哪些内容可以对外展示。

## 9.0 Evidence Freeze

### 输入

- 已完成的 case cards
- rule cards
- paper cards
- 横向比较表
- framework v1

### 输出

- `synthesis_evidence_manifest.md`

### AI 可做

- 列出可用材料。
- 生成材料索引。
- 检查缺失字段。

### 禁止事项

- 不得新增案例、法条、论文。
- 不得从记忆或常识补充材料。
- 不得使用未列入 evidence manifest 的材料。

### 人工检查点

- 人确认 evidence manifest 是否完整。
- 人确认是否有材料需要排除或标记待核验。

## 9.1 Claim Extraction

### 输入

- evidence manifest
- case cards
- rule cards
- paper cards
- 横向比较表

### 输出

- `claim_ledger.md`

### AI 可做

- 抽取候选命题。
- 标注来源。
- 标注 claim 类型。
- 标注支持材料和反向材料。

### 禁止事项

- 不得把 claim 直接写成 final conclusion。
- 不得省略来源。
- 不得把论文观点写成法院规则。

### 人工检查点

- 人审查每条 claim 的来源是否真实。
- 人判断是否存在过度表述。

## 9.2 Pattern Drafting

### 输入

- claim ledger
- framework v1
- factor weighting model

### 输出

- `synthesis_pattern_draft.md`

### AI 可做

- 按观察要素组织初步模式。
- 提示高频因素。
- 列出差异和例外。

### 禁止事项

- 不得使用“法院规则是”“司法实践已经确立”等强规范表述。
- 不得省略样本范围。
- 不得忽略反向材料。

### 人工检查点

- 人判断哪些 pattern 可以保留。
- 人判断哪些只是样本噪音。

## 9.3 Rule Anchor Mapping

### 输入

- claim ledger
- rule cards
- case cards
- paper cards

### 输出

- `rule_anchor_map.md`

### AI 可做

- 为每个 pattern 寻找对应 rule card 或 authoritative case rule anchor。
- 标记 anchor 支持什么、不支持什么。
- 标记适用范围限制。

### 禁止事项

- 不得把普通案例直接映射成 rule anchor。
- 不得把论文观点直接映射成 rule anchor。
- 不得创造新的 rule anchor。

### 人工检查点

- 人判断 rule anchor 是否足以支撑后续结论。

## 9.4 Risk & Overclaim Review

### 输入

- pattern draft
- claim ledger
- rule anchor map

### 输出

- `synthesis_risk_review.md`

### AI 可做

- 标记过度概括。
- 标记证据不足。
- 标记来源错配。
- 标记论文观点和法院规则混淆。
- 标记强语言风险。

### 禁止事项

- 不得在风险审查中新增结论来“修补”原结论。
- 不得用风险审查替代人工判断。

### 人工检查点

- 人决定是否降级、删除、改写相关 claim。

## 9.5 Human Legal Judgment Lock

### 输入

- claim ledger
- pattern draft
- rule anchor map
- risk review

### 输出

- `human_legal_judgment_memo.md`

### AI 可做

- 提供整理后的备选结论。
- 提供风险提示。
- 提供表达强度建议。

### 禁止事项

- AI 不得自行把 tentative pattern 提升为 final legal conclusion。
- AI 不得替人签署 legal judgment。

### 人工检查点

人逐条决定：

- keep as observation
- keep as tentative pattern
- upgrade to legal conclusion
- reject / mark pending verification

没有 human decision 的内容，不得进入 final legal conclusion。

## 9.6 Final Document Assembly

### 输入

- human legal judgment memo
- claim ledger
- rule anchor map

### 输出

- `final_synthesis_report.md`

### AI 可做

- 改写结构。
- 润色表达。
- 生成摘要。
- 调整展示顺序。

### 禁止事项

- 不得新增结论。
- 不得强化结论语言。
- 不得删除限制条件。
- 不得让 output 层表达反向污染 synthesis 判断。

### 人工检查点

- 人最终通读。
- 人确认 final report 只包含 human-confirmed conclusions。

## 核心闸门

```text
AI may draft → AI may not conclude
Human may elevate → Human must sign off
Output may present → Output may not create new synthesis
```
