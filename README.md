# 🎓 全球高校信息检索 Skill

[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://github.com/sst/opencode)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-orange.svg)](https://github.com/openclaw)
[![Data Source](https://img.shields.io/badge/数据来源-教育部官方-green.svg)](https://www.moe.gov.cn/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.8.0-brightgreen.svg)](#版本记录)

> 中国高校 + 全球国际高校信息查询与情报分析工具 —— 让 AI Agent 成为你的高校情报助手。

覆盖中国 **148 所高校** + 全球 **164 所国际高校**（27 国），支持 **30 种查询类型**，核心数据源自**教育部官方文件**及 **QS/THE/ARWU 排名**。

---

## ✨ 特性

- 🏛️ **权威数据** — 985/211/双一流名单、学科评估均源自教育部原始文件
- 🌍 **全球覆盖** — 164 所国际高校（美50/英30/加10/澳10/日10/德5/新加坡5/港5/印度19/中东11/东南亚5）
- 🔍 **30 种查询** — 中国高校14种 + 学术会议4种 + 赛事2种 + 国际高校10种
- 📖 **1483 条学科评估** — 95 个一级学科 A+/A/A-/B+ 四档全覆盖
- 🏆 **软科排名** — 2026 中国大学排名 TOP239 集成
- 🎓 **国际排名** — QS/THE/ARWU 三大排名全覆盖 + 10 学科排名 TOP20
- 📊 **学术会议** — 42 个国际顶会（CCF-A/B）+ 6 国内顶会
- 🏅 **竞赛赛事** — 37 个国际赛事 + 20+ 国内 A/B 类赛事
- 💰 **留学费用** — 10 国学费 + 16 城市生活成本 + 9 国奖学金
- 🎯 **录取评估** — 49 校含 GRE/GMAT 要求，5 级难度分级
- 👨‍🏫 **师资数据** — 69 所高校院士/杰青/长江学者数量
- 💬 **自然语言** — 支持 "北大就业怎么样？"、"MIT排名多少？" 等口语化提问
- 🗺️ **简称识别** — 内置 283 个别名（北大/MIT/斯坦福/牛津/BIT/SCUT...）
- 🌐 **智能补充** — 本地数据不足时自动通过 Web Search 获取最新信息

---

## 📦 安装

```bash
mkdir -p ~/.opencode/skills
git clone https://github.com/MRLMRML/university-info-skill.git /tmp/uni-skill
cp -r /tmp/uni-skill ~/.opencode/skills/university-info-skill
```

> 兼容 OpenCode / Claude Code / OpenClaw。也支持项目级安装。

---

## 🚀 使用示例

### 中国高校

```
> 北京大学的基本信息
> 清华有哪些A+学科？
> 计算机学科哪些学校最强？
> 北航的毕业生主要去哪些公司？
> 浙大和上交对比一下
```

### 国际高校 & 留学

```
> MIT的QS排名是多少？
> CMU和斯坦福CS哪个好？
> 清华和MIT工程专业对比
> CS硕士去美国哪些学校好？
> 我GPA3.5能冲CMU吗？
> 帝国理工回国认可度怎么样？
> 去英国哪些学校招人？
> MIT学费多少？有奖学金吗？
> 伦敦和纽约留学哪个贵？
```

### 学术会议 & 赛事

```
> NeurIPS是什么级别的会议？
> CS领域CCF-A顶会有哪些？
> 挑战杯和互联网+哪个含金量高？
> 教育部A类竞赛有哪些？
```

### 印度高校

```
> IIT Bombay排名多少？
> 印度最好的大学有哪些？
> IIT和IIM有什么区别？
```

---

## 📁 项目结构

```
university-info-skill/
├── 高校信息检索/                        ← 主 Skill (30种查询类型)
│   ├── SKILL.md
│   └── data/
│       ├── universities.json           # 148所中国高校
│       ├── international_universities.json  # 164所国际高校(27国)
│       ├── india_universities.json     # 印度TOP20高校
│       ├── subject_rankings.json       # QS学科排名(10学科TOP20)
│       ├── tuition_costs.json          # 留学费用(10国+16城市)
│       ├── disciplines.csv             # 1483条学科评估
│       ├── rankings.csv                # 软科2026排名 TOP239
│       ├── scores.db                   # 504条录取分数线
│       ├── conferences.json            # 42个学术会议
│       ├── competitions.json           # 37个赛事
│       └── config.yaml                 # 985/211/双一流名单
│   └── references/
│       ├── aliases.json                # 283个别名映射
│       ├── templates.md                # 20种输出模板(含国际场景)
│       └── search_strategy.md          # 搜索策略(含国际搜索)
├── 校招助手/                            ← HR 校招决策 Skill
│   ├── SKILL.md                        # 含海外校招+海归评估
│   └── data/
│       ├── recruitment.json            # 15行业目标校映射
│       └── talent_flow.csv             # 41校毕业生流向
├── 择校分析/                            ← 学生择校 Skill
│   ├── SKILL.md
│   └── data/
│       ├── admission.db                # 110条考研报录比
│       └── programs.json               # 15学科择校指南
└── scripts/
    ├── validate_all.py                 # 17项数据校验
    ├── sync_json_db.py                 # JSON↔SQLite同步
    ├── backup_data.py                  # 自动备份
    ├── import_scores.py                # 分数线导入
    ├── import_admission.py             # 报录比导入
    └── pipeline/
        ├── run_all.py                  # 一键更新
        └── check_updates.py            # 时效性检查
```

---

## 📊 数据覆盖

### 中国高校（148 所）

| 维度 | 数据量 | 时效 |
|------|--------|------|
| 高校总数 | 148 所（含全部 147 所双一流） | — |
| 学科评估 | 1483 条（95 学科 A+/A/A-/B+） | 第四轮(2017) |
| 大学排名 | 239 所（软科 2026） | 2026 |
| 录取分数线 | 504 条（79 校 31 省） | 2024+2025 |
| 考研报录比 | 110 条（53 校 15 学科） | 2024+2025 |
| 就业数据 | 57 所（985 全覆盖 + 部分 211） | 2023+2024 |
| 师资数据 | 69 所（院士/杰青/长江学者） | 2024 |
| 生源数据 | 69 所（在校生规模/本硕博比例） | 2024 |

### 国际高校（164 所, 27 国）

| 区域 | 数量 | 代表院校 | 录取数据 |
|------|------|---------|---------|
| 美国 | 50 | MIT / Stanford / Harvard / CMU | ✅ GPA+TOEFL+GRE |
| 英国 | 30 | Oxford / Cambridge / Imperial | ✅ IELTS |
| 加拿大 | 10 | Toronto / UBC / McGill | ✅ IELTS |
| 澳洲 | 10 | Melbourne / Sydney / ANU | ✅ IELTS |
| 日本 | 10 | 东大 / 京大 / 早稻田 | ✅ TOEFL |
| 欧洲大陆 | 20 | ETH / TUM / EPFL / KTH | ✅ IELTS |
| 新加坡/港校 | 10 | NUS / NTU / 港大 | ✅ IELTS |
| 印度 | 19 | IIT / IIM / BITS | ✅ JEE/CAT |
| 中东 | 11 | KAUST / Technion / TAU | ✅ IELTS |
| 东南亚 | 5 | 朱拉隆功 / UPM | ✅ IELTS |

### 学科排名（10 学科, QS 2026）

| 学科 | 覆盖 | 中国高校表现 |
|------|------|-------------|
| 计算机科学 | TOP30 | 清华#11 / 北大#13 / 上交#26 / 浙大#30 |
| 工程与技术 | TOP20 | 清华#11 / 北大#15 |
| 电气电子 | TOP20 | 清华#7 / 北大#16 |
| 机械工程 | TOP20 | 清华#7 / 北大#14 |
| 数据科学/AI | TOP20 | 清华#7 / 北大#18 / 上交#19 |
| 商学管理 | TOP20 | — |
| 医学 | TOP20 | — |
| 自然科学 | TOP20 | 北大#12 / 清华#13 |
| 法学 | TOP20 | 清华#14 / 北大#17 |
| 教育学 | TOP20 | 北大#9 / 清华#20 |

### 学术会议 & 赛事

| 类型 | 量 | 覆盖 |
|------|-----|------|
| 国际会议 | 42 个 | AI/CV/NLP/系统/安全/SE/数据库/HCI/数据挖掘 |
| 国内会议 | 6 个 | CNCC/CCAI/NLPCC/ChinaSys/CCF-GAIR/VALSE |
| 国际赛事 | 17 个 | 编程/数学/数据科学/创新/设计/商业 |
| 国内赛事 | 20 个 | A类/B类，综合创新/数学建模/编程/硬件/英语/设计/金融 |

### 留学费用

| 国家 | 学费范围/年 | 生活费范围/年 | 总费用/年 |
|------|-----------|-------------|----------|
| 美国 | $30K-$65K | $15K-$25K | $45K-$90K |
| 英国 | $25K-$50K | $12K-$20K | $37K-$70K |
| 加拿大 | $20K-$45K | $10K-$15K | $30K-$60K |
| 澳洲 | $25K-$50K | $12K-$18K | $37K-$68K |
| 新加坡 | $15K-$30K | $10K-$15K | $25K-$45K |
| 德国 | $0-$3K | $10K-$12K | $10K-$15K |
| 日本 | $5K-$10K | $8K-$12K | $13K-$22K |

---

## 🎯 30 种查询类型

| # | 类型 | 触发词示例 | 数据源 |
|---|------|-----------|--------|
| 1 | 基础信息 | "基本信息"、"什么层次" | universities.json |
| 2 | 学科实力 | "A+学科"、"学科排名" | disciplines.csv |
| 3 | 科研水平 | "实验室"、"科研经费" | universities.json |
| 4 | 就业质量 | "就业率"、"毕业生去向" | universities.json |
| 5 | 生源结构 | "多少学生"、"男女比" | universities.json |
| 6 | 院校筛选 | "985有哪些"、"北京211" | config.yaml |
| 7 | 高校对比 | "浙大和上交对比" | 多文件聚合 |
| 8 | 录取分数线 | "多少分能上" | scores.db |
| 9 | 大学排名 | "软科排名" | rankings.csv |
| 10 | 师资实力 | "院士"、"杰青" | universities.json |
| 11 | 智能推荐 | "推荐学校"、"目标校" | 多源聚合 |
| 12 | 报告生成 | "校招策略"、"择校报告" | 全量数据 |
| 13 | 学科交叉 | "XX和XX都强" | disciplines.csv |
| 14 | 综合画像 | "怎么样"、"介绍一下" | 全量数据 |
| 15 | 学术会议 | "NeurIPS什么级别" | conferences.json |
| 16 | 会议对比 | "CS顶会有哪些" | conferences.json |
| 17 | 赛事查询 | "挑战杯是什么" | competitions.json |
| 18 | 赛事对比 | "A类竞赛有哪些" | competitions.json |
| 19 | 国际高校 | "MIT排名"、"牛津怎么样" | international_universities.json |
| 20 | 国际对比 | "CMU和斯坦福哪个好" | international_universities.json |
| 21 | 中外对比 | "清华和MIT对比" | 两源聚合 |
| 22 | 留学择校 | "CS硕士去美国哪些学校" | international_universities.json |
| 23 | 海归评估 | "帝国理工回国认可度" | international_universities.json |
| 24 | 海外校招 | "去英国哪些学校招人" | international_universities.json |
| 25 | 学科排名 | "CS全球TOP10是哪些" | subject_rankings.json |
| 26 | 学费查询 | "MIT学费多少" | tuition_costs.json |
| 27 | 生活成本 | "伦敦和纽约留学哪个贵" | tuition_costs.json |
| 28 | 印度高校 | "IIT Bombay排名" | india_universities.json |
| 29 | 录取难度 | "我GPA3.5能冲CMU吗" | international_universities.json |
| 30 | 海归增强 | "NUS回国薪资" | international_universities.json |

---

## 🏷️ 简称映射（283 个）

### 中国高校（示例）

| 简称 | 全称 | 简称 | 全称 |
|------|------|------|------|
| 北大 | 北京大学 | 清华 | 清华大学 |
| 复旦 | 复旦大学 | 上交/交大 | 上海交通大学 |
| 浙大 | 浙江大学 | 南大 | 南京大学 |
| 北理/BIT | 北京理工大学 | 北邮 | 北京邮电大学 |
| 华工/SCUT | 华南理工大学 | 成电 | 电子科技大学 |
| 北交/BJTU | 北京交通大学 | 西电/XDU | 西安电子科技大学 |

### 国际高校（示例）

| 简称 | 全称 | 简称 | 全称 |
|------|------|------|------|
| MIT | Massachusetts Institute of Technology | 斯坦福 | Stanford University |
| 哈佛 | Harvard University | CMU | Carnegie Mellon University |
| 牛津 | University of Oxford | 剑桥 | University of Cambridge |
| ETH | ETH Zurich | 帝国理工 | Imperial College London |
| NUS | National University of Singapore | 港大 | The University of Hong Kong |
| 东大 | The University of Tokyo | 首尔大学 | Seoul National University |
| 滑铁卢 | University of Waterloo | 墨尔本 | University of Melbourne |

---

## 📋 版本记录

### v2.8.0 (2026-04) — 全面升级：数据标准化 + 模板国际化

- ✅ **国际高校数据标准化** — 164 校全部补全 GPA/TOEFL/IELTS/难度分级/QS/THE/ARWU
- ✅ **GRE/GMAT 要求** — 49 校含 GRE/GMAT 录取要求
- ✅ **学科排名扩展** — 10 学科全部 TOP20（CS 保持 TOP30）
- ✅ **输出模板国际化** — 新增国际高校/留学选校/中外对比/学科排名/费用模板
- ✅ **搜索策略国际化** — 新增国际高校/会议赛事搜索关键词
- ✅ **海外校招能力** — 校招助手新增海外目标校筛选 + 海归评估
- ✅ **中东高校扩展** — +10 所（KAUST/Technion/TAU 等）
- ✅ **东南亚高校扩展** — +5 所（朱拉隆功/UPM 等）
- ✅ **留学费用数据** — 10 国学费 + 16 城市生活成本 + 9 国奖学金
- ✅ **印度高校数据** — 19 所（IIT×9 / IIM×2 / BITS 等）
- ✅ **competitions.json 修复** — JSON 语法错误

### v2.7.0 (2026-04) — 国际高校 + 学术会议 + 赛事

- ✅ 国际高校数据 149 所，QS/THE/ARWU 三大排名
- ✅ 学术会议 42 个（CCF-A/B）+ 国内 6 个
- ✅ 赛事 37 个（国际+国内 A/B 类）
- ✅ 查询类型 14→24 种
- ✅ 别名 26→283 个
- ✅ 软科排名 2024→2026
- ✅ 录取分数线 149→504 条
- ✅ 考研报录比 30→110 条
- ✅ 双一流名单修正 54→147 所
- ✅ 新增 5 个自动化脚本 + Pipeline

### v2.6.0 (2025-04) — Phase 6 数据补充

- ✅ 师资数据百度百科核实 37/39 所精确院士数
- ✅ 毕业生流向 39 所 985 全覆盖
- ✅ 录取分数线 31/31 省全覆盖
- ✅ 新增「按需实时补充」策略

### v2.5.0 (2025-04) — Phase 5 架构优化

- ✅ SKILL.md 瘦身 436→75 行
- ✅ 数据层升级 universities.db SQLite
- ✅ 新增爬虫脚本

### v2.4.0 (2025-04) — Phase 3 场景化拆分

- ✅ 新增「校招助手」Skill
- ✅ 新增「择校分析」Skill

---

## 🔄 数据更新

```bash
cd /tmp/uni-skill && git pull
cp -r /tmp/uni-skill ~/.opencode/skills/university-info-skill
```

或使用 Pipeline：
```bash
python3 scripts/pipeline/run_all.py          # 一键更新
python3 scripts/pipeline/check_updates.py    # 检查时效性
```

---

## ⚠️ 约束与免责

- 本 Skill 专注信息检索，**不提供**志愿填报建议或录取分数预测
- 不对高校做主观好坏评价或排名
- 就业/科研数据为概括性参考，具体以各校官方发布为准
- 国际排名数据标注年份，排名每年变化
- 不收录任何个人隐私信息
- 数据仅供参考，不作为正式决策依据

---

## 🤝 贡献

欢迎提交 PR 补充数据或修正错误：

- 补充更多高校的就业/科研/生源数据
- 修正已有数据中的不准确信息（请附来源链接）
- 新增高校简称映射
- 补充国际高校数据

---

## 📄 License

[MIT](LICENSE)
