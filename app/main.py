from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, tags, tasks, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tasks API", version="0.1.0")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(tags.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
