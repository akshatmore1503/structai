"""Auth routes — upsert user on first OAuth login."""
from fastapi import APIRouter, Depends
from datetime import datetime
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/upsert-user")
async def upsert_user(payload: UserCreate, db=Depends(get_db)):
    """Called by the frontend after successful Google OAuth to sync the user into MongoDB."""
    existing = await db.users.find_one({"email": payload.email})
    if existing:
        user = existing
    else:
        user_doc = {
            "name": payload.name,
            "email": payload.email,
            "image": payload.image,
            "role": "student",
            "created_at": datetime.utcnow(),
            "design_count": 0,
            "quiz_count": 0,
        }
        result = await db.users.insert_one(user_doc)
        user = await db.users.find_one({"_id": result.inserted_id})

    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "image": user.get("image"),
        "role": user["role"],
        "created_at": user["created_at"].isoformat(),
        "design_count": user.get("design_count", 0),
        "quiz_count": user.get("quiz_count", 0),
    }


@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "id": str(current_user["_id"]),
        "name": current_user["name"],
        "email": current_user["email"],
        "image": current_user.get("image"),
        "role": current_user["role"],
        "created_at": current_user["created_at"].isoformat(),
        "design_count": current_user.get("design_count", 0),
        "quiz_count": current_user.get("quiz_count", 0),
    }
