import time

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()


@router.get("/greet")
def greet(name: str):
    return HTMLResponse(f"<h1>Hello {name}</h1>")


@router.get("/go")
def go(next: str):
    return RedirectResponse(next)


@router.get("/report")
async def report():
    time.sleep(3)
    return {"ok": True}
