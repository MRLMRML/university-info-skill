---
name: 高校信息检索
description: 中国高校信息查询与情报分析工具。覆盖全国 985/211/双一流高校、全球 TOP100 国际高校、印度 TOP20 高校，支持基础信息、学科实力、科研水平、就业质量、生源结构、学术会议、竞赛赛事、国际高校、学科排名、留学费用等多维度查询。当用户提到中国大学、高校查询、校园招聘、校企合作、学科评估、985/211/双一流筛选、高校对比、就业数据、毕业生去向、顶会、学术会议、竞赛、挑战杯、数学建模、Kaggle、ACM、MIT、斯坦福、牛津、剑桥、QS排名、留学、海归、海外校招、IIT、印度理工、学费、生活费、奖学金、CS排名、学科排名时，务必使用此 Skill。
---

# 高校信息检索 Skill

面向校园招聘、校企合作、学术研究、综合评估等场景的中国高校信息查询工具。

## 数据文件

| 文件 | 内容 | 查询方式 |
|------|------|----------|
| `data/universities.db` | 148所高校全维度（5表：基础/就业/科研/师资/生源） | `sqlite3` SQL查询 |
| `data/universities.json` | 同上（JSON格式，兼容旧版） | 直接读取 |
| `data/disciplines.csv` | 1483条学科评估（95学科 A+/A/A-/B+） | grep/awk |
| `data/rankings.csv` | 软科2024排名 TOP240 | grep/awk |
| `data/scores.db` | 录取分数线（SQLite） | `sqlite3` SQL查询 |
| `data/config.yaml` | 985/211/双一流名单 | 直接读取 |
| `data/conferences.json` | 国际+国内顶级学术会议（CCF-A/B等） | 直接读取 |
| `data/competitions.json` | 国际+国内顶级赛事（A类/B类） | 直接读取 |
| `data/international_universities.json` | 全球 TOP100 国际高校（QS 2026） | 直接读取 |
| `data/subject_rankings.json` | QS 2026 学科排名（10学科 TOP10/30） | 直接读取 |
| `data/india_universities.json` | 印度TOP20高校（IIT/IIM等） | 直接读取 |
| `data/tuition_costs.json` | 留学费用参考（学费+生活成本+奖学金） | 直接读取 |

**推荐使用 universities.db（SQLite）进行复杂查询**，支持 JOIN/WHERE/ORDER BY：
```bash
sqlite3 data/universities.db "SELECT u.name, f.academicians FROM universities u JOIN faculty f ON u.name=f.university WHERE u.is_985=1 ORDER BY f.academicians DESC LIMIT 10"
```

数据可信度：层次/学科评估/名单 = 权威（教育部）；就业/科研/师资 = 近似参考。
输出时标注"数据为概括性参考"。

## 查询处理流程

1. **意图识别** — 判断查询类型（见下方18种），提取参数（高校名/学科/地区/层次/会议名/赛事名）
2. **名称匹配** — 支持全称/简称/模糊匹配（简称映射见 `references/aliases.json`）
3. **本地检索** — 读取对应数据文件，聚合多源数据（含 conferences.json / competitions.json）
4. **按需实时补充** — 本地数据不足时，**必须**通过 web search 实时获取（见下方策略）
5. **格式化输出** — 按 `references/templates.md` 模板输出，标注来源和年份

## 按需实时补充策略（重要）

本地数据覆盖 39 所 985 的核心字段。以下场景**必须自动触发 web search 补充**：

| 场景 | 触发条件 | 搜索策略 |
|------|---------|---------|
| 就业数据精确化 | 本地仅有概括值（如"95%以上"） | 搜索 "{学校} 就业质量报告 {当前年份-1}" 获取精确数字 |
| 非985高校就业 | 本地无就业数据的 211/双一流 | 搜索 "{学校} 毕业生就业质量年度报告" |
| 报录比 | 本地 admission.db 无该校/学科 | 搜索 "{学校} {专业} 报录比 {年份}" |
| 生源数据 | 本地无生源概况的非985高校 | 搜索 "{学校} 在校生 本科生 研究生 规模" |
| 师资精确 | 本地标注"估算值" | 搜索 "{学校} 院士 杰青 师资队伍 site:edu.cn" |
| 分数线细化 | 本地无该省份/年份 | 搜索 "{学校} {省份} {年份} 录取分数线 最低分" |

**执行原则**：
- 搜到精确数据后，直接在回复中使用精确值（而非本地估算值）
- 标注"数据来源：{URL}"和年份
- 搜不到时回退到本地估算值并标注"为概括性参考"
- 详细搜索关键词模板见 `references/search_strategy.md`

## 28 种查询类型

