"""
待办事项 CLI
练习点：JSON 文件读写、列表操作、枚举、datetime
"""
import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path

DATA_FILE = Path(__file__).parent / "todos.json"


class Status(Enum):
    PENDING = "待完成"
    DONE = "已完成"


@dataclass
class Todo:
    title: str
    status: Status = Status.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))
    id: int = 0

    def to_dict(self) -> dict:
        # TODO: 返回可 JSON 序列化的字典
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict) -> "Todo":
        # TODO: 从字典还原 Todo 对象
        raise NotImplementedError


def load() -> list[Todo]:
    # TODO: 从 DATA_FILE 读取，文件不存在返回 []
    raise NotImplementedError


def save(todos: list[Todo]) -> None:
    # TODO: 序列化后写入 DATA_FILE
    raise NotImplementedError


def add(title: str) -> Todo:
    # TODO: 创建新 Todo（id 自增），追加保存
    raise NotImplementedError


def complete(todo_id: int) -> bool:
    # TODO: 找到对应 id，将 status 改为 DONE，返回是否成功
    raise NotImplementedError


def delete(todo_id: int) -> bool:
    # TODO: 删除对应 id 的条目
    raise NotImplementedError


def show_list(todos: list[Todo]) -> None:
    # TODO: 用格式化字符串打印编号、状态、标题、创建时间
    raise NotImplementedError


MENU = """
1. 查看全部  2. 添加  3. 完成  4. 删除  0. 退出
"""

def main():
    while True:
        print(MENU, end="")
        choice = input(">>> ").strip()
        todos = load()

        if choice == "0":
            break
        elif choice == "1":
            show_list(todos)
        elif choice == "2":
            title = input("内容：").strip()
            if title:
                add(title)
        elif choice == "3":
            show_list(todos)
            # TODO: 获取 id 输入，调用 complete()
        elif choice == "4":
            show_list(todos)
            # TODO: 获取 id 输入，调用 delete()
        else:
            print("无效选项")


if __name__ == "__main__":
    main()
