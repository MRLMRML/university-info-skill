#!/usr/bin/env python3
"""
高校信息检索 Skill 数据校验脚本
用法: python3 scripts/validate_all.py [--json]
"""

import json
import csv
import sqlite3
import sys
import os
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_ROOT / "data"
REF_DIR = SKILL_ROOT / "references"

class ValidationReport:
    def __init__(self):
        self.results = []

    def ok(self, check_name, detail=""):
        self.results.append(("✅", check_name, detail))

    def warn(self, check_name, detail=""):
        self.results.append(("⚠️", check_name, detail))

    def fail(self, check_name, detail=""):
        self.results.append(("❌", check_name, detail))

    def print_report(self, as_json=False):
        if as_json:
            output = [{"status": s, "check": c, "detail": d} for s, c, d in self.results]
            print(json.dumps(output, ensure_ascii=False, indent=2))
        else:
            for status, check, detail in self.results:
                line = f"{status} {check}"
                if detail:
                    line += f": {detail}"
                print(line)

        fails = sum(1 for s, _, _ in self.results if s == "❌")
        warns = sum(1 for s, _, _ in self.results if s == "⚠️")
        oks = sum(1 for s, _, _ in self.results if s == "✅")
        print(f"\n{'='*50}")
        print(f"总计: {oks} 通过, {warns} 警告, {fails} 失败")
        return fails == 0


def load_config():
    import yaml
    config_path = DATA_DIR / "config.yaml"
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_csv_rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_985_count(config, report):
    schools = config.get("985高校", [])
    count = len(schools)
    if count == 39:
        report.ok("985名单", f"{count} 所")
    else:
        report.fail("985名单", f"应为39所，实际{count}所")


def check_211_count(config, report):
    all_211 = set()
    for region, schools in config.get("211高校", {}).items():
        if isinstance(schools, list):
            all_211.update(schools)
    count = len(all_211)
    if count == 118:
        report.ok("211名单", f"{count} 所")
    else:
        report.warn("211名单", f"应为118所，实际{count}所")


def check_syl_count(config, report):
    syl = config.get("双一流建设高校", {})
    all_syl = set()

    for key in ["原985高校", "第一轮新增非211", "第二轮新增"]:
        schools = syl.get(key, [])
        if isinstance(schools, list):
            all_syl.update(schools)

    non985_211 = syl.get("非985的211高校", {})
    for region, schools in non985_211.items():
        if isinstance(schools, list):
            all_syl.update(schools)

    count = len(all_syl)
    if count >= 144:
        report.ok("双一流总数", f"{count} 所（去重）")
    else:
        report.fail("双一流总数", f"应>=144所，实际{count}所")


def check_no_overlap(config, report):
    syl = config.get("双一流建设高校", {})
    groups = {}

    for key in ["原985高校", "第一轮新增非211", "第二轮新增"]:
        schools = syl.get(key, [])
        groups[key] = set(schools) if isinstance(schools, list) else set()

    non985_211 = set()
    for region, schools in syl.get("非985的211高校", {}).items():
        if isinstance(schools, list):
            non985_211.update(schools)
    groups["非985的211高校"] = non985_211

    group_names = list(groups.keys())
    overlaps = []
    for i in range(len(group_names)):
        for j in range(i + 1, len(group_names)):
            shared = groups[group_names[i]] & groups[group_names[j]]
            if shared:
                overlaps.append(f"{group_names[i]} ∩ {group_names[j]}: {shared}")

    if not overlaps:
        report.ok("双一流分组无重叠")
    else:
        for o in overlaps:
            report.fail("双一流分组重叠", o)


def check_985_syl_consistency(config, report):
    s985 = set(config.get("985高校", []))
    syl = config.get("双一流建设高校", {})
    syl_985 = set(syl.get("原985高校", []))

    if s985 == syl_985:
        report.ok("985与双一流原985一致")
    else:
        missing = s985 - syl_985
        extra = syl_985 - s985
        detail = ""
        if missing:
            detail += f"985中缺失: {missing}. "
        if extra:
            detail += f"双一流多出: {extra}. "
        report.fail("985与双一流原985不一致", detail)


