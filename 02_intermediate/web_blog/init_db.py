"""Initialize the local blog database.

Run this script manually before starting the Flask app:

    python init_db.py
"""

from database import DB_FILE, init_db


def main():
    init_db()
    print(f"Database initialized: {DB_FILE}")


if __name__ == "__main__":
    main()
