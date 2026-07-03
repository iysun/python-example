"""
网页数据爬虫
练习点：requests、BeautifulSoup、数据清洗、CSV 导出
默认示例：爬取 quotes.toscrape.com（专为练习设计的合法爬取网站）
"""

import csv
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
OUTPUT_FILE = Path(__file__).parent / "quotes.csv"
REQUEST_TIMEOUT = 10


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]

    def to_row(self) -> list:
        return [self.text, self.author, ", ".join(self.tags)]


def fetch_page(url: str) -> BeautifulSoup:
    """请求页面并返回解析后的 BeautifulSoup 对象。"""
    res = requests.get(url, timeout=REQUEST_TIMEOUT)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    return soup


def parse_quotes(soup: BeautifulSoup) -> list[Quote]:
    """从页面解析出所有名言。"""
    divs = soup.select(".quote")

    quotes: list[Quote] = []
    for div in divs:
        text_ele = div.select_one("span.text")
        author_ele = div.select_one("small.author")
        if text_ele is None or author_ele is None:
            continue

        tags = div.select("a.tag")
        quotes.append(
            Quote(
                text=text_ele.get_text(strip=True),
                author=author_ele.get_text(strip=True),
                tags=[tag.get_text(strip=True) for tag in tags],
            )
        )

    return quotes


def get_next_url(soup: BeautifulSoup) -> str | None:
    """返回下一页的 URL，没有则返回 None。"""
    next_ele = soup.select_one("li.next")
    if not next_ele:
        return None
    a = next_ele.select_one("a[href]")
    if not a:
        return None
    href = a.get("href")
    if not href:
        return None
    next_url = urljoin(BASE_URL, href)

    return next_url


def save_to_csv(quotes: list[Quote]) -> None:
    """将名言列表保存为 CSV 文件。"""
    with open(OUTPUT_FILE, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        
        csv_writer.writerow(['Text', 'Author', 'Tags'])

        for quote in quotes:
            csv_writer.writerow(quote.to_row())


def main(max_pages: int = 3) -> None:
    all_quotes: list[Quote] = []
    url = BASE_URL

    try:
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
    except requests.RequestException as exc:
        print(f"\n请求失败：{exc}")
    finally:
        save_to_csv(all_quotes)
        print(f"\n共爬取 {len(all_quotes)} 条，已保存至 {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
