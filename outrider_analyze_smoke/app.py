from fastapi import FastAPI, HTTPException

from . import db, runner


app = FastAPI(title="outrider-analyze-smoke")


@app.on_event("startup")
def _startup() -> None:
    db.init_schema()


@app.post("/users")
def create_user(username: str, email: str) -> dict:
    user_id = db.create_user(username, email)
    return {"id": user_id, "username": username, "email": email}


@app.get("/users/{username}")
def get_user(username: str) -> dict:
    user = db.get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@app.get("/users")
def search_users(prefix: str) -> list[dict]:
    return db.search_users(prefix)


@app.get("/users/by-email-domain")
def users_by_email_domain(domain: str) -> list[dict]:
    with db.connect() as conn:
        return db.UserSearch(conn).by_email_domain(domain)


@app.get("/ops/ping")
def ops_ping(host: str) -> dict:
    result = runner.ping(host)
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
