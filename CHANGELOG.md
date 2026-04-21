# Changelog

All notable changes to this project will be documented in this file.

## [2.4.0] - 2025-04-21

### Added
- 「校招助手」Skill (recruitment.json + talent_flow.csv)
- 「择校分析」Skill (admission.db + programs.json)
- 10 行业→目标校映射
- 32 所高校毕业生流向数据
- 考研报录比种子数据 (6学科16校)
- 三 Skill 联合测试通过

## [2.3.0] - 2025-04-20

### Added
- scores.db SQLite 录取分数线数据库
- 查询类型扩展至 14 种 (新增: 录取分数线/排名/师资/智能推荐/报告生成/学科交叉/综合画像)

## [2.2.0] - 2025-04-20

### Added
- rankings.csv 软科 2024 中国大学排名 TOP240
- 39 所 985 师资数据 (院士/杰青/长江学者)

### Changed
- disciplines.csv: 477 → 1483 条 (95 学科 A+/A/A-/B+ 全覆盖)
- 39 所 985 就业/科研数据全覆盖

## [2.1.0] - 2025-04-20

### Fixed
- 新增缺失的东北大学
- 修正天津医科大学层次标记
- 修正哈工大深圳校区分类

### Changed
- universities.json 扩充至 148 所

## [2.0.0] - 2025-04-20

### Added
- YAML frontmatter 支持 Skill 自动触发
- 7 种查询类型完整处理流程
- 2022 年第二轮双一流调整 (7所新增+15所警示)
- 26 个常用简称映射
- Web Search 线上补充策略

### Changed
- SKILL.md 全面重写

## [1.0.0] - 2025-04-20

### Added
- 初始版本
- 基础信息查询
- universities.json + disciplines.csv + config.yaml
