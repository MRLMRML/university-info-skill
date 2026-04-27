#!/usr/bin/env python3
"""
数据备份脚本 — 在更新前自动备份 data/ 目录
用法: python3 scripts/backup_data.py
"""

import shutil
import sys
from datetime import datetime
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = SKILL_ROOT / "data"
BACKUP_ROOT = SKILL_ROOT / "data" / "backup"


def backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = BACKUP_ROOT / timestamp

    backup_dir.mkdir(parents=True, exist_ok=True)

    files_backed_up = []
    for f in DATA_DIR.iterdir():
        if f.is_file() and f.suffix in (".json", ".csv", ".db", ".yaml"):
            shutil.copy2(f, backup_dir / f.name)
            files_backed_up.append(f.name)

    print(f"备份完成: {backup_dir}")
    print(f"备份文件: {', '.join(files_backed_up)}")

    old_backups = sorted(BACKUP_ROOT.iterdir())
    if len(old_backups) > 5:
        for old in old_backups[:-5]:
            shutil.rmtree(old)
            print(f"清理旧备份: {old.name}")

    return backup_dir


if __name__ == "__main__":
    backup()
