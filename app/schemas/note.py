from pydantic import BaseModel


class NoteRead(BaseModel):
    id: int
    title: str
