# Canonical Operating Flow

本文是本项目的固定运行流程。任何 agent，包括 Codex、Claude Code、MiMo 或其他协作工具，在没有用户明确改变流程的情况下，都应按本文推进。

本流程现在由两部分组成：

1. 五层目录边界：`0_raw → 1_digest → 2_framework → 3_synthesis → 4_output`
2. 可追溯组装方法：`研究对象 → 组装动作 → 质量门禁 → 人工复核`

一句话版本：

```text
activate topic config
→ 0_raw collect materials
→ 1_digest extract single-source cards and research atoms
→ 2_framework design issues, factors, weights, and fields
→ pilot run
→ framework v1 lock
→ batch case cards
→ 3_synthesis comparison + judgment packets + risk review
→ human legal judgment lock
→ final document assembly
→ 4_output presentation adaptation
```

## 0. Method Gate

开始任何任务前，先判断任务属于哪一类：

- 收材料
- 单材料消化
- 观察框架设计
- pilot
- 批量 case cards
- 横向比较
- 判断包 / 论证包 / 风险包
- final_doc
- output 展示适配
- 新主题迁移

然后检查是否需要调用：

- [docs/可追溯法律研究组装框架-v0.1.md](可追溯法律研究组装框架-v0.1.md)
- [docs/研究对象模型.md](研究对象模型.md)
- [docs/研究组装操作规则.md](研究组装操作规则.md)
- [docs/质量评价模型.md](质量评价模型.md)
- [docs/法律研究工作流设计清单.md](法律研究工作流设计清单.md)

禁止：

- 不判断层级就直接生成内容。
- 不检查前置条件就进入 synthesis 或 output。
- 为了写得完整而补充未经来源支持的内容。

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
- 哪些话允许说？
- 哪些话禁止说？
- 哪些环节必须人工复核？

禁止：

- 直接写法律结论
- 直接生成观察要素
- 直接生成 case card 字段
- 直接生成判断包
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
- 放研究对象模板成品
- 放判断包
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
- 来源卡、事实卡、规则卡、证据卡草稿

这一层只回答：

```text
这个单个材料说了什么？
```

禁止：

- 写“法院通常认为”
- 做横向结论
- 生成 final legal conclusion
- 把论文观点写成法院规则
- 用单个普通案例概括规则

权威案例和普通案例要分流：

- 权威案例：case card + rule anchor clue，必要时进入 rule anchor map
- 普通案例：case card only，不单独作为 rule anchor

## 4. Framework Design：2_framework

`2_framework` 是当前 topic instance 的观察框架层。

它负责把 topic config、rule cards、paper cards、课堂约束和 pilot case 需求转化为：

- normative map
- literature debate map
- issue model
- adjudication factor model
- factor weighting model
- derived case fields
- derived comparison columns
- 争点卡和裁判因素卡

这一层回答：

```text
读案例时看什么？
优先看什么？
围绕哪些争点组织材料？
case card 应该有哪些字段？
横向比较表应该有哪些列？
```

禁止：

- 生成最终法律结论
- 生成判断包作为结论
- 把观察要素写成法院规则
- 凭直觉给高权重
- 没有 topic config 就生成观察要素

### Normative Sufficiency Check

进入 framework design 前，应检查当前 `0_raw/laws`、`1_digest/rule_cards` 和 `2_framework/normative_map` 是否足以支撑当前 topic config。

如果 case cards、paper cards、判断包草稿或 preliminary notes 暴露出规范缺口，应启动 `docs/normative-backfill-workflow.md`：

```text
case/literature/judgment-packet clue
→ normative backfill review
→ 0_raw/laws 保存规范原文
→ 1_digest/rule_cards 生成或更新规则卡
→ 2_framework/normative_map 更新
→ 再继续 framework design 或 synthesis
```

case card 或判断包中的法条引用只能作为 backfill clue，不能直接作为 rule anchor。

