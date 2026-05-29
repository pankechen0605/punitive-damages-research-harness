# Source Atoms：PD-PILOT-001 张某山等 32 人非法采矿案

> 本文件用于登记本 pilot 使用的来源。来源卡只说明材料边界，不直接生成法律结论。

## SA-ZHANG-001：既有 case card

source_id：`COURT_ZHANG_32_ILLEGAL_MINING_YANCHENG`

source_type：case card

所在路径：`1_digest/case_cards/CC-COURT-ZHANG-32-ILLEGAL-MINING-YANCHENG.md`

authority_level：digest draft；来源角色为 ordinary_case / judgment

usable_for：

- TARA 方法试跑
- fact atoms 初步提取
- factor atoms 初步映射
- decision packets 草稿

not_usable_for：

- 直接上升为一般裁判规则
- 替代原始判决或案例原文
- 支撑 final legal conclusion

limitation：

- case card 状态为 draft。
- 是否生成 rule anchor 仍为 pending。
- 需要继续回查 raw source 与规则卡。

human_review_status：需复核

## SA-ZHANG-002：raw source

source_id：`COURT_ZHANG_32_ILLEGAL_MINING_YANCHENG_RAW`

source_type：raw case material

所在路径：`0_raw/ordinary_cases/judgments/张某山等32人非法采矿案——破坏江河生态环境公益诉讼中惩罚性赔偿的适用-北大法宝V6官网.md`

authority_level：普通案例材料；北大法宝剪藏文本；《人民司法·案例》文章来源

usable_for：

- 核验 case card 摘要
- 补充 evidence atoms 的原文定位
- 检查金额、基数和说理表达

not_usable_for：

- 单独作为权威 rule anchor
- 概括“法院通常认为”
- 直接生成 final synthesis

limitation：

- 本轮只摘取少量定位用于 pilot。
- 若进入正式 synthesis，应逐条核验全文、页码和来源形态。

human_review_status：需补完整原文核验

## SA-ZHANG-003：规则线索

source_id：`RULE-CLUE-ZHANG-001`

source_type：rule clue from case card / raw source

所在路径：`1_digest/case_cards/CC-COURT-ZHANG-32-ILLEGAL-MINING-YANCHENG.md`

authority_level：pending_backfill

usable_for：

- 标记可能需要回填的规范依据
- 提醒后续 rule card 建设

not_usable_for：

- 作为已确认 rule card
- 作为 rule anchor
- 支撑最终法律结论

limitation：

- `1_digest/rule_cards` 当前未提供可引用规则卡。
- 本 pilot 中涉及《民法典》第1232条、生态环境侵权惩罚性赔偿司法解释等，只作为规则线索。

human_review_status：需 normative backfill
