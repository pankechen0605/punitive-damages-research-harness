# Source Atoms：PD-PILOT-002 陈某平生态破坏案

> 本文件用于登记本 pilot 使用的来源。来源卡只说明材料边界，不直接生成法律结论。

## SA-CHEN-001：既有 case card

source_id：`COURT_CHEN_GUJK_CULTURAL_RELIC`

source_type：case card

所在路径：`1_digest/case_cards/CC-COURT-CHEN-GUJK-CULTURAL-RELIC.md`

authority_level：digest draft；来源角色为 authoritative_case / reference_case

usable_for：

- TARA 方法试跑
- fact atoms 初步提取
- factor atoms 初步映射
- decision packets 草稿

not_usable_for：

- 直接替代原始裁判材料
- 直接生成 final legal conclusion
- 在未完成 rule anchor map 前写成一般裁判规则

limitation：

- case card 状态为 draft。
- 是否生成 rule anchor 仍为 pending。
- 参考案例的规则价值仍需人工确认。

human_review_status：需复核

## SA-CHEN-002：raw source

source_id：`COURT_CHEN_GUJK_CULTURAL_RELIC_RAW`

source_type：raw case material

所在路径：`0_raw/authoritative_cases/reference_cases/贵州省江口县人民检察院诉陈某平生态破坏民事公益诉讼案-北大法宝V6官网.md`

authority_level：人民法院案例库参考案例剪藏文本

usable_for：

- 核验 case card 摘要
- 补充 evidence atoms 的原文定位
- 检查固定金额、劝阻后继续实施和行政处罚因素

not_usable_for：

- 未经 rule anchor map 直接作为最终规则总结
- 直接迁移到其他主题

limitation：

- 本轮只摘取少量定位用于 pilot。
- 若进入正式 synthesis，应逐条核验全文、案号、裁判要旨和来源形态。

human_review_status：需补完整原文核验

## SA-CHEN-003：规则线索

source_id：`RULE-CLUE-CHEN-001`

source_type：rule clue from case card / raw source

所在路径：`1_digest/case_cards/CC-COURT-CHEN-GUJK-CULTURAL-RELIC.md`

authority_level：pending_backfill

usable_for：

- 标记可能需要回填的规范依据
- 提醒后续 rule card 建设

not_usable_for：

- 作为已确认 rule card
- 直接作为 rule anchor
- 支撑最终法律结论

limitation：

- `1_digest/rule_cards` 当前未提供可引用规则卡。
- 本 pilot 中涉及《民法典》第1232条和相关司法解释等，只作为规则线索。

human_review_status：需 normative backfill
