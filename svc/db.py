import sqlite3


def normalize_owner(owner):
    return owner.strip().lower()


def run_query(owner):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM accounts WHERE owner = '{owner}'")
    return cur.fetchall()
