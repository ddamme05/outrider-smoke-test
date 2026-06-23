"""Direct account lookups for the admin billing console."""

import sqlite3


def _conn() -> sqlite3.Connection:
    return sqlite3.connect("billing.db")


def find_by_plan(plan: str):
    """List accounts on a given billing plan."""
    cur = _conn().cursor()
    cur.execute(f"SELECT id, email FROM accounts WHERE plan = '{plan}'")
    return cur.fetchall()
