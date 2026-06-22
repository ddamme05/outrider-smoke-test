from fastapi import APIRouter

router = APIRouter()


class UserService:
    def create(self, email: str, age: int):
        return {"email": email, "age": age}


svc = UserService()


@router.post("/users")
def create_user(payload: dict):
    return svc.create(payload["email"], payload["age"])
