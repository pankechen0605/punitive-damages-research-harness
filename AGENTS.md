# AGENTS.md

## 方法入口

本项目不是普通 PPT 项目，而是一个可迁移的法律/合规研究工作流模板。当前生态环境惩罚性赔偿是一个 topic instance，不是仓库方法的上限。

任何 agent 在本仓库工作时，必须先遵守：

1. [docs/canonical-operating-flow.md](docs/canonical-operating-flow.md)
2. [docs/可追溯法律研究组装框架-v0.1.md](docs/可追溯法律研究组装框架-v0.1.md)
3. 五层目录边界：`0_raw → 1_digest → 2_framework → 3_synthesis → 4_output`

本项目的核心方法是：

```text
研究对象 → 组装动作 → 质量门禁 → 人工复核
```

AI 的职责是拆材料、建对象、组判断包、提示风险和生成待复核草稿。AI 不得自行完成最终法律判断。

## 核心原则

1. `0_raw` 层不可污染。
2. AI 输出不能进入 `0_raw`，除非是明确的机器可读副本，并且不包含模型总结。
3. 论文观点不等于法院规则。
4. 案例事实不等于法律结论。
5. 来源线索不等于 rule anchor。
6. 判断包不等于 final legal conclusion。
7. `1_digest` 层只处理单一材料，不做横向结论。
8. `2_framework` 层设计观察维度，不下最终结论。
9. `3_synthesis` 层才允许做横向比较、判断包、论证包和风险审查。
10. `4_output` 层只是展示适配，不反向修改研究结论。
11. 不确定内容必须标记“待核验”。
12. 不允许编造案例、案号、法院、法条、论文、作者或裁判结果。

## 固定运行流程

默认顺序是：

```text
activate topic config
→ 0_raw 收材料
→ 1_digest 单材料消化和研究对象提取
→ 2_framework 设计观察要素、权重、争点和字段
→ pilot 试跑
→ framework v1 lock
→ 批量 case cards
→ 3_synthesis/cross_case_comparison 横向比较
→ 3_synthesis 判断包、论证包、风险包和 human-in-the-loop 规则总结 / 最终分析文档
→ 4_output 展示适配
```

如果用户要求跳到后续环节，agent 必须先检查前置环节是否已经完成。若未完成，应提醒风险，优先补齐前置文档或标记“待核验”。

禁止在没有 topic config、factor model、weighting model 和 pilot 检查的情况下，直接批量生成主题化 case cards、判断包或横向比较表。

## 研究对象规则

研究对象定义见 [docs/研究对象模型.md](docs/研究对象模型.md)。通用模板位于：

- `_templates/atoms/`
- `_templates/packets/`

使用规则：

- 来源卡用于标识材料，不替代原始材料。
- 事实卡只记录可观察事实，不写法律结论。
- 规则卡必须回到规范文本、权威案例或完成 backfill 的规则材料。
- 争点卡只提出问题，不预设答案。
- 裁判因素卡只回答“看什么”，不得写成法院规则。
- 证据卡必须能回到原文摘录或定位。
- 判断包必须同时写支持事实、规则依据、反向材料、不确定性、允许表述和禁止表述。
- 风险包必须在输出前检查来源、权威、边界、反向材料和 human sign-off。

## 组装动作规则

组装动作见 [docs/研究组装操作规则.md](docs/研究组装操作规则.md)。agent 应按任务阶段选择动作：

- 材料分类
- 提取事实
- 拆解规则
- 事实和规则绑定
- 案例和裁判因素绑定
- 生成判断包
- 挑战判断包
- 组装报告段落
- 校验输出
- 迁移到新题目

凡是判断强度提高的动作，都必须经过质量评价和人工复核。

## 质量门禁

质量评价见 [docs/质量评价模型.md](docs/质量评价模型.md)。输出进入下一层前至少检查：

- 可追溯性：重要判断有没有来源。
- 权威匹配：来源权威是否支撑表述强度。
- 边界安全：是否越过当前层级。
- 问题覆盖：核心争点是否被事实和规则覆盖。
- 反向材料：是否记录限制、例外和不支持材料。
- 可复用性：对象和模板是否能迁移到新题。
- 人工复核友好：人能否快速看出风险。

出现以下情形必须阻断：

