"""
CSV 数据分析器
练习点：csv 模块、collections、统计计算、简单可视化（可选）
用法：将 CSV 文件放入 data/ 目录，运行后选择文件和分析维度
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent / "data"


def load_csv(filepath: Path) -> tuple[list[str], list[dict]]:
    """读取 CSV 文件，返回 (列名列表, 行数据列表)。"""
    # TODO: 用 csv.DictReader 读取文件，返回 headers 和 rows
    raise NotImplementedError


def summary(rows: list[dict], column: str) -> dict:
    """对数值列进行统计：最大值、最小值、平均值、总和。"""
    # TODO: 提取指定列的数值，计算统计量
    # 提示：用 float() 转换，跳过无法转换的值
    raise NotImplementedError


def frequency(rows: list[dict], column: str) -> Counter:
    """统计文本列中各值的出现频次。"""
    # TODO: 用 Counter 统计指定列的值频率
    raise NotImplementedError


def group_sum(rows: list[dict], group_col: str, value_col: str) -> dict:
    """按 group_col 分组，对 value_col 求和。"""
    # TODO: 用 defaultdict(float) 按分组累加
    raise NotImplementedError


def print_table(data: dict, title: str = "") -> None:
    """简单打印字典数据为表格（不依赖第三方库）。"""
    if title:
        print(f"\n=== {title} ===")
    for k, v in data.items():
        print(f"  {k:<20} {v}")


def main():
    csv_files = list(DATA_DIR.glob("*.csv"))
    if not csv_files:
        print(f"请将 CSV 文件放入 {DATA_DIR} 目录")
        return

    print("可用文件：")
    for i, f in enumerate(csv_files, 1):
        print(f"  {i}. {f.name}")

    # TODO: 让用户选择文件
    # TODO: 加载后打印列名，让用户选择要分析的列和操作类型
    # TODO: 根据列的数据类型（数值/文本）调用对应分析函数并展示结果
    raise NotImplementedError


if __name__ == "__main__":
    main()
