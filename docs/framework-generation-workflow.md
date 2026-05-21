# Framework 生成工作流

framework 层只生成观察框架，不生成最终法律结论。

```text
activate topic config
→ current_topic_config
→ normative map
→ literature debate map
→ preliminary adjudication factor model
→ preliminary factor weighting model
→ derived case fields
→ derived comparison columns
→ pilot case cards
→ revised factor model and weighting model
→ framework v1 lock
```

批量 case card 前，factor model 和 weighting model 都应至少经过 `pilot-tested`。

没有 topic config，不应直接生成观察要素模型或 case card 字段。

## 1. activate topic config

### 输入

- 用户对研究主题的初步想法
- 任务场景
- 已知的不做事项

### 处理

- 运行 `_prompts/activate_topic_config_prompt.md`
- 分三轮确认研究边界、材料和案例、输出和限制
- 未确认内容标记“待确认”

### 输出

- `2_framework/field_design/current_topic_config.md` 草稿

### 人工检查点

- 是否真的经过用户确认
- 是否没有生成法律结论
- 是否没有编造材料或案例

### 常见错误

- 没有提问就直接生成 topic config
- 在 topic config 中写法院规则

## 2. current_topic_config

### 输入

- 当前研究主题
- 任务范围
- 课堂或项目约束

### 处理

- 明确 research question
- 明确 scope in / scope out
- 明确材料需求和预期产出

### 输出

- `2_framework/field_design/current_topic_config.md`

### 人工检查点

- 是否过大
- 是否能在当前任务时间内完成
- 是否明确不做什么

### 常见错误

- 直接写结论
- 把多个主题混成一个主题

## 3. normative map

### 输入

- rule cards
- 法条、司法解释、权威案例规则锚点

### 处理

- 整理规范结构
- 提取可能影响案例观察的构成要件和判断因素

### 输出

- `2_framework/normative_map/`

### 人工检查点

- 是否区分规范文本与解释说明
- 是否标记待核验规范

### 常见错误

- 把规范要件直接写成实务结论

## 4. literature debate map

### 输入

- paper cards
- notebook outputs

### 处理

- 整理论文争议
- 把争议转化成观察问题

### 输出

- `2_framework/literature_debate_map/`

### 人工检查点

- 是否把论文观点误当法院规则
- 是否服务当前 topic config

### 常见错误

- 为了理论完整而扩大研究范围

## 5. preliminary adjudication factor model

### 输入

- topic config
- normative map
- literature debate map
- 初步案例阅读问题

### 处理

- 生成观察要素
- 标记来源和验证状态

### 输出

- `2_framework/adjudication_factors/*_factor_model.md`

### 人工检查点

- 要素是否可在案例中填写
- 要素是否过多
- 是否全部标记 validation status

### 常见错误

- 把要素写成结论

## 6. preliminary factor weighting model

### 输入

- preliminary adjudication factor model
- topic config
- rule cards
- paper cards

### 处理

- 为每个观察要素记录研究优先级
- 标记 Normative Weight、Literature Weight、Case Observability、Discriminative Power、Task Relevance
- 标记 Priority 和 Weight Status

### 输出

- `2_framework/adjudication_factors/*_factor_weighting_model.md`

### 人工检查点

- 每个权重是否有 basis
- 是否把权重误写成法律结论
- P0 数量是否可控

### 常见错误

- 凭直觉给高权重
- 让论文热度单独决定 Priority

## 7. derived case fields

### 输入

- adjudication factor model
- factor weighting model

### 处理

- 将观察要素转化为 case card 字段
- 根据 Priority 标记字段必填程度

### 输出

- `2_framework/field_design/*_derived_case_fields.md`

### 人工检查点

- 字段是否可操作
- 是否区分通用字段和主题字段

### 常见错误

- 把旧主题字段直接复制到新主题

## 8. derived comparison columns

### 输入

- adjudication factor model
- factor weighting model
- derived case fields

### 处理

- 将观察要素转化为横向比较列
- P0 进入主列，P1 进入辅助列，P2/P3 通常进入备注或附表

### 输出

- cross-case comparison 表结构草稿

### 人工检查点

- 列是否能服务研究问题
- 是否过度细碎

### 常见错误

- 手工随意加列，导致与 factor model 脱节

## 9. pilot case cards

### 输入

- 2-3 个已入库案例
- derived case fields

### 处理

- 试填 case card
- 记录字段缺失和不适配问题

### 输出

- pilot case cards
- factor revision notes

### 人工检查点

- 是否忠于单一材料
- 是否出现无法填写的字段

### 常见错误

- 用 pilot 案例直接概括规则

## 10. revised factor model and weighting model

### 输入

- pilot case cards
- factor revision notes

### 处理

- 合并、删除、重命名或补充观察要素
- 调整权重状态和 Priority

### 输出

- revised adjudication factor model
- revised factor weighting model

### 人工检查点

- 是否保留不确定性
- 是否仍符合 topic config
- 权重是否至少达到 pilot-tested

### 常见错误

- 为了适配少数案例而扭曲研究问题

## 11. framework v1 lock

### 输入

- revised factor model
- revised weighting model
- derived fields
- derived comparison columns

### 处理

- 锁定当前版本
- 后续新增案例按该版本填写

### 输出

- framework v1

### 人工检查点

- 是否可支持批量案例卡
- 是否可支持横向比较

### 常见错误

- 未锁定版本导致后续字段漂移
