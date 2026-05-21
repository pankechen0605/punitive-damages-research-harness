# 材料路由规则

当一个材料进入项目时，先判断它是原始材料、机器可读副本、单一材料消化结果、框架材料、综合材料，还是展示材料。不要因为文件看起来“有用”就直接放入 `0_raw`。

| 材料类型 | 放入位置 | 是否可由 AI 生成 | 是否可进入 raw | 备注 |
|---|---|---|---|---|
| 民法典条文 | `0_raw/laws/statutes/` | 否 | 是 | 应保存原文或人工整理的忠实摘录，并记录来源。 |
| 司法解释 | `0_raw/laws/judicial_interpretations/` | 否 | 是 | 应保存原文，不加入解释性总结。 |
| 规范性文件 | `0_raw/laws/normative_documents/` | 否 | 是 | 只放规范原文或忠实摘录。 |
| 指导案例 | `0_raw/authoritative_cases/guiding_cases/` | 否 | 是 | 原文入 raw；digest 层生成 case card + rule anchor。 |
| 典型案例 | `0_raw/authoritative_cases/typical_cases/` | 否 | 是 | 原文入 raw；digest 层生成 case card + rule anchor；不得当成统计样本。 |
| 人民法院案例库参考案例 | `0_raw/authoritative_cases/reference_cases/` | 否 | 是 | 原文入 raw；digest 层生成 case card + rule anchor；保持与 source-index 一致。 |
| 公报案例 | `0_raw/authoritative_cases/gazette_cases/` | 否 | 是 | 原文入 raw；digest 层生成 case card + rule anchor。 |
| 普通判决书 | `0_raw/ordinary_cases/judgments/` | 否 | 是 | 原文入 raw；digest 层生成 case card only，作为实务样本。 |
| 普通裁定书 | `0_raw/ordinary_cases/rulings/` | 否 | 是 | 原文入 raw；digest 层生成 case card only，作为实务样本。 |
| CSSCI 论文 PDF | `0_raw/papers/pdf/` | 否 | 是 | PDF 是底本，尽量长期保留。 |
| PDF 转出来的 extracted_md | `0_raw/papers/extracted_md/` | 可由脚本生成 | 是 | 只是机器可读副本，不是摘要，不得加入模型观点。 |
| NotebookLM 原文摘录导出 | `0_raw/papers/notebook_exports/` | 可由工具导出 | 有条件 | 只限带来源定位的原文摘录或片段。 |
| NotebookLM 总结 | `1_digest/notebook_outputs/` 或 `2_framework/` | 是 | 否 | 不能放 raw。 |
| Gemini 争议地图 | `2_framework/literature_debate_map/` | 是 | 否 | 属于观察框架草稿，不是原始材料。 |
| MiMo 案例卡初稿 | `1_digest/case_cards/` | 是 | 否 | 必须标记来源和待核验项。 |
| 人工核验后的案例卡 | `1_digest/case_cards/` | 可由 AI 起草，人工核验 | 否 | 仍属于 digest，不回流 raw。 |
| 横向比较表 | `3_synthesis/cross_case_comparison/` | 可由 AI 辅助 | 否 | 必须能回溯 case cards。 |
| 最终文档版材料 | `3_synthesis/final_doc/` | 可由 AI 辅助 | 否 | 是综合产物，不是 raw。 |
| PPT 素材提纲 | `4_output/ppt_materials/` | 可由 AI 辅助 | 否 | 只做展示适配，不新增结论。 |
| 老师课堂原始录音/课件 | 可新建合适 raw 子目录前先人工确认，或暂存外部 | 否 | 有条件 | 若作为原始课堂材料入库，应保留原文件和来源信息。 |
| 老师课堂整理笔记 | `2_framework/field_design/` 或 `docs/current-pre-scope.md` | 可由人工或 AI 整理 | 否 | 如果不是原始材料，不应进入 raw。 |
| 本项目阶段摘要 / handoff | 根目录、`docs/` 或 `_logs/` | 可由 AI 辅助 | 否 | 用于协作交接，不是研究材料底本。 |

## 快速判断

- 如果它是原文或忠实机器可读副本，才可能进入 `0_raw`。
- 如果它回答“这个单一材料说了什么”，进入 `1_digest`。
- 如果它回答“我们应该怎么看材料”，进入 `2_framework`。
- 如果它回答“多个材料放在一起说明什么”，进入 `3_synthesis`。
- 如果它回答“课堂或组员怎么使用”，进入 `4_output`。
