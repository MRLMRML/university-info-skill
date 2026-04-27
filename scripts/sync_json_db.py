#!/usr/bin/env python3
"""
universities.json ↔ universities.db 双向同步脚本
用法:
  python3 scripts/sync_json_db.py json2db   # JSON → DB
  python3 scripts/sync_json_db.py db2json   # DB → JSON
  python3 scripts/sync_json_db.py check     # 一致性检查
"""

import json
import sqlite3
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_ROOT / "data"
JSON_PATH = DATA_DIR / "universities.json"
DB_PATH = DATA_DIR / "universities.db"


def load_json():
    with open(JSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def get_db():
    return sqlite3.connect(DB_PATH)


def json_to_db():
    data = load_json()
    conn = get_db()
    cursor = conn.cursor()

    updated = 0
    inserted = 0

    for name, info in data.items():
        level = info.get("层次", [])
        is_985 = 1 if "985" in level else 0
        is_211 = 1 if "211" in level else 0
        is_syl = 1 if "双一流" in level else 0

        disciplines = info.get("一流学科", [])
        if isinstance(disciplines, list):
            disciplines = ",".join(disciplines)

        cursor.execute("SELECT name FROM universities WHERE name = ?", (name,))
        exists = cursor.fetchone()

        if exists:
            cursor.execute("""
                UPDATE universities SET level=?, city=?, type=?,
                first_class_disciplines=?, website=?, is_985=?, is_211=?, is_syl=?
                WHERE name=?
            """, (
                ",".join(level),
                info.get("城市", ""),
                info.get("类型", ""),
                disciplines,
                info.get("网址", ""),
                is_985, is_211, is_syl,
                name
            ))
            updated += 1
        else:
            cursor.execute("""
                INSERT INTO universities (name, level, city, type,
                first_class_disciplines, website, is_985, is_211, is_syl)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                ",".join(level),
                info.get("城市", ""),
                info.get("类型", ""),
                disciplines,
                info.get("网址", ""),
                is_985, is_211, is_syl
            ))
            inserted += 1

        # Sync employment
        emp = info.get("就业概况", {})
        if emp and emp.get("就业率") not in [None, "", "暂无"]:
            industries = emp.get("主要去向行业", [])
            employers = emp.get("代表性雇主", [])
            cursor.execute("""
                INSERT OR REPLACE INTO employment
                (university, employment_rate, further_study_rate, top_industries, top_employers, data_year)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                name,
                emp.get("就业率", ""),
                emp.get("深造率", ""),
                ",".join(industries) if isinstance(industries, list) else str(industries),
                ",".join(employers) if isinstance(employers, list) else str(employers),
                emp.get("数据年份", "")
            ))

        # Sync research
        res = info.get("科研概况", {})
        if res and res.get("国家重点实验室") not in [None, "", "暂无"]:
            platforms = res.get("代表性平台", [])
            lab_detail = res.get("国家重点实验室详细", [])
            cursor.execute("""
                INSERT OR REPLACE INTO research
                (university, national_labs, annual_funding, key_platforms, data_year, national_labs_detail)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                name,
                str(res.get("国家重点实验室", "")),
                str(res.get("年度科研经费", "")),
                ",".join(platforms) if isinstance(platforms, list) else str(platforms),
                res.get("数据年份", ""),
                json.dumps(lab_detail, ensure_ascii=False) if lab_detail else ""
            ))

        # Sync faculty
        fac = info.get("师资概况", {})
        if fac and fac.get("两院院士") is not None:
            cursor.execute("""
                INSERT OR REPLACE INTO faculty
                (university, academicians, nsfc_distinguished, changjiang_scholars, data_year)
                VALUES (?, ?, ?, ?, ?)
            """, (
                name,
                fac.get("两院院士", 0),
                fac.get("国家杰青", 0),
                fac.get("长江学者", 0),
                fac.get("数据年份", "")
            ))

        # Sync students
        stu = info.get("生源概况", {})
        if stu and stu.get("在校生规模") not in [None, "", "暂无"]:
            cursor.execute("""
                INSERT OR REPLACE INTO students
                (university, total_students, undergrad, master, phd, gender_ratio, data_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                str(stu.get("在校生规模", "")),
                str(stu.get("本科生", "")),
                str(stu.get("硕士生", "")),
                str(stu.get("博士生", "")),
                str(stu.get("男女比例", "")),
                stu.get("数据年份", "")
            ))

    conn.commit()
    conn.close()
    print(f"JSON → DB 完成: 更新 {updated}, 新增 {inserted}")


def db_to_json():
    data = load_json()
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM universities")
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    updated = 0
    for row in rows:
        row_dict = dict(zip(columns, row))
        name = row_dict["name"]

        if name not in data:
            data[name] = {
                "层次": row_dict.get("level", "").split(","),
                "城市": row_dict.get("city", ""),
                "类型": row_dict.get("type", ""),
                "一流学科": row_dict.get("first_class_disciplines", "").split(","),
                "网址": row_dict.get("website", ""),
            }
            updated += 1

    conn.close()

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"DB → JSON 完成: 新增/更新 {updated} 所高校")


def check_consistency():
    data = load_json()
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM universities")
    db_names = {row[0] for row in cursor.fetchall()}
    json_names = set(data.keys())

    only_json = json_names - db_names
    only_db = db_names - json_names
    common = json_names & db_names

    print(f"JSON: {len(json_names)} 所, DB: {len(db_names)} 所")
    print(f"共同: {len(common)} 所")

    if only_json:
        print(f"仅JSON ({len(only_json)}): {sorted(only_json)}")
    if only_db:
        print(f"仅DB ({len(only_db)}): {sorted(only_db)}")

    if not only_json and not only_db:
        print("✅ 完全一致")

    conn.close()


def main():
    if len(sys.argv) < 2:
        print("用法: python3 sync_json_db.py [json2db|db2json|check]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "json2db":
        json_to_db()
    elif cmd == "db2json":
        db_to_json()
    elif cmd == "check":
        check_consistency()
    else:
        print(f"未知命令: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
