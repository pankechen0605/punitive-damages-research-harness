# 材料生命周期

本文说明材料从进入项目到最终输出的流转路径。每条链路都应保留可回溯关系。

## 案例链路

案例链路需要区分普通案例与权威案例。所有案例都可以生成 case card，但权威案例还应额外生成 rule anchor card，用于保留其规则锚点功能。

### 普通案例链路

```text
0_raw/ordinary_cases
→ 1_digest/case_cards
→ 3_synthesis/cross_case_comparison
```

普通案例主要作为实务样本进入横向比较。不得用单个普通案例直接概括法院规则。

### 权威案例链路

```text
0_raw/authoritative_cases
→ 1_digest/case_cards
→ 1_digest/rule_cards/*.rule-anchor.md
→ 2_framework/normative_map 或 2_framework/adjudication_factors
→ 3_synthesis/rule_summary
```

权威案例同时承担单案样本和规则锚点功能。case card 记录单案事实与裁判处理，rule anchor card 记录裁判要点、典型意义或可参照范围。

### 输入

- 指导案例、典型案例、参考案例、公报案例
- 普通判决书、普通裁定书

### 中间产物

- case card
- rule anchor card
- 裁判观察要素表
- 横向比较表
- 裁判规则总结
- PPT 素材提纲

### 人工核验点

- 入库前核验案例来源
- case card 生成后核验案号、法院、请求、判项、说理
- synthesis 前核验案例数量和类型是否足以比较
- output 前核验展示材料是否忠于横向结论

### 常见错误

- 只看摘要，不看裁判原文
- case card 中补写原文没有的信息
- 单个案例直接推出一般规则
- 把普通案例单独写成法院规则
- 把典型案例当作统计样本
- 只保留支持案例，忽略不支持案例

### 完成标准

- 案例原文可追溯
- case card 字段完整或标记待核验
- 权威案例已判断是否需要 rule anchor card
- 横向比较能回到具体案例
- 展示材料没有新增实质判断

## 论文链路

```text
0_raw/papers/pdf
→ 0_raw/papers/extracted_md
→ 1_digest/paper_cards 或 1_digest/notebook_outputs
→ 2_framework/literature_debate_map
→ 2_framework/field_design
→ 3_synthesis/final_doc
```

### 输入

- CSSCI 论文 PDF
- PDF 转出的 extracted_md
- NotebookLM 基于论文生成的中间输出

### 中间产物

- paper card
- NotebookLM 问题清单或争议地图草稿
- literature debate map
- 案例字段设计
- final document 中的学术背景或问题意识

### 人工核验点

- PDF 与 extracted_md 是否对应
- paper card 是否忠于论文
- NotebookLM 输出是否只作为中间材料
- 论文争议是否被正确转化为观察字段

### 常见错误

- 把 NotebookLM 总结放入 raw
- 把论文观点当成法院规则
- 为了理论完整扩大 pre 范围
- 用论文观点替代案例验证

### 完成标准

- PDF 底本保留
- paper card 可回溯单篇论文
- framework 中的争议能转化为案例观察问题
- final document 区分论文观点与裁判规则

## 规范链路

```text
0_raw/laws
→ 1_digest/rule_cards
→ 2_framework/normative_map
→ 3_synthesis/rule_summary
→ 4_output/handout
```

### 输入

- 法条
- 司法解释
- 规范性文件
- 具有规则锚点价值的权威案例裁判要点

### 中间产物

- rule card
- normative map
- rule summary
- handout 中的规范依据页

### 人工核验点

- 规范文本是否准确
- 生效时间、适用范围是否标记
- rule card 是否区分条文内容与解释说明
- rule summary 是否有案例支撑

### 常见错误

- 用过期规范解释当前问题但未标记时间
- 把规范条文的抽象要件直接当成具体裁判结论
- 忽略司法解释与案例事实之间的衔接

### 完成标准

- 规范原文可追溯
- rule card 提取结构清楚
- normative map 能为案例观察提供规则锚点
- handout 不新增未经核验的法律结论

## 观察要素生成链路

观察要素生成链路适用于所有主题。它是将 topic instance 转化为可执行案例阅读任务的桥。

```text
paper cards / rule cards
→ factor model
→ weighting model
→ derived case fields
→ case cards
→ cross-case comparison
→ rule summary
```

### 输入

- topic config
- rule cards
- paper cards
- literature debate map
- normative map
- 初步案例阅读中的字段需求

### 中间产物

- adjudication factor model
- factor weighting model
- derived case fields
- derived comparison columns
- pilot case cards

### 人工核验点

- 观察要素是否只是问题而非结论
- 观察要素是否可在案例中填写
- 权重是否有 basis
- 主题字段是否由 factor model 派生
- 横向比较列是否能回到 factor model

### 常见错误

- 直接从旧主题复制观察要素
- 把观察要素写成法院规则
- 凭直觉设置高权重
- 手工随意增加比较列
- 在案例验证前写“法院通常认为”

### 完成标准

- topic config 已明确当前主题边界
- factor model 已标记 validation status
- weighting model 已标记 weight status
- case card 字段和 comparison columns 能回溯到 factor
- framework v1 锁定前保留待核验状态

文献卡主要影响 Literature Weight。规则卡主要影响 Normative Weight。pilot case cards 主要影响 Case Observability 和 Discriminative Power。topic config 主要影响 Task Relevance。
