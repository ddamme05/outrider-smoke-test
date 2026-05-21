import sqlite3
from contextlib import contextmanager
from typing import Iterator, Optional


DB_PATH = "smoke.db"


@contextmanager
def connect(path: str = DB_PATH) -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(path)
    try:
        conn.row_factory = sqlite3.Row
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_schema() -> None:
    with connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL
            )
            """
        )


def create_user(username: str, email: str) -> int:
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email),
        )
        return int(cur.lastrowid)


def get_user_by_username(username: str) -> Optional[dict]:
    with connect() as conn:
        cur = conn.execute(
            "SELECT id, username, email FROM users WHERE username = ?",
            (username,),
        )
        row = cur.fetchone()
        return dict(row) if row else None


def search_users(prefix: str) -> list[dict]:
    with connect() as conn:
        cur = conn.execute(
            "SELECT id, username, email FROM users WHERE username LIKE ? ORDER BY id",
            (f"{prefix}%",),
        )
        return [dict(row) for row in cur.fetchall()]


class UserSearch:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def by_name(self, name: str) -> list[dict]:
        cur = self.conn.execute(
            "SELECT id, username, email FROM users WHERE username = ?",
            (name,),
        )
        return [dict(row) for row in cur.fetchall()]

    def by_email_domain(self, domain: str) -> list[dict]:
        cur = self.conn.execute(
            "SELECT id, username, email FROM users WHERE email LIKE ? ORDER BY id",
            (f"%@{domain}",),
        )
        return [dict(row) for row in cur.fetchall()]
