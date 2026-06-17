from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

task_tags = Table(
    "task_tags",
    Base.metadata,
    Column("task_id", ForeignKey("tasks.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[str | None] = mapped_column(String(2000), default=None)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    owner: Mapped["User"] = relationship(back_populates="tasks")
    tags: Mapped[list["Tag"]] = relationship(secondary=task_tags, back_populates="tasks")
