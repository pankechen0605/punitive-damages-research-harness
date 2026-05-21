# Claim Taxonomy and Elevation Rules

本文定义第 9 步 synthesis 中的 claim 层级，以及从观察到结论的升格规则。

## 1. Case Observation

### 定义

从一个或多个 case cards 中直接观察到的事实、裁判说理、赔偿结果或法院关注因素。

### 允许来源

- case cards
- cross-case comparison 中可回溯到 case cards 的字段

### 允许语言

- “在 C-001 案中，法院在说理部分提及……”
- “在当前样本中，若干案件显示……”

### 禁止语言

- “法院通常认为……”
- “裁判规则是……”
- “司法实践已经确立……”

### 是否需要 human sign-off

进入 final report 前需要人工确认来源和表述范围。

### 是否可进入 final synthesis report

可以，但只能作为 observation，不得自动升格为法律结论。

## 2. Tentative Pattern

### 定义

多个 case observations 之间呈现出的可能规律，但尚未获得足够规范支撑。

### 允许来源

- 多个 case observations
- cross-case comparison
- factor model
- factor weighting model

### 允许语言

- “在当前样本范围内，似乎可以观察到……”
- “该模式可能说明……，但仍需结合 rule anchors 和更多样本确认。”

### 禁止语言

- “规则是……”
- “法院一贯认为……”
- “司法实践已经确立……”

### 是否需要 human sign-off

需要。是否保留为 tentative pattern，由人决定。

### 是否可进入 final synthesis report

可以，但必须保留样本范围和不确定性。

## 3. Rule Anchor

### 定义

能够为法律判断提供规范支撑的材料。

### 允许来源

- 法律条文
- 司法解释
- 指导性案例
- 公报案例
- 典型案例
- 参考案例
- 其他权威规范材料

### 允许语言

- “该判断的规范锚点包括……”
- “该 rule anchor 支撑的是……，但不直接解决……”

### 禁止语言

- 用普通案例替代 rule anchor。
- 用论文观点替代 rule anchor。
- 无限扩大 rule anchor 的适用范围。

### 是否需要 human sign-off

需要。人必须判断 rule anchor 的适用范围和支撑强度。

### 是否可进入 final synthesis report

可以，通常作为 legal conclusion 的规范支撑。

## 4. Final Legal Conclusion

### 定义

经过人工判断后，可以写入最终 synthesis report 的法律分析结论。

### 允许来源

- rule anchors
- case observations
- tentative patterns
- paper cards
- human legal judgment memo

### 必要条件

- 有明确来源。
- 有 rule anchor，或充分说明为何没有 rule anchor。
- 有样本范围限制。
- 处理过反例和不确定性。
- 经过 human sign-off。

### 允许语言

- “综合 rule anchors 与当前样本，可以谨慎认为……”
- “在本研究范围内，更稳妥的结论是……”
- “尚不能得出……，但可以观察到……”

### 禁止语言

- 没有人类确认时写成最终结论。
- 省略样本范围。
- 删除反向材料或限制条件。

### 是否需要 human sign-off

必须。

### 是否可进入 final synthesis report

只有 human-confirmed legal conclusions 可以进入。

## Claim Elevation Rules

```text
单个普通案例 → case observation only
多个普通案例 → at most tentative pattern
普通案例 + rule anchor + 人工确认 → possible final legal conclusion
```

规则：

- Academic papers 只能作为 scholarly interpretation，不是 court rules。
- Rule anchors 必须来自规范或权威材料。
- Final legal conclusions require human sign-off。
- Frequency does not equal normativity。
- 高频出现只说明样本频率，不等于法律规则。

## Strong Language Warning

以下表达必须自动标记风险：

- 一贯认为
- 普遍认为
- 通常应当
- 裁判规则是
- 司法实践已经确立
- 法院均认为
- 可以得出规则
- 当然适用
- 必然导致

这些表达只有在有 rule anchor、足够样本、反例检查和 human sign-off 时才可以考虑使用。
