#!/usr/bin/env python3
"""
Crawl faculty and national key laboratory data from university websites.

Usage:
    python scripts/crawl_faculty.py [--batch 10]

Targets:
- 两院院士 exact counts
- 国家杰青 exact counts  
- 国家重点实验室 names and counts
- 重点学科带头人/知名教授
"""

import json
import os
import sys
import time
import sqlite3

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("pip install playwright && playwright install chromium")
    sys.exit(1)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "universities.json")
DB_PATH = os.path.join(BASE_DIR, "data", "universities.db")

SCHOOLS_985 = [
    "北京大学", "清华大学", "复旦大学", "上海交通大学", "浙江大学",
    "南京大学", "中国科学技术大学", "哈尔滨工业大学", "西安交通大学",
    "北京航空航天大学", "北京理工大学", "中国农业大学", "北京师范大学",
    "中央民族大学", "南开大学", "天津大学", "大连理工大学", "东北大学",
    "吉林大学", "同济大学", "华东师范大学", "东南大学", "厦门大学",
    "山东大学", "中国海洋大学", "武汉大学", "华中科技大学",
    "湖南大学", "中南大学", "中山大学", "华南理工大学",
    "重庆大学", "四川大学", "电子科技大学", "西北工业大学",
    "兰州大学", "西北农林科技大学", "中国人民大学", "国防科技大学",
]


def search_faculty_data(page, school_name):
    """Search for faculty/lab data via Bing."""
    queries = [
        f"{school_name} 院士 国家杰青 师资队伍 site:edu.cn",
        f"{school_name} 国家重点实验室 列表",
    ]

    results = {"labs": [], "faculty_url": None}

    for query in queries:
        try:
            page.goto(f"https://www.bing.com/search?q={query}", timeout=12000)
            page.wait_for_timeout(1500)

            links = page.evaluate("""() => {
                const items = document.querySelectorAll('#b_results .b_algo h2 a');
                return Array.from(items).slice(0, 3).map(a => ({
                    title: a.innerText, url: a.href
                }));
            }""")

            for link in links:
                if "师资" in link["title"] or "院士" in link["title"] or "人才" in link["title"]:
                    results["faculty_url"] = link["url"]
                if "实验室" in link["title"] or "重点" in link["title"]:
                    results["labs"].append(link["title"])

        except Exception:
            pass

        time.sleep(1)

    return results


def main():
    batch_size = 10
    if "--batch" in sys.argv:
        idx = sys.argv.index("--batch")
        batch_size = int(sys.argv[idx + 1])

    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    print(f"Starting faculty/lab data crawl (batch={batch_size})")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()

        for school in SCHOOLS_985[:batch_size]:
            print(f"\n[{school}]")
            result = search_faculty_data(page, school)

            if result["faculty_url"]:
                print(f"  Faculty page: {result['faculty_url'][:60]}")
            if result["labs"]:
                print(f"  Labs found: {result['labs'][:2]}")

            time.sleep(2)

        browser.close()

    print("\nDone. Run with --batch N to process more schools.")


if __name__ == "__main__":
    main()
