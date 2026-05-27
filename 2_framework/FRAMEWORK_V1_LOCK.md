# Framework v1 Lock

锁定日期：2026-05-27
分支：framework/lock-v1-after-pilot
锁定人：人工确认后生效

---

## 一、Lock 范围

本文锁定以下内容，供后续批量 case cards 和 synthesis 使用：

1. Case card v1 字段
2. Case type 标签体系
3. Comparison table v1 字段
4. Synthesis claim rules v1

本文不锁定：

- 最终法律结论
- 裁判规则总结
- 最终文档结构

---

## 二、Pilot Evidence Base

### 已完成的 3 个 Pilot Case Cards

| Pilot | Case Card | Source ID | Source Level | 支持/不支持 | 故意路径 | 计算结构 |
|---|---|---|---|---|---|---|
| 001 | CC-SPP-TYPICAL-WUHAN-ILLEGAL-MINING | SPP_TYPICAL_WUHAN_ILLEGAL_MINING | 权威/典型案例 | 支持 | 屡罚不改 | 未明确区分 |
| 002 | CC-COURT-ZHANG-32-ILLEGAL-MINING-YANCHENG | COURT_ZHANG_32_ILLEGAL_MINING_YANCHENG | 普通/判决书 | 支持 | 前科+取保再犯 | 1倍（基数=生态功能损失） |
| 003 | CC-COURT-CHEN-GUJK-CULTURAL-RELIC | COURT_CHEN_GUJK_CULTURAL_RELIC | 权威/参考案例 | 支持 | 劝阻后仍执意 | 固定金额25000元 |

### 当前覆盖不足

**3 个 pilot 均为"支持惩罚性赔偿"类型。尚未覆盖"不支持惩罚性赔偿"类型案例。**

该类型应在 batch 阶段优先补充，以确保 comparison table 具有支持/不支持对照能力。

其他覆盖不足：

- 仅 1 个案例涉及刑附民程序（pilot 002）
- 仅 1 个案例涉及个人行为人（pilot 003）
- 仅 1 个案例有明确倍数计算（pilot 002：1倍）
- 仅 1 个案例有明确固定金额（pilot 003：25000元）
- 仅 1 个案例涉及罚金刑竞合（pilot 002）
- 仅 1 个案例涉及行政处罚后仍判赔（pilot 003）

---

## 三、Case Card v1 字段

基于 3 个 pilot 的实际填写表现，确认以下字段。

### 3.1 Frontmatter（必填）

| 字段 | 说明 | 来源 |
|---|---|---|
| type | 固定值 `case_card` | 模板 |
| topic | 固定值 `惩罚性损害赔偿` | topic config |
| topic_id | 固定值 `environmental_punitive_damages` | topic config |
| factor_model | 固定值 `v1` | 本文锁定 |
| derived_fields_version | 固定值 `v1` | 本文锁定 |
| source_id | 唯一标识符，与 source-index.md 对应 | source inventory |
| source_category | `authoritative_case` 或 `ordinary_case` | source inventory |
| authority_subtype | `guiding_case` / `typical_case` / `reference_case` / `gazette_case` / `judgment` / `ruling` | source inventory |
| research_role | `punitive_damage_sample` 或其他 | 人工指定 |
| linked_rule_anchor | 关联的 rule card ID，无则填 `pending` | 人工核验 |
| status | `draft` / `reviewed` / `locked` | 人工确认 |

### 3.2 来源角色（必填）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| 来源类别 | 是 | 3/3 填写 |
| 权威类型 | 是（权威案例）/ 不适用（普通案例） | 3/3 填写或标注不适用 |
| 本卡用途 | 是 | 3/3 填写 |
| 是否需要生成 rule anchor | 是 | 3/3 填写（均为"待核验"） |

### 3.3 通用案例信息（必填）

