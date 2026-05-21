# Synthesis Review Prompt

## 目标

检查 synthesis draft / final_doc 草稿是否遵守 human-in-the-loop synthesis 规则。

只使用提供的材料，不得搜索、补充或编造案例、法条、论文、法院观点或法律结论。

## 检查清单

- 是否只使用 provided materials？
- 是否区分 case observation / tentative pattern / rule anchor / final legal conclusion？
- 是否每个 claim 都能回溯到 case cards / rule cards / paper cards？
- 是否把论文观点写成 court rule？
- 是否把 ordinary case 单独当作 rule anchor？
- 是否从少量案例过度概括？
- 是否标记不确定内容为“待核验”？
- 是否存在没有 human sign-off 的 final legal conclusion？
- 是否存在 output-layer language 强化 synthesis-layer conclusion？

## 输出格式

```
## 审稿报告

### 整体评价
- 通过 / 需要修改 / 需要重写

### 问题列表
| 问题编号 | 问题类型 | 具体位置 | 问题描述 | 修改建议 |
|---|---|---|---|---|
| S-001 | | | | |

### 修改建议摘要
-
```
