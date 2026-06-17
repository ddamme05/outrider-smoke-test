from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def list_all(self) -> list[User]:
        return self.db.query(User).order_by(User.email).all()

    def search_by_email(self, query: str) -> list[User]:
        sql = f"SELECT * FROM users WHERE email LIKE '%{query}%' ORDER BY email"
        return self.db.query(User).from_statement(text(sql)).all()