| 字段 | 必填? | Pilot 表现 | 备注 |
|---|---|---|---|
| 案号 | 是 | 2/3 有明确案号，1/3 标注"原文未载明" | 缺失时必须标注"原文未载明"或"待核验" |
| 法院 | 是 | 3/3 填写 | |
| 裁判日期 | 建议 | 3/3 填写 | |
| 文书类型 | 建议 | 3/3 填写 | |
| 案由 | 是 | 3/3 填写 | |
| 所属领域 | 是 | 3/3 填写（均为"生态环境侵权"） | |
| source_id | 是 | 3/3 填写 | 与 frontmatter 一致 |
| 原始材料路径 | 是 | 3/3 填写 | |
| 来源 | 建议 | 3/3 填写 | |
| 发布日期 | 建议 | 3/3 填写 | |

### 3.4 法律依据（建议填写）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| 主要条文 | 建议 | 3/3 填写 |
| 司法解释 | 建议 | 3/3 填写 |
| 指导案例/典型案例关联 | 建议 | 3/3 填写 |

### 3.5 基本事实（必填）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| F-001, F-002, ... | 是（至少 2 条） | 3/3 填写，数量 4-5 条 |

### 3.6 当事人主张（建议填写）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| 原告主张 | 建议 | 3/3 填写 |
| 被告抗辩 | 建议 | 2/3 标注"原文未载明"，1/3 有内容 | 缺失时必须标注"原文未载明" |

### 3.7 争议焦点（建议填写）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| 是否请求惩罚性赔偿 | 是 | 3/3 填写 |
| 争议集中在 | 建议 | 3/3 填写 |

### 3.8 法院判断（核心必填）

| 字段 | 必填? | Pilot 表现 | 备注 |
|---|---|---|---|
| 是否支持惩罚性赔偿 | 是 | 3/3 填写 | `支持` / `不支持` / `部分支持` / `不涉及` / `待核验` |
| 主观要件 | 是 | 3/3 填写 | 必须摘录法院原文或标注"未见明确表述" |
| 客观要件 | 是 | 3/3 填写 | |
| 损害后果 | 是 | 3/3 填写 | |
| 赔偿基数 | 是 | 3/3 填写 | 001 未区分、002 有明确基数、003 固定金额 |
| 倍数/金额 | 是 | 3/3 填写 | |
| 关键说理 | 是 | 3/3 填写 | |

### 3.9 惩罚性赔偿裁量因素（必填）

| 字段 | 必填? | Pilot 表现 | 备注 |
|---|---|---|---|
| 是否存在故意/明知 | 是 | 3/3 填写 | |
| 是否存在重复侵权 | 是 | 1/3 是，1/3 待核验，1/3 未见明确表述 | 缺失时标注"未见明确表述"或"待核验" |
| 是否存在隐瞒、欺诈、拒不整改 | 是 | 1/3 是，2/3 未见明确表述 | |
| 是否存在举证妨碍 | 是 | 3/3 标注"未见明确表述" | 可全部为"未见明确表述" |
| 是否存在严重后果 | 是 | 3/3 填写 | |
| 是否有违法获利 | 是 | 1/3 待核验，1/3 是，1/3 否 | |
| 原告损失是否可计算 | 是 | 3/3 填写 | |
| 法院如何确定倍数 | 是 | 1/3 未见明确表述，1/3 1倍，1/3 固定金额 | |

### 3.10 本案观察标签（必填）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| 支持 / 不支持 | 是 | 3/3 填写 |
| 明知 / 故意 | 是 | 3/3 填写 |
| 情节严重 | 是 | 3/3 填写 |
| 基数争议 | 是 | 3/3 填写 |
| 倍数裁量 | 是 | 3/3 填写 |
| 证明责任 | 是 | 3/3 填写 |
| 特别法 / 侵权责任编 | 是 | 3/3 填写 |

### 3.11 不确定点 / 待核验 / 不得越界提示（必填）

| 字段 | 必填? | Pilot 表现 |
|---|---|---|
| 不确定点 | 是 | 3/3 填写 |
| 待核验 | 是 | 3/3 填写 |
| 不得越界提示 | 是 | 3/3 填写 |

### 3.12 字段调整建议

基于 pilot 实际表现，以下字段需要微调：

1. **"可提炼裁判规则"字段**：现有 3 个 pilot case card 均未填写此字段。建议在 batch 阶段对权威案例（指导案例、典型案例、参考案例）填写，普通案例不强制。
2. **"本案观察标签"中的"证明责任"**：3 个 pilot 均为"未见明确表述"或"检察机关举证"。建议保留但不作为 P0 比较列。
3. **frontmatter 增加 `proceeding_type` 字段**：3 个 pilot 分别为纯民事公益诉讼、刑附民公益诉讼、纯民事公益诉讼，该维度对横向比较有价值。

