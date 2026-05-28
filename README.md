# 惩罚性损害赔偿实务判例梳理

## 项目目标

搭建一个可复用的法律研究管线，用于把"原始法律材料"逐步转化为结构化的案例卡、规范卡、论文卡、学术争议地图、裁判观察要素表、横向比较表、文档版 pre 材料，以及后续可复用的法律案例分析 workflow。

本仓库新增 **可追溯法律研究组装框架 v0.1**，作为五层目录之上的通用方法层。它用于增强来源追溯、结论边界控制、研究零件复用和跨主题迁移；当前生态环境惩罚性赔偿是一个试验主题，后续可迁移至 BEPS、Temu/PDD 双支柱、数据合规、平台合规、游戏合规等研究项目。详见 [docs/可追溯法律研究组装框架-v0.1.md](docs/可追溯法律研究组装框架-v0.1.md)。

---

## 分层结构 / Layered Structure

```
punitive-damages-research/
│
├── 0_raw/                          ← 原始材料层 / Raw Materials Layer
│   ├── laws/                       ← 法律法规 / Laws & Regulations
│   │   ├── statutes/               ← 法律条文 / Statutes
│   │   ├── judicial_interpretations/  ← 司法解释 / Judicial Interpretations
│   │   └── normative_documents/    ← 规范性文件 / Normative Documents
│   ├── authoritative_cases/        ← 权威案例 / Authoritative Cases
│   │   ├── guiding_cases/          ← 指导案例 / Guiding Cases
│   │   ├── typical_cases/          ← 典型案例 / Typical Cases
│   │   ├── reference_cases/        ← 参考性案例 / Reference Cases
│   │   └── gazette_cases/          ← 公报案例 / Gazette Cases
│   ├── ordinary_cases/             ← 普通案例 / Ordinary Cases
│   │   ├── judgments/              ← 判决书 / Judgments
│   │   └── rulings/                ← 裁定书 / Rulings
│   ├── papers/                     ← 学术论文 / Academic Papers
│   │   ├── pdf/                    ← PDF 原文 / Original PDFs
│   │   ├── extracted_md/           ← 提取的 MD / Extracted Markdown
│   │   └── notebook_exports/       ← 历史/归档导出 / Archived Notebook Exports
│   └── metadata/                   ← 元数据 / Metadata
│       └── source-index.md         ← 材料索引 / Source Index
│
├── 1_digest/                       ← 单一材料消化层 / Single-Source Digest Layer
│   ├── case_cards/                 ← 案例卡 / Case Cards
│   ├── rule_cards/                 ← 规范卡 / Rule Cards
│   ├── paper_cards/                ← 论文卡 / Paper Cards
│   └── notebook_outputs/           ← 历史/归档中间输出 / Archived Notebook Outputs
│
├── 2_framework/                    ← 跨材料观察框架层 / Cross-Source Framework Layer
│   ├── normative_map/              ← 规范地图 / Normative Map
│   ├── adjudication_factors/       ← 裁判观察要素 / Adjudication Factors
│   ├── literature_debate_map/      ← 学术争议地图 / Literature Debate Map
│   └── field_design/               ← 字段设计 / Field Design
│
├── 3_synthesis/                    ← 横向综合层 / Synthesis Layer
│   ├── cross_case_comparison/      ← 案例横向比较 / Cross-Case Comparison
│   ├── rule_summary/               ← 裁判规则总结 / Rule Summary
│   └── final_doc/                  ← 文档版材料 / Final Document
│
├── 4_output/                       ← 输出层 / Output Layer
│   ├── ppt_materials/              ← PPT 素材提纲 / PPT Material Outline
│   └── handout/                    ← 讲义 / Handout
│
├── _templates/                     ← Markdown 模板 / Templates
├── _prompts/                       ← Prompt 模板 / Prompt Templates
├── _logs/                          ← 日志 / Logs
└── scripts/                        ← 工具脚本 / Scripts
```

### 分层逻辑 / Layer Logic

