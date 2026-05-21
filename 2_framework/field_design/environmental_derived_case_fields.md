# 案例卡字段派生表：生态环境侵权惩罚性赔偿

Universal fields 是所有案例都需要的字段。

Topic-specific fields 由当前主题观察要素派生。

主题字段不能未经检查就复制到其他主题。

| Field Name | Universal or Topic-Specific | Derived From Factor | Where to Fill in Case Card | Required? | Notes |
|---|---|---|---|---|---|
| 案号 | Universal | 无 | 通用案例信息 | 是 | 用于来源核验。 |
| 法院 | Universal | 无 | 通用案例信息 | 是 | 用于来源核验。 |
| 裁判日期 | Universal | 无 | 通用案例信息 | 建议 | 缺失时标记待核验。 |
| 文书类型 | Universal | 无 | 通用案例信息 | 建议 | 区分判决、裁定等。 |
| 来源角色 | Universal | 无 | 来源角色 | 是 | 区分权威案例和普通案例。 |
| 主观故意/明知 | Topic-Specific | F-001 | 主题观察字段 | 待核验 | 根据案例原文填写。 |
| 严重后果 | Topic-Specific | F-002 | 主题观察字段 | 待核验 | 根据案例原文填写。 |
| 赔偿基数 | Topic-Specific | F-003 | 主题观察字段 | 待核验 | 根据案例原文填写。 |
| 倍数裁量 | Topic-Specific | F-004 | 主题观察字段 | 待核验 | 根据案例原文填写。 |
| 行政处罚/刑事责任竞合 | Topic-Specific | F-005 | 主题观察字段 | 待核验 | 根据案例原文填写。 |
| 是否支持惩罚性赔偿 | Topic-Specific | F-006 | 主题观察字段 | 待核验 | 根据判项和法院判断填写。 |
