from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.schemas.user import UserRead
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    users = UserService(db).list_users()
    return [
        UserRead(id=user.id, email=user.email, display_name=user.display_name, task_count=len(user.tasks))
        for user in users
    ]


@router.get("/search", response_model=list[UserRead])
def search_users(q: str, db: Session = Depends(get_db)):
    return UserService(db).search_users(q)
