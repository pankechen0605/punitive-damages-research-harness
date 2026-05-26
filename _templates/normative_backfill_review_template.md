# Normative Backfill Review：{{topic_name}}

> 本模板用于记录从 case card、claim ledger 或 rule anchor map 发现规范缺口后的回填过程。它不生成法律结论。

## 一、Trigger

| Item | Content |
|---|---|
| Backfill Review ID | |
| Trigger Stage | case card / claim ledger / rule anchor map / risk review / article spine / other |
| Trigger Source | |
| Detected Normative Clue | |
| Why Existing Rule Cards Are Insufficient | |

## 二、Backfill Clue Classification

| Clue | Appears In | Clue Type | Verification Status | Notes |
|---|---|---|---|---|
| | case card / claim / pattern / risk review | statute / judicial interpretation / normative document / authoritative case rule / other | pending / verified / not found | |

## 三、Raw Source Preservation

| Source ID | Source Type | Raw Location | Source URL / Citation | Version / Effective Date | Status |
|---|---|---|---|---|---|
| | statute / judicial_interpretation / normative_document / authoritative_case | `0_raw/laws/...` | | | pending / preserved / not found |

## 四、Digest and Framework Updates

| Required Update | File | Status | Notes |
|---|---|---|---|
| Update source-index | `0_raw/metadata/source-index.md` | pending / done / not applicable | |
| Generate/update rule card | `1_digest/rule_cards/` | pending / done / not applicable | |
| Update normative map | `2_framework/normative_map/` | pending / done / not applicable | |
| Update rule anchor map | `3_synthesis/rule_summary/` or current rule anchor map | pending / done / not applicable | |
| Rerun risk review | `3_synthesis/rule_summary/` or current risk review | pending / done / not applicable | |

## 五、Rule Anchor Impact

| Claim / Pattern ID | Before Backfill Status | After Backfill Status | Supported Proposition | Still Unsupported | Human Review Needed |
|---|---|---|---|---|---|
| | anchor gap / pending / weak | pending / supported / still unsupported | | | yes / no |

## 六、Constraints

- case card 中的法条引用只能作为 clue，不能直接作为 rule anchor。
- 未找到规范原文时，必须标记“待核验”。
- 回填不能改变 case card 的单案忠实记录。
- 回填不能为了文章主线新增无来源法律结论。

## 七、Reviewer Decision

| Decision Item | Decision | Reviewer | Date | Notes |
|---|---|---|---|---|
| Backfill complete? | yes / no / pending verification | | | |
| May rule anchor mapping continue? | yes / no / limited | | | |
| Claim strength adjustment needed? | yes / no | | | |
