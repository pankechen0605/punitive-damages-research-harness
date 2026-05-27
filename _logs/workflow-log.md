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
| 2026-05-27 | Add MCP layer validation tools | mcp / validation | mcp/tools/validators.py; mcp/server.py; mcp/smoke_test.py; mcp/README.md | PR-MCP-3: 新增只读启发式验证工具 validate_layer_boundary、validate_digest_card、validate_synthesis_claims；仅检查层级边界、来源可追溯性和过度提升风险，不修改研究文件、不写入 0_raw、不生成法律结论、不联网、不调用 LLM API。 |
| 2026-05-27 | Add MCP PDF extraction wrapper | mcp / 0_raw/extracted_md | mcp/tools/pdf.py; mcp/server.py; mcp/smoke_test.py; mcp/README.md | PR-MCP-4: 新增 run_pdf_to_md 受控工具，默认 dry_run，仅允许将 0_raw 下 PDF 提取为 0_raw/extracted_md 下 Markdown 机器可读副本；不修改原始 PDF、不摘要、不生成 digest cards、不生成法律分析、不联网、不调用 LLM API。 |
| 2026-05-27 | Finalize MCP v1 docs and smoke test | mcp / docs | mcp/USAGE.md; mcp/TOOL_CATALOG.md; mcp/V1_COMPLETION.md; mcp/smoke_v1.py; mcp/README.md | PR-MCP-5: 新增 MCP v1 接入文档、工具清单、完成说明和端到端 smoke test；不新增研究生成能力、不生成法律结论、不联网、不调用 LLM API、不修改 0_raw 原始材料。 |
| 2026-05-27 | Update homepage for current workflow | README / docs | README.md | 将 NotebookLM 调整为历史/可选工具说明，新增 MCP v1 首页入口；本次仅更新项目说明，不生成法律内容、不修改原始材料。 |
| 2026-05-27 | MCP v1 pilot: 新增真实案例 | 0_raw / 1_digest | 0_raw/authoritative_cases/typical_cases/最高人民检察院发布10件生态环境和资源保护检察公益诉讼起诉典型案例之八：湖北省武汉市人民检察院诉某建工集团等非法采矿破坏生态环境民事公益诉讼案-北大法宝V6官网.md; 1_digest/case_cards/CC-SPP-TYPICAL-WUHAN-ILLEGAL-MINING.md | pilot/add-real-case-001 分支；选择 SPP_TYPICAL_WUHAN_ILLEGAL_MINING 作为 pilot 案例；原始材料为文本格式（非PDF），无需提取；创建并填写 case card；case card 的 digest card validator 和 layer boundary validator 通过；raw-layer validator 返回 false positive（北大法宝页面残留"大数据分析"等 chrome 文本触发启发式规则，非 AI 分析污染、非案例卡内容问题）；修正源文件分类：guiding_cases→typical_cases；更新 source-index.md；未扩展 MCP 功能、未生成 final report、未生成横向结论；case card 内容均有案例文本依据。 |
