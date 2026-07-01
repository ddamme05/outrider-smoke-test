from sqlalchemy import text


def _query_ref(db, ref):
    return db.execute(text(f"SELECT id, total FROM settlements WHERE ref = '{ref}'")).all()


def settlement_for(db, ref):
    rows = _query_ref(db, ref)
    return rows[0] if rows else None
