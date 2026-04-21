#!/usr/bin/env python3
"""Data integrity validation for 高校信息检索 Skill."""

import json
import csv
import sqlite3
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "高校信息检索", "data")

errors = []
warnings = []


def validate_universities():
    path = os.path.join(DATA_DIR, "universities.json")
    with open(path, "r") as f:
        data = json.load(f)

    c985 = sum(1 for v in data.values() if "985" in v.get("层次", []))
    csyl = sum(1 for v in data.values() if "双一流" in v.get("层次", []))

    if c985 != 39:
        errors.append(f"universities.json: 985 count = {c985}, expected 39")
    if csyl != 147:
        errors.append(f"universities.json: 双一流 count = {csyl}, expected 147")

    for name, info in data.items():
        for field in ["层次", "城市", "类型", "一流学科", "网址"]:
            if not info.get(field):
                errors.append(f"universities.json: {name} missing {field}")
        if "985" in info.get("层次", []) and "211" not in info.get("层次", []):
            errors.append(f"universities.json: {name} is 985 but not 211")

    print(f"  universities.json: {len(data)} entries, 985={c985}, 双一流={csyl}")


def validate_disciplines():
    path = os.path.join(DATA_DIR, "disciplines.csv")
    with open(path, "r") as f:
        records = list(csv.DictReader(f))

    subjects = set(r["学科代码"] for r in records)
    if len(subjects) < 95:
        errors.append(f"disciplines.csv: only {len(subjects)} subjects, expected 95")

    seen = set()
    dupes = 0
    for r in records:
        key = (r["学科代码"], r["院校"], r["评估结果"])
        if key in seen:
            dupes += 1
        seen.add(key)

    if dupes > 0:
        errors.append(f"disciplines.csv: {dupes} duplicate records")

    print(f"  disciplines.csv: {len(records)} records, {len(subjects)} subjects, {dupes} dupes")


def validate_rankings():
    path = os.path.join(DATA_DIR, "rankings.csv")
    if not os.path.exists(path):
        warnings.append("rankings.csv not found")
        return

    with open(path, "r") as f:
        records = list(csv.DictReader(f))

    if len(records) < 100:
        warnings.append(f"rankings.csv: only {len(records)} records, expected 200+")

    print(f"  rankings.csv: {len(records)} records")


def validate_scores_db():
    path = os.path.join(DATA_DIR, "scores.db")
    if not os.path.exists(path):
        warnings.append("scores.db not found")
        return

    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM admission_scores")
    count = c.fetchone()[0]
    conn.close()

    print(f"  scores.db: {count} records")


def main():
    print("=" * 50)
    print("DATA VALIDATION")
    print("=" * 50)

    validate_universities()
    validate_disciplines()
    validate_rankings()
    validate_scores_db()

    print("\n" + "=" * 50)
    if errors:
        print(f"FAILED: {len(errors)} error(s)")
        for e in errors:
            print(f"  ❌ {e}")
        sys.exit(1)
    elif warnings:
        print(f"PASSED with {len(warnings)} warning(s)")
        for w in warnings:
            print(f"  ⚠️ {w}")
    else:
        print("PASSED ✅")


if __name__ == "__main__":
    main()
