#!/usr/bin/env python3
"""
数据更新流水线 — 一键执行全部数据更新流程
用法:
  python3 scripts/pipeline/run_all.py              # 执行全部更新
  python3 scripts/pipeline/run_all.py --dry-run    # 预览模式
  python3 scripts/pipeline/run_all.py --only=scores # 仅更新分数线
"""

import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = SKILL_ROOT / "scripts"
DATA_DIR = SKILL_ROOT / "data"

TASKS = [
    {
        "name": "backup",
        "desc": "备份当前数据",
        "cmd": ["python3", str(SCRIPTS_DIR / "backup_data.py")],
    },
    {
        "name": "sync_json_db",
        "desc": "同步 JSON → SQLite",
        "cmd": ["python3", str(SCRIPTS_DIR / "sync_json_db.py"), "json2db"],
    },
    {
        "name": "validate",
        "desc": "数据校验",
        "cmd": ["python3", str(SCRIPTS_DIR / "validate_all.py")],
    },
]


def run_task(task, dry_run=False):
    name = task["name"]
    desc = task["desc"]
    cmd = task["cmd"]

    print(f"\n{'='*50}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {desc} ({name})")
    print(f"  命令: {' '.join(cmd)}")

    if dry_run:
        print("  [DRY RUN] 跳过执行")
        return True

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                print(f"  {line}")
        if result.returncode != 0:
            print(f"  ❌ 失败 (exit code {result.returncode})")
            if result.stderr:
                print(f"  错误: {result.stderr.strip()}")
            return False
        print(f"  ✅ 完成")
        return True
    except subprocess.TimeoutExpired:
        print(f"  ❌ 超时 (>120s)")
        return False
    except Exception as e:
        print(f"  ❌ 异常: {e}")
        return False


def main():
    dry_run = "--dry-run" in sys.argv
    only = None
    for arg in sys.argv[1:]:
        if arg.startswith("--only="):
            only = arg.split("=")[1]

    print(f"{'='*50}")
    print(f"数据更新流水线")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"模式: {'预览' if dry_run else '执行'}")
    if only:
        print(f"范围: 仅 {only}")
    print(f"{'='*50}")

    tasks_to_run = TASKS
    if only:
        tasks_to_run = [t for t in TASKS if t["name"] == only]
        if not tasks_to_run:
            print(f"未知任务: {only}")
            print(f"可用任务: {[t['name'] for t in TASKS]}")
            sys.exit(1)

    results = {}
    for task in tasks_to_run:
        ok = run_task(task, dry_run)
        results[task["name"]] = ok

    print(f"\n{'='*50}")
    print("执行摘要:")
    all_ok = True
    for task in tasks_to_run:
        status = "✅" if results[task["name"]] else "❌"
        print(f"  {status} {task['desc']}")
        if not results[task["name"]]:
            all_ok = False

    if all_ok:
        print("\n✅ 全部完成")
    else:
        print("\n❌ 部分任务失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