```
        人工收集                AI 辅助加工              人工核验
   Human Collection    →    AI-Assisted Processing   →   Human Review
        ↓                        ↓                         ↓
   ┌─────────┐            ┌─────────────┐           ┌───────────┐
   │ 0_raw   │ ────────→ │ 1_digest    │ ────────→ │ 2_framework│
   │ 原始材料 │            │ 单一材料消化 │           │ 观察框架    │
   └─────────┘            └─────────────┘           └───────────┘
                                                          │
                                                          ↓
                              ┌─────────────┐      ┌───────────┐
                              │ 4_output    │ ←─── │ 3_synthesis│
                              │ PPT素材/讲义 │      │ 横向综合    │
                              └─────────────┘      └───────────┘
```

---

## 各层职责

### 0_raw — 原始材料层

- **只放原始材料或机器可读副本。**
- PDF 原文永远是底本。
- `extracted_md` 是为了 AI 读取方便而生成的机器可读副本，**不等同于最终摘要**。
- `notebook_exports` 仅作为历史/归档目录保留；当前流程不推荐继续依赖 NotebookLM 导出。
- **严禁把 AI 总结当成原始材料。** 任何模型生成的总结、问答、观点归纳不能放 raw，应放 `1_digest` 或 `2_framework` 并标明来源和待核验状态。

### 1_digest — 单一材料消化层

- `case_cards`：案例卡，回答"法院怎么判"。
- `rule_cards`：规范卡或裁判规则锚点，回答"规则是什么"。
- `paper_cards`：论文卡，回答"学界怎么看"。
- `notebook_outputs`：历史/归档中间输出目录；当前推荐优先使用 MCP、模板和人工核验流程。
- 权威案例与普通案例在 raw 层分类后，digest 层通过 `source_category` / `research_role` / rule anchor 继续保留其不同研究功能。详见 [docs/case-digest-routing.md](docs/case-digest-routing.md)。

### 2_framework — 跨材料观察框架层

- `normative_map`：民法典侵权责任编、特别法、司法解释、指导案例等规范地图。
- `adjudication_factors`：惩罚性赔偿裁判观察要素表。
- `literature_debate_map`：CSSCI 文献争议地图。
- `field_design`：由论文层反推出来的案例卡字段设计。

### 3_synthesis — 横向综合层

- `cross_case_comparison`：支持/不支持惩罚性赔偿的案例比较。
- `rule_summary`：裁判规则总结。
- `final_doc`：文档版 pre 材料（不做 PPT）。

### 4_output — 输出层

- `ppt_materials`：只放 PPT 素材提纲，**不制作 PPT**。
- `handout`：课堂展示或分享用的简版材料。

---

## 工具角色分工

### MiMo（AI 助手）

- 根据提供的案例文本生成**案例卡初稿**
- 根据提供的法条/司法解释文本生成**规范卡初稿**
- 检查案例卡是否存在遗漏、矛盾、无来源推断
- **不联网、不补充外部信息、不编造案例**

### NotebookLM（历史/可选）

- 上一轮实践中发现 NotebookLM 不适合作为当前主线工具。
- 相关目录仅作为历史输出或可选实验空间保留。
- 当前推荐优先使用 MCP v1、固定模板、smoke tests 和人工核验来推进研究流程。

### PDF-to-MD 脚本

- 将 PDF 论文转为 Markdown，保留页码和段落
- 输出放入 `0_raw/papers/extracted_md/`
- **只是机器可读副本，不是最终摘要**

### MCP v1（本地工作流控制器）

- 暴露项目文档、模板和 prompts 给 MCP 客户端读取
- 提供项目状态检查、前置条件检查、受控模板创建、workflow log 追加和层级边界验证
- 支持 `run_pdf_to_md` 的 dry-run-first 机械提取流程
- **不生成法律结论、不联网、不调用 LLM API、不替代人工核验**
- 详见 [mcp/README.md](mcp/README.md)、[mcp/USAGE.md](mcp/USAGE.md)、[mcp/TOOL_CATALOG.md](mcp/TOOL_CATALOG.md)

### 人工（你）

- 收集原始材料（PDF、案例、法条、论文）
- 核验 AI 生成的卡片初稿
- 做最终的法律判断和综合

---

## 推荐工作流

