# Canonical Operating Flow

本文是本项目的固定运行流程。任何 agent，包括 Codex、Claude Code、MiMo 或其他协作工具，在没有用户明确改变流程的情况下，都应按本文顺序推进。

一句话版本：

```text
1. activate topic config
→ 2. 0_raw collect materials
→ 3. 1_digest single-source digestion
→ 4. 2_framework design adjudication factors and weighting model
→ 5. pilot run
→ 6. framework v1 lock
→ 7. batch case cards
→ 8. 3_synthesis/cross_case_comparison horizontal comparison
→ 9. 3_synthesis/rule_summary + final_doc human-in-the-loop rule summary / final document
→ 10. 4_output presentation adaptation
```

## 1. Activate Topic Config

新主题启动前，先运行：

```text
_prompts/activate_topic_config_prompt.md
```

目标是生成或更新：

```text
2_framework/field_design/current_topic_config.md
```

这一阶段只回答：

- 研究什么？
- 不研究什么？
- 需要什么材料？
- 需要什么案例？
- 最终输出什么？

禁止：

- 直接写法律结论
- 直接生成观察要素
- 直接生成 case card 字段
- 直接生成横向比较表

## 2. Collect Materials：0_raw

材料先进入 `0_raw`。

这一层只放：

- 法条、司法解释、规范性文件原文
- 案例原文
- 论文 PDF
- PDF 转出的 extracted_md
- 带来源定位的原文摘录

禁止：

- 放 AI 总结
- 放 case card
- 放论文观点归纳
- 放横向比较结论

如果材料来源、类型或可信度不清楚，标记“待核验”。

## 3. Single-Source Digestion：1_digest

先把每个材料单独读薄。

输出包括：

- `case_cards`
- `rule_cards`
- `paper_cards`
- `notebook_outputs`

这一层只回答：

```text
这个单个材料说了什么？
```

禁止：

- 写“法院通常认为”
- 做横向结论
- 把论文观点写成法院规则
- 用单个普通案例概括规则

权威案例和普通案例要分流：

- 权威案例：case card + rule anchor
- 普通案例：case card only

## 4. Framework Design：2_framework

`2_framework` 是当前 topic instance 的核心。

它负责把 topic config、rule cards、paper cards、课堂约束和 pilot case 需求转化为：

- normative map
- literature debate map
- adjudication factor model
- factor weighting model
- derived case fields
- derived comparison columns

这一层回答：

```text
读案例时看什么？
优先看什么？
case card 应该有哪些字段？
横向比较表应该有哪些列？
```

禁止：

- 生成最终法律结论
- 把观察要素写成法院规则
- 凭直觉给高权重
- 没有 topic config 就生成观察要素

### Normative Sufficiency Check

进入 framework design 前，应检查当前 `0_raw/laws`、`1_digest/rule_cards` 和 `2_framework/normative_map` 是否足以支撑当前 topic config。

如果 case cards、paper cards 或 preliminary notes 暴露出规范缺口，应启动 `docs/normative-backfill-workflow.md`：

```text
case/literature clue
→ normative backfill review
→ 0_raw/laws 保存规范原文
→ 1_digest/rule_cards 生成或更新规则卡
→ 2_framework/normative_map 更新
→ 再继续 framework design
```

case card 中的法条引用只能作为 backfill clue，不能直接作为 rule anchor。

## 5. Pilot Run：2-3 个案例

不要一开始就批量生成所有 case cards。

先选 2-3 个已入库案例试跑，目标是测试：

- 观察要素能不能填写
- P0 字段是否真的能稳定观察
- case card 字段是否太多
- 横向比较列是否可操作

pilot 阶段输出：

- pilot case cards
- factor revision notes
- weighting revision notes

禁止：

- 用 pilot 案例直接概括规则
- 因少数案例强行扭曲研究问题
- 在未人工确认前锁定 P0/P1

## 6. Framework v1 Lock

pilot 后，人工决定是否锁定：

- adjudication factor model
- factor weighting model
- derived case fields
- derived comparison columns

锁定后，后续批量 case cards 按同一套字段填写。

这一阶段的目标是防止“移动靶心”。

如果发现重大问题，可以版本化修订，但不得边批量跑边随意改字段。

## 7. Batch Case Cards：1_digest/case_cards

framework v1 锁定后，再批量生成 case cards。

case card 必须：

- 对应 source
- 区分 source_category 和 research_role
- 根据 derived case fields 填写
- 保留待核验项
- 忠于单一案例

禁止：

- 补写原文没有的信息
- 把普通案例写成规则锚点
- 把 case card 写成 final doc

### Incremental Case Intake

framework v1 lock 或 synthesis 形成后新增的案例，不能直接进入批量样本或 final conclusions。

新增案例必须走：

```text
case submission
→ intake review
→ raw source preservation
→ case card generation
→ human verification
→ comparison delta
→ synthesis impact review
→ human decision
```

