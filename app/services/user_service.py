from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repo import UserRepository


class UserService:
    def __init__(self, db: Session):
        self.users = UserRepository(db)

    def list_users(self) -> list[User]:
        return self.users.list_all()

    def search_users(self, query: str) -> list[User]:
        return self.users.search_by_email(query)
