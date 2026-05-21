# Raw 层使用指南

## 1. raw 层定义

`0_raw` 是项目的材料底座。它只保存原始法律材料、论文原文、裁判文书原文，以及为了 AI 读取而生成的机器可读副本。

raw 层不负责解释材料，不负责总结观点，也不负责形成研究结论。

## 2. raw 层与 extracted_md 的关系

PDF 原文是底本，`extracted_md` 是机器可读副本。

正确示例：

- `0_raw/papers/pdf/PAPER-001.pdf`
- `0_raw/papers/extracted_md/PAPER-001.extracted.md`

`extracted_md` 可以进入 raw，是因为它只是从 PDF 提取出的文本。它不应包含“本文认为”“学界普遍认为”等模型生成语言，除非这些文字原本就在论文中。

## 3. raw 层与 AI 总结的边界

AI 总结不能进入 raw。

错误示例：

- 把 Gemini 总结的“学界认为……”放进 `0_raw`
- 把 MiMo 生成的 case card 放进 `0_raw`
- 把 NotebookLM 的问答、归纳、观点地图放进 `0_raw`

允许进入 raw 的 AI 或工具产物只有一种：明确的机器可读副本，例如 PDF-to-MD 文本，并且没有加入模型总结。

## 4. source-index.md 如何维护

每个重要材料入库后，应更新 `0_raw/metadata/source-index.md`。

建议记录：

- Source ID
- 类型
- 文件路径
- 标题或名称
- 作者、法院或发布机关
- 日期
- 备注
- 是否已转 MD
- 是否已生成卡片

如果某项信息缺失，不要补猜，应写“待核验”。

## 5. 文件命名建议

文件名应尽量同时满足可读和可追溯。

建议：

- 法条：规范名称或核心条文名
- 案例：案例名称或当事人简称加来源
- 论文：论文标题加作者
- PDF 与 extracted_md 尽量同名

避免：

- `新建文档.md`
- `案例1.md`
- `总结.md`
- 无法判断来源的长串复制文件名

## 6. 什么情况下需要保留原始 PDF

以下情况必须保留 PDF：

- 论文作为项目论证来源
- PDF 是唯一可核验底本
- extracted_md 可能有缺字、乱序、页码丢失
- 后续需要核对页码、引文或作者原意

原则：PDF 永远优先于 extracted_md。

## 7. 什么情况下需要生成 extracted_md

以下情况建议生成 extracted_md：

- 需要 AI 读取论文全文
- 需要批量检索关键词
- 需要制作 paper card
- PDF 文本层可提取，且转换结果基本可读

如果 PDF 是扫描件，脚本可能输出 `[NO TEXT EXTRACTED - OCR MAY BE REQUIRED]`，此时应标记待 OCR，不要让 AI 根据空文本生成论文卡。

## 8. 什么情况下材料不能进入 raw

不能进入 raw 的材料包括：

- AI 生成的摘要
- NotebookLM 总结
- Gemini 争议地图
- MiMo case card
- 人工综合判断
- PPT 提纲
- 阶段 handoff
- 没有来源的案例或论文信息

这些材料应根据功能放入 `1_digest`、`2_framework`、`3_synthesis`、`4_output` 或 `docs`。

## 9. raw 层污染示例

污染示例一：

把“法院通常认为行政处罚不能免除惩罚性赔偿”写进某个案例原文文件。

污染示例二：

将 NotebookLM 对 10 篇论文的总结保存为 `0_raw/papers/notebook_exports/争议地图.md`。

污染示例三：

将 MiMo 生成的案例卡命名为“某某案原文.md”放入 `0_raw/ordinary_cases/judgments/`。

污染示例四：

把人工为 pre 写的“展示主线”放进 `0_raw/laws/`。

## 10. raw 层检查清单

- [ ] 这是原始材料或忠实机器可读副本吗？
- [ ] 是否有来源信息？
- [ ] 是否已经放入正确子目录？
- [ ] 是否需要更新 `source-index.md`？
- [ ] PDF 与 extracted_md 是否能对应？
- [ ] 是否混入 AI 总结或人工判断？
- [ ] 不确定信息是否标记为“待核验”？
