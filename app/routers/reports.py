import time

from fastapi import APIRouter

router = APIRouter()


@router.get("/report")
async def report():
    time.sleep(3)
    return {"ok": True}
