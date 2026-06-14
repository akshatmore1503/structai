"""Admin Control Panel routes."""
import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.core.security import get_admin_user
from app.core.database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])

FAISS_INDEX_PATH = os.path.join(
    os.path.dirname(__file__), "../../../../vector_store/faiss_index"
)


class RebuildIndexRequest(BaseModel):
    confirm: bool = False


@router.get("/health")
async def health_check(admin: dict = Depends(get_admin_user)):
    """Verify connectivity to MongoDB and FAISS index status."""
    from app.core.database import get_db
    db = get_db()
    ping = await db.client.admin.command("ping")
    faiss_exists = os.path.exists(FAISS_INDEX_PATH)
    return {
        "mongodb": "ok" if ping.get("ok") == 1 else "error",
        "faiss_index": "ready" if faiss_exists else "not_built",
    }


@router.post("/rebuild-index")
async def rebuild_faiss_index(
    payload: RebuildIndexRequest,
    admin: dict = Depends(get_admin_user),
):
    """Delete and rebuild the FAISS vector index from seed data."""
    if not payload.confirm:
        raise HTTPException(status_code=400, detail="Set confirm=true to rebuild")

    import shutil
    if os.path.exists(FAISS_INDEX_PATH):
        shutil.rmtree(FAISS_INDEX_PATH)

    # Reset the cached vector store so it rebuilds on next request
    from app.services.design_builder import rag
    rag._vector_store = None

    return {"status": "Index cleared. Will rebuild on next design generation."}


@router.get("/users")
async def list_users(
    admin: dict = Depends(get_admin_user),
    db=Depends(get_db),
):
    cursor = db.users.find({}, {"name": 1, "email": 1, "role": 1, "design_count": 1, "quiz_count": 1, "created_at": 1})
    return [
        {
            "id": str(u["_id"]),
            "name": u["name"],
            "email": u["email"],
            "role": u["role"],
            "design_count": u.get("design_count", 0),
            "quiz_count": u.get("quiz_count", 0),
            "created_at": u["created_at"].isoformat(),
        }
        async for u in cursor
    ]


@router.patch("/users/{user_id}/role")
async def update_user_role(
    user_id: str,
    role: str,
    admin: dict = Depends(get_admin_user),
    db=Depends(get_db),
):
    if role not in ("student", "admin"):
        raise HTTPException(status_code=400, detail="Role must be 'student' or 'admin'")
    from bson import ObjectId
    result = await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"role": role}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"updated": True}
