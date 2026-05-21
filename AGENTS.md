# AGENTS.md

## 项目定位

本项目不是普通 PPT 项目，而是一个法律研究管线。它用于把原始法律材料逐步转化为：

- case cards
- rule cards
- paper cards
- literature debate map
- adjudication factor table
- cross-case comparison
- final document
- PPT material outline

项目的目标不是让 agent 直接产出最终法律结论，而是让 Codex、Claude Code、MiMo、NotebookLM、Gemini 和人工在同一套材料边界内协作：原始材料先保持干净，单一材料先被结构化，再形成观察框架，最后才进入横向比较和展示适配。

## 核心原则

1. `0_raw` 层不可污染。
2. AI 输出不能进入 `0_raw`，除非是明确的机器可读副本，并且不包含模型总结。
3. 论文观点不等于法院规则。
4. 案例事实不等于法律结论。
5. `1_digest` 层只处理单一材料，不做横向结论。
6. `2_framework` 层设计观察维度，不下最终结论。
7. `3_synthesis` 层才允许做横向比较和规则总结。
8. `4_output` 层只是展示适配，不反向修改研究结论。
9. 不确定内容必须标记“待核验”。
10. 不允许编造案例、案号、法院、法条、论文、作者或裁判结果。

## 固定运行流程

任何 agent 在本项目中工作时，必须优先遵守 [docs/canonical-operating-flow.md](docs/canonical-operating-flow.md)。

默认顺序是：

```text
activate topic config
→ 0_raw 收材料
→ 1_digest 单材料消化
→ 2_framework 设计观察要素和权重
→ pilot 试跑
→ framework v1 lock
→ 批量 case cards
→ 3_synthesis 横向比较和规则总结
→ 4_output 展示适配
```

如果用户要求跳到后续环节，agent 必须先检查前置环节是否已经完成；若未完成，应提醒用户风险，并优先补齐前置文档或标记“待核验”。

禁止在没有 topic config、factor model、weighting model 和 pilot 检查的情况下，直接批量生成主题化 case cards 或横向比较表。

## Agent 允许做什么

### Codex

允许：

- 优化文档结构
- 创建模板
- 创建检查清单
- 创建脚本骨架
- 重构 README
- 创建工作流说明
- 创建 handoff 文件

禁止：

- 生成真实法律内容
- 编造案例
- 替用户判断法律结论
- 把 AI 总结放进 `0_raw`

### MiMo

允许：

- 根据用户提供的案例文本生成 case card 初稿
- 根据用户提供的规范文本生成 rule card 初稿
- 根据用户提供的论文文本生成 paper card 初稿
- 检查卡片遗漏和格式问题

禁止：

- 联网搜索
- 补充外部内容
- 编造材料
- 替用户做最终法律判断

### NotebookLM / Gemini

允许：

- 基于用户上传的论文整理争议地图
- 把论文观点转化为案例观察字段建议
- 生成检索矩阵草稿

禁止：

- 把论文观点写成法院规则
- 把模型输出当 `0_raw`
- 生成未经案例验证的裁判结论

### Human

必须由人完成：

- 收集 raw 材料
- 判断材料是否纳入
- 核验 AI 卡片
- 选择最终案例
- 做最终法律判断
- 决定 pre 主线

## 修改规则

- 修改任何模板时，要说明影响哪些层。
- 修改 README 时，不得删除严禁事项。
- 新增目录前必须说明为什么现有目录不能承载。
- 不得为了美观重命名核心目录。
- 所有 documentation PR 必须更新 `_logs/workflow-log.md`。

## 新主题规则

- 任何 agent 在开启新研究主题前，必须先检查是否存在 `2_framework/field_design/current_topic_config.md`。
- 如果不存在，应先运行 `_prompts/activate_topic_config_prompt.md`。
- 任何 agent 在创建新主题时，必须先创建 topic config，再生成观察要素模型。
- 不得在没有 topic config 的情况下直接生成观察要素、权重、case card 字段或横向比较列。
- 任何 agent 不得跳过 topic config，直接生成 case card 字段或横向比较表。
- 任何 agent 不得把观察要素写成法律结论。
- 观察要素只能回答“读案例时看什么”，不能回答“法院规则最终是什么”。
- 新主题不得直接复制旧主题的具体观察要素、案例结论或 pre 范围；只能复用 workflow 和模板。

## 观察要素权重规则

1. 任何 agent 不得凭直觉给观察要素设高权重。
2. 权重必须有 basis。
3. 论文卡只能影响 Literature Weight，不能单独决定 Priority。
4. 规则卡主要影响 Normative Weight，但仍需考虑案例可观察性和任务相关性。
5. 批量 case card 前，观察要素权重应至少经过 pilot case 检查。
6. 未锁定的权重不得用于输出最终规则总结。
7. 不得把 P0 要素写成法院通常规则。

## Synthesis Human Review 规则

- 第 9 步必须按 [docs/synthesis-human-review-workflow.md](docs/synthesis-human-review-workflow.md) 执行。
- AI 可以生成 synthesis draft、claim ledger、rule anchor map 和 risk review。
- AI 不得自行把 case observation 或 tentative pattern 提升为 final legal conclusion。
- final legal conclusion 必须有 human legal judgment memo 或明确 human sign-off。
- 普通案例不能单独作为 rule anchor。
- paper card 只能作为 scholarly interpretation，不能写成 court rule。
- final document assembly 只能使用 human-confirmed conclusions。
- output 层不得强化、删改或新增 synthesis 层结论。