| # | 类型 | 触发词 | 数据源 |
|---|------|--------|--------|
| 1 | 基础信息 | 基本信息、什么层次、是不是985 | universities.json |
| 2 | 学科实力 | A+学科、优势学科、学科排名 | disciplines.csv |
| 3 | 科研水平 | 实验室、科研经费、研究方向 | universities.json + web |
| 4 | 就业质量 | 就业、毕业生、薪资、去向 | universities.json + web |
| 5 | 生源结构 | 多少学生、本硕博比例、男女比 | universities.json |
| 6 | 院校筛选 | 有哪些、列表、筛选 | config.yaml |
| 7 | 高校对比 | 对比、VS、哪个好 | 多文件聚合 |
| 8 | 录取分数线 | 分数线、多少分能上、位次 | scores.db (SQLite) |
| 9 | 大学排名 | 排名、排第几、软科 | rankings.csv |
| 10 | 师资实力 | 院士、杰青、长江学者 | universities.json |
| 11 | 智能推荐 | 推荐学校、目标校、哪些学校适合 | 多源聚合 |
| 12 | 报告生成 | 校招策略、择校报告、分析报告 | 全量数据 |
| 13 | 学科交叉 | 同时XX和XX都强、跨学科 | disciplines.csv |
| 14 | 综合画像 | 怎么样、介绍一下 | 全量数据聚合 |
| 15 | 学术会议查询 | 顶会、CCF-A、会议级别、录用率 | conferences.json |
| 16 | 会议对比/筛选 | CS顶会有哪些、AI领域顶会 | conferences.json |
| 17 | 赛事查询 | 竞赛、挑战杯、数学建模、Kaggle | competitions.json |
| 18 | 赛事对比/筛选 | A类赛事有哪些、创业类竞赛 | competitions.json |
| 19 | 国际高校查询 | MIT排名、牛津怎么样 | international_universities.json |
| 20 | 国际高校对比 | CMU和斯坦福哪个好、Oxford vs Cambridge | international_universities.json |
| 21 | 中外高校对比 | 清华和MIT对比、北大vs哈佛 | universities.json + international_universities.json |
| 22 | 留学择校推荐 | CS硕士去美国哪些学校、英国留学推荐 | international_universities.json |
| 23 | 海归背景评估 | 帝国理工回国认可度、NUS回国好找工作吗 | international_universities.json |
| 24 | 海外校招目标校 | 去美国哪些学校招人、英国校招目标校 | international_universities.json |
| 25 | 学科排名查询 | CS全球TOP10是哪些、商学排名 | subject_rankings.json |
| 26 | 学费查询 | MIT学费多少、留学费用 | tuition_costs.json |
| 27 | 生活成本查询 | 伦敦和纽约留学哪个贵 | tuition_costs.json |
| 28 | 印度高校查询 | IIT Bombay排名、印度最好的大学 | india_universities.json |

## 各类型处理要点

**学科查询**：问"XX大学学科" → disciplines.csv 筛选该校，按 A+>A>A- 排序；问"XX学科哪些学校强" → 按院校排序。

**分数线查询**：通过 bash 执行 `sqlite3 data/scores.db "SELECT ..."` 查询。本地不全时 web search 补充。

**智能推荐**：解析岗位/专业需求 → disciplines.csv 匹配学科强校 → rankings.csv 排名加权 → universities.json 就业/地区匹配 → 按核心校/重点校/储备校三梯队输出。

**报告生成**：聚合多维数据，按结构化模板（6章：目标定位/院校清单/各校分析/排期/ROI/风险）输出。

**学科交叉**：识别多学科 → disciplines.csv 分别筛选 → 取交集 → 按综合评级排序。

**学术会议查询**：问"NeurIPS什么级别" → conferences.json 检索该会议，返回级别/领域/录用率/时间；问"CS顶会有哪些" → 按领域筛选 CCF-A 级别会议；问"哪些会议录用率低于20%" → 按录用率筛选。支持国际/国内分别展示。

**赛事查询**：问"挑战杯是什么" → competitions.json 检索该赛事，返回级别/主办方/周期/描述；问"A类竞赛有哪些" → 按级别筛选；问"编程类竞赛" → 按领域筛选。支持国际/国内分别展示。国内赛事按教育部 A/B 类分级。

**国际高校查询**：问"MIT排名" → international_universities.json 检索该校，返回QS/THE/ARWU排名+优势学科+录取要求；问"CS硕士去美国哪些学校" → 按学科+国家筛选；问"清华和MIT对比" → 同时读取两个数据文件，生成对比表。支持中英文名/简称匹配。

**留学/海归场景**：留学推荐按学科排名+录取难度+就业数据综合排序；海归评估按QS排名+国内认可度+就业去向分析。

## 参考文件

需要详细输出模板时读取：`references/templates.md`
需要简称映射时读取：`references/aliases.json`
需要线上搜索策略时读取：`references/search_strategy.md`

## 约束

- 不提供志愿填报建议或录取分数预测
- 不对高校做主观排名或好坏评价
- 不收录个人隐私信息
- 准确性 > 完整性 > 速度
- 本地缓存 > 线上搜索
- 官方数据 > 第三方数据
