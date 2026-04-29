<div align="center">

# 🎓 全球高校信息检索 Skill

**覆盖 323+ 高校 · 30 种查询 · 27 国数据的 AI Agent 高校情报系统**

[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-blue.svg)](https://github.com/sst/opencode)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-orange.svg)](https://github.com/openclaw)
[![Cursor](https://img.shields.io/badge/Cursor-Compatible-black.svg)](https://cursor.sh)
[![Windsurf](https://img.shields.io/badge/Windsurf-Compatible-teal.svg)](https://codeium.com/windsurf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[中文](#-特性) | [English](README_en.md)

> 让 AI Agent 成为你的高校情报助手

</div>

---

## ✨ 特性

- **权威数据** — 985/211/双一流名单、学科评估均源自教育部原始文件
- **全球覆盖** — 175 所国际高校（美56/英30/加10/澳10/日10/欧20/新港10/印19/中东11/东南亚5）
- **30 种查询** — 基础信息/学科实力/就业/科研/录取/排名/会议/赛事/实验室...
- **多维数据** — 1483 条学科评估 + 50 个顶会 + 48 个赛事 + 56 个实验室
- **自然语言** — 支持 "北大就业怎么样？"、"MIT排名多少？" 等口语化提问
- **简称识别** — 内置 283 个别名（北大/MIT/斯坦福/牛津/BIT/SCUT...）
- **智能补充** — 本地数据不足时自动通过 Web Search 获取最新信息

---

## 🚀 安装 & 更新

```bash
# 安装
mkdir -p ~/.opencode/skills
git clone https://github.com/MRLMRML/university-info-skill.git /tmp/uni-skill
cp -r /tmp/uni-skill ~/.opencode/skills/university-info-skill

# 更新
cd ~/.opencode/skills/university-info-skill && git pull
```

---

## 📖 使用示例

```
# 中国高校
> 北京大学的基本信息
> 清华有哪些A+学科？
> 计算机学科哪些学校最强？
> 浙大和上交对比一下

# 国际高校 & 留学
> MIT的QS排名是多少？
> CMU和斯坦福CS哪个好？
> 我GPA3.5能冲CMU吗？
> MIT学费多少？有奖学金吗？

# 学术会议 & 赛事
> NeurIPS是什么级别的会议？
> CS领域CCF-A顶会有哪些？
> 挑战杯是什么？

# 实验室查询
> 清华有哪些重点实验室？
> MIT CSAIL有哪些研究方向？
```

---

## 📊 数据概览

| 类别 | 数据量 |
|------|--------|
| 中国高校 | 148 所（含全部 147 所双一流） |
| 国际高校 | 175 所（27 个国家/地区） |
| 学科评估 | 1483 条（95 学科 A+/A/A-/B+） |
| 学术会议 | 50 个（44 国际 + 6 国内） |
| 竞赛赛事 | 48 个（28 国际 + 20 国内） |
| 实验室 | 56 个（36 国内 + 20 国际） |
| 学科排名 | 10 学科 QS 2026 TOP20 |

---

## ⚠️ 免责声明

- 本 Skill 专注信息检索，不提供志愿填报建议或录取分数预测
- 就业/科研数据为概括性参考，具体以各校官方发布为准
- 数据仅供参考，不作为正式决策依据

---

## 🤝 贡献 & 联系

欢迎提交 PR 补充数据或修正错误。

合作联系：realJerryKing@163.com

---

## 📄 License

[MIT](LICENSE)
