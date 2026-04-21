#!/usr/bin/env python3
"""
Crawl employment quality data from university websites.
Targets: 39 985 universities' annual employment reports.

Usage:
    python scripts/crawl_employment.py [--batch 10] [--output data/universities.json]

Strategy:
1. Search for "{大学名} 就业质量报告 2024" via web
2. Find PDF links from official university employment portals
3. Download and parse key metrics: employment rate, further study rate, top industries, top employers
4. Update universities.json with precise data
"""

import json
import os
import sys
import time

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("pip install playwright && playwright install chromium")
    sys.exit(1)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "universities.json")

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

EMPLOYMENT_PORTALS = {
    "北京大学": "https://scc.pku.edu.cn",
    "清华大学": "https://career.tsinghua.edu.cn",
    "复旦大学": "https://career.fudan.edu.cn",
    "上海交通大学": "https://career.sjtu.edu.cn",
    "浙江大学": "https://career.zju.edu.cn",
    "南京大学": "https://job.nju.edu.cn",
    "哈尔滨工业大学": "https://career.hit.edu.cn",
    "武汉大学": "https://job.whu.edu.cn",
    "华中科技大学": "https://job.hust.edu.cn",
}


def crawl_school_employment(page, school_name, year=2024):
    """Try to find and extract employment data for a school."""
    search_query = f"{school_name} {year}届毕业生就业质量报告"

    try:
        page.goto(f"https://www.bing.com/search?q={search_query}", timeout=15000)
        page.wait_for_timeout(2000)

        results = page.evaluate("""() => {
            const links = document.querySelectorAll('#b_results .b_algo h2 a');
            return Array.from(links).slice(0, 5).map(a => ({
                title: a.innerText,
                url: a.href
            }));
        }""")

        for result in results:
            if "就业" in result["title"] and (school_name[:2] in result["title"] or "质量" in result["title"]):
                return {"source_url": result["url"], "source_title": result["title"]}

    except Exception as e:
        print(f"  Search failed: {e}")

    return None


def main():
    batch_size = 10
    if "--batch" in sys.argv:
        idx = sys.argv.index("--batch")
        batch_size = int(sys.argv[idx + 1])

    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    print(f"Starting employment data crawl (batch={batch_size})")
    print(f"Total 985 schools: {len(SCHOOLS_985)}")

    updated = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()

        for school in SCHOOLS_985[:batch_size]:
            print(f"\n[{school}]")
            result = crawl_school_employment(page, school)
            if result:
                print(f"  Found: {result['source_title'][:50]}")
                if school in data and data[school].get("就业概况"):
                    data[school]["就业概况"]["数据来源"] = result["source_url"]
                    updated += 1
            else:
                print(f"  No report found")

            time.sleep(2)

        browser.close()

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nDone. Updated {updated} schools with source URLs.")


if __name__ == "__main__":
    main()
