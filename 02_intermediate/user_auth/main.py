"""
用户注册 / 登录系统（SQLite + 密码哈希）
练习点：SQLite、hashlib / bcrypt、会话 token、输入验证
"""
import hashlib
import secrets
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "users.db"


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                username      TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt          TEXT NOT NULL,
                created_at    TEXT DEFAULT (datetime('now'))
            )
        """)


def hash_password(password: str, salt: str) -> str:
    """用 SHA-256 + salt 哈希密码（实际项目建议用 bcrypt）。"""
    return hashlib.sha256(f"{salt}{password}".encode()).hexdigest()


def register(username: str, password: str) -> bool:
    """注册新用户，用户名重复返回 False。"""
    # TODO: 生成随机 salt（secrets.token_hex(16)）
    # TODO: 计算 password_hash，插入数据库
    # TODO: 捕获 sqlite3.IntegrityError（用户名重复），返回 False
    raise NotImplementedError


def login(username: str, password: str) -> dict | None:
    """验证登录，成功返回用户信息字典，失败返回 None。"""
    # TODO: 查询用户，取出 salt，重新哈希后比对
    raise NotImplementedError


def generate_session_token() -> str:
    return secrets.token_urlsafe(32)


MENU = "1.注册  2.登录  0.退出\n>>> "

def main():
    init_db()
    current_user = None

    while True:
        if current_user:
            print(f"\n当前用户：{current_user['username']}")
        choice = input(MENU).strip()

        if choice == "0":
            break
        elif choice == "1":
            username = input("用户名：").strip()
            password = input("密码：").strip()
            # TODO: 调用 register()，打印成功或失败信息
        elif choice == "2":
            username = input("用户名：").strip()
            password = input("密码：").strip()
            # TODO: 调用 login()，成功则更新 current_user
        else:
            print("无效选项")


if __name__ == "__main__":
    main()