---

## 四、Case Type 标签体系

以下标签仅用于观察和分类，不是法律规则。

### 4.1 来源层级 (source_level)

| 标签 | 说明 | Pilot 覆盖 |
|---|---|---|
| `spp_typical` | 最高检典型案例 | 001 |
| `spc_reference` | 人民法院案例库参考案例 | 003 |
| `court_typical` | 法院系统典型案例 | — |
| `court_gazette` | 公报案例 | — |
| `guiding` | 指导案例 | — |
| `ordinary_judgment` | 普通判决书 | 002 |
| `ordinary_ruling` | 普通裁定书 | — |
| `other` | 其他来源 | — |
| `pending_review` | 待分类 | — |

### 4.2 程序类型 (proceeding_type)

| 标签 | 说明 | Pilot 覆盖 |
|---|---|---|
| `civil_pil` | 纯民事公益诉讼 | 001, 003 |
| `criminal_attached_civil_pil` | 刑附民公益诉讼 | 002 |
| `pure_civil` | 纯民事诉讼（非公益） | — |
| `eco_damage_compensation` | 生态环境损害赔偿诉讼 | — |
| `unclear` | 不明确 | — |
| `pending_review` | 待核验 | — |

### 4.3 惩罚性赔偿结果 (punitive_result)

| 标签 | 说明 | Pilot 覆盖 |
|---|---|---|
| `supported` | 支持 | 001, 002, 003 |
| `not_supported` | 不支持 | — |
| `partially_supported` | 部分支持 | — |
| `not_applicable` | 不涉及 | — |
| `unclear` | 不明确 | — |
| `pending_review` | 待核验 | — |

### 4.4 故意认定路径 (intentionality_path)

| 标签 | 说明 | Pilot 覆盖 |
|---|---|---|
| `repeated_violation` | 屡罚不改 | 001 |
| `prior_record_reoffend` | 前科/行政处罚后再犯 | 002 |
| `warning_ignored` | 劝阻后仍执意实施 | 003 |
| `direct_knowledge` | 明知（直接证据） | — |
| `other` | 其他认定路径 | — |
| `unclear` | 不明确 | — |
| `pending_review` | 待核验 | — |

### 4.5 计算结构 (calculation_structure)

| 标签 | 说明 | Pilot 覆盖 |
|---|---|---|
| `amount_not_separated` | 未明确区分基数与惩罚性赔偿金额 | 001 |
| `explicit_multiplier` | 有明确倍数（如 1 倍、2 倍） | 002 |
| `fixed_amount` | 固定金额（非倍数计算） | 003 |
| `equal_amount_language` | "等额"表述 | — |
| `discretionary_amount` | 法院酌定金额（无明确公式） | — |
| `unclear` | 不明确 | — |
| `pending_review` | 待核验 | — |

### 4.6 侵权行为类型 (infringement_type)

| 标签 | 说明 | Pilot 覆盖 |
|---|---|---|
| `illegal_mining` | 非法采矿 | 001, 002 |
| `illegal_sand_dredging` | 非法采砂 | 002 |
| `water_pollution` | 水污染 | — |
| `air_pollution` | 大气污染 | — |
| `soil_pollution` | 土壤污染 | — |
| `ecological_destruction` | 生态破坏（非污染型） | 003 |
| `cultural_relic_damage` | 文物/文化遗产损害 | 003 |
| `other` | 其他 | — |
| `unclear` | 不明确 | — |
| `pending_review` | 待核验 | — |

---

## 五、Comparison Table v1 字段

以下字段用于后续横向比较表。P0 为主列，P1 为辅助列。

### P0 主列（必须在横向比较表中出现）

