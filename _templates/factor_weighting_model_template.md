---
type: factor_weighting_model
topic_id:
topic_name:
status: draft
version: v0.1
---

# 观察要素权重模型：{{topic_name}}

## 一、模型说明

本模型用于定义本研究主题中各观察要素的研究优先级。

本模型不是法律结论，不用于预测案件结果，不得替代真实案例分析。

## 二、权重维度说明

| 维度 | 含义 | 评分范围 | 说明 |
|---|---|---:|---|
| Normative Weight | 是否来自规范结构或构成要件 | 0-3 |  |
| Literature Weight | 是否被论文高频讨论或存在明显争议 | 0-3 |  |
| Case Observability | 是否能在裁判文书中稳定观察 | 0-3 |  |
| Discriminative Power | 是否能区分不同裁判结果或路径 | 0-3 |  |
| Task Relevance | 是否服务当前任务输出 | 0-3 |  |

## 三、Priority Level

| Priority | 含义 | 下游影响 |
|---|---|---|
| P0 | 核心要素 | case card 必填；横向比较主列；final doc 主线 |
| P1 | 重要要素 | case card 尽量填写；横向比较辅助列 |
| P2 | 辅助要素 | 有材料则填写；用于补充分析 |
| P3 | 背景要素 | 不进入主线；仅作延伸 |

## 四、观察要素权重表

| Factor ID | Factor Name | Normative | Literature | Observable | Discriminative | Task | Priority | Basis | Status | Do Not Conclude |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| | | | | | | | | | | |

## 五、权重版本记录

| Version | Date | Change | Reason | Human Reviewer |
|---|---|---|---|---|
| | | | | |

## 六、锁定状态

- 当前状态：
- 是否经过 paper card 支撑：
- 是否经过 rule card 支撑：
- 是否经过 pilot case 测试：
- 是否可以进入批量 case card：

## 七、人工核验清单

- [ ] 每个高权重要素都有 basis。
- [ ] 没有把论文观点写成法院规则。
- [ ] 没有把观察要素写成法律结论。
- [ ] P0 要素数量可控。
- [ ] P0 / P1 要素能在案例中填写。
- [ ] 已完成至少 2-3 个 pilot case 测试，或明确标记尚未完成。
