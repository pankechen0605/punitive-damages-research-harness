# 案例观察要素模型

## 什么是观察要素

观察要素是从研究问题、规范结构、论文争议、任务约束和初步案例阅读中提炼出来的案例观察变量。

它回答：

```text
读每个案例时应该看什么？
```

它不回答：

```text
法院规则最终是什么？
```

观察要素不是法律结论，而是案例阅读、摘录和横向比较的稳定变量。

## 观察要素的来源

### 1. Normative sources

可能来源包括：

- 法条构成要件
- 司法解释判断因素
- 指导案例 / 典型案例的裁判要点

规范来源提供的是规则锚点和结构，不等于已经完成案例验证。

### 2. Literature debates

可能来源包括：

- 学界争议
- 制度评价
- 实证发现
- 改革建议

论文争议可以生成观察问题，但不能直接生成法院规则。

### 3. Task constraints

可能来源包括：

- 课堂 pre 时间
- 老师要求
- 研究主题边界
- 输出形式

任务约束决定本次研究优先观察什么、暂不展开什么。

### 4. Pilot case reading

可能来源包括：

- 初读案例中反复出现的裁判因素
- 实务中出现但论文没有充分讨论的变量

pilot reading 只能帮助修订观察要素，不能绕过人工核验。

## 观察要素的结构

每个观察要素应包含：

- `factor_id`
- `factor_name`
- `factor_type`
- `research_question`
- `source_basis`
- `derived_case_fields`
- `comparison_columns`
- `evidence_to_extract`
- `possible_values`
- `validation_status`
- `do_not_conclude`

`factor_type` 可包括：

- `threshold_factor`
- `subjective_factor`
- `objective_factor`
- `calculation_factor`
- `procedural_factor`
- `remedy_factor`
- `policy_factor`
- `evidentiary_factor`

## 观察要素与法律结论的区别

- 观察要素是问题，不是答案。
- 观察要素可以来自论文争议，但不能把论文观点当法院规则。
- 观察要素需要通过案例卡和横向比较验证。
- 在 synthesis 前，不得写“法院通常认为”。

示例表达：

```text
观察要素：法院如何认定主观状态？
```

不合格表达：

```text
法院通常以某种行为认定故意。
```

后一种表达只能在充分案例验证后，进入 synthesis 层并保留来源支撑。

## 观察要素如何影响下游

观察要素会派生：

- case card 字段
- cross-case comparison 列
- rule summary 结构
- final doc 小标题
- output 层展示重点

关系如下：

```text
factor
→ derived case fields
→ case cards
→ comparison columns
→ cross-case comparison
→ rule summary / final doc
→ output material
```

## 观察要素与权重

观察要素回答“看什么”。

权重回答“优先看什么”。

权重决定字段必填程度、横向比较列和最终输出主线，但权重不能替代案例验证。

权重应经历：

```text
literature-informed
→ normative-adjusted
→ pilot-tested
→ locked-v1
```

其中，paper cards 主要影响 Literature Weight，rule cards 主要影响 Normative Weight，pilot case cards 主要影响 Case Observability 和 Discriminative Power，topic config 主要影响 Task Relevance。

详见 [factor-weighting-model.md](factor-weighting-model.md)。

## 失败模式

- 把观察要素写成法律结论
- 把论文观点写成法院规则
- 观察要素太抽象，无法在案例中填写
- 观察要素太多，导致案例卡不可操作
- 只关注支持案例，忽略不支持案例
- 用普通案例直接概括规则
