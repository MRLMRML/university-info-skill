#!/usr/bin/env python3
"""Crawl 软科中国大学排名 and update rankings.csv."""

import csv
import os
import time
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "高校信息检索", "data", "rankings.csv")

TARGET_GRADES = {"A+", "A", "A-", "B+"}


def crawl_rankings(year=2024, max_pages=8):
    all_rankings = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        )

        page.goto(f"https://www.shanghairanking.cn/rankings/bcur/{year}", timeout=30000)
        page.wait_for_timeout(3000)

        page_num = 1
        while page_num <= max_pages:
            data = page.evaluate("""() => {
                const rows = document.querySelectorAll('table tbody tr');
                return Array.from(rows).map(row => {
                    const cells = row.querySelectorAll('td');
                    return {
                        rank: cells[0]?.innerText?.trim() || '',
                        name: cells[1]?.innerText?.trim() || '',
                        province: cells[2]?.innerText?.trim() || '',
                        type: cells[3]?.innerText?.trim() || '',
                        score: cells[4]?.innerText?.trim() || ''
                    };
                });
            }""")

            all_rankings.extend(data)
            print(f"Page {page_num}: {len(data)} rows")

            if not data:
                break

            clicked = page.evaluate("""() => {
                const items = document.querySelectorAll('.ant-pagination-item, [class*=pager] li');
                let found = false;
                for (const item of items) {
                    if (item.classList.contains('ant-pagination-item-active') || item.classList.contains('active')) {
                        found = true;
                        continue;
                    }
                    if (found) { item.click(); return true; }
                }
                const nexts = document.querySelectorAll('[class*=next]:not([class*=disabled])');
                if (nexts.length > 0) { nexts[0].click(); return true; }
                return false;
            }""")

            if not clicked:
                break

            page.wait_for_timeout(1500)
            page_num += 1

        browser.close()

    cleaned = []
    seen = set()
    for r in all_rankings:
        name = r["name"].split("\n")[0].strip()
        if name and name not in seen:
            seen.add(name)
            cleaned.append({
                "rank": int(r["rank"]) if r["rank"].isdigit() else 0,
                "name": name,
                "province": r["province"],
                "type": r["type"],
                "score": r["score"],
            })

    cleaned.sort(key=lambda x: x["rank"])

    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["rank", "name", "province", "type", "score"])
        writer.writeheader()
        writer.writerows(cleaned)

    print(f"\nSaved {len(cleaned)} records to {OUTPUT_PATH}")
    return cleaned


if __name__ == "__main__":
    crawl_rankings()