def check_json_db_consistency(report):
    json_path = DATA_DIR / "universities.json"
    db_path = DATA_DIR / "universities.db"

    if not json_path.exists():
        report.fail("universities.json", "文件不存在")
        return
    if not db_path.exists():
        report.fail("universities.db", "文件不存在")
        return

    json_data = load_json(json_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM universities")
    db_names = {row[0] for row in cursor.fetchall()}
    conn.close()

    json_names = set(json_data.keys())

    only_json = json_names - db_names
    only_db = db_names - json_names

    if not only_json and not only_db:
        report.ok("JSON ↔ DB 一致性", f"均为 {len(json_names)} 所")
    else:
        detail = ""
        if only_json:
            detail += f"仅JSON: {len(only_json)}所. "
        if only_db:
            detail += f"仅DB: {len(only_db)}所. "
        report.warn("JSON ↔ DB 不一致", detail)


def check_disciplines(report):
    csv_path = DATA_DIR / "disciplines.csv"
    if not csv_path.exists():
        report.fail("disciplines.csv", "文件不存在")
        return

    rows = load_csv_rows(csv_path)
    count = len(rows)
    schools = len(set(r["院校"] for r in rows))
    disciplines = len(set(r["学科名称"] for r in rows))

    if count >= 1483:
        report.ok("学科评估", f"{count} 条, {schools} 校, {disciplines} 学科")
    else:
        report.warn("学科评估", f"应>=1483条，实际{count}条")


def check_rankings(report):
    csv_path = DATA_DIR / "rankings.csv"
    if not csv_path.exists():
        report.fail("rankings.csv", "文件不存在")
        return

    rows = load_csv_rows(csv_path)
    count = len(rows)

    if count >= 100:
        report.ok("大学排名", f"{count} 条")
    else:
        report.warn("大学排名", f"应>=100条，实际{count}条")


def check_scores_db(report):
    db_path = DATA_DIR / "scores.db"
    if not db_path.exists():
        report.fail("scores.db", "文件不存在")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM admission_scores")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT university) FROM admission_scores")
    schools = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT province) FROM admission_scores")
    provinces = cursor.fetchone()[0]

    conn.close()

    if total >= 100:
        report.ok("录取分数线", f"{total} 条, {schools} 校, {provinces} 省")
    else:
        report.warn("录取分数线", f"数据偏少: {total} 条, {schools} 校")


def check_admission_db(report):
    db_path = SKILL_ROOT.parent / "择校分析" / "data" / "admission.db"
    if not db_path.exists():
        report.warn("admission.db", "择校分析数据文件不存在")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM admission_ratio")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT university) FROM admission_ratio")
    schools = cursor.fetchone()[0]
    conn.close()

    if total >= 30:
        report.ok("考研报录比", f"{total} 条, {schools} 校")
    else:
        report.warn("考研报录比", f"数据偏少: {total} 条")


def check_aliases(report):
    alias_path = REF_DIR / "aliases.json"
    if not alias_path.exists():
        report.fail("aliases.json", "文件不存在")
        return

    aliases = load_json(alias_path)
    count = len(aliases)

    if count >= 26:
        report.ok("简称映射", f"{count} 个")
    else:
        report.warn("简称映射", f"应>=26个，实际{count}个")


def check_templates(report):
    tpl_path = REF_DIR / "templates.md"
    if not tpl_path.exists():
        report.fail("templates.md", "文件不存在")
        return

    with open(tpl_path, encoding="utf-8") as f:
        content = f.read()

    sections = content.count("## ")
    if sections >= 10:
        report.ok("输出模板", f"{sections} 个模板节")
    else:
        report.warn("输出模板", f"模板节数偏少: {sections}")


def check_search_strategy(report):
    path = REF_DIR / "search_strategy.md"
    if path.exists():
        report.ok("搜索策略文档")
    else:
        report.fail("search_strategy.md", "文件不存在")


def check_cross_skill_refs(report):
    base = SKILL_ROOT.parent
    skills = {
        "高校信息检索": base / "高校信息检索" / "data",
        "校招助手": base / "校招助手" / "data",
        "择校分析": base / "择校分析" / "data",
    }

    for name, path in skills.items():
        if path.exists():
            files = list(path.glob("*"))
            report.ok(f"Skill [{name}]", f"{len(files)} 个数据文件")
        else:
            report.fail(f"Skill [{name}]", "数据目录不存在")


def main():
    as_json = "--json" in sys.argv

    report = ValidationReport()

    try:
        config = load_config()
    except Exception as e:
        report.fail("config.yaml 加载", str(e))
        report.print_report(as_json)
        sys.exit(1)

    report.ok("config.yaml 加载")

    check_985_count(config, report)
    check_211_count(config, report)
    check_syl_count(config, report)
    check_no_overlap(config, report)
    check_985_syl_consistency(config, report)
    check_json_db_consistency(report)
    check_disciplines(report)
    check_rankings(report)
    check_scores_db(report)
    check_admission_db(report)
    check_aliases(report)
    check_templates(report)
    check_search_strategy(report)
    check_cross_skill_refs(report)

    success = report.print_report(as_json)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
