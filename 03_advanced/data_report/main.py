"""
数据分析报告生成器
练习点：pandas、matplotlib、数据清洗、可视化、PDF/HTML 报告输出
将 CSV 文件放入 data/ 目录运行即可
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def load_data(filepath: Path) -> pd.DataFrame:
    """加载 CSV 并做基本清洗。"""
    # TODO: pd.read_csv()，去除全空行，strip 字符串列的空格
    raise NotImplementedError


def basic_stats(df: pd.DataFrame) -> pd.DataFrame:
    """返回数值列的描述性统计（count / mean / std / min / max）。"""
    # TODO: df.describe() 并格式化
    raise NotImplementedError


def plot_distribution(df: pd.DataFrame, column: str, output_path: Path):
    """绘制指定列的分布直方图并保存。"""
    # TODO: plt.hist() + 标题 / 标签，保存到 output_path
    raise NotImplementedError


def plot_correlation(df: pd.DataFrame, output_path: Path):
    """绘制数值列的相关性热力图。"""
    # TODO: df.corr() + plt.imshow() 或 seaborn.heatmap()
    raise NotImplementedError


def plot_time_series(df: pd.DataFrame, date_col: str, value_col: str, output_path: Path):
    """绘制时间序列折线图（如果数据包含日期列）。"""
    # TODO: 将 date_col 转为 datetime，按日期排序，绘制折线图
    raise NotImplementedError


def generate_html_report(df: pd.DataFrame, stats: pd.DataFrame, image_paths: list[Path]):
    """将统计结果和图表合并成一个 HTML 报告。"""
    # TODO: 用 f-string 拼接 HTML，将图片用 base64 内嵌，写入 output/report.html
    raise NotImplementedError


def main():
    csv_files = list(DATA_DIR.glob("*.csv"))
    if not csv_files:
        print(f"请将 CSV 文件放入 {DATA_DIR}")
        return

    filepath = csv_files[0]
    print(f"分析文件：{filepath.name}")

    df = load_data(filepath)
    print(f"数据维度：{df.shape[0]} 行 x {df.shape[1]} 列")

    stats = basic_stats(df)
    print(stats)

    numeric_cols = df.select_dtypes("number").columns.tolist()
    images = []
    for col in numeric_cols[:3]:
        out = OUTPUT_DIR / f"dist_{col}.png"
        plot_distribution(df, col, out)
        images.append(out)

    if len(numeric_cols) >= 2:
        out = OUTPUT_DIR / "correlation.png"
        plot_correlation(df, out)
        images.append(out)

    generate_html_report(df, stats, images)
    print(f"报告已生成：{OUTPUT_DIR / 'report.html'}")


if __name__ == "__main__":
    main()
