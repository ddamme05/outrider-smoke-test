from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.security.tokens import make_reset_token

router = APIRouter()


@router.get("/login/callback")
def login_callback(user, next: str = "/dashboard"):
    if user.is_authenticated:
        user.reset_token = make_reset_token()
        return RedirectResponse(next)
    return RedirectResponse("/login")
