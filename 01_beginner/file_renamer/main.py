"""
文件批量重命名工具
练习点：os / pathlib、字符串处理、命令行参数（argparse）
"""
import argparse
from pathlib import Path


def rename_files(directory: str, prefix: str = "", suffix: str = "", dry_run: bool = True):
    """批量重命名目录下的文件。

    Args:
        directory: 目标目录路径
        prefix:    添加到文件名前的字符串
        suffix:    添加到扩展名前的字符串（如 '_backup'）
        dry_run:   True 时只打印预览，不实际重命名
    """
    folder = Path(directory)
    if not folder.is_dir():
        print(f"错误：{directory} 不是有效目录")
        return

    files = [f for f in folder.iterdir() if f.is_file()]
    if not files:
        print("目录下没有文件。")
        return

    for f in files:
        new_name = f"{prefix}{f.stem}{suffix}{f.suffix}"
        new_path = f.parent / new_name

        if dry_run:
            # TODO: 打印 "预览: 旧名 -> 新名"
            pass
        else:
            # TODO: 调用 f.rename(new_path) 执行重命名
            pass


def build_parser() -> argparse.ArgumentParser:
    # TODO: 用 argparse 定义 directory / --prefix / --suffix / --run 参数
    parser = argparse.ArgumentParser(description="批量重命名文件")
    raise NotImplementedError


def main():
    parser = build_parser()
    args = parser.parse_args()
    rename_files(args.directory, args.prefix, args.suffix, dry_run=not args.run)


if __name__ == "__main__":
    main()
