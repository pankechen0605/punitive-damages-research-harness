# Synthesis 与 Output 使用指南

## 二者的区别

`3_synthesis` 是研究综合层，负责横向比较、human-in-the-loop 规则总结和最终分析文档。

`4_output` 是展示适配层，负责把已经形成的研究结果转成课堂、组员或讲义可以使用的表达。

一句话区分：

```text
3_synthesis 负责“研究上能说什么”。
4_output 负责“已经确认的研究内容怎么展示”。
```

## 3_synthesis 可以做什么

`3_synthesis` 允许：

- 做横向比较
- 总结支持或不支持惩罚性赔偿的裁判因素
- 比较赔偿基数、倍数、责任竞合处理
- 形成最终文档版 pre 材料
- 标记证据不足或待核验的问题
- 通过 human legal judgment memo 锁定 final legal conclusions

`3_synthesis` 必须引用或回溯：

- case cards
- rule cards
- paper cards
- framework 中的观察维度

如果一个结论无法回到卡片或原始材料，应标记“待核验”，不能写成确定规则。

## 4_output 可以做什么

`4_output` 只做展示适配：

- 生成 PPT 素材提纲
- 生成讲义
- 将复杂表格压缩成课堂可读版本
- 调整讲述顺序
- 划分组员发言材料

`4_output` 不新增实质结论。

`4_output` 不能强化、弱化、改写或发明 `3_synthesis` 中的法律结论。

## output 层不能反向污染 synthesis 层

output 层不能为了讲得好听、节奏更顺或观点更鲜明，反向修改、强化或软化 `3_synthesis` 中的研究判断。

如果在制作展示材料时发现问题，应回到对应层级处理：

- 原文缺失：回到 `0_raw`
- 单案字段缺失：回到 `1_digest`
- 观察维度不清：回到 `2_framework`
- 横向结论支撑不足：回到 `3_synthesis`

不要在 `4_output` 里直接补一个看似漂亮但无来源的结论。

## 常见错误

- 在 PPT 提纲中新增没有案例支撑的判断
- 为了压缩时间，删除所有不确定性
- 把引入材料扩展成新主线
- 把论文争议当成法院规则讲给听众
- 让展示稿比研究底稿更确定、更夸张
