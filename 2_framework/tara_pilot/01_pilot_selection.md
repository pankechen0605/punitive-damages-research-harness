# Pilot Selection

## 选择标准

本轮选择两个既有案例作为 TARA pilot，标准如下：

1. 已有 case card，避免新增原始研究负担。
2. 已在 framework v1 lock 的 pilot evidence base 中出现，便于和既有观察字段对齐。
3. 两个案例结构差异明显，可测试框架适应性。
4. 都涉及主观故意、损害后果、赔偿基数或赔偿表达方式。
5. 一个偏刑附民 / 多人主体 / 倍数表达，一个偏纯民事 / 个人行为人 / 固定金额表达。

## 入选案例

| Pilot | Case Card | Source ID | 测试价值 |
|---|---|---|---|
| PD-PILOT-001 | `1_digest/case_cards/CC-COURT-ZHANG-32-ILLEGAL-MINING-YANCHENG.md` | `COURT_ZHANG_32_ILLEGAL_MINING_YANCHENG` | 测试刑附民结构、多人主体、非法采矿、前科/取保后再犯、1倍赔偿和基数剔除 |
| PD-PILOT-002 | `1_digest/case_cards/CC-COURT-CHEN-GUJK-CULTURAL-RELIC.md` | `COURT_CHEN_GUJK_CULTURAL_RELIC` | 测试纯民事公益诉讼、个人行为人、劝阻后继续实施、文物/自然遗产、固定金额 25000 元 |

## 差异覆盖

| 维度 | 张某山等 32 人非法采矿案 | 陈某平生态破坏案 |
|---|---|---|
| 程序结构 | 刑事附带民事公益诉讼 | 民事公益诉讼 |
| 主体结构 | 多人共同实施 | 单一个人行为人 |
| 损害对象 | 长江禁采区河道、河床结构、水生生物等生态功能 | 文物及世界自然遗产保护范围内的人文景观 |
| 故意路径 | 前科 + 取保候审期间再犯 | 劝阻提醒后仍执意刻划 |
| 赔偿表达 | 1倍，按非法采砂数量比例分担 | 固定金额 25000 元 |
| 方法测试重点 | 裁判因素拆分和金额基数边界 | 固定金额表达与倍数化表达边界 |

## 试跑边界

本轮不是全量迁移，不生成最终规则总结。两个案例均只用于验证 TARA 能否把既有 case card 和 raw source 拆成可追溯研究零件，再形成带边界的判断包。
