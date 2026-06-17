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
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status.value,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Todo":
        return cls(
            title=data["title"],
            status=Status(data["status"]),
            id=data.get("id", 0),
            created_at=data.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M")),
        )


def load() -> list[Todo]:
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"警告: {DATA_FILE.name} 不是有效的 JSON，已按空列表处理")
        return []

    if not isinstance(data, list):
        print(f"警告: {DATA_FILE.name} 格式错误，顶层应为列表")
        return []

    todos = []
    for item in data:
        if isinstance(item, dict):
            todos.append(Todo.from_dict(item))
    return todos



def save(todos: list[Todo]) -> None:
    data = [ todo.to_dict() for todo in todos]
    json_str = json.dumps(data)
    DATA_FILE.write_text(json_str, encoding="utf-8")


def add(todos: list[Todo],title: str) -> Todo:
    max_id = max([todo.id for todo in todos]) if todos else 0
    new_id = max_id+1

    new_todo = Todo(title=title, id=new_id)

    todos.append(new_todo)
    save(todos)

    return new_todo


def complete(todos: list[Todo],todo_id: int) -> bool:
    for todo in todos:
        if todo.id == todo_id:
            todo.status = Status.DONE
            save(todos)
            return True
    return False


def delete(todos:list[Todo], todo_id: int) -> bool:
    for i,todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            save(todos)
            return True
    return False
    
    


def show_list(todos: list[Todo]) -> None:
    for todo in todos:
        print(f"编号 : {todo.id}")
        print(f"标题 : {todo.title}")
        print(f"状态 : {todo.status.value}")
        print(f"创建时间 : {todo.created_at}")
        print("======")


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
                add(todos, title)
        elif choice == "3":
            show_list(todos)
            id_str = input("id: ").strip()
            try:
                todo_id = int(id_str)
            except ValueError:
                print(f"警告: {id_str}, id 必须为数字")
                continue
            if complete(todos, todo_id):
                print(f"已完成待办 #{todo_id}")
            else:
                print(f"未找到 id 为 {todo_id} 的待办")
        elif choice == "4":
            show_list(todos)
            id_str = input("id: ").strip()
            try:
                todo_id = int(id_str)
            except ValueError:
                print(f"警告: {id_str}, id 必须为数字")
                continue

            if delete(todos, todo_id):
                print(f"已删除待办 #{todo_id}")
            else:
                print(f"未找到 id 为 {todo_id} 的待办")
        else:
            print("无效选项")


if __name__ == "__main__":
    main()
