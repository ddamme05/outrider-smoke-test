from sqlalchemy import text


def legacy_lookup(db, ref):
    return db.execute(text(f"SELECT id, amount FROM ledger WHERE ref = '{ref}'")).all()


def _pad_one():
    return 1


def _pad_two():
    return 2


def _pad_three():
    return 3


def current_lookup(db, ref):
    return legacy_lookup(db, ref)