## 5. Pilot Run：2-3 个案例

不要一开始就批量生成所有 case cards。

先选 2-3 个已入库案例试跑，目标是测试：

- 观察要素能不能填写
- 事实卡、证据卡和案例因素包是否能稳定生成
- P0 字段是否真的能稳定观察
- case card 字段是否太多
- 横向比较列是否可操作

pilot 阶段输出：

- pilot case cards
- 案例因素包
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
- 判断包最低字段和质量门禁

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
- 直接从 case card 生成最终规则总结

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
- pilot 检查后的案例因素包

P0 要素进入主列，P1 进入辅助列，P2/P3 通常进入备注或附表。

禁止：

- 手工随意加列
- 只比较支持案例
- 从少量案例过度概括
- 忽略不支持或不涉及案例
- 直接把比较结果写成 final legal conclusion

## 9. Judgment Packets and Human-in-the-loop Synthesis：3_synthesis

在 `3_synthesis` 中，可以开始形成：

- cross-case comparison
- 判断包
- 论证包
- 风险包
- rule summary draft
- final_doc draft

但第 9 步不是 AI 自动生成规则，而是证据层级提升流程：

```text
9.0 Evidence Freeze
→ 9.1 Claim / Issue Extraction
→ 9.2 Judgment Packet Drafting
→ 9.3 Pattern Drafting
→ 9.4 Rule Anchor Mapping
→ 9.5 Risk & Overclaim Review
→ 9.6 Article Spine Confirmation
→ 9.7 Section Blueprint and Writing Rationale Matrix
→ 9.8 Human Legal Judgment Lock
→ 9.9 Final Document Assembly
```

详见：

- `docs/synthesis-human-review-workflow.md`
- `docs/claim-taxonomy-and-elevation-rules.md`
- `docs/研究对象模型.md`
- `docs/质量评价模型.md`

AI 可以整理、归类、比对、生成判断包和提示风险，但不能独立把 observation、判断包或 tentative pattern 提升为 final legal conclusion。

如果 `Rule Anchor Mapping` 或 `Risk & Overclaim Review` 发现规范锚点不足，应暂停第 9 步并启动 `docs/normative-backfill-workflow.md`。未完成 backfill 的 claim 或判断包只能保留为 observation、tentative pattern 或“待核验”，不得进入 final legal conclusion。

所有 final legal conclusions 必须能回溯到：

- case cards
- rule cards
- paper cards
- 判断包
- 风险包
- framework 文件
- article spine / section blueprint / legal writing rationale matrix
- human legal judgment memo

禁止：

- 无来源法律结论
- 把论文观点当法院规则
- 把普通案例单独概括为规则
- 把 draft Priority 当最终研究结论
- 没有 human sign-off 就写 final legal conclusion
- 没有 confirmed article spine 就从 synthesis 直接写 final document
- 为了文章主线选择性隐藏反向材料或待核验材料
- 从 case card 或判断包中直接抽取法条当作 rule anchor，而不回到 `0_raw/laws` 和 rule card

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
- 删除来源、风险和待核验提示

## Agent 执行检查清单

每次 agent 接到任务时，先判断当前任务属于哪一步：

- [ ] 是否已有 `current_topic_config.md`？
- [ ] raw 材料是否已经入库并可追溯？
- [ ] 是否需要先生成 rule card / paper card / case card？
- [ ] 是否需要研究对象卡片？
- [ ] 是否已有 factor model？
- [ ] 是否已有 weighting model？
- [ ] 是否已经 pilot-tested？
- [ ] 是否已经 locked-v1？
- [ ] 是否需要判断包、论证包或风险包？
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
- 判断包缺少来源、反向材料或禁止表述，不进入 final_doc。
- rule anchor gap 未回填或未标记待核验，不升级为最终法律结论。
- 没有 human sign-off，不写最终法律结论。
- 没有 confirmed article spine，不组装 final document。
- 没有 synthesis，不做 output。
