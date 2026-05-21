# 案例消化路由：权威案例与普通案例

本文说明 `0_raw/authoritative_cases` 与 `0_raw/ordinary_cases` 的分类，如何在 `1_digest` 和 `3_synthesis` 中继续发挥作用。

## 基本区分

`authoritative_cases` 是具有规则提示、示范裁判或参照价值的案例集合，包括：

- guiding_cases
- typical_cases
- reference_cases
- gazette_cases

`ordinary_cases` 是普通裁判文书集合，包括：

- judgments
- rulings

二者都是真实案例原文，都可以生成 case card。但它们在研究中的角色不同：权威案例不仅是事实样本，还可能提供规则锚点；普通案例主要用于观察实务分布和裁判因素。

## 为什么二者都可以生成 case card

case card 回答的是“这个单个案例说了什么”。只要案例原文进入项目，就可以生成 case card，用来结构化记录：

- 基本事实
- 当事人主张
- 法院判断
- 惩罚性赔偿请求与处理
- 赔偿基数、倍数、裁量因素
- 待核验项

因此，权威案例和普通案例都可以生成 case card。

## 为什么权威案例还需要 rule anchor card

权威案例除了有单案事实，还可能承担规则示范功能。为了避免把这种功能埋在普通 case card 里，应额外生成 rule anchor card。

rule anchor card 的作用是：

- 摘出权威案例中的裁判要点、典型意义或可参照规则
- 标记该规则锚点的权威类型
- 说明可参照范围
- 在 `2_framework/normative_map` 或 `3_synthesis/rule_summary` 中提供规则支撑

rule anchor card 不等于从案例中自行发明规则。它只能基于原文中已有的裁判要点、典型意义、指导意义或明确说理。

## 不同案例类型的研究角色

| 类型 | raw 位置 | digest 产物 | synthesis 角色 | 注意事项 |
|---|---|---|---|---|
| 指导案例 | `0_raw/authoritative_cases/guiding_cases/` | case card + rule anchor | 规则锚点、规范地图支撑 | 不作为普通统计样本处理。 |
| 典型案例 | `0_raw/authoritative_cases/typical_cases/` | case card + rule anchor | 示范裁判、规则说明素材 | 不得把 typical case 当成统计样本。 |
| 参考案例 | `0_raw/authoritative_cases/reference_cases/` | case card + rule anchor | 参考性规则锚点、类案观察支撑 | 标明参考案例的来源和适用范围。 |
| 公报案例 | `0_raw/authoritative_cases/gazette_cases/` | case card + rule anchor | 重要裁判说理或规则锚点 | 不得脱离原文扩大规则。 |
| 普通案例 | `0_raw/ordinary_cases/` | case card only | 实务样本、横向比较素材 | 不得单独概括为法院规则。 |

## rule anchor 与 case card 的区别

| 项目 | case card | rule anchor card |
|---|---|---|
| 回答的问题 | 这个案子说了什么？ | 这个权威案例提供了什么规则锚点？ |
| 适用对象 | 所有案例 | 权威案例 |
| 主要内容 | 事实、请求、抗辩、法院判断、金额、待核验 | 裁判要点、典型意义、可参照范围、与普通样本区别 |
| 输出位置 | `1_digest/case_cards/` | `1_digest/rule_cards/*.rule-anchor.md` |
| synthesis 角色 | 横向比较素材 | 规则总结和规范地图锚点 |

## synthesis 层使用规则

权威案例在 synthesis 层主要作为规则锚点。它可以帮助说明某一裁判思路具有更高的示范或参照价值，但仍需标明权威类型和适用范围。

普通案例在 synthesis 层主要作为实务样本。它可以进入横向比较，用来观察不同法院在事实、要件、基数、倍数、责任竞合上的处理差异。

不得把 ordinary case 单独概括为法院规则。若普通案例数量不足，只能写“该案显示”“该样本中出现”，不能写成“法院通常认为”。

不得把 typical case 当成统计样本。典型案例的价值在于示范性，不在于代表一般发生频率。

## 字段建议

case card 应保留以下字段：

- `source_category`
- `authority_subtype`
- `research_role`
- `linked_rule_anchor`

rule anchor card 应保留以下字段：

- `type: rule_anchor`
- `source_id`
- `linked_case_card`
- `source_category: authoritative_case`
- `authority_subtype`
- `status`
