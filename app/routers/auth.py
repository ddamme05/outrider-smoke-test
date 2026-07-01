from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/login/callback")
def login_callback(user):
    if user.is_authenticated:
        return RedirectResponse("/dashboard")
    return RedirectResponse("/login")
