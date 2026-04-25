#!/usr/bin/env python3
"""
机场状态检测脚本
- 检测各机场官网是否可访问
- 记录响应时间
- 每周由 GitHub Actions 自动运行
"""

import json
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# 机场列表：[名称, URL, 注册链接]
AIRPORTS = [
    {"name": "自由猫 Freecat", "url": "https://freecat.cloud", "aff": "https://freecat.cloud/register?code=USRIiAoO"},
    {"name": "贝贝云", "url": "https://888.2beibei.com", "aff": "https://888.2beibei.com/register?code=Ilet9Gpi"},
    {"name": "WgetCloud", "url": "https://invite.wgetcloud.ltd", "aff": "https://invite.wgetcloud.ltd/auth/register?code=djq10H"},
    {"name": "悠兔", "url": "https://666.youtu6.shop", "aff": "https://666.youtu6.shop/register?code=Vfs3Qqkm"},
    {"name": "三十六行", "url": "https://qqq.nfsqttt.com", "aff": "https://qqq.nfsqttt.com/register?code=JjW59PTY"},
    {"name": "太极", "url": "https://xn--tfrza853d44tvst.xyz", "aff": "https://xn--tfrza853d44tvst.xyz/register?code=hm0iLlzT"},
    {"name": "NXO Earth", "url": "https://nxonearth.com", "aff": "https://nxonearth.com/signupbyemail.aspx?MemberCode=0fc11e330b274bc6a8dfc2445e56fe0f20260421212953"},
]

TIMEOUT = 10  # 秒


def check_airport(airport):
    """检测单个机场状态"""
    name = airport["name"]
    url = airport["url"]

    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        start = time.time()
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            elapsed_ms = int((time.time() - start) * 1000)
            status_code = resp.getcode()
            return {
                "name": name,
                "url": url,
                "aff": airport["aff"],
                "status": "up" if 200 <= status_code < 400 else "down",
                "status_code": status_code,
                "response_ms": elapsed_ms,
                "last_checked": datetime.now(timezone(timedelta(hours=8))).isoformat(),  # 北京时间
                "note": ""
            }
    except urllib.error.HTTPError as e:
        return {
            "name": name,
            "url": url,
            "aff": airport["aff"],
            "status": "down" if e.code >= 500 else "degraded",
            "status_code": e.code,
            "response_ms": None,
            "last_checked": datetime.now(timezone(timedelta(hours=8))).isoformat(),
            "note": f"HTTP {e.code}"
        }
    except Exception as e:
        return {
            "name": name,
            "url": url,
            "aff": airport["aff"],
            "status": "down",
            "status_code": None,
            "response_ms": None,
            "last_checked": datetime.now(timezone(timedelta(hours=8))).isoformat(),
            "note": str(e)[:50]
        }


def main():
    results = []
    for airport in AIRPORTS:
        print(f"检测中: {airport['name']} ...", end=" ", flush=True)
        result = check_airport(airport)
        status_emoji = "✅" if result["status"] == "up" else "⚠️" if result["status"] == "degraded" else "❌"
        ms_str = f"{result['response_ms']}ms" if result["response_ms"] else "超时"
        print(f"{status_emoji} {result['status']} ({ms_str})")
        results.append(result)
        time.sleep(1)  # 间隔1秒，避免对目标服务器造成压力

    # 生成汇总
    summary = {
        "last_updated": datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "Asia/Shanghai",
        "total": len(results),
        "up": sum(1 for r in results if r["status"] == "up"),
        "down": sum(1 for r in results if r["status"] == "down"),
        "degraded": sum(1 for r in results if r["status"] == "degraded"),
        "airports": results
    }

    # 写入 JSON 文件
    output_path = "data/airport-status.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 检测完成: {summary['up']}/{summary['total']} 正常, {summary['down']} 异常, {summary['degraded']} 降级")
    print(f"📁 结果已保存到 {output_path}")


if __name__ == "__main__":
    main()
