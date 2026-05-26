# 工作日志

## 日志格式

| 日期 | 操作 | 层级 | 文件 | 备注 |
|---|---|---|---|---|
| | | | | |

---

## 日志条目

| 日期 | 操作 | 层级 | 文件 | 备注 |
|---|---|---|---|---|
| 2026-05-20 | 项目初始化 | all | 全部 | 搭建目录结构、模板、prompt |
| 2026-05-20 | PDF批量转换 | 0_raw | 28篇论文PDF→extracted_md | pdf_to_md.py |
| 2026-05-20 | 北大法宝剪藏清理 | 0_raw | 15个案例文件 | clean_pkulaw.py，去除网页噪音 |
| 2026-05-20 | 规范卡生成 | 1_digest/rule_cards | RC-001~003 | 民法典1232条+两个司法解释 |
| 2026-05-20 | 案例卡生成 | 1_digest/case_cards | CC-001~013 | 3个agent并行生成中 |
| 2026-05-20 | 材料索引更新 | 0_raw/metadata | source-index.md | 3法+13案+28论文 |
| 2026-05-20 | 横向比较表 | 3_synthesis/cross_case_comparison | 横向比较表.md | 12案例，支持6/不支持4/不涉及3 |
| 2026-05-20 | 裁判规则总结 | 3_synthesis/rule_summary | 裁判规则总结.md | 15条规则，均有案例支撑 |
| 2026-05-20 | 论文卡生成 | 1_digest/paper_cards | PC-001~025 | 5个agent并行，25篇论文 |
| 2026-05-20 | 论文卡重编号 | 1_digest/paper_cards | PC-001~025 | 按主题分组：生态环境10、个人信息3、知识产权2、其他10 |
| 2026-05-21 | 赔偿基数公式对比 | 3_synthesis/cross_case_comparison | 赔偿基数计算公式对比分析.md | 6案对比，两条路径+虚拟治理成本法 |
| 2026-05-21 | Documentation hardening and agent operating rules | docs / all | AGENTS.md; docs/*.md; README.md | 创建 AGENTS.md 和 docs 层级说明；明确 raw/digest/framework/synthesis/output 协作规则与当前 pre 范围；本次没有做法律分析、没有生成案例、没有找材料 |
| 2026-05-21 | Clarify authoritative vs ordinary case digest routing | docs / templates | docs/case-digest-routing.md; _templates/case_card_template.md; _templates/rule_card_template.md; docs/source-lifecycle.md; docs/material-routing-rules.md; README.md | 区分权威案例与普通案例在 digest 和 synthesis 层的研究角色；本次没有生成法律内容、没有新增真实案例、没有改变核心目录结构 |
| 2026-05-21 | Introduce reusable topic configuration and adjudication factor model | docs / templates / 2_framework | docs/reusability-model.md; docs/topic-configuration-guide.md; docs/adjudication-factor-model.md; docs/framework-generation-workflow.md; _templates/topic_config_template.md; _templates/adjudication_factor_model_template.md; 2_framework/field_design/current_topic_config.md | 新增可复用性文档和观察要素模型模板；区分 project template layer 与 topic instance layer；创建当前生态环境主题实例占位文件；本次没有生成法律结论、没有新增案例、没有改动核心五层结构 |
| 2026-05-21 | Introduce adjudication factor weighting model | docs / templates / 2_framework | docs/factor-weighting-model.md; _templates/factor_weighting_model_template.md; 2_framework/adjudication_factors/environmental_punitive_damages_factor_weighting_model.md | 新增 factor weighting model 文档和模板；更新观察要素、案例字段派生、横向比较模板；增加当前生态环境主题的权重模型占位文件；本次没有生成法律结论、没有新增案例、没有改变核心五层结构 |
| 2026-05-21 | Add activatable topic config workflow | docs / templates / prompts | _templates/topic_config_template.md; _prompts/activate_topic_config_prompt.md; docs/topic-configuration-guide.md; docs/framework-generation-workflow.md; AGENTS.md; README.md | 升级 topic config 模板；新增 activate_topic_config_prompt；明确新主题启动必须先生成 current_topic_config；本次没有生成法律结论、没有新增案例、没有改变核心五层结构 |
| 2026-05-21 | Generate factor weighting draft without NotebookLM or Gemini | 2_framework/adjudication_factors | environmental_punitive_damages_factor_weighting_model.md | 基于已有 paper cards、rule cards、case cards 生成权重草稿；本次未使用 NotebookLM / Gemini；本次没有生成法律结论；本次没有新增案例；最终 Priority 仍需人工锁定 |
| 2026-05-21 | Fix canonical operating flow for all agents | docs / README / AGENTS | docs/canonical-operating-flow.md; README.md; AGENTS.md; docs/framework-generation-workflow.md | 固定项目运行流程：topic config→raw→digest→framework→pilot→lock→batch case cards→synthesis→output；要求 Codex/Claude Code/MiMo 按前置条件推进；本次没有生成法律结论、没有新增案例、没有改变核心五层结构 |
| 2026-05-21 | Add human-in-the-loop synthesis workflow | docs / templates / prompts | docs/synthesis-human-review-workflow.md; docs/claim-taxonomy-and-elevation-rules.md; _templates/synthesis_*; _templates/claim_ledger_template.md; _prompts/synthesis_* | 固定第 9 步为 AI-assisted synthesis, human-validated legal conclusion workflow；新增 evidence freeze、claim ledger、rule anchor map、risk review、human judgment memo 等模板和 prompts；本次没有生成法律结论、没有新增案例、没有改变核心五层结构 |
| 2026-05-25 | Add article spine writing gate | 3_synthesis/final_doc / docs / templates | AGENTS.md; docs/canonical-operating-flow.md; docs/synthesis-human-review-workflow.md; docs/synthesis-output-guide.md; _templates/article_spine_template.md; _templates/section_blueprint_template.md; _templates/legal_writing_rationale_matrix_template.md; _templates/final_doc_template.md | 在第 9 步 risk review 与 human judgment lock 之间新增 article spine、section blueprint、legal writing rationale matrix 写作闸门；9.1-9.4 作为 synthesis 初筛，9.7 再结合文章主线进行 human legal judgment lock；cards 仍决定证据边界，article spine 只决定表达结构；本次没有生成法律结论、没有新增案例、没有改变核心五层结构 |
| 2026-05-25 | Add normative backfill loop | 0_raw/laws / 1_digest/rule_cards / 2_framework/normative_map / 3_synthesis | AGENTS.md; docs/normative-backfill-workflow.md; docs/canonical-operating-flow.md; docs/synthesis-human-review-workflow.md; docs/source-lifecycle.md; docs/material-routing-rules.md; docs/raw-layer-guide.md; _templates/normative_backfill_review_template.md; _templates/rule_anchor_map_template.md; _templates/rule_card_template.md | 制度化从 case card、claim ledger 或 rule anchor map 发现规范缺口后的回填流程；case card 中的法条引用只能作为 backfill clue，必须回到 0_raw/laws、source-index、rule card 和 normative map 后才可作为 rule anchor；本次没有生成法律结论、没有新增真实规范材料、没有改变核心五层结构 |
