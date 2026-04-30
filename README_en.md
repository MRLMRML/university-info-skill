<div align="center">

# 🎓 Global University Information Retrieval Skill

**The World's First AI Agent University Intelligence System Covering 300+ Universities, 30 Query Types, and 27 Countries**

[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://github.com/sst/opencode)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-Compatible-purple.svg)](https://hermes-agent.nousresearch.com/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-orange.svg)](https://github.com/openclaw)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[中文](README.md) | [English](#-features)

> 🚀 **The World's First** AI Agent University Intelligence System — Make Your AI the Ultimate University Expert
>
> 📊 Covering **148 Chinese Universities** + **175 International Universities** + **50 Top Conferences** + **48 Competitions**
>
> 🎯 Supporting **30 Query Types**, from "Peking University employment rate?" to "MIT tuition fees?", one sentence does it all

</div>

---

## 🏆 Why Choose Us?

<div align="center">

| 🥇 World's First | 📊 Most Complete | 🔍 Most Queries | 🌍 Widest Coverage |
|:---:|:---:|:---:|:---:|
| AI Agent University System | 300+ Multi-dimensional Data | 30 Query Types | 27 Countries/Regions |
| **First** to integrate QS/THE/ARWU | **First** Lab Query Support | **First** Tuition Comparison | **First** Conference/Competition Query |

</div>

---

## ✨ Features

### 🏛️ Authoritative Data, Official Sources

- 📜 **Ministry of Education** — 985/211/Double First-Class lists, discipline evaluations from official documents
- 🏅 **Three Major Rankings** — QS/THE/ARWU global rankings fully covered, 10 disciplines TOP20
- 📊 **ShanghaiRanking** — 2026 Chinese University Ranking TOP239 integrated
- 👨‍🏫 **Faculty Data** — 69 universities with Academicians/NSFC Distinguished Young Scholars/Cheung Kong Scholars

### 🌍 Global Vision, All-in-One

- 🇺🇸 **US 50 Schools** — MIT/Stanford/Harvard/CMU etc., with GPA+TOEFL+GRE requirements
- 🇬🇧 **UK 30 Schools** — Oxford/Cambridge/Imperial etc., with IELTS requirements
- 🇨🇦🇦🇺🇯🇰🇸🇬🇪🇺 **More Countries** — Canada/Australia/Japan/Singapore/Europe/India/Middle East/Southeast Asia
- 💰 **Tuition Costs** — 10 countries tuition + 16 cities living costs + 9 countries scholarships

### 🔍 Query Capabilities, Industry Leading

- 📖 **1483 Discipline Evaluations** — 95 first-level disciplines A+/A/A-/B+ fully covered
- 🎯 **Admission Assessment** — 49 schools with GRE/GMAT requirements, 5-level difficulty grading
- 📊 **Academic Conferences** — 42 international top conferences (CCF-A/B) + 6 domestic
- 🏅 **Competitions** — 28 international competitions + 20+ domestic A/B class
- 🏫 **Lab Information** — Key laboratories and research directions for domestic and international universities

### 💬 Smart Interaction, Natural Language

- 🗣️ **Conversational Queries** — "Peking University employment rate?", "MIT ranking?"
- 🗺️ **Alias Recognition** — Built-in 283 aliases (PKU/MIT/Stanford/Oxford/BIT/SCUT...)
- 🌐 **Smart Supplementation** — Automatically fetches latest info via Web Search when local data is insufficient
- 🔄 **Real-time Updates** — One-click data update support, keeping information current

---

## 🚀 Quick Start

### Installation

```bash
# One-click install
mkdir -p ~/.opencode/skills
git clone https://github.com/MRLMRML/university-info-skill.git /tmp/uni-skill
cp -r /tmp/uni-skill ~/.opencode/skills/university-info-skill

# Verify installation
ls ~/.opencode/skills/university-info-skill
```

### Update

```bash
# Pull latest data
cd ~/.opencode/skills/university-info-skill && git pull

# Or use Pipeline one-click update
python3 scripts/pipeline/run_all.py
```

---

## 📖 Usage Examples

### 🇨🇳 Chinese University Queries

```
# Basic Information
> Basic information about Peking University
> What tier is Tsinghua University?
> Compare Zhejiang University and Shanghai Jiao Tong University

# Academic Strength
> What A+ disciplines does Tsinghua have?
> Which universities are strongest in computer science?
> What are Beihang's top majors?

# Employment & Research
> Where do Beihang graduates mainly work?
> How much research funding does Fudan have?
> What labs does Shanghai Jiao Tong have?

# Admission & Rankings
> What score is needed for Zhejiang University?
> What are the top 10 in ShanghaiRanking?
> Which is harder to get into, PKU or Tsinghua?
```

### 🌍 International Universities & Study Abroad

```
# Rankings
> What is MIT's QS ranking?
> Which is better, Oxford or Cambridge?
> Which is stronger in CS, CMU or Stanford?

# Study Abroad Planning
> Which US schools are good for CS Master's?
> Can I get into CMU with a 3.5 GPA?
> How is Imperial College recognized back home?

# Cost Comparison
> How much is MIT tuition? Any scholarships?
> Which is more expensive, London or New York?
> How much does it cost to study in the UK for a year?

# Returnee Assessment
> What's the salary for NUS graduates returning to China?
> Which UK schools do companies recruit from?
> What are the advantages of being a returnee?
```

### 📊 Academic Conferences & Competitions

```
# Conference Queries
> What level is NeurIPS?
> What are the CCF-A top conferences in CS?
> Which is harder to publish at, CVPR or ICCV?

# Competition Queries
> What is the Challenge Cup?
> Which has more value, Internet+ or Challenge Cup?
> What are the Ministry of Education A-class competitions?
```

### 🏫 Lab Queries (New)

```
# Domestic Labs
> What key labs does Tsinghua have?
> What research directions does PKU CS department have?
> What does Zhejiang University's AI lab focus on?

# International Labs
> What research directions does MIT CSAIL have?
> What does Stanford AI Lab focus on?
> How is CMU's Robotics Institute?
```

---

## 📁 Project Structure

```
university-info-skill/
├── 高校信息检索/                        ← Main Skill (30 Query Types)
│   ├── SKILL.md
│   └── data/
│       ├── universities.json           # 148 Chinese Universities
│       ├── international_universities.json  # 175 International (27 Countries)
│       ├── india_universities.json     # India TOP20
│       ├── subject_rankings.json       # QS Subject Rankings (10 Subjects TOP20)
│       ├── tuition_costs.json          # Tuition Costs (10 Countries + 16 Cities)
│       ├── labs.json                   # University Lab Info (New)
│       ├── disciplines.csv             # 1483 Discipline Evaluations
│       ├── rankings.csv                # ShanghaiRanking 2026 TOP239
│       ├── scores.db                   # 504 Admission Scores
│       ├── conferences.json            # 44 Academic Conferences
│       ├── competitions.json           # 48 Competitions
│       └── config.yaml                 # 985/211/Double First-Class Lists
│   └── references/
│       ├── aliases.json                # 283 Alias Mappings
│       ├── templates.md                # 20 Output Templates
│       └── search_strategy.md          # Search Strategy
├── 校招助手/                            ← Campus Recruitment Skill
│   ├── SKILL.md                        # Includes Overseas + Returnee Assessment
│   └── data/
│       ├── recruitment.json            # 15 Industry Target School Mapping
│       └── talent_flow.csv             # 41 School Graduate Flow
├── 择校分析/                            ← School Selection Skill
│   ├── SKILL.md
│   └── data/
│       ├── admission.db                # 110 Postgraduate Admission Ratios
│       └── programs.json               # 15 Discipline Selection Guide
└── scripts/
    ├── validate_all.py                 # 17 Data Validations
    ├── sync_json_db.py                 # JSON↔SQLite Sync
    ├── backup_data.py                  # Auto Backup
    ├── import_scores.py                # Score Import
    ├── import_admission.py             # Admission Import
    └── pipeline/
        ├── run_all.py                  # One-click Update
        └── check_updates.py            # Timeliness Check
```

---

## 📊 Data Coverage

### Chinese Universities (148)

| Dimension | Volume | Timeliness |
|-----------|--------|------------|
| Total Universities | 148 (including all 147 Double First-Class) | — |
| Discipline Evaluations | 1483 (95 disciplines A+/A/A-/B+) | 4th Round (2017) |
| University Rankings | 239 (ShanghaiRanking 2026) | 2026 |
| Admission Scores | 504 (79 schools, 31 provinces) | 2024+2025 |
| Postgraduate Admission | 110 (53 schools, 15 disciplines) | 2024+2025 |
| Employment Data | 57 (all 985 + some 211) | 2023+2024 |
| Faculty Data | 69 (Academicians/NSFC/Cheung Kong) | 2024 |
| Student Data | 69 (enrollment scale/UG:PG ratio) | 2024 |
| Lab Data | 50+ (Key Labs/Research Directions) | 2024 |

### International Universities (164, 27 Countries)

| Region | Count | Representative Schools | Admission Data |
|--------|-------|----------------------|----------------|
| USA | 50 | MIT / Stanford / Harvard / CMU | ✅ GPA+TOEFL+GRE |
| UK | 30 | Oxford / Cambridge / Imperial | ✅ IELTS |
| Canada | 10 | Toronto / UBC / McGill | ✅ IELTS |
| Australia | 10 | Melbourne / Sydney / ANU | ✅ IELTS |
| Japan | 10 | UTokyo / Kyoto / Waseda | ✅ TOEFL |
| Europe | 20 | ETH / TUM / EPFL / KTH | ✅ IELTS |
| Singapore/HK | 10 | NUS / NTU / HKU | ✅ IELTS |
| India | 19 | IIT / IIM / BITS | ✅ JEE/CAT |
| Middle East | 11 | KAUST / Technion / TAU | ✅ IELTS |
| Southeast Asia | 5 | Chulalongkorn / UPM | ✅ IELTS |

### Subject Rankings (10 Subjects, QS 2026)

| Subject | Coverage | Chinese University Performance |
|---------|----------|-------------------------------|
| Computer Science | TOP30 | Tsinghua#11 / PKU#13 / SJTU#26 / ZJU#30 |
| Engineering & Tech | TOP20 | Tsinghua#11 / PKU#15 |
| Electrical & Electronic | TOP20 | Tsinghua#7 / PKU#16 |
| Mechanical Engineering | TOP20 | Tsinghua#7 / PKU#14 |
| Data Science/AI | TOP20 | Tsinghua#7 / PKU#18 / SJTU#19 |
| Business & Management | TOP20 | — |
| Medicine | TOP20 | — |
| Natural Sciences | TOP20 | PKU#12 / Tsinghua#13 |
| Law | TOP20 | Tsinghua#14 / PKU#17 |
| Education | TOP20 | PKU#9 / Tsinghua#20 |

### Academic Conferences & Competitions

| Type | Count | Coverage |
|------|-------|----------|
| International Conferences | 42 | AI/CV/NLP/Systems/Security/SE/DB/HCI/Data Mining |
| Domestic Conferences | 6 | CNCC/CCAI/NLPCC/ChinaSys/CCF-GAIR/VALSE |
| International Competitions | 17 | Programming/Math/Data Science/Innovation/Design/Business |
| Domestic Competitions | 20 | A-class/B-class, Innovation/Math/Programming/Hardware/English/Design/Finance |

### Tuition Costs

| Country | Tuition/Year | Living Cost/Year | Total/Year |
|---------|-------------|------------------|------------|
| USA | $30K-$65K | $15K-$25K | $45K-$90K |
| UK | $25K-$50K | $12K-$20K | $37K-$70K |
| Canada | $20K-$45K | $10K-$15K | $30K-$60K |
| Australia | $25K-$50K | $12K-$18K | $37K-$68K |
| Singapore | $15K-$30K | $10K-$15K | $25K-$45K |
| Germany | $0-$3K | $10K-$12K | $10K-$15K |
| Japan | $5K-$10K | $8K-$12K | $13K-$22K |

---

## 🎯 30 Query Types

| # | Type | Trigger Examples | Data Source |
|---|------|------------------|-------------|
| 1 | Basic Info | "basic info", "what tier" | universities.json |
| 2 | Academic Strength | "A+ disciplines", "subject ranking" | disciplines.csv |
| 3 | Research Level | "labs", "research funding" | universities.json |
| 4 | Employment | "employment rate", "graduate destinations" | universities.json |
| 5 | Student Structure | "how many students", "gender ratio" | universities.json |
| 6 | School Filter | "985 list", "Beijing 211" | config.yaml |
| 7 | University Compare | "ZJU vs SJTU" | Multi-file |
| 8 | Admission Scores | "score needed" | scores.db |
| 9 | University Ranking | "ShanghaiRanking" | rankings.csv |
| 10 | Faculty Strength | "Academicians", "NSFC" | universities.json |
| 11 | Smart Recommend | "recommend schools", "target schools" | Multi-source |
| 12 | Report Generate | "recruitment strategy", "selection report" | All data |
| 13 | Cross-discipline | "strong in both X and Y" | disciplines.csv |
| 14 | Comprehensive | "how is it", "introduce" | All data |
| 15 | Conference | "what level is NeurIPS" | conferences.json |
| 16 | Conference Compare | "CS top conferences" | conferences.json |
| 17 | Competition | "what is Challenge Cup" | competitions.json |
| 18 | Competition Compare | "A-class competitions" | competitions.json |
| 19 | International | "MIT ranking", "how is Oxford" | international_universities.json |
| 20 | International Compare | "CMU vs Stanford" | international_universities.json |
| 21 | China-Intl Compare | "Tsinghua vs MIT" | Two sources |
| 22 | Study Abroad | "CS Master's in US" | international_universities.json |
| 23 | Returnee Assessment | "Imperial College recognition" | international_universities.json |
| 24 | Overseas Recruitment | "UK schools for hiring" | international_universities.json |
| 25 | Subject Ranking | "CS global TOP10" | subject_rankings.json |
| 26 | Tuition Query | "MIT tuition" | tuition_costs.json |
| 27 | Living Cost | "London vs New York" | tuition_costs.json |
| 28 | India Universities | "IIT Bombay ranking" | india_universities.json |
| 29 | Admission Difficulty | "can I get CMU with 3.5 GPA" | international_universities.json |
| 30 | Lab Query | "Tsinghua key labs" | labs.json |

---

## 🏫 Lab Information (New)

### Domestic University Labs

| University | Key Lab | Research Directions |
|------------|---------|---------------------|
| Tsinghua University | State Key Lab of Intelligent Technology & Systems | AI, Machine Learning, Computer Vision |
| Peking University | MOE Key Lab of Machine Perception & Intelligence | Computer Vision, Pattern Recognition, Multimedia |
| Zhejiang University | State Key Lab of Industrial Control Technology | Industrial Automation, Intelligent Control, Robotics |
| Shanghai Jiao Tong | State Key Lab of Advanced Optical Communication | Optical Communication, Network Tech, Info Security |
| USTC | MOE Key Lab of Multimedia Computing & Communication | Multimedia, Computer Vision, Graphics |

### International University Labs

| University | Lab | Research Directions |
|------------|-----|---------------------|
| MIT | CSAIL (Computer Science & AI Lab) | AI, Robotics, NLP, Computer Vision |
| Stanford | Stanford AI Lab (SAL) | Machine Learning, Deep Learning, NLP |
| CMU | Robotics Institute | Robotics, Computer Vision, Machine Learning |
| UC Berkeley | BAIR (Berkeley AI Research) | Reinforcement Learning, Robotics, NLP |
| ETH Zurich | Computer Vision Lab | Computer Vision, 3D Reconstruction, Autonomous Driving |

---

## 🏷️ Alias Mappings (283)

### Chinese Universities (Examples)

| Alias | Full Name | Alias | Full Name |
|-------|-----------|-------|-----------|
| PKU | Peking University | Tsinghua | Tsinghua University |
| Fudan | Fudan University | SJTU | Shanghai Jiao Tong University |
| ZJU | Zhejiang University | NJU | Nanjing University |
| BIT | Beijing Institute of Technology | BUPT | Beijing Univ of Posts & Telecom |
| SCUT | South China University of Tech | UESTC | Univ of Electronic Sci & Tech |

### International Universities (Examples)

| Alias | Full Name | Alias | Full Name |
|-------|-----------|-------|-----------|
| MIT | Massachusetts Institute of Technology | Stanford | Stanford University |
| Harvard | Harvard University | CMU | Carnegie Mellon University |
| Oxford | University of Oxford | Cambridge | University of Cambridge |
| ETH | ETH Zurich | Imperial | Imperial College London |
| NUS | National University of Singapore | HKU | University of Hong Kong |
| UTokyo | University of Tokyo | SNU | Seoul National University |
| Waterloo | University of Waterloo | Melbourne | University of Melbourne |

---

## 🔄 Data Update

```bash
# Method 1: Git Pull
cd ~/.opencode/skills/university-info-skill && git pull

# Method 2: Pipeline One-click
python3 scripts/pipeline/run_all.py

# Method 3: Check Timeliness
python3 scripts/pipeline/check_updates.py
```

---

## ⚠️ Constraints & Disclaimer

- This Skill focuses on information retrieval, **does not provide** admission advice or score predictions
- Does not make subjective evaluations or rankings of universities
- Employment/research data is general reference, please refer to official sources
- International ranking data is annotated with year, rankings change annually
- Does not collect any personal privacy information
- Data is for reference only, not for formal decision-making

---

## 🤝 Contributing

Welcome to submit PRs to supplement data or correct errors:

- Supplement more university employment/research/student/lab data
- Correct inaccurate information in existing data (please attach source links)
- Add new university alias mappings
- Supplement international university data

See [CONTRIBUTING.md](CONTRIBUTING.md) for details

---


---

## 📄 License

[MIT](LICENSE)

---

<div align="center">

**⭐ If this project helps you, please give us a Star! ⭐**

**🔗 Project Link**: [https://github.com/MRLMRML/university-info-skill](https://github.com/MRLMRML/university-info-skill)

**📧 Contact Us**: [realJerryKing@163.com](mailto:realJerryKing@163.com)

We welcome the following forms of collaboration:

- 📊 **Data Contribution** — Supplement university employment/research/lab/admission data
- 🐛 **Bug Reports** — Found incorrect data? Submit an Issue or PR with source links
- 💡 **Feature Suggestions** — New query scenarios or data dimensions? Let's discuss
- 🌍 **Internationalization** — Help expand university data for more countries/regions
- 🏫 **Institutional Partnership** — Data collaboration with universities/edu platforms/recruiters
- 📝 **Documentation** — Help translate or improve multilingual docs

</div>
