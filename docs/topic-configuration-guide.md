# Topic Configuration 使用指南

## Topic Config 的作用

Topic Config 是主题实例的入口文件。它记录当前研究主题的范围、问题、材料需求、任务约束和预期产出。

Topic Config 不是研究结论，不放案例事实，不写法院规则。

## Topic Config 必填项

- `topic_id`
- `topic_name`
- `research_question`
- `scope_in`
- `scope_out`
- `normative_sources_needed`
- `literature_questions`
- `case_search_targets`
- `task_constraints`
- `expected_outputs`
- `human_review_points`
- `status`

## Topic Config 与各层关系

- 它不放 raw。
- 它属于 `2_framework/field_design`。
- 它会指导 case card 字段设计。
- 它会指导 cross-case comparison 表列设计。
- 它不能直接生成法律结论。

Topic Config 是 topic instance 的起点。后续的 normative map、literature debate map、adjudication factor model 和 derived case fields 都应能回到它。

## 新主题启动步骤

1. 通过 `_prompts/activate_topic_config_prompt.md` 激活 topic config。
2. 收集 raw 材料。
3. 生成 rule cards / paper cards。
4. 形成 normative map / literature debate map。
5. 生成观察要素模型。
6. 派生 case card 字段。
7. 试跑 2-3 个案例。
8. 修订观察要素。
9. 锁定 framework v1。

## 使用边界

Topic Config 可以写研究问题和材料需求，但不能写“法院通常认为”。

Topic Config 可以写预期要观察的变量，但不能把变量的可能答案提前确定为法律结论。

Topic Config 不直接定义最终权重，但可以影响 Task Relevance。

例如：

- 课堂 pre
- 论文研究
- 案例实证
- 面试作品集
- 内部 memo

不同任务会改变观察要素的 Task Relevance。最终 Priority 仍需结合规范基础、文献讨论、案例可观察性和区分能力。

## 可激活的 Topic Config 流程

topic config 不应直接由 AI 自由生成。

新主题启动时，应通过 `_prompts/activate_topic_config_prompt.md` 引导用户回答后生成。

提问顺序应保持为：

1. 先问研究边界。
2. 再问材料和案例。
3. 最后问输出和限制。

Topic Config 是后续观察要素、权重、case card 字段和横向比较表的上游配置。

`current-pre-scope.md` 可以从 topic config 派生，但不等于 topic config。前者是当前 pre 的展示范围约束，后者是整个 topic instance 的入口配置。

如果用户回答不足，应使用“待确认”占位，而不是让 AI 自行补全。
