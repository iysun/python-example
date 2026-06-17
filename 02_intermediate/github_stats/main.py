"""
GitHub 个人提交统计
练习点：requests、GitHub REST API、数据聚合、日期处理
文档：https://docs.github.com/en/rest
"""
import os
from collections import Counter, defaultdict
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
API_BASE = "https://api.github.com"


def get_headers() -> dict:
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def get_user_repos(username: str) -> list[dict]:
    """获取用户的所有公开仓库。"""
    # TODO: 请求 /users/{username}/repos，处理分页（per_page=100）
    raise NotImplementedError


def get_commits(username: str, repo: str, since_days: int = 365) -> list[dict]:
    """获取仓库最近 since_days 天内的提交。"""
    since = (datetime.utcnow() - timedelta(days=since_days)).isoformat() + "Z"
    # TODO: 请求 /repos/{username}/{repo}/commits，参数：author=username, since=since
    raise NotImplementedError


def analyze(username: str, since_days: int = 365):
    """统计用户在所有仓库的提交情况。"""
    repos = get_user_repos(username)
    print(f"找到 {len(repos)} 个仓库，正在统计近 {since_days} 天的提交...\n")

    total = 0
    by_repo: dict[str, int] = {}
    by_weekday: Counter = Counter()

    for repo in repos:
        commits = get_commits(username, repo["name"], since_days)
        count = len(commits)
        if count == 0:
            continue
        by_repo[repo["name"]] = count
        total += count

        for c in commits:
            date_str = c["commit"]["author"]["date"]
            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            by_weekday[dt.strftime("%A")] += 1

    # TODO: 打印总提交数、最活跃仓库 Top5、每周各天提交分布
    raise NotImplementedError


def main():
    username = input("GitHub 用户名：").strip()
    if not username:
        return
    analyze(username)


if __name__ == "__main__":
    main()
