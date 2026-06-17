"""
网页自动化 —— 自动登录并截图示例
练习点：playwright（推荐）或 selenium、等待策略、截图、数据提取
目标网站：https://the-internet.herokuapp.com/login（公开练习站）
"""
from pathlib import Path

# 安装：pip install playwright && playwright install chromium
from playwright.sync_api import sync_playwright, Page

SCREENSHOT_DIR = Path(__file__).parent / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

TARGET_URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def login(page: Page):
    """执行登录操作。"""
    page.goto(TARGET_URL)
    # TODO: 用 page.fill("#username", USERNAME) 填写用户名
    # TODO: 用 page.fill("#password", PASSWORD) 填写密码
    # TODO: 用 page.click("button[type='submit']") 点击登录
    # TODO: 用 page.wait_for_selector(".flash.success") 等待成功消息
    raise NotImplementedError


def take_screenshot(page: Page, name: str):
    path = SCREENSHOT_DIR / f"{name}.png"
    page.screenshot(path=str(path))
    print(f"截图已保存：{path}")


def extract_items(page: Page) -> list[str]:
    """提取页面上的列表项文字。"""
    # TODO: 用 page.query_selector_all() 找到目标元素，提取 inner_text()
    raise NotImplementedError


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True 不弹出窗口
        page = browser.new_page()

        login(page)
        take_screenshot(page, "after_login")

        items = extract_items(page)
        for item in items:
            print(f"  - {item}")

        browser.close()


if __name__ == "__main__":
    main()
