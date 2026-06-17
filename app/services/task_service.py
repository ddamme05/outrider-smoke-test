from sqlalchemy.orm import Session

from app.models.tag import Tag
from app.models.task import Task
from app.repositories.task_repo import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, db: Session):
        self.db = db
        self.tasks = TaskRepository(db)

    def list_tasks(self, owner_id: int, include_completed: bool = True) -> list[Task]:
        return self.tasks.list_for_owner(owner_id, include_completed=include_completed)

    def create_task(self, owner_id: int, payload: TaskCreate) -> Task:
        task = Task(title=payload.title, description=payload.description, owner_id=owner_id)
        task.tags = [self.get_or_create_tag(name) for name in payload.tag_names]
        return self.tasks.create(task)

    def update_task(self, owner_id: int, task_id: int, payload: TaskUpdate) -> Task | None:
        task = self.tasks.get_owned(owner_id, task_id)
        if task is None:
            return None

        for field in ("title", "description", "completed"):
            value = getattr(payload, field)
            if value is not None:
                setattr(task, field, value)

        if payload.tag_names is not None:
            task.tags = [self.get_or_create_tag(name) for name in payload.tag_names]

        self.db.commit()
        self.db.refresh(task)
        return task

    def get_or_create_tag(self, name: str) -> Tag:
        tag = self.tasks.get_tag_by_name(name)
        if tag is not None:
            return tag
        return self.tasks.create_tag(Tag(name=name))

    def list_tags(self, owner_id: int) -> list[Tag]:
        return self.tasks.list_tags_for_owner(owner_id)