详见 `docs/incremental-case-intake-workflow.md`。

新增案例不得直接修改 framework lock、rule summary、final_doc 或 output documents。

## 8. Horizontal Comparison：3_synthesis/cross_case_comparison

case cards 形成后，才进入横向比较。

横向比较表的列应来自：

- adjudication factor model
- factor weighting model
- derived comparison columns

P0 要素进入主列，P1 进入辅助列，P2/P3 通常进入备注或附表。

禁止：

- 手工随意加列
- 只比较支持案例
- 从少量案例过度概括
- 忽略不支持或不涉及案例

## 9. Human-in-the-loop Rule Summary / Final Document：3_synthesis/rule_summary + 3_synthesis/final_doc

在 `3_synthesis` 中，可以开始形成：

- rule summary
- final document
- cross-case analysis

但第 9 步不是 AI 自动生成规则，而是证据层级提升流程：

```text
9.0 Evidence Freeze
→ 9.1 Claim Extraction
→ 9.2 Pattern Drafting
→ 9.3 Rule Anchor Mapping
→ 9.4 Risk & Overclaim Review
→ 9.5 Article Spine Confirmation
→ 9.6 Section Blueprint and Writing Rationale Matrix
→ 9.7 Human Legal Judgment Lock
→ 9.8 Final Document Assembly
```

详见：

- `docs/synthesis-human-review-workflow.md`
- `docs/claim-taxonomy-and-elevation-rules.md`

AI 可以整理、归类、比对、提示风险，但不能独立把 observation 或 tentative pattern 提升为 final legal conclusion。

9.1-9.4 是 synthesis 初筛，回答“材料里有哪些可说内容、证据和风险”。9.5-9.6 是写作组织，回答“这篇文章围绕哪条主线说、哪些材料进入正文论证链”。9.7 才由人结合文章主线和写作矩阵锁定最终法律判断。

如果 `9.3 Rule Anchor Mapping` 或 `9.4 Risk & Overclaim Review` 发现规范锚点不足，应暂停第 9 步并启动 `docs/normative-backfill-workflow.md`。未完成 backfill 的 claim 只能保留为 observation、tentative pattern 或“待核验”，不得进入 final legal conclusion。

所有 final legal conclusions 必须能回溯到：

- case cards
- rule cards
- paper cards
- framework 文件
- article spine / section blueprint / legal writing rationale matrix
- human legal judgment memo

在 human legal judgment lock 和 final document assembly 前，必须先形成并确认：

- `3_synthesis/final_doc/article_spine.md`
- `3_synthesis/final_doc/section_blueprint.md`
- `3_synthesis/final_doc/legal_writing_rationale_matrix.md`

这三个文件只决定文章主线、材料取舍和写作单元功能，不新增法律结论。cards 和横向比较决定证据边界；article spine 决定读者面对的表达结构。

禁止：

- 无来源法律结论
- 把论文观点当法院规则
- 把普通案例单独概括为规则
- 把 draft Priority 当最终研究结论
- 没有 human sign-off 就写 final legal conclusion
- 没有 confirmed article spine 就从 synthesis 直接写 final document
- 为了文章主线选择性隐藏反向材料或待核验材料
- 从 case card 中直接抽取法条当作 rule anchor，而不回到 `0_raw/laws` 和 rule card

## 10. Presentation Adaptation：4_output

最后才进入 `4_output`。

输出包括：

- PPT 素材提纲
- handout
- 展示版表格
- 组员分工材料

这一层只做展示适配。

禁止：

- 新增实质结论
- 为了讲得顺改变研究判断
- 反向污染 `3_synthesis`

## Agent 执行检查清单

每次 agent 接到任务时，先判断当前任务属于哪一步：

- [ ] 是否已有 `current_topic_config.md`？
- [ ] raw 材料是否已经入库并可追溯？
- [ ] 是否需要先生成 rule card / paper card / case card？
- [ ] 是否已有 factor model？
- [ ] 是否已有 weighting model？
- [ ] 是否已经 pilot-tested？
- [ ] 是否已经 locked-v1？
- [ ] 当前任务是否过早进入 synthesis 或 output？

如果答案显示流程缺口，应先补前置环节，而不是跳到后面。

## 最重要的红线

- 没有 topic config，不生成观察要素。
- 没有观察要素，不生成主题 case card 字段。
- 没有 pilot，不锁定权重。
- 没有 framework v1，不批量跑 case cards。
- 新增案例没有 intake review，不进入 case cards。
- 新增案例没有 synthesis delta review，不修改 synthesis。
- 没有 case cards，不做横向比较。
- 没有横向比较，不进入 synthesis human review。
- rule anchor gap 未回填或未标记待核验，不升级为最终法律结论。
- 没有 human sign-off，不写最终法律结论。
- 没有 confirmed article spine，不组装 final document。
- 没有 synthesis，不做 output。
