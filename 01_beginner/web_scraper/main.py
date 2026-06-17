"""
网页数据爬虫
练习点：requests、BeautifulSoup、数据清洗、CSV 导出
默认示例：爬取 quotes.toscrape.com（专为练习设计的合法爬取网站）
"""
import csv
import time
from dataclasses import dataclass
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
OUTPUT_FILE = Path(__file__).parent / "quotes.csv"


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]

    def to_row(self) -> list:
        return [self.text, self.author, ", ".join(self.tags)]


def fetch_page(url: str) -> BeautifulSoup:
    """请求页面并返回解析后的 BeautifulSoup 对象。"""
    # TODO: 用 requests.get() 请求，检查状态码，返回 BeautifulSoup(response.text, "html.parser")
    raise NotImplementedError


def parse_quotes(soup: BeautifulSoup) -> list[Quote]:
    """从页面解析出所有名言。"""
    # TODO: 用 soup.select(".quote") 找到每个名言块
    # TODO: 从每块中提取 text / author / tags
    raise NotImplementedError


def get_next_url(soup: BeautifulSoup) -> str | None:
    """返回下一页的 URL，没有则返回 None。"""
    # TODO: 查找 .next a 标签，拼接 BASE_URL + href
    raise NotImplementedError


def save_to_csv(quotes: list[Quote]) -> None:
    """将名言列表保存为 CSV 文件。"""
    # TODO: 用 csv.writer 写入表头和每行数据
    raise NotImplementedError


def main(max_pages: int = 3):
    all_quotes: list[Quote] = []
    url = BASE_URL

    for page in range(1, max_pages + 1):
        print(f"正在爬取第 {page} 页：{url}")
        soup = fetch_page(url)
        quotes = parse_quotes(soup)
        all_quotes.extend(quotes)
        print(f"  获取 {len(quotes)} 条名言")

        next_url = get_next_url(soup)
        if not next_url:
            break
        url = next_url
        time.sleep(1)  # 礼貌性延迟，避免频繁请求

    save_to_csv(all_quotes)
    print(f"\n共爬取 {len(all_quotes)} 条，已保存至 {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
