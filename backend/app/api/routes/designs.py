"""Design Builder routes."""
from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from bson import ObjectId
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.design import DesignCreate, ClarificationSubmit
from app.services.design_builder.pipeline import run_initial, run_with_clarifications

router = APIRouter(prefix="/designs", tags=["designs"])


def _serialize(doc: dict) -> dict:
    doc["id"] = str(doc.pop("_id"))
    return doc


@router.post("/generate")
async def generate_design(
    payload: DesignCreate,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    """
    Step 1: Submit a problem statement.
    Returns clarifying questions if ambiguities detected, otherwise returns the full architecture.
    """
    state = await run_initial(payload.problem_statement)

    if state.get("error"):
        raise HTTPException(status_code=500, detail=state["error"])

    design_doc = {
        "user_id": str(current_user["_id"]),
        "problem_statement": payload.problem_statement,
        "requirements": state.get("requirements", {}),
        "architecture": state.get("architecture"),
        "explanations": {},
        "status": "complete" if state.get("architecture") else "awaiting_clarification",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    if state.get("clarifying_questions"):
        design_doc["clarifying_questions"] = state["clarifying_questions"]

    result = await db.designs.insert_one(design_doc)
    design_id = str(result.inserted_id)

    # Increment user design count
    await db.users.update_one(
        {"_id": current_user["_id"]},
        {"$inc": {"design_count": 1}},
    )

    if state.get("architecture"):
        return {
            "design_id": design_id,
            "status": "complete",
            "architecture": state["architecture"],
        }
    else:
        return {
            "design_id": design_id,
            "status": "awaiting_clarification",
            "clarifying_questions": state.get("clarifying_questions", []),
        }


@router.post("/{design_id}/clarify")
async def submit_clarifications(
    design_id: str,
    payload: ClarificationSubmit,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    """Step 2: Submit answers to clarifying questions → get full architecture."""
    design = await db.designs.find_one({
        "_id": ObjectId(design_id),
        "user_id": str(current_user["_id"]),
    })
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")

    state = await run_with_clarifications(
        design["problem_statement"],
        design["requirements"],
        payload.clarifications,
    )

    if state.get("error"):
        raise HTTPException(status_code=500, detail=state["error"])

    await db.designs.update_one(
        {"_id": ObjectId(design_id)},
        {"$set": {
            "architecture": state["architecture"],
            "clarifications": payload.clarifications,
            "status": "complete",
            "updated_at": datetime.utcnow(),
        }},
    )

    return {
        "design_id": design_id,
        "status": "complete",
        "architecture": state["architecture"],
    }


@router.get("/{design_id}")
async def get_design(
    design_id: str,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    design = await db.designs.find_one({
        "_id": ObjectId(design_id),
        "user_id": str(current_user["_id"]),
    })
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    return _serialize(design)


@router.get("/")
async def list_designs(
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    cursor = db.designs.find(
        {"user_id": str(current_user["_id"])},
        {"problem_statement": 1, "status": 1, "created_at": 1},
    ).sort("created_at", -1).limit(20)

    return [_serialize(d) async for d in cursor]


@router.delete("/{design_id}")
async def delete_design(
    design_id: str,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    result = await db.designs.delete_one({
        "_id": ObjectId(design_id),
        "user_id": str(current_user["_id"]),
    })
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Design not found")

    await db.users.update_one(
        {"_id": current_user["_id"]},
        {"$inc": {"design_count": -1}},
    )
    return {"deleted": True}
