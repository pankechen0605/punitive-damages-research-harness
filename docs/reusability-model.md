# 可复用性模型

本文说明本项目如何从单一主题项目，升级为可复用的法律研究管线模板。

## 1. 两层结构

### Project Template Layer

Project Template Layer 是可复用的项目规则层。

包括：

- `README.md`
- `AGENTS.md`
- `docs/`
- `_templates/`
- `scripts/`

作用：

- 规定通用法律研究流程
- 规定层级契约
- 规定材料路由
- 规定 agent 操作规则
- 提供模板和检查清单
- 保持 raw、digest、framework、synthesis、output 的分工稳定

这一层可以被下一个研究主题继续使用。

### Topic Instance Layer

Topic Instance Layer 是当前具体研究主题层。

包括：

- `2_framework/` 中的当前主题配置、观察要素、规范地图、论文争议地图
- `3_synthesis/` 中的横向比较和最终文档
- `4_output/` 中的展示素材

作用：

- 承载某一个具体研究主题
- 把当前主题的问题、范围、材料和观察字段落实到项目中
- 服务当前 pre 或当前研究任务

这一层不能被无检查地复制到下一个主题。

## 2. 哪些东西可复用

以下内容可以复用到新主题：

- 五层结构
- source lifecycle
- material routing rules
- case digest routing
- topic config 模板
- adjudication factor model 模板
- case card 通用字段
- review checklist
- agent 操作边界
- raw 层不可污染原则

这些内容描述的是工作流，而不是当前主题的法律结论。

## 3. 哪些东西不可直接复用

以下内容不能直接复用到新主题：

- 当前生态环境主题的具体观察要素
- 当前 pre 选题范围
- 当前案例检索关键词
- 当前论文争议地图中的具体观点
- 当前案例横向比较中的结论
- 当前 final document 或 PPT 素材中的主题表达

这些内容属于当前 topic instance。新主题可以参考其结构，但不能复制其结论。

## 4. 复用新主题的流程

当研究主题从生态环境惩罚性赔偿切换到其他主题时，例如：

```text
生态环境惩罚性赔偿
→ 知识产权惩罚性赔偿
→ 产品责任惩罚性赔偿
→ 个人信息侵权赔偿
```

应复用 workflow 和模板，而不是复用旧主题结论。

推荐流程：

1. 新建 topic config。
2. 明确新主题的 scope in / scope out。
3. 收集新主题 raw 材料。
4. 生成 rule cards / paper cards。
5. 形成新主题 normative map / literature debate map。
6. 生成新主题 adjudication factor model。
7. 由观察要素派生 case card 字段和 cross-case comparison 列。
8. 试跑 2-3 个案例。
9. 人工修订并锁定 framework v1。

任何新主题都不能直接复制旧主题的“法院通常如何”类结论。
