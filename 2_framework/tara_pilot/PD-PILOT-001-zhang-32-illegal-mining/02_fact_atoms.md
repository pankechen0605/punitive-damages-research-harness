# Fact Atoms：PD-PILOT-001 张某山等 32 人非法采矿案

> Fact atom 只记录可观察事实，不写法律结论。

## FA-ZHANG-001：多人共同非法采砂结构

fact_id：`FA-ZHANG-001`

entity：张某山等 32 人

claim：案件涉及多人共同实施非法采砂相关行为，包含出资、提供采砂船、购砂等不同角色。

source_id：`SA-ZHANG-001`; `SA-ZHANG-002`

usable_for：

- 主体复杂性观察
- 刑附民案件结构观察
- 横向比较中的 proceeding_type / actor_structure 字段

not_usable_for：

- 推导所有多人案件均支持惩罚性赔偿
- 推导每名行为人均承担同等惩罚性赔偿

uncertainty：中

human_review_status：需核验各被告参与数量和责任分配

## FA-ZHANG-002：长江禁采区非法采砂数量和价值

fact_id：`FA-ZHANG-002`

entity：张某山等非法采砂行为

claim：case card 记录非法采运江砂 46765.04 吨，价值 2893129 元。

source_id：`SA-ZHANG-001`; `SA-ZHANG-002`

usable_for：

- 损害规模观察
- 违法获利 / 资源价值观察
- 赔偿基数边界观察

not_usable_for：

- 直接证明惩罚性赔偿基数应包含全部江砂价值
- 推导固定倍数规则

uncertainty：中

human_review_status：需核验 raw source 中数量、价值和计算来源

## FA-ZHANG-003：生态环境损害评估

fact_id：`FA-ZHANG-003`

entity：长江生态环境损害

claim：case card 记录生态环境损害价值为 5157476.86 元，其中包含河床结构、鱼类资源、底栖生物、生物多样性服务价值和后续监测费用。

source_id：`SA-ZHANG-001`

usable_for：

- 损害后果观察
- 赔偿基数拆分观察
- evidence gap 标记

not_usable_for：

- 直接确认评估机构资质
- 直接确认所有损害项目均可作为惩罚性赔偿基数

uncertainty：中

human_review_status：需补评估机构和方法原文

## FA-ZHANG-004：前科与取保候审期间再犯

fact_id：`FA-ZHANG-004`

entity：张某山、鲍某文

claim：case card 记录张某山曾因非法采矿罪被判处罚金；鲍某文在涉嫌非法采矿罪取保候审期间实施本案非法采砂行为。

source_id：`SA-ZHANG-001`; `SA-ZHANG-002`

usable_for：

- 主观故意 / 明知违法观察
- 重复侵权或再犯路径观察

not_usable_for：

- 推导“有前科或取保再犯必然构成惩罚性赔偿故意”
- 替代法院原文说理

uncertainty：中

human_review_status：需核验法院原文表述

## FA-ZHANG-005：1倍惩罚性赔偿和分担金额

fact_id：`FA-ZHANG-005`

entity：张某山、鲍某文

claim：case card 记录法院支持 1 倍惩罚性赔偿，张某山 135445.02 元、鲍某文 12688.88 元，按非法采砂数量比例分担。

source_id：`SA-ZHANG-001`

usable_for：

- 倍数表达观察
- 金额分担方式观察
- 与固定金额表达进行对照

not_usable_for：

- 推导生态环境惩罚性赔偿通常按 1 倍确定
- 推导全部被告的分担明细

uncertainty：中

human_review_status：需核验原文金额和计算式