| 字段名 | 说明 | 对应标签体系 |
|---|---|---|
| source_id | 唯一标识 | — |
| case_name | 案件简称 | — |
| source_level | 来源层级 | §4.1 |
| proceeding_type | 程序类型 | §4.2 |
| infringement_type | 侵权行为类型 | §4.6 |
| punitive_result | 惩罚性赔偿结果 | §4.3 |
| intentionality_path | 故意认定路径 | §4.4 |
| calculation_structure | 计算结构 | §4.5 |
| damage_base_amount | 赔偿基数金额 | — |
| punitive_amount | 惩罚性赔偿金额 | — |
| court_reasoning_anchor | 法院关键说理（原文摘录锚点） | — |
| uncertainty_flags | 不确定标记 | — |
| human_review_required | 是否需要人工复核 | — |

### P1 辅助列（建议在横向比较表中出现）

| 字段名 | 说明 |
|---|---|
| punitive_damages_requested | 是否请求惩罚性赔偿 |
| support_status_detail | 支持/不支持的具体理由摘要 |
| multiplier_or_ratio_text | 倍数或比例原文表述 |
| formula_text | 计算公式原文（如有） |
| illegal_gain_mentioned | 是否提及违法获利 |
| admin_or_criminal_penalty | 行政处罚/刑事责任情况 |
| boundary_warnings | 层级边界警告 |

### 不进入 Comparison Table 的字段

以下字段属于 case card 内部，不进入横向比较表：

- 基本事实全文
- 当事人主张全文
- 法律依据全文
- 待核验事项全文
- 不得越界提示全文

---

## 六、Synthesis Claim Rules v1

### 6.1 基本规则

1. **每条 synthesis claim 必须能回到至少一个 case card。** 没有 case card 支撑的 claim 不得进入 synthesis。

2. **强横向判断必须有多个 case card 支撑。** "多个"指至少 2 个不同案件，且来源层级不限于普通案例。

3. **不能从 3 个 pilot 直接得出整体司法实践结论。** 当前 3 个 pilot 均为"支持"类型，样本不具有代表性。

4. **不能把"等额"自动写成"1 倍"。** "等额"与"1 倍"是不同表述，必须按原文记录。

5. **不能把固定金额案例改写成倍数模型。** pilot 003 的 25000 元是法院综合酌定的固定金额，不是基于基数的倍数计算。

6. **不支持案例缺失时，不得总结"不支持规则"。** 当前 3 个 pilot 均为"支持"类型，无法总结"不支持"的规律。

7. **source level 必须影响表述强度。** 权威案例（指导案例、典型案例、参考案例）可提供规则锚点；普通案例只能作为观察样本，不能单独支撑规则。

8. **不确定点必须进入 synthesis 的限制说明。** 每条 claim 的不确定点不得被省略。

### 6.2 表述强度分级

| 表述强度 | 适用条件 | 示例 |
|---|---|---|
| **规则级** | 有权威案例 rule anchor + 多个案例支撑 + 人工确认 | "根据《民法典》第 1232 条……" |
| **模式级** | 多个案例一致呈现 + 有规范依据 + 人工确认 | "在已观察的 X 个案例中，法院均……" |
| **观察级** | 单个或少数案例呈现 + 尚需更多验证 | "在 pilot 案例中观察到……" |
| **待核验** | 证据不足或存在矛盾 | "本案显示……但尚需更多案例验证" |

当前 3 个 pilot 阶段，所有 synthesis claim 最高只能达到"观察级"。

### 6.3 禁止的 synthesis 表述

- "法院通常认为……"（3 个 pilot 不足以支撑"通常"）
- "司法实践已经确立……"（未经过充分案例验证）
- "普遍采用……"（样本不足）
- "根据多数案例……"（3 个案例不构成"多数"）
- 任何将单个普通案例概括为规则的表述

### 6.4 允许的 synthesis 表述

- "在已观察的 3 个 pilot 案例中，法院均支持了惩罚性赔偿请求"
- "3 个 pilot 案例展示了三种不同的故意认定路径"
- "pilot 002 和 003 在计算结构上存在差异：前者采用倍数，后者采用固定金额"
- "当前 pilot 尚未覆盖'不支持'类型，该类型应在 batch 阶段优先补充"

---

## 七、Human Review Checklist

批量 case cards 阶段，每张 case card 完成后需人工核验：

### 7.1 来源核验

- [ ] source_id 与 source-index.md 一致
- [ ] 原始材料路径存在且可访问
- [ ] 案号、法院、裁判日期与原文一致
- [ ] source_category 和 authority_subtype 分类正确

