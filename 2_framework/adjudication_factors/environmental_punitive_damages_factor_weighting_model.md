# 观察要素权重模型：生态环境侵权惩罚性赔偿

## 一、模型说明

本模型用于决定本研究中各观察要素的研究优先级。

本模型不是法律结论，不用于预测案件结果。

最终 Priority 需要人工锁定。本文仅基于项目中已有的 paper cards、rule cards、case cards、topic config 和 existing factor model 生成 draft 建议。

## 二、材料来源

| 材料类型 | 目录 | 文件数量 | 备注 |
|---|---|---:|---|
| paper cards | `1_digest/paper_cards/` | 25 | 已读取文件名和关键词覆盖；其中生态环境主题论文卡主要为 PC-001 至 PC-010，其他主题论文卡仅作背景材料。 |
| rule cards | `1_digest/rule_cards/` | 6 | 包含 3 个规范卡和 3 个 authoritative case rule anchor。 |
| case cards | `1_digest/case_cards/` | 14 | 本次读取时目录不为空；已有 case cards 可作为 pilot 材料，但尚未人工锁定。 |
| topic config / scope files | `2_framework/field_design/` | 3 | 包含 `current_topic_config.md`、`environmental_derived_case_fields.md` 和课堂范围材料。 |
| existing factor model | `2_framework/adjudication_factors/` | 2 | 包含观察要素模型和本权重模型。 |

## 三、观察要素候选

| Factor ID | Factor Name | 来源依据                                                                                                                 | 是否已有案例字段                          | 是否已有横向比较字段              | 备注                               |
| --------- | ----------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ----------------------- | -------------------------------- |
| F-001     | 是否支持惩罚性赔偿   | `current_topic_config.md` 要求比较支持与不支持样本；case cards 中已有支持、不涉及、未支持等片段                                                   | 是，factor model 中为“支持状态、支持金额、驳回理由” | 是，factor model 中为“是否支持” | 作为分类变量有用，但不能据此推出法院规则。            |
| F-002     | 主观故意/明知     | RC-001、RC-002 明确将主观状态列为观察对象；paper cards 中“故意”出现于 15 个文件，“明知”出现于 3 个文件；case cards 中相关词汇出现在多份文件                        | 是                                 | 是                       | 属于门槛类观察要素，仍需逐案摘录原文说理。            |
| F-003     | 严重后果        | RC-001、RC-002 均将严重后果列为观察对象；paper cards 中“严重后果”出现于 10 个文件；case cards 中相关字段已有出现                                        | 是                                 | 是                       | 属于门槛类观察要素，不能在 synthesis 前写成通用标准。 |
| F-004     | 赔偿基数        | RC-001、RC-002 均提示观察基数；paper cards 中“赔偿基数”出现于 25 个文件，“计算基数”出现于 3 个文件；case cards 中“基数”出现于 12 个文件                       | 是                                 | 是                       | 与当前 topic config 的“计算基数”切口直接相关。  |
| F-005     | 倍数裁量        | RC-002 提示倍数/金额观察；paper cards 中“倍数”出现于 25 个文件；case cards 中“倍数”出现于 9 个文件                                               | 是                                 | 是                       | 与基数共同影响数额结构，但 Priority 仍需人工判断。   |
| F-006     | 行政处罚/刑事责任竞合 | RC-002、RC-003 和 rule anchors 均涉及责任协调问题；paper cards 中“行政处罚”出现于 3 个文件，“刑事”出现于 8 个文件，“罚金”出现于 7 个文件；case cards 中相关词汇出现较多 | 是                                 | 是                       | 当前 topic config 将责任竞合作为核心切口之一。   |
| F-007     | 修复/整改情况     | rule anchors 和 case cards 中均多次出现修复、整改、替代性修复等字段；paper cards 中“修复”出现于 9 个文件                                            | 否，derived case fields 尚未单列        | 否，factor model 尚未单列     | 现有材料显示可观察性较强，但是否进入主线需人工核验。       |
| F-008     | 赔偿金归属       | paper cards 中“赔偿金归属”仅出现于 1 个文件；case cards 中未检出该字段                                                                    | 否                                 | 否                       | 材料不足，需人工核验。                      |


