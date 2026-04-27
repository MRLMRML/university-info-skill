#!/usr/bin/env python3
"""
数据更新前检查 — 确认哪些数据需要更新
用法: python3 scripts/pipeline/check_updates.py
"""

import json
import sqlite3
import csv
from datetime import datetime
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = SKILL_ROOT / "data"


def check_rankings():
    path = DATA_DIR / "rankings.csv"
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    year = "2026" if any(r.get("score", "") > "500" for r in rows[:5]) else "unknown"
    return {"name": "软科排名", "count": len(rows), "year": year, "status": "✅" if len(rows) >= 200 else "⚠️"}


def check_scores():
    conn = sqlite3.connect(DATA_DIR / "scores.db")
    c = conn.cursor()
    c.execute("SELECT year, COUNT(*) FROM admission_scores GROUP BY year ORDER BY year")
    dist = dict(c.fetchall())
    c.execute("SELECT COUNT(*) FROM admission_scores")
    total = c.fetchone()[0]
    conn.close()
    latest_year = max(dist.keys()) if dist else 0
    return {"name": "录取分数线", "count": total, "year": str(latest_year), "dist": dist,
            "status": "✅" if latest_year >= datetime.now().year - 1 else "⚠️"}


def check_admission():
    db_path = SKILL_ROOT.parent / "择校分析" / "data" / "admission.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT year, COUNT(*) FROM admission_ratio GROUP BY year ORDER BY year")
    dist = dict(c.fetchall())
    c.execute("SELECT COUNT(*) FROM admission_ratio")
    total = c.fetchone()[0]
    conn.close()
    latest_year = max(dist.keys()) if dist else 0
    return {"name": "考研报录比", "count": total, "year": str(latest_year), "dist": dist,
            "status": "✅" if latest_year >= datetime.now().year - 1 else "⚠️"}


def check_employment():
    d = json.load(open(DATA_DIR / "universities.json"))
    years = {}
    for name, info in d.items():
        y = info.get("就业概况", {}).get("数据年份", "")
        if y:
            years[y] = years.get(y, 0) + 1
    latest_year = max(years.keys()) if years else "无"
    return {"name": "就业数据", "count": sum(years.values()), "year": latest_year, "years": years,
            "status": "✅" if years.get("2024", 0) > 20 else "⚠️"}


def main():
    print(f"数据更新检查 — {datetime.now().strftime('%Y-%m-%d')}\n")

    checks = [check_rankings(), check_scores(), check_admission(), check_employment()]

    for c in checks:
        print(f"{c['status']} {c['name']}: {c['count']} 条, 最新 {c['year']}")
        if "dist" in c:
            for y, cnt in sorted(c["dist"].items()):
                print(f"    {y}: {cnt} 条")
        if "years" in c:
            for y, cnt in sorted(c["years"].items()):
                print(f"    {y}: {cnt} 校")

    print(f"\n需要更新的数据:")
    needs_update = [c for c in checks if c["status"] == "⚠️"]
    if needs_update:
        for c in needs_update:
            print(f"  - {c['name']}: 当前最新 {c['year']}")
    else:
        print("  无，所有数据已是最新")


if __name__ == "__main__":
    main()
