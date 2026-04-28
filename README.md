# 🎓 高校信息检索 Skill

[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://github.com/sst/opencode)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-orange.svg)](https://github.com/openclaw)
[![Data Source](https://img.shields.io/badge/数据来源-教育部官方-green.svg)](https://www.moe.gov.cn/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.7.0-brightgreen.svg)](#版本记录)

> 中国高校 + 全球 TOP100 国际高校信息查询与情报分析工具 —— 让 AI Agent 成为你的高校情报助手。

覆盖中国 **147 所双一流高校** + 全球 **149 所国际高校**（QS 2026），支持 **24 种查询类型**，核心数据源自**教育部官方文件**及 **QS/THE/ARWU 排名**。

---

## ✨ 特性

- 🏛️ **权威数据** — 985/211/双一流名单、学科评估均源自教育部原始文件
- 🌍 **全球覆盖** — 149 所国际高校（美50/英30/欧20/加10/澳10/亚27/其他2）
- 🔍 **24 种查询** — 中国高校14种 + 学术会议4种 + 赛事2种 + 国际高校6种
- 📖 **1483 条学科评估** — 95 个一级学科 A+/A/A-/B+ 四档全覆盖
- 🏆 **软科排名** — 2026 中国大学排名 TOP239 集成
- 🎓 **国际排名** — QS/THE/ARWU 三大排名全覆盖
- 📊 **学术会议** — 40+ 国际顶会（CCF-A/B）+ 6 国内顶会
- 🏅 **竞赛赛事** — 35+ 国际赛事 + 20+ 国内 A/B 类赛事
- 👨‍🏫 **师资数据** — 69 所高校院士/杰青/长江学者数量
- 💬 **自然语言** — 支持 "北大就业怎么样？"、"MIT排名多少？" 等口语化提问
- 🗺️ **简称识别** — 内置 283 个别名（北大/MIT/斯坦福/牛津...）
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

### 国际高校

```
> MIT的QS排名是多少？
> CMU和斯坦福CS哪个好？
> 清华和MIT工程专业对比
> CS硕士去美国哪些学校好？
> 帝国理工回国认可度怎么样？
> 去英国哪些学校招人？
```

### 学术会议 & 赛事

```
> NeurIPS是什么级别的会议？
> CS领域CCF-A顶会有哪些？
> 挑战杯和互联网+哪个含金量高？
> 教育部A类竞赛有哪些？
```

---

## 📁 项目结构

```
university-info-skill/
├── 高校信息检索/                        ← 主 Skill (24种查询类型)
│   ├── SKILL.md
│   └── data/
│       ├── universities.json           # 148所中国高校
│       ├── international_universities.json  # 149所国际高校
│       ├── disciplines.csv             # 1483条学科评估
│       ├── rankings.csv                # 软科2026排名 TOP239
│       ├── scores.db                   # 504条录取分数线
│       ├── conferences.json            # 46个学术会议
│       ├── competitions.json           # 35+个赛事
│       └── config.yaml                 # 985/211/双一流名单
│   └── references/
│       ├── aliases.json                # 283个别名映射
│       ├── templates.md                # 15种输出模板
│       └── search_strategy.md          # Web Search策略
├── 校招助手/                            ← HR 校招决策 Skill
│   ├── SKILL.md
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

### 中国高校

| 维度 | 数据量 |
|------|--------|
| 高校总数 | 148 所（含全部 147 所双一流） |
| 学科评估 | 1483 条（95 学科 A+/A/A-/B+） |
| 大学排名 | 239 所（软科 2026） |
| 录取分数线 | 504 条（79 校 31 省，2024+2025） |
| 考研报录比 | 110 条（53 校 14 学科，2024+2025） |
| 就业数据 | 57 所（985 全覆盖 + 部分 211） |
| 师资数据 | 69 所（院士/杰青/长江学者） |
| 生源数据 | 69 所（在校生规模/本硕博比例） |
| 毕业生流向 | 41 校 |
| 行业校招映射 | 15 行业 |
| 择校学科指南 | 15 学科 |

### 国际高校（QS 2026）

| 区域 | 数量 | 代表院校 |
|------|------|---------|
| 美国 | 50 | MIT / Stanford / Harvard / CMU / Berkeley |
| 英国 | 30 | Oxford / Cambridge / Imperial / UCL / Edinburgh |
| 欧洲大陆 | 20 | ETH / TUM / EPFL / KTH / Sorbonne |
| 加拿大 | 10 | Toronto / UBC / McGill / Waterloo |
| 澳洲 | 10 | Melbourne / Sydney / ANU / UNSW |
| 新加坡 | 5 | NUS / NTU / SMU / SUTD |
| 日本 | 10 | 东大 / 京大 / 东工大 / 名古屋 / 早稻田 |
| 韩国 | 4 | 首尔大 / KAIST / 延世 / 高丽 |
| 中国香港 | 5 | 港大 / 港中文 / 港科大 / 港城大 / 港理工 |
| 其他 | 5 | 马来亚 / 台大 / 奥克兰 / KFUPM / UBA |

### 学术会议

| 领域 | 会议 |
|------|------|
| AI/ML | NeurIPS / ICML / ICLR / AAAI / IJCAI |
| CV | CVPR / ICCV / ECCV |
| NLP | ACL / EMNLP / NAACL |
| 系统 | OSDI / SOSP / SIGCOMM / NSDI |
| 安全 | IEEE S&P / CCS / USENIX Security / NDSS |
| SE | ICSE / FSE / ASE |
| 数据库 | SIGMOD / VLDB / ICDE |

### 竞赛赛事

| 类型 | 赛事 |
|------|------|
| 综合创新 | 挑战杯 / 互联网+ / 创青春 |
| 数学建模 | 国赛(CUMCM) / 美赛(MCM/ICM) |
| 编程 | ACM-ICPC / 蓝桥杯 / Kaggle |
| 硬件 | 电子设计大赛 / RoboMaster |
| 国际 | MIT $100K / Hult Prize / Red Dot |

---

## 🎯 24 种查询类型

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

### v2.7.0 (2026-04) — 国际高校 + 学术会议 + 赛事

- ✅ **国际高校数据** — 149 所（美50/英30/欧20/加10/澳10/亚27），QS/THE/ARWU 三大排名
- ✅ **学术会议数据** — 40+ 国际顶会（CCF-A/B）+ 6 国内顶会
- ✅ **赛事数据** — 35+ 国际赛事 + 20+ 国内 A/B 类赛事
- ✅ **查询类型扩展** — 14→24 种（+会议/赛事/国际高校/留学/海归）
- ✅ **别名大幅扩充** — 26→283 个（含中国高校英文缩写 + 国际高校中英文简称）
- ✅ **软科排名更新** — 2024→2026，TOP239
- ✅ **录取分数线扩充** — 149→504 条（含 2025 年数据）
- ✅ **考研报录比扩充** — 30→110 条（含 2025 年数据）
- ✅ **就业/师资/生源扩充** — 就业57校/师资69校/生源69校
- ✅ **校招行业扩充** — 10→15 行业（+AI/新能源/芯片/游戏/电商）
- ✅ **双一流名单修正** — 54→147 所，消除 A/B 重叠
- ✅ **211 名单校验** — 移除 8 所非 211，118→109
- ✅ **新增 5 个自动化脚本** — validate/sync/backup/import_scores/import_admission
- ✅ **数据更新 Pipeline** — run_all.py + check_updates.py

### v2.6.0 (2025-04) — Phase 6 数据补充

- ✅ 师资数据百度百科核实 **37/39所**精确院士数
- ✅ 实验室精确名单 **11→37/39所**
- ✅ 毕业生流向 **39所985全覆盖**
- ✅ 录取分数线 **31/31省全覆盖**
- ✅ 新增「**按需实时补充**」策略

### v2.5.0 (2025-04) — Phase 5 架构优化

- ✅ SKILL.md 瘦身 **436行→75行**
- ✅ 数据层升级 **universities.db** SQLite
- ✅ 新增爬虫脚本

### v2.4.0 (2025-04) — Phase 3 场景化拆分

- ✅ 新增「**校招助手**」Skill
- ✅ 新增「**择校分析**」Skill

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