- `0_raw` 混入 AI 总结。
- 无来源法律结论。
- 论文观点被写成法院规则。
- 普通案例单独作为 rule anchor。
- 没有 human sign-off 的 final legal conclusion。
- output 层新增、删改或强化 synthesis 结论。

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
- 生成研究对象和判断包模板
- 对输出做边界和质量检查

禁止：

- 生成真实法律内容
- 编造案例
- 替用户判断法律结论
- 把 AI 总结放进 `0_raw`
- 越过 human sign-off 写 final legal conclusion

### MiMo

允许：

- 根据用户提供的案例文本生成 case card 初稿
- 根据用户提供的规范文本生成 rule card 初稿
- 根据用户提供的论文文本生成 paper card 初稿
- 根据用户提供材料提取事实卡、证据卡或判断包草稿
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
- 锁定 factor model 和 weighting model
- 判断 claim 是否可升级
- 做最终法律判断
- 决定 pre 主线

## 修改规则

- 修改任何模板时，要说明影响哪些层。
- 修改 README 时，不得删除严禁事项。
- 新增目录前必须说明为什么现有目录不能承载。
- 不得为了美观重命名核心目录。
- 所有 documentation PR 必须更新 `_logs/workflow-log.md`。

## 新主题规则

- 新主题启动前必须使用 [docs/法律研究工作流设计清单.md](docs/法律研究工作流设计清单.md) 明确研究形态、材料权威层级、允许表述、禁止表述和人工复核点。
- 任何 agent 在开启新研究主题前，必须先检查是否存在 `2_framework/field_design/current_topic_config.md`。
- 如果不存在，应先运行 `_prompts/activate_topic_config_prompt.md`。
- 任何 agent 在创建新主题时，必须先创建 topic config，再生成观察要素模型。
- 不得在没有 topic config 的情况下直接生成观察要素、权重、case card 字段、判断包或横向比较列。
- 观察要素只能回答“读案例时看什么”，不能回答“法院规则最终是什么”。
- 新主题不得直接复制旧主题的具体观察要素、案例结论或 pre 范围；只能复用 workflow、对象模型、模板和提示词。

## 观察要素权重规则

1. 任何 agent 不得凭直觉给观察要素设高权重。
2. 权重必须有 basis。
3. 论文卡只能影响 Literature Weight，不能单独决定 Priority。
4. 规则卡主要影响 Normative Weight，但仍需考虑案例可观察性和任务相关性。
5. 批量 case card 前，观察要素权重应至少经过 pilot case 检查。
6. 未锁定的权重不得用于输出最终规则总结。
7. 不得把 P0 要素写成法院通常规则。

## Normative Backfill 规则

- 从 case card、claim ledger、判断包或 rule anchor map 发现的法条、司法解释或规范性文件只能作为 backfill clue。
- backfill clue 不能直接进入 `0_raw/laws`，也不能直接作为 rule anchor。
- 发现规范缺口时，应按 [docs/normative-backfill-workflow.md](docs/normative-backfill-workflow.md) 执行。
- 规范原文或忠实摘录入 `0_raw/laws` 后，必须更新 `source-index.md`，并生成或更新 `1_digest/rule_cards`。
- rule anchor map 应标记 anchor 是 `initial_intake`、`backfilled` 还是 `pending_backfill`。
- 未完成 backfill 的 claim 或判断包不得升级为 final legal conclusion。

## Synthesis Human Review 规则

- 第 9 步必须按 [docs/synthesis-human-review-workflow.md](docs/synthesis-human-review-workflow.md) 执行。
- AI 可以生成 synthesis draft、claim ledger、rule anchor map、判断包、论证包和 risk review。
- AI 不得自行把 case observation、判断包或 tentative pattern 提升为 final legal conclusion。
- final legal conclusion 必须有 human legal judgment memo 或明确 human sign-off。
- 普通案例不能单独作为 rule anchor。
- paper card 只能作为 scholarly interpretation，不能写成 court rule。
- final document assembly 前必须先确认 article spine、section blueprint 和 legal writing rationale matrix；这些文件只组织表达结构，不新增法律结论。
- final document assembly 只能使用 human-confirmed conclusions。
- output 层不得强化、删改或新增 synthesis 层结论。
