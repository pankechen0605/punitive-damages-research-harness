# Digest 层使用指南

## digest 层是什么

`1_digest` 是单一材料消化层。它把一个原始材料读薄、结构化，使后续能够比较，但它本身不做横向结论。

## case card 是什么

case card 是单个案例的结构化摘要。它回答这个案子本身怎么判、法院如何说理、请求和判项是什么、哪些字段需要待核验。

case card 不能直接写“本类案件法院通常……”，因为这是横向结论，应放到 `3_synthesis`。

## rule card 是什么

rule card 是单个规范或规则锚点的结构化摘要。它可以来自法条、司法解释，也可以来自权威案例中的裁判要点。

如果 authoritative case 同时具有事实样本价值和规则锚点价值，可以同时生成 case card 和 rule anchor card，但两者功能不同。

## paper card 是什么

paper card 是单篇论文的结构化摘要。它回答作者讨论什么问题、提出什么观点、对本项目有什么启发。

paper card 不能把论文观点写成法院规则。论文观点只能进入后续 framework，作为观察案例的角度。

## notebook_outputs 是什么

`notebook_outputs` 存放 NotebookLM 生成的中间输出，例如问题清单、论文争议地图草稿、概念框架草稿。

这些内容不是 raw，也不是最终结论。后续应进入 `2_framework` 被筛选和转化。

## 为什么只处理单一材料

digest 层的任务是确保每一个材料先被忠实理解。如果在这一层提前做横向判断，后续就很难区分：

- 哪些是原文内容
- 哪些是 AI 推断
- 哪些是人工综合

因此 digest 层必须克制，只回答单一材料。

## digest 类型表

| digest 类型 | 来源 | 回答的问题 | 不回答的问题 | 输出到哪里 |
|---|---|---|---|---|
| case card | 单个案例原文 | 这个案子怎么判？法院说了什么？ | 同类案件通常如何？ | `1_digest/case_cards/` |
| rule card | 单个法条、司法解释或规则锚点 | 规则文本是什么？构成要件是什么？ | 实务中是否稳定适用？ | `1_digest/rule_cards/` |
| paper card | 单篇论文 | 作者观点是什么？争议点是什么？ | 法院是否采纳该观点？ | `1_digest/paper_cards/` |
| notebook output | NotebookLM 中间输出 | 论文材料可以提出哪些问题？ | 最终裁判规则是什么？ | `1_digest/notebook_outputs/` |

## digest 层检查清单

- [ ] 是否只处理一个材料？
- [ ] 是否能回到 source？
- [ ] 是否标记待核验？
- [ ] 是否避免横向结论？
- [ ] 是否区分法院说理、论文观点和整理者判断？
