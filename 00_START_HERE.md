# 从这里开始

## 第一步：放入原始材料

在开始任何分析之前，你需要先收集并放入原始材料。

### 法条和司法解释

放入 `0_raw/laws/` 目录：
- `statutes/` — 法律条文（如民法典第 1185 条、第 1207 条、第 1232 条等）
- `judicial_interpretations/` — 司法解释
- `normative_documents/` — 规范性文件

### 案例

放入 `0_raw/authoritative_cases/` 或 `0_raw/ordinary_cases/`：

| 类型 | 目录 | 说明 |
|---|---|---|
| 指导案例 | `authoritative_cases/guiding_cases/` | 最高法发布的指导案例，效力最高 |
| 典型案例 | `authoritative_cases/typical_cases/` | 最高法发布的典型案例 |
| 参考性案例 | `authoritative_cases/reference_cases/` | 各地高院发布的参考性案例 |
| 公报案例 | `authoritative_cases/gazette_cases/` | 最高法公报刊登的案例 |
| 普通判决 | `ordinary_cases/judgments/` | 一般裁判文书 |
| 普通裁定 | `ordinary_cases/rulings/` | 一般裁定文书 |

**权威案例和普通案例必须分开存放，不能混在一起。**

### 论文

放入 `0_raw/papers/`：
- `pdf/` — CSSCI 论文 PDF 原文
- `extracted_md/` — PDF 转 Markdown 后的机器可读副本（用 `scripts/pdf_to_md.py` 生成）
- `notebook_exports/` — NotebookLM 导出的带来源定位的摘录

---

## PDF 和 extracted_md 的关系

- **PDF 原文是底本**，永远保留在 `pdf/` 目录。
- `extracted_md` 是用脚本从 PDF 提取的纯文本版本，方便 AI 读取。
- `extracted_md` 不是最终摘要，只是机器可读副本。
- 如果 PDF 是扫描件，脚本可能提取不到文字，会标记 `[NO TEXT EXTRACTED - OCR MAY BE REQUIRED]`。

---

## 最小可运行版本

本次 pre 的最小目标：

| 材料类型 | 数量 | 放入位置 |
|---|---|---|
| 规范来源 | 3 个 | `0_raw/laws/` |
| 案例 | 5-8 个 | `0_raw/authoritative_cases/` + `0_raw/ordinary_cases/` |
| CSSCI 论文 | 3-5 篇 | `0_raw/papers/` |
| 横向比较表 | 1 张 | `3_synthesis/cross_case_comparison/` |
| 裁判规则总结 | 1 份 | `3_synthesis/rule_summary/` |
| PPT 素材提纲 | 1 份 | `4_output/ppt_materials/` |

---

## 下一步

1. 把你收集的 PDF 和案例文件放入 `0_raw/` 对应目录。
2. 更新 `0_raw/metadata/source-index.md`，记录每个材料的基本信息。
3. 对论文 PDF 运行 `scripts/pdf_to_md.py` 生成 extracted_md。
4. 把案例文本提供给 MiMo，生成案例卡初稿。
5. 把论文上传到 NotebookLM，生成争议地图初稿。
