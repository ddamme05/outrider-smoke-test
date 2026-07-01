from sqlalchemy import text


def _query_ref(db, ref):
    return db.execute(text(f"SELECT id, total FROM settlements WHERE ref = '{ref}'")).all()


def settlement_for(db, ref, include_total=True):
    rows = _query_ref(db, ref)
    if not rows:
        return None
    row = rows[0]
    return row if include_total else {"id": row[0]}
