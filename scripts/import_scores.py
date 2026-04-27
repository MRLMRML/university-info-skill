#!/usr/bin/env python3
"""
分数线数据扩展脚本 — 从 JSON 模板导入 scores.db
用法: python3 scripts/import_scores.py data/new_scores.json
"""

import json
import sqlite3
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = SKILL_ROOT / "data" / "scores.db"


def import_scores(json_path):
    with open(json_path, encoding="utf-8") as f:
        records = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    added = 0
    skipped = 0

    for r in records:
        cursor.execute("""
            SELECT id FROM admission_scores
            WHERE university=? AND province=? AND year=? AND subject_type=?
        """, (r["university"], r["province"], r["year"], r.get("subject_type", "")))

        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO admission_scores
            (university, province, year, batch, subject_type, min_score, min_rank, avg_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            r["university"],
            r["province"],
            r["year"],
            r.get("batch", ""),
            r.get("subject_type", ""),
            r.get("min_score"),
            r.get("min_rank"),
            r.get("avg_score")
        ))
        added += 1

    conn.commit()
    conn.close()

    print(f"导入完成: 新增 {added}, 跳过(已存在) {skipped}")


def generate_template(universities, provinces, year=2024):
    template = []
    for uni in universities:
        for prov in provinces:
            template.append({
                "university": uni,
                "province": prov,
                "year": year,
                "batch": "本科一批",
                "subject_type": "理科",
                "min_score": None,
                "min_rank": None,
                "avg_score": None
            })
    return template


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 import_scores.py <json_file>")
        print("或:   python3 import_scores.py --template")
        sys.exit(1)

    if sys.argv[1] == "--template":
        template = generate_template(
            ["北京大学", "清华大学"],
            ["北京", "上海", "广东", "浙江", "江苏"]
        )
        print(json.dumps(template, ensure_ascii=False, indent=2))
    else:
        import_scores(sys.argv[1])
