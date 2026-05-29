# Temu/PDD 双支柱迁移说明

## 定位

本文不是 Temu/PDD 双支柱正式报告，不新增 Temu/PDD 实体结论，不判断 PDD/Temu 是否适用 GloBE、是否触发补税或任何 jurisdictional ETR。

本文只说明：当前 punitive 项目的 TARA 结构迁移到 Temu/PDD 双支柱研究时，应如何改变工作模式和边界。

## 模式切换

当前惩罚性赔偿项目使用 `case-factor mode`：

```text
case
→ fact
→ evidence
→ factor
→ decision packet
→ comparison
```

Temu/PDD 双支柱项目应使用 `compliance-mapping mode`：

```text
source
→ rule
→ fact
→ issue
→ rule-fact binding
→ decision packet
→ data gap
→ quality review
```

核心区别：

- punitive 项目观察法院如何处理案例。
- Temu/PDD 项目观察公开来源中的公司事实如何与官方规则形成映射。
- Temu/PDD 不应主打裁判因素，也不应做判决横向比较。

## 推荐链条

Temu/PDD 项目建议采用：

```text
01_source_atoms
→ 02_rule_atoms
→ 03_fact_atoms
→ 04_issue_map
→ 05_rule_fact_bindings
→ 06_decision_packets
→ 07_data_gap_checklist
→ 08_quality_review
→ 09_assembly_notes
```

## 可复用对象

可以复用：

- 来源卡
- 事实卡
- 规则卡
- 争点卡
- 证据卡
- 判断包
- 风险包
- 质量审查

使用方式：

- 来源卡：区分 OECD / 税务机关 / 年报 / 公司公告 / 律所文章 / 媒体报道。
- 规则卡：记录官方规则和适用条件。
- 事实卡：记录公开披露的公司事实。
- 争点卡：定义是否进入合规准备视野、需要哪些数据、哪些不能判断。
- 判断包：形成待复核的合规观察，不写最终税务判断。
- 风险包：记录过强表述、数据缺口和来源权威不足。

## 不应直接照搬的对象

不应直接照搬：

- 裁判因素卡。
- 案例因素包。
- 判决横向比较表。
- punitive 项目的赔偿基数、倍数表达或故意路径字段。

这些对象服务于司法案例观察，不适合直接迁移到双支柱合规映射。

## 初始 forbidden claims

Temu/PDD 项目中，未经充分官方规则、公司披露、税务数据和人工复核，不得写：

1. PDD/Temu 已确定适用 GloBE。
2. PDD/Temu 已触发补税义务。
3. 某辖区实际 ETR 低于 15%。
4. Cayman / Ireland / Singapore 等辖区当然构成低税风险。
5. 仅凭公开年报即可完成 jurisdictional ETR 判断。
6. 仅凭媒体或律所文章即可替代 OECD / 年报 / 官方规则。
7. Temu/PDD 必然构成低税辖区风险。
8. 已经证明某一辖区需要补税。

## 初始 allowed claims

在仅基于公开资料和方法试跑阶段，可以写：

1. PDD/Temu 可以进入 Pillar Two 合规观察和数据准备视野。
2. 可以基于公开资料建立规则-事实映射样本。
3. 现有公开资料不足以计算 jurisdictional ETR。
4. 需要进一步获取集团实体、辖区税负、GloBE income、covered taxes 等数据。
5. 可以形成数据缺口清单和合规准备路线。
6. 媒体和律所文章只能作为问题线索或背景材料，不能替代官方规则。

## source hierarchy 建议

Temu/PDD 主题建议优先级：

1. OECD Pillar Two / GloBE 官方文件。
2. 相关辖区税务机关或财政部门官方文件。
3. PDD / PDD Holdings / Temu 公开年报、公告、审计披露。
4. 交易所文件、监管披露。
5. 专业机构报告、律所文章、税务评论。
6. 媒体报道和公众号材料。

任何低权威材料只能作为 clue，不得替代规则卡或事实卡的高权威来源。

## data gap checklist 方向

Temu/PDD 判断包至少应暴露以下缺口：

- 集团实体清单。
- 各实体所在辖区。
- jurisdictional income。
- covered taxes。
- GloBE income or loss。
- 有效税率计算所需调整项。
- safe harbour 或过渡规则相关数据。
- 官方规则适用时间点。
- 披露口径和年报口径差异。

## human review gate

以下内容必须人工复核：

- 规则适用范围。
- 公司事实是否来自年报或官方披露。
- jurisdictional ETR 是否可计算。
- 是否存在补税义务。
- 是否可以形成对外报告或展示材料。

没有 human sign-off，不得把 decision packet 写成最终税务或法律结论。