### 7.2 内容核验

- [ ] 基本事实摘录忠于原文，无编造
- [ ] 法院判断摘录忠于原文，无过度推断
- [ ] 惩罚性赔偿金额、基数、倍数与原文一致
- [ ] "待核验"项确实无法从原文确认
- [ ] "未见明确表述"项确实原文未提及

### 7.3 层级边界核验

- [ ] case card 不包含跨案例结论
- [ ] case card 不包含"法院通常认为"等横向表述
- [ ] 不确定点已标注
- [ ] 不得越界提示已填写

### 7.4 标签核验

- [ ] punitive_result 标签与法院判断一致
- [ ] intentionality_path 标签与法院说理一致
- [ ] calculation_structure 标签与计算方式一致
- [ ] proceeding_type 标签与案件程序一致

---

## 八、Batch Case Card 阶段优先顺序

### Phase 1：优先补充不支持类型（最高优先）

当前最大覆盖缺口是"不支持惩罚性赔偿"类型案例。batch 阶段应首先从 source inventory 中筛选可能不支持的案例，生成 case card。

候选来源：
- source inventory 中标注"无"惩罚性赔偿关键词的案例
- 人工判断可能不涉及或不支持的案例

### Phase 2：补充权威案例

优先处理：
- 指导案例（G1-G3）
- 典型案例中尚未处理的多案例合集（T2-T6）
- 参考案例（R1, R3）

### Phase 3：补充普通案例

处理剩余普通案例（J1-J8），重点关注：
- 包含基数或倍数说理的案例
- 涉及行政处罚或刑事责任竞合的案例

### Phase 4：多案例合集拆分

部分文件为多案例合集（如"最高检第四十批指导性案例"），需要：
- 识别合集中各子案例
- 为每个子案例生成独立 case card
- 在 source-inventory.md 中更新

---

## 九、当前覆盖不足汇总

| 维度 | 已覆盖 | 缺失 | 影响 |
|---|---|---|---|
| 惩罚性赔偿结果 | 支持（3案） | 不支持、部分支持 | 无法总结"不支持"规律 |
| 程序类型 | 纯民事 PIL（2案）、刑附民 PIL（1案） | 纯民事非 PIL、生态损害赔偿 | 程序类型对照不足 |
| 行为人类型 | 企业（2案）、个人（1案） | 更多个人案例 | 个人 vs 企业对照不足 |
| 故意认定路径 | 屡罚不改、前科再犯、劝阻执意 | 明知（直接证据） | 故意认定路径覆盖不全 |
| 计算结构 | 未区分（1案）、1倍（1案）、固定金额（1案） | 等额、酌定金额 | 计算结构覆盖不全 |
| 侵权类型 | 非法采矿/采砂（2案）、文物刻划（1案） | 水污染、大气污染、土壤污染 | 侵权类型覆盖不全 |
| 责任竞合 | 有罚金（1案）、有行政处罚（1案）、无竞合（1案） | 更多竞合案例 | 责任竞合对照不足 |
| 来源层级 | 典型案例（1案）、参考案例（1案）、普通判决（1案） | 指导案例、公报案例 | 权威层级覆盖不全 |

---

## 十、禁止事项

1. 不得在 batch case cards 阶段修改 framework lock 字段（如需修订，应创建 v2 lock 文档）。
2. 不得从 3 个 pilot 概括为"司法实践通常认为"。
3. 不得在 synthesis 中省略"不支持"类型案例的缺失说明。
4. 不得把固定金额案例改写为倍数模型。
5. 不得把"等额"等同于"1 倍"。
6. 不得把普通案例单独作为规则锚点。
7. 不得在 case card 中写跨案例结论。
8. 不得在 synthesis 中使用未经 human sign-off 的 final legal conclusion。
9. 不得在 4_output 中新增未经 3_synthesis 支撑的实质判断。
10. 不得在 framework lock 后随意新增或删除字段（须走版本化修订流程）。

---

## 十一、版本记录

| 版本 | 日期 | 说明 |
|---|---|---|
| v1 | 2026-05-27 | 基于 3 个 pilot case cards 首次锁定 |
