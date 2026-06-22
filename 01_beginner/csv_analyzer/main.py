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
    # 用 csv.DictReader 读取文件，返回 headers 和 rows
    with open(filepath, mode='r', encoding="utf-8") as file:
        reader = csv.DictReader(f=file)
        headers = reader.fieldnames
        rows = list(reader)
    return headers, rows


def summary(rows: list[dict], column: str) -> dict:
    """对数值列进行统计：最大值、最小值、平均值、总和。"""
    values = []
    for row in rows:
        try:
            values.append(float(row[column]))
        except (ValueError, TypeError):
            continue
    if not values:
        return {}
    return {
        "max": max(values),
        "min": min(values),
        "avg": sum(values) / len(values),
        "sum": sum(values),
        "count": len(values),
    }


def frequency(rows: list[dict], column: str) -> Counter:
    """统计文本列中各值的出现频次。"""
    return Counter(row[column] for row in rows)


def group_sum(rows: list[dict], group_col: str, value_col: str) -> dict:
    """按 group_col 分组，对 value_col 求和。"""
    result = defaultdict(float)
    for row in rows:
        try:
            result[row[group_col]] += float(row[value_col])
        except (ValueError, TypeError):
            continue
    return dict(result)


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

    while True:
        fileIndex = input("请选择文件: ")
        file = csv_files[int(fileIndex)]
        print(f'你选择了 {file.name}')
        # 加载后打印列名，让用户选择要分析的列和操作类型
        headers, rows  = load_csv(file)
        print(f'csv 列 {" ".join([f"{index}:{item}" for index, item in enumerate(headers)])}')
        rowIndex = input("请选择你要操作的列名: ")
        col = headers[int(rowIndex)]

        print(f'1: summary  2: frequency  3: group_sum')
        action = input("请选择操作类型: ")

        match action:
            case "1":
                result = summary(rows, col)
                print_table(result, f"统计结果 - {col}")
            case "2":
                result = frequency(rows, col)
                print_table(result, f"频次统计 - {col}")
            case "3":
                print(f'csv 列 {" ".join([f"{index}:{item}" for index, item in enumerate(headers)])}')
                _i = input("请选择要累加值的列名: ")
                value_col = headers[int(_i)]
                result = group_sum(rows, col, value_col)
                print_table(result, f"分组求和 - {col} -> {value_col}")
            case _:
                print("unknown action")


if __name__ == "__main__":
    main()
