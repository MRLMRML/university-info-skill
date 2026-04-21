# Skill 联动设计

## 架构概述

```
用户查询 → Agent 意图识别 → 触发对应 Skill
                ↓
    ┌───────────┼───────────┐
    ▼           ▼           ▼
 高校信息检索   校招助手    择校分析
 (通用查询)   (HR场景)   (学生场景)
    │           │           │
    └─────┬─────┘           │
          ▼                 │
    共享数据层              │
    (universities.json     │
     disciplines.csv       │
     rankings.csv)         │
          ▲                 │
          └─────────────────┘
```

## 数据共享约定

三个 Skill 共享「高校信息检索」的 data/ 目录作为基础数据层：

| 数据文件 | 所有者 | 消费者 |
|----------|--------|--------|
| universities.json | 高校信息检索 | 校招助手、择校分析 |
| disciplines.csv | 高校信息检索 | 校招助手、择校分析 |
| rankings.csv | 高校信息检索 | 校招助手、择校分析 |
| scores.db | 高校信息检索 | 择校分析 |
| config.yaml | 高校信息检索 | 校招助手 |
| recruitment.json | 校招助手 | — |
| talent_flow.csv | 校招助手 | — |
| admission.db | 择校分析 | — |
| programs.json | 择校分析 | — |

## 与外部 Skill 联动

### 潜在联动 Skill

| 外部 Skill | 联动方式 | 场景 |
|------------|----------|------|
| 简历筛选 Skill | 读取 universities.json | 候选人院校背景自动评估 |
| 行业研究 Skill | 读取 talent_flow.csv | 行业人才来源分析 |
| 面试助手 Skill | 读取 disciplines.csv | 根据候选人学科背景定制问题 |

### 数据接口约定

外部 Skill 可通过以下路径读取数据：

```
~/.opencode/skills/高校信息检索/data/universities.json
~/.opencode/skills/高校信息检索/data/disciplines.csv
~/.opencode/skills/高校信息检索/data/rankings.csv
```

JSON 结构约定（universities.json 单校 schema）：

```json
{
  "高校名": {
    "层次": ["985", "211", "双一流"],
    "城市": "string",
    "类型": "string",
    "一流学科": ["string"],
    "网址": "string",
    "就业概况": { "就业率": "string", "深造率": "string", "主要去向行业": ["string"], "代表性雇主": ["string"] },
    "科研概况": { "国家重点实验室": "string", "年度科研经费": "string", "代表性平台": ["string"] },
    "师资概况": { "两院院士": "number", "国家杰青": "number", "长江学者": "number" }
  }
}
```

## 触发边界

| 查询类型 | 触发 Skill | 不触发 |
|----------|-----------|--------|
| "北大怎么样" | 高校信息检索 | 校招助手、择校分析 |
| "我们公司去哪招人" | 校招助手 | 高校信息检索、择校分析 |
| "XX专业好不好考" | 择校分析 | 高校信息检索、校招助手 |
| "对比清华和北大" | 高校信息检索 | 校招助手、择校分析 |
| "校招预算怎么分配" | 校招助手 | 高校信息检索、择校分析 |
| "考研推荐哪些学校" | 择校分析 | 高校信息检索、校招助手 |
