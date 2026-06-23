"""Authentication routes."""

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/login/callback")
def login_callback(user, next: str = "/dashboard"):
    """Resume the user's original destination after authenticating."""
    if user.is_authenticated:
        return RedirectResponse(next)
    return RedirectResponse("/login")
