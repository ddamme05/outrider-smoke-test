from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    display_name: str
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    display_name: str
    task_count: int = 0

    model_config = {"from_attributes": True}


class TokenRead(BaseModel):
    access_token: str
    token_type: str = "bearer"
