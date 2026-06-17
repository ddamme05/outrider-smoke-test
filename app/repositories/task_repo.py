from sqlalchemy.orm import Session

from app.models.tag import Tag
from app.models.task import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_owned(self, owner_id: int, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.owner_id == owner_id, Task.id == task_id).first()

    def list_for_owner(self, owner_id: int, include_completed: bool = True) -> list[Task]:
        query = self.db.query(Task).filter(Task.owner_id == owner_id).order_by(Task.created_at.desc())
        if not include_completed:
            query = query.filter(Task.completed.is_(False))
        return query.all()

    def get_tag_by_name(self, name: str) -> Tag | None:
        return self.db.query(Tag).filter(Tag.name == name).first()

    def create_tag(self, tag: Tag) -> Tag:
        self.db.add(tag)
        self.db.commit()
        self.db.refresh(tag)
        return tag

    def list_tags_for_owner(self, owner_id: int) -> list[Tag]:
        return (
            self.db.query(Tag)
            .join(Tag.tasks)
            .filter(Task.owner_id == owner_id)
            .order_by(Tag.name)
            .distinct()
            .all()
        )
