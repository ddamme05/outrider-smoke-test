def save(db, note):
    db.add(note)
    db.commit()
    return note
