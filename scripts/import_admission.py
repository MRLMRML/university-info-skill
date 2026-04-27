#!/usr/bin/env python3
"""
考研报录比数据扩展脚本 — 从 JSON 模板导入 admission.db
用法: python3 scripts/import_admission.py data/new_admission.json
"""

import json
import sqlite3
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = SKILL_ROOT.parent / "择校分析" / "data" / "admission.db"


def import_admission(json_path):
    with open(json_path, encoding="utf-8") as f:
        records = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    added = 0
    skipped = 0

    for r in records:
        cursor.execute("""
            SELECT id FROM admission_ratio
            WHERE university=? AND discipline=? AND year=?
        """, (r["university"], r["discipline"], r["year"]))

        if cursor.fetchone():
            skipped += 1
            continue

        applicants = r.get("applicants", 0)
        admitted = r.get("admitted", 0)
        ratio = round(applicants / admitted, 1) if admitted > 0 else 0

        cursor.execute("""
            INSERT INTO admission_ratio
            (university, department, discipline, year, applicants, admitted, ratio, exempted_ratio)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            r["university"],
            r.get("department", ""),
            r["discipline"],
            r["year"],
            applicants,
            admitted,
            ratio,
            r.get("exempted_ratio", None)
        ))
        added += 1

    conn.commit()
    conn.close()
    print(f"导入完成: 新增 {added}, 跳过(已存在) {skipped}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 import_admission.py <json_file>")
        sys.exit(1)
    import_admission(sys.argv[1])
