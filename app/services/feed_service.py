class Post:
    user_id: int


def feed(db, users):
    return [(u, db.query(Post).filter_by(user_id=u.id).all()) for u in users]
