"""Explainability Engine routes."""
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.core.database import get_db
from app.core.security import get_current_user
from app.services.explainability.explainer import explain_component
from pydantic import BaseModel

router = APIRouter(prefix="/explain", tags=["explain"])


class ExplainRequest(BaseModel):
    design_id: str
    component_id: str


@router.post("/component")
async def explain(
    payload: ExplainRequest,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    design = await db.designs.find_one({
        "_id": ObjectId(payload.design_id),
        "user_id": str(current_user["_id"]),
    })
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")

    arch = design.get("architecture")
    if not arch:
        raise HTTPException(status_code=400, detail="Design not yet generated")

    # Check cache
    cached = design.get("explanations", {}).get(payload.component_id)
    if cached:
        return cached

    # Find the node
    node = next((n for n in arch.get("nodes", []) if n["id"] == payload.component_id), None)
    if not node:
        raise HTTPException(status_code=404, detail="Component not found in design")

    explanation = await explain_component(
        component_id=node["id"],
        component_label=node["label"],
        component_type=node["type"],
        component_tech=node["tech"],
        architecture_summary=arch.get("summary", ""),
    )

    # Persist explanation so subsequent clicks are instant
    await db.designs.update_one(
        {"_id": ObjectId(payload.design_id)},
        {"$set": {f"explanations.{payload.component_id}": explanation}},
    )

    return explanation
