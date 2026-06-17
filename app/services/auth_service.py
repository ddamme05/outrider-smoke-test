import secrets

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.users = UserRepository(db)

    def get_user_by_email(self, email: str) -> User | None:
        return self.users.get_by_email(email)

    def register(self, payload: UserCreate) -> User:
        user = User(
            email=payload.email,
            display_name=payload.display_name,
            password_hash=payload.password,
            api_token=secrets.token_urlsafe(32),
        )
        return self.users.create(user)

    def login(self, email: str, password: str) -> str | None:
        user = self.users.get_by_email(email)
        if not user or user.password_hash != password:
            return None
        return user.api_token

    def user_from_token(self, token: str) -> User | None:
        for user in self.users.list_all():
            if user.api_token == token:
                return user
        return None
