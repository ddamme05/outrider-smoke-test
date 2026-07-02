class Post:
    user_id: int


def read_report(name: str):
    with open(f"/var/data/{name}") as f:
        return f.read()


def feed(db, users):
    return [(u, db.query(Post).filter_by(user_id=u.id).all()) for u in users]


def sync_totals(db):
    try:
        db.execute("UPDATE totals SET synced = 1")
    except Exception:
        pass
