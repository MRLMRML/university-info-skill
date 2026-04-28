# 线上搜索策略

本 Skill 采用「本地缓存 + 按需实时补充」架构。本地数据覆盖中国 148 所高校 + 全球 164 所国际高校，其余数据在用户查询时自动通过 web search 实时获取。

## 搜索关键词模板 - 中国高校

| 查询类型 | 搜索关键词 | 优先目标网站 |
|----------|-----------|-------------|
| 就业数据 | "{高校} 就业质量报告 {当前年份-1}" | 各校就业信息网 |
| 科研数据 | "{高校} 科研经费 OR 重点实验室" | 各校官网/科研处 |
| 招生数据 | "{高校} 招生简章 {当前年份}" | 阳光高考平台 |
| 排名数据 | "{高校} 排名 软科 OR 校友会 {当前年份}" | 软科/校友会官网 |
| 分数线 | "{高校} {省份} {年份} 录取分数线" | 各省教育考试院 |
| 师资数据 | "{高校} 院士 杰青 师资队伍" | 各校人事处/官网 |

## 搜索关键词模板 - 国际高校

| 查询类型 | 搜索关键词 | 优先目标网站 |
|----------|-----------|-------------|
| 排名 | "{University} QS ranking {year}" | topuniversities.com |
| 录取 | "{University} acceptance rate GPA requirements" | 各校官网 admission 页面 |
| 学费 | "{University} tuition fees international students" | 各校官网 fees 页面 |
| 就业 | "{University} career outcomes employment report" | 各校官网 career services |
| 学科 | "{University} {subject} QS subject ranking" | topuniversities.com |
| 奖学金 | "{University} scholarships international students" | 各校官网 financial aid |
| 生活成本 | "{city} cost of living students {year}" | numbeo.com / expatistan.com |
| 安全 | "{city} crime rate safety students" | numbeo.com |

## 搜索关键词模板 - 学术会议/赛事

| 查询类型 | 搜索关键词 | 优先目标网站 |
|----------|-----------|-------------|
| 会议信息 | "{会议名} {年份} deadline acceptance rate" | 官网 / wikicfp.com |
| 赛事信息 | "{赛事名} 报名时间 参赛要求" | 官网 |
| 赛事含金量 | "{赛事名} 含金量 认可度 保研加分" | 知乎 / 各校政策 |

## 注意事项

- 优先使用权威数据源（教育部、各校官网、QS/THE/ARWU 官网）
- 明确标注数据年份
- 国际排名以 QS 为主要参考，THE/ARWU 为辅助
- 多个来源数据有冲突时，优先信任官方来源
- 线上搜索补充的数据必须标注来源 URL
- 国际高校数据以英文搜索为主，中文搜索为辅

## 按需实时补充场景

以下场景本地数据不完整，**必须自动触发搜索**：

### 中国高校
| 场景 | 搜索关键词 |
|------|-----------|
| 非985就业数据 | "{高校} 毕业生就业质量年度报告" |
| 就业精确数字 | "{高校} 就业质量报告 {年份} 就业率 深造率" |
| 考研报录比 | "{高校} {专业} 报录比 {年份} 研究生招生" |
| 缺失省份分数线 | "{高校} {省份} {年份} 录取分数线 最低分 位次" |

### 国际高校
| 场景 | 搜索关键词 |
|------|-----------|
| 录取率 | "{University} acceptance rate {year}" |
| 学费更新 | "{University} tuition {year} international" |
| 就业薪资 | "{University} median salary graduates {year}" |
| 奖学金 | "{University} merit scholarships international {year}" |
| 生活成本 | "{city} monthly cost of living student {year}" |

## 不确定性处理

- 本地数据不足 → 自动搜索补充，不需要告知用户"正在搜索"
- 搜到精确值 → 直接使用精确值，标注来源URL
- 搜不到 → 使用本地估算值，标注"为概括性参考，具体请查阅官方发布"
- 数据可能过时 → 标注"该数据为{年份}数据，最新情况请参考官方发布"
- 国际排名每年变化 → 标注排名年份，提供多排名对比