## 四、权重草稿表

评分规则：

- 0 = 无明显依据
- 1 = 弱
- 2 = 中
- 3 = 强
- TBD = 现有材料不足，暂不判断

| Factor ID | Factor Name | Normative Weight | Literature Weight | Case Observability | Discriminative Power | Task Relevance | Priority Draft          | Basis                                                                                                                                                 | Status       | Do Not Conclude        |
| --------- | ----------- | ---------------: | ----------------: | -----------------: | -------------------: | -------------: | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------------- |
| F-001     | 是否支持惩罚性赔偿   |                2 |                 1 |                  2 |                    3 |              3 | P0 draft recommendation | Normative basis 来自 RC-001、RC-002 对请求权和条件的整理；Task basis 来自 topic config 的支持/不支持样本需求；case basis 来自已有 case cards 中支持、不涉及、未支持等片段。                         | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-002     | 主观故意/明知     |                3 |                 2 |                  3 |                    2 |              3 | P0 draft recommendation | Normative basis 来自 RC-001、RC-002；Literature basis 来自 paper cards 中“故意/明知”关键词覆盖；case basis 来自已有 case cards 中主观状态字段。                                    | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-003     | 严重后果        |                3 |                 2 |                  2 |                    2 |              3 | P0 draft recommendation | Normative basis 来自 RC-001、RC-002；Literature basis 来自 paper cards 中“严重后果”关键词覆盖；case basis 来自已有 case cards 中严重后果字段，但覆盖不如主观要件稳定。                         | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-004     | 赔偿基数        |                3 |                 3 |                  3 |                    2 |              3 | P0 draft recommendation | Normative basis 来自 RC-001、RC-002；Literature basis 来自 25 个 paper cards 中均出现“赔偿基数”；Task basis 来自 topic config 的计算基数切口；case basis 来自已有 case cards 中基数字段。 | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-005     | 倍数裁量        |                3 |                 3 |                  2 |                    2 |              2 | P1 draft recommendation | Normative basis 来自 RC-002；Literature basis 来自 paper cards 中“倍数”关键词覆盖；case basis 来自已有 case cards 中倍数/金额字段。                                             | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-006     | 行政处罚/刑事责任竞合 |                2 |                 2 |                  3 |                    2 |              3 | P1 draft recommendation | Normative basis 来自 RC-002、RC-003 和 rule anchors；Literature basis 来自 paper cards 中行政处罚、刑事、罚金等关键词覆盖；Task basis 来自 topic config 的责任竞合切口。                 | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-007     | 修复/整改情况     |                2 |                 2 |                  3 |                    2 |              2 | P2 draft recommendation | Normative basis 主要来自 rule anchors；Literature basis 来自 paper cards 中“修复”关键词覆盖；case basis 来自已有 case cards 中修复/整改字段高频出现。尚未进入 existing factor model。      | pilot-tested | 不得在案例验证和人工锁定前写成法院通常规则。 |
| F-008     | 赔偿金归属       |              TBD |                 1 |                  0 |                  TBD |              1 | P3 draft recommendation | Literature basis 仅来自少量 paper card 关键词；现有 rule cards 和 case cards 支撑不足。                                                                                | draft        | 不得在案例验证和人工锁定前写成法院通常规则。 |

## 五、P0/P1/P2/P3 建议，不得锁定

以下只是 draft recommendation，最终由人工决定。

