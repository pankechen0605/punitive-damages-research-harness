# Incremental Case Intake Workflow

本文规定初始批量研究完成后，如何接收新增案例，包括组员提交的案例。

核心规则：

```text
New cases must not directly modify final legal conclusions, framework locks, or output documents.
```

新增案例必须先经过：

```text
case submission
→ intake review
→ raw source preservation
→ case card generation
→ human verification
→ comparison delta
→ synthesis impact review
→ human decision
```

## 为什么需要 intake workflow

初始批量研究通常在 framework v1 lock 后进行。此时 case card 字段、横向比较列、权重模型和 synthesis 判断已经形成一套相对稳定的工作结构。

如果新增案例直接进入 case cards、rule summary 或 output，会产生风险：

- 新案例未经核验，污染样本。
- 新案例重复或不在 scope 内。
- 新案例只支持展示效果，却未经过 synthesis 审查。
- 新案例推翻或削弱既有 tentative pattern，但没有被记录。
- output 层先更新，反向污染 synthesis 层。

因此，新增案例必须作为 incremental update 处理，而不是直接插入最终结论。

## Initial Batch Mode 与 Incremental Update Mode

| 模式 | 使用场景 | 主要目标 | 关键控制 |
|---|---|---|---|
| Initial Batch Mode | framework v1 lock 后批量整理第一批案例 | 形成基础 case cards 和横向比较 | 按 locked framework 统一填写 |
| Incremental Update Mode | 后续新增案例、组员补充案例、发现新材料 | 判断新增案例是否影响既有 synthesis | intake review + synthesis delta review + human decision |

## Group-Submitted Cases

组员提交案例时，不得直接放入 `1_digest/case_cards`。

建议流程：

1. 组员填写 `case_submission_form_template.md`。
2. 将原始来源放入 `0_raw` 或提供可核验 source path。
3. 由 AI 进行 intake triage 草稿。
4. 人工完成 intake review。
5. 被接受后，才生成 case card draft。
6. case card 经人工核验后，才进入 comparison delta。

## Required Stages

### 1. Case Submission

输入：

- 组员提交的案例信息
- source link / file path
- 初步相关性说明

输出：

- case submission form

禁止：

- 不得直接写入 final_doc。
- 不得直接更新 cross-case comparison。

### 2. Scope / Duplicate / Source Check

输入：

- case submission form
- current topic config
- existing source index
- existing case cards

输出：

- case intake review

检查：

- 是否属于当前 scope。
- 是否重复。
- 是否有可靠来源。
- 是否缺少案号、法院、日期、原文等基本信息。

### 3. Raw Source Preservation

输入：

- 已通过 intake 的案例来源

输出：

- preserved raw source in `0_raw`
- updated source index, if applicable

禁止：

- 不得把 AI 摘要当作 raw source。
- 不得用无法核验的转述替代原始来源。

### 4. Case Card Drafting

输入：

- preserved raw source
- locked derived case fields

输出：

- draft case card

禁止：

- 不得补写缺失事实。
- 不得生成横向结论。
- 不得把普通案例写成 rule anchor。

### 5. Human Verification

输入：

- draft case card
- raw source

输出：

- verified case card / need_verify case card

人工检查：

- 案号、法院、日期是否可靠。
- 事实、判项、说理是否忠于原文。
- 不确定内容是否标记“待核验”。

### 6. Comparison Delta

输入：

- verified case card
- existing cross-case comparison
- factor model / weighting model

输出：

- comparison delta notes

目标：

- 判断新增案例影响哪些 comparison fields。
- 不直接改写 rule summary。

### 7. Synthesis Impact Assessment

输入：

- verified case card
- comparison delta
- existing claim ledger / rule summary / final_doc

输出：

- synthesis delta review

分类：

- no impact
- minor supplement
- contrary evidence
- framework gap

### 8. Human Decision

输入：

- synthesis delta review

输出：

- human decision

可能决定：

- archive only
- update comparison table
- create synthesis delta
- revise framework

## Possible Outcomes

| Outcome | Meaning | Next Step |
|---|---|---|
| reject as out of scope | 与 current topic config 不符 | 不进入 case cards |
| mark as duplicate | 已有相同或实质相同案例 | 记录重复，不新增样本 |
| mark as need_verify | 来源或字段不足 | 暂不进入 synthesis |
| accept as additional sample with no synthesis impact | 可作为样本，但不影响既有判断 | 可更新 case inventory 或备注 |
| accept and trigger synthesis delta | 对既有 claim 或 comparison 有影响 | 生成 synthesis delta review |
| accept and trigger framework revision | 暴露现有 factor model / weighting model 缺口 | 回到 framework revision |

## Non-Contamination Rules

- 新案例不能直接修改 final legal conclusions。
- 新案例不能直接修改 framework lock。
- 新案例不能直接修改 output documents。
- 新案例不能绕过 raw preservation 和 human verification。
- output-layer documents cannot be updated to reflect new cases unless synthesis-layer review has been completed.

## Minimal File Flow

```text
_templates/case_submission_form_template.md
→ _templates/case_intake_review_template.md
→ 0_raw preserved source
→ 1_digest/case_cards draft
→ verified case card
→ _templates/synthesis_delta_review_template.md
→ human decision
→ optional comparison / synthesis update
```
