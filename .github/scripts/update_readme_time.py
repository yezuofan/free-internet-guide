#!/usr/bin/env python3
"""
读取 data/airport-status.json，更新各 README 中的最后检测时间标记
"""

import re
import json
from datetime import datetime, timezone, timedelta

# 北京时间
tz_beijing = timezone(timedelta(hours=8))
now_str = datetime.now(tz_beijing).strftime("%Y-%m-%d %H:%M")

def load_status():
    try:
        with open("data/airport-status.json", encoding="utf-8") as f:
            data = json.load(f)
        last = data.get("last_updated", now_str)
        up = data.get("up", "?")
        total = data.get("total", "?")
        return last, f"{up}/{total}"
    except Exception:
        return now_str, "?"


def update_file(filepath, last_updated, status_summary):
    """在文件中替换最后检测时间标记"""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False

    # 替换形如 "⏱️ 最后自动检测：YYYY-MM-DD HH:MM" 的内容
    pattern = r"⏱️ 最后自动检测：\d{4}-\d{2}-\d{2}( \d{2}:\d{2})?"
    replacement = f"⏱️ 最后自动检测：{last_updated}（{status_summary}正常）"
    new_content, count = re.subn(pattern, replacement, content)

    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    last_updated, status_summary = load_status()

    files_to_update = [
        "README.md",
        "getting-started/how-to-choose.md",
        "airport-reviews/README.md",
    ]

    updated = []
    for f in files_to_update:
        if update_file(f, last_updated, status_summary):
            updated.append(f)

    print(f"✅ 更新时间：{last_updated}（{status_summary}正常）")
    for f in updated:
        print(f"   → {f}")


if __name__ == "__main__":
    main()