| Factor      | Suggested Priority | Why                                                 | Risk                          | Human Check Needed             |
| ----------- | ------------------ | --------------------------------------------------- | ----------------------------- | ------------------------------ |
| 是否支持惩罚性赔偿   | P0                 | 作为横向比较的基本分类变量，服务 topic config 中支持/不支持样本需求。          | 容易被误写成结果预测。                   | 核验每张 case card 是否有明确判项或法院判断支撑。 |
| 主观故意/明知     | P0                 | 规范卡和 topic config 均指向适用门槛，paper/case cards 中也有较高覆盖。 | 可能把个案事实归纳为统一标准。               | 必须逐案摘录法院原文说理。                  |
| 严重后果        | P0                 | 与适用门槛直接相关，规范卡有明确来源。                                 | case cards 中覆盖不如主观要件稳定。       | 核验是否每案都能填写，不能填写时是否标记缺失。        |
| 赔偿基数        | P0                 | 与当前研究切口高度一致，paper cards 和 case cards 覆盖较强。          | 容易把论文争议写成法院规则。                | 区分论文观点、规范依据和判决计算。              |
| 倍数裁量        | P1                 | 与数额结构相关，规范和文献均有材料支撑。                                | 可能与基数问题混同。                    | 人工判断是否进入主线，或作为基数分析的辅助列。        |
| 行政处罚/刑事责任竞合 | P1                 | 与当前 topic config 的责任竞合切口一致，case cards 中可观察性较强。      | 不同案件材料差异大，容易过度概括。             | 检查是否有足够案例支撑责任竞合比较。             |
| 修复/整改情况     | P2                 | case cards 中可观察性强，rule anchors 中有提示。                | 尚未进入现有 factor model，可能导致字段膨胀。 | 决定是否提升为 P1，或仅作修复态度/裁量因素补充。     |
| 赔偿金归属       | P3                 | 当前材料支撑弱，适合作为延伸。                                     | 若强行进入主线会分散研究重点。               | 需要额外材料或人工确认是否保留。               |

## 六、字段影响

| Factor | Suggested Priority | Case Card Impact | Cross-Case Comparison Impact | Final Doc Impact |
|---|---|---|---|---|
| 是否支持惩罚性赔偿 | P0 | 必填：支持状态、金额或驳回/不涉及理由。 | 主列：用于区分支持、不支持、不涉及、待核验。 | 作为横向比较入口。 |
| 主观故意/明知 | P0 | 必填：摘录法院关于主观状态的原文说理和证据。 | 主列：比较不同个案中的主观状态呈现。 | 进入适用门槛部分。 |
| 严重后果 | P0 | 必填：摘录严重后果或损害后果说理。 | 主列：比较严重后果的事实呈现。 | 进入适用门槛部分。 |
| 赔偿基数 | P0 | 必填：记录基数构成、金额、计算说明。 | 主列：比较基数类型和计算方式。 | 进入计算基数主线。 |
| 倍数裁量 | P1 | 尽量填写：记录倍数、金额和裁量理由。 | 辅助列：与基数共同观察数额结构。 | 作为基数分析的延伸或分支。 |
| 行政处罚/刑事责任竞合 | P1 | 尽量填写：记录罚款、罚金、刑责及法院处理。 | 辅助列：比较责任竞合处理。 | 进入责任竞合部分，视样本充足程度展开。 |
| 修复/整改情况 | P2 | 有材料则填：记录修复、整改、验收、替代性修复等。 | 可作备注或附表；若人工提升权重，可进入辅助列。 | 作为裁量因素或边界案例讨论。 |
| 赔偿金归属 | P3 | 一般不强制填写；有明确材料时备注。 | 通常不进入主表。 | 可作为后续研究线索。 |

## 七、需要人工核验的问题

1. 缺少 rule card 支撑的权重：
   - 赔偿金归属缺少明确 rule card 支撑。
   - 修复/整改情况主要来自 rule anchors，是否足以形成独立观察要素需人工判断。

2. 缺少 paper card 支撑的权重：
   - 是否支持惩罚性赔偿的 Literature Weight 较弱，paper cards 更集中于要件、基数、倍数、责任协调等问题。
   - 赔偿金归属仅有少量关键词支撑。

3. 缺少 case card 验证的权重：
   - 赔偿金归属在现有 case cards 中未检出。
   - 严重后果虽有 case card 支撑，但覆盖稳定性需要逐案复核。
   - Discriminative Power 仍需基于人工确认后的支持/不支持对照表进一步校正。

4. 可能过重的字段：
   - 是否支持惩罚性赔偿是分类变量，不应被误用为裁判理由。
   - 倍数裁量可能与赔偿基数重复，应避免双重占用主线。
   - 修复/整改情况可观察性强，但是否服务当前主线需人工确认。

5. 不应进入最终结论的要素：
   - 赔偿金归属目前不宜进入最终主线。
   - 任何未经过 case card 验证和人工锁定的 P0/P1 建议，都不得写成“法院通常认为”。
