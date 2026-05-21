# Framework 层使用指南

## framework 层不是结论层

`2_framework` 是研究设计层。它负责把论文争议、规范结构、案例字段设计转成观察框架，帮助后续读案例和做比较。

它不负责形成最终法律结论，也不负责替代法院裁判。

framework 层是 topic instance 的核心。它负责把当前主题转化为观察要素模型，并将观察要素继续派生为案例卡字段和横向比较列。

framework 层产物包括：

- topic config
- normative map
- literature debate map
- adjudication factor model
- derived case fields
- derived comparison columns

## 三条来源线

```text
论文层 → 生成观察字段
案例层 → 填入真实裁判材料
规范层 → 提供规则锚点
```

三者在 framework 层形成“看案例的尺子”。

## literature_debate_map 的作用

`literature_debate_map` 用来整理论文争议。

它应回答：

- 学者围绕什么问题有分歧？
- 分歧能否转化为案例观察问题？
- 哪些争议适合当前 pre？
- 哪些争议只适合作为背景？

它不能回答：

- 法院最终规则是什么
- 某观点已经被实务采纳
- 本项目应当作出何种最终法律评价

## adjudication_factors 的作用

`adjudication_factors` 是裁判观察要素表。

它应把抽象问题变成可填字段，例如：

- 主观故意或明知如何认定？
- 严重后果如何认定？
- 赔偿基数由哪些项目组成？
- 倍数如何裁量？
- 行政处罚或刑事罚金是否影响民事惩罚性赔偿？

它是连接 `2_framework` 和 `3_synthesis` 的核心桥。

观察要素模型回答“读每个案例时看什么”，不回答“法院最终规则是什么”。每个观察要素都应保留来源、派生字段、比较列和验证状态。

## normative_map 的作用

`normative_map` 用来整理规范结构。

它应说明：

- 哪些法条提供请求基础
- 哪些司法解释提供操作规则
- 哪些权威案例可能提供规则锚点
- 不同规则之间如何衔接

它不应加入未经核验的实务结论。

## field_design 的作用

`field_design` 用来设计案例卡字段、横向比较字段和当前 pre 的取舍边界。

课堂范围约束也可以放在 `field_design` 或 `docs/current-pre-scope.md`。

例如：

- 本次不做全景综述
- 只做生态环境侵权
- 重点看计算基数、适用门槛、责任竞合
- 麦当劳案只作引入

## 关键边界

学术争议只能指导检索和观察，不能替代判例验证。

课堂提示可以帮助收束范围，但不能直接写成法律规则。

framework 层可以提出问题：

```text
法院是否将永久性损害纳入基数？
```

但不能直接下结论：

```text
法院一律不将永久性损害纳入基数。
```

后者必须等到 `3_synthesis` 基于案例比较后才能讨论。
