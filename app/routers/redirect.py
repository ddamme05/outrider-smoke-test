from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/go")
def go(next: str):
    return RedirectResponse(next)
