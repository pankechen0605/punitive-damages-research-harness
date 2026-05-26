# Synthesis Human Review Workflow

第 9 步不是“AI 自动总结规则”，而是：

```text
AI-assisted synthesis, human-validated legal conclusion workflow
```

AI 可以辅助归纳、提示风险、整理证据链；人负责判断哪些内容能被提升为法律结论。

## 目的

第 9 步的目标是把已经完成的 case cards、rule cards、paper cards、framework v1 和横向比较结果，转化为可审查、可回溯、可降级的 synthesis 产物。

它不是完全自动化的规则生成步骤。

如果第 9 步之后出现新增案例，应先执行 `docs/incremental-case-intake-workflow.md`。新增案例不能直接修改 final legal conclusions；必须先生成 synthesis delta review，并经过 human decision。

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
- 必要时输出 `normative_backfill_review.md`

### AI 可做

- 为每个 pattern 寻找对应 rule card 或 authoritative case rule anchor。
- 标记 anchor 支持什么、不支持什么。
- 标记适用范围限制。

### 禁止事项

- 不得把普通案例直接映射成 rule anchor。
- 不得把论文观点直接映射成 rule anchor。
- 不得创造新的 rule anchor。
- 不得把 case card 中的法条引用直接当成 rule anchor。

### 人工检查点

- 人判断 rule anchor 是否足以支撑后续结论。
- 如果出现 anchor gap，人决定是否启动 `docs/normative-backfill-workflow.md`。

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
- 不得用文章主线需求替代规范回填。

### 人工检查点

- 人决定是否降级、删除、改写相关 claim。
- 对于规范依据不足的 claim，人决定 backfill、降级或标记待核验。

## 9.5 Article Spine Confirmation

### 输入

- evidence manifest
- claim ledger
- pattern draft
- rule anchor map
- risk review

### 输出

- `article_spine.md`

### AI 可做

- 提出 2-3 个可选文章主线。
- 说明每个主线与现有证据的匹配程度。
- 标记每个主线的过度概括风险。
- 建议哪些 cards 进入正文、附表、背景、反例或待核验。

### 禁止事项

- 不得为了形成文章主线而新增案例、法条、论文或结论。
- 不得把 tentative pattern 写成文章中心结论。
- 不得选择性隐藏反向材料或待核验材料。
- 不得让 article spine 替代后续 human legal judgment memo。

### 人工检查点

- 人确认本轮 final document 的读者面对主线。
- 人确认哪些 cards / claims 进入正文论证链。
- 人确认哪些材料只作为附表、背景、反例或待核验。

## 9.6 Section Blueprint and Writing Rationale Matrix

### 输入

- article spine
- claim ledger
- rule anchor map
- risk review

### 输出

- `section_blueprint.md`
- `legal_writing_rationale_matrix.md`

### AI 可做

- 把 article spine 转化为章节结构。
- 说明每一节的写作功能。
- 为每个写作单元绑定 claim、source/card anchor 和 human review status。
- 标记每个写作单元允许使用的表述强度。

### 禁止事项

- 不得把章节标题写成未经确认的法律结论。
- 不得让没有来源的段落进入 final document。
- 不得把 paper card 当作 court rule。
- 不得把普通案例单独提升为 rule anchor。

### 人工检查点

- 人确认章节顺序服务 article spine。
- 人确认每个写作单元都有证据边界和表述强度限制。
- 人确认可以进入 human legal judgment lock。

## 9.7 Human Legal Judgment Lock

### 输入

- article spine
- section blueprint
- legal writing rationale matrix
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
- 标记某个 claim 在文章结构中可能被说得过强的位置。

### 禁止事项

- AI 不得自行把 tentative pattern 提升为 final legal conclusion。
- AI 不得替人签署 legal judgment。
- AI 不得为了适配 article spine 而强化、软化或重写法律判断。

### 人工检查点

人逐条决定：

- keep as observation
- keep as tentative pattern
- upgrade to legal conclusion
- reject / mark pending verification

没有 human decision 的内容，不得进入 final legal conclusion。

## 9.8 Final Document Assembly

### 输入

- human legal judgment memo
- claim ledger
- rule anchor map
- article spine
- section blueprint
- legal writing rationale matrix

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
- 不得偏离 confirmed article spine。
- 不得使用 legal writing rationale matrix 未登记的核心 claim。
- 不得让 output 层表达反向污染 synthesis 判断。

### 人工检查点

- 人最终通读。
- 人确认 final report 只包含 human-confirmed conclusions。
- 人确认 final report 的文章主线没有选择性隐藏反向材料或待核验内容。

## 核心闸门

```text
AI may draft → AI may not conclude
Human may elevate → Human must sign off
Article spine may organize → Article spine may not invent
Human may lock after spine → Human judgment is not a writing convenience
Output may present → Output may not create new synthesis
```
