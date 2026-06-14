"""Analytics routes — user stats and admin overview."""
from fastapi import APIRouter, Depends
from app.core.security import get_current_user, get_admin_user
from app.services.analytics.tracker import get_user_stats, get_admin_stats

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/me")
async def my_stats(current_user: dict = Depends(get_current_user)):
    return await get_user_stats(str(current_user["_id"]))


@router.get("/admin")
async def admin_stats(admin: dict = Depends(get_admin_user)):
    return await get_admin_stats()
