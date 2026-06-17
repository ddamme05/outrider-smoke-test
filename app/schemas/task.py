from datetime import datetime

from pydantic import BaseModel

from app.schemas.tag import TagRead


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    tag_names: list[str] = []


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    tag_names: list[str] | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    tags: list[TagRead] = []

    model_config = {"from_attributes": True}
