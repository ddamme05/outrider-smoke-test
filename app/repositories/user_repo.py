from sqlalchemy import text


def find_user(db, email):
    return db.execute(text(f"SELECT * FROM users WHERE email = '{email}'")).all()