```
1. activate topic config，先定题和边界
        ↓
2. 0_raw 收集原始材料
        ↓
3. 1_digest 生成单材料卡片
        ↓
4. 2_framework 生成观察要素、权重和字段
        ↓
5. pilot 试跑 2-3 个案例
        ↓
6. 锁定 framework v1
        ↓
7. 批量生成 case cards
        ↓
8. 3_synthesis/cross_case_comparison 做横向比较
        ↓
9. 3_synthesis/rule_summary + final_doc 做 human-in-the-loop 规则总结 / 最终分析文档
        ↓
10. 4_output 做展示适配
```

---

## 进一步阅读 / Operating Docs

- Agent 操作规则见 [AGENTS.md](AGENTS.md)。
- 固定运行流程见 [docs/canonical-operating-flow.md](docs/canonical-operating-flow.md)。
- 可追溯法律研究组装框架见 [docs/可追溯法律研究组装框架-v0.1.md](docs/可追溯法律研究组装框架-v0.1.md)。
- 研究对象模型见 [docs/研究对象模型.md](docs/研究对象模型.md)。
- 研究组装操作规则见 [docs/研究组装操作规则.md](docs/研究组装操作规则.md)。
- 质量评价模型见 [docs/质量评价模型.md](docs/质量评价模型.md)。
- 法律研究工作流设计清单见 [docs/法律研究工作流设计清单.md](docs/法律研究工作流设计清单.md)。
- 详细层级契约见 [docs/layer-contracts.md](docs/layer-contracts.md)。
- 材料路由规则见 [docs/material-routing-rules.md](docs/material-routing-rules.md)。
- raw 层边界见 [docs/raw-layer-guide.md](docs/raw-layer-guide.md)。
- digest 层规则见 [docs/digest-layer-guide.md](docs/digest-layer-guide.md)。
- framework 层说明见 [docs/framework-layer-guide.md](docs/framework-layer-guide.md)。
- synthesis 与 output 区分见 [docs/synthesis-output-guide.md](docs/synthesis-output-guide.md)。
- 材料生命周期见 [docs/source-lifecycle.md](docs/source-lifecycle.md)。
- 增量案例进入流程见 [docs/incremental-case-intake-workflow.md](docs/incremental-case-intake-workflow.md)。
- 人工核验清单见 [docs/human-review-checkpoints.md](docs/human-review-checkpoints.md)。
- 第 9 步 synthesis 人工审查流程见 [docs/synthesis-human-review-workflow.md](docs/synthesis-human-review-workflow.md)。
- claim 层级与升格规则见 [docs/claim-taxonomy-and-elevation-rules.md](docs/claim-taxonomy-and-elevation-rules.md)。
- 当前 pre 范围见 [docs/current-pre-scope.md](docs/current-pre-scope.md)。

---

## Reusability / 可复用性

本项目区分 project template layer 与 topic instance layer。当前生态环境惩罚性赔偿是一个 topic instance。通用复用规则见 [docs/reusability-model.md](docs/reusability-model.md)、[docs/topic-configuration-guide.md](docs/topic-configuration-guide.md)、[docs/adjudication-factor-model.md](docs/adjudication-factor-model.md)、[docs/framework-generation-workflow.md](docs/framework-generation-workflow.md)。

观察要素模型定义“看什么”，观察要素权重模型定义“优先看什么”。详见 [docs/adjudication-factor-model.md](docs/adjudication-factor-model.md) 和 [docs/factor-weighting-model.md](docs/factor-weighting-model.md)。

新主题启动前，应先通过 [_prompts/activate_topic_config_prompt.md](_prompts/activate_topic_config_prompt.md) 激活 topic config；详见 [docs/topic-configuration-guide.md](docs/topic-configuration-guide.md)。

---

## 严禁事项

1. **严禁把 AI 总结当成原始材料。**
2. **严禁无来源法律结论。** 所有法律判断必须有出处。
3. **严禁编造案例、法条、论文。** 不确定就写"待核验"。
4. **严禁在 raw 层放入模型总结。** raw 层只放原始材料。
5. **严禁从少量案例过度概括规则。** 横向比较必须有足够案例支撑。
