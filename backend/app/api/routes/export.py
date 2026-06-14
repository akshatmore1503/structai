"""Document Exporter routes."""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from bson import ObjectId
from app.core.database import get_db
from app.core.security import get_current_user
from app.services.exporter.pdf_exporter import generate_pdf
from app.services.exporter.md_exporter import generate_markdown

router = APIRouter(prefix="/export", tags=["export"])


async def _get_complete_design(design_id: str, user_id: str, db):
    design = await db.designs.find_one({
        "_id": ObjectId(design_id),
        "user_id": user_id,
    })
    if not design:
        raise HTTPException(status_code=404, detail="Design not found")
    if not design.get("architecture"):
        raise HTTPException(status_code=400, detail="Design not yet complete")
    return design


@router.get("/{design_id}/pdf")
async def export_pdf(
    design_id: str,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    design = await _get_complete_design(design_id, str(current_user["_id"]), db)
    pdf_bytes = generate_pdf(
        design["problem_statement"],
        design["architecture"],
        design.get("explanations", {}),
    )
    filename = f"structai-design-{design_id[:8]}.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/{design_id}/markdown")
async def export_markdown(
    design_id: str,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    design = await _get_complete_design(design_id, str(current_user["_id"]), db)
    md_content = generate_markdown(
        design["problem_statement"],
        design["architecture"],
        design.get("explanations", {}),
    )
    filename = f"structai-design-{design_id[:8]}.md"
    return Response(
        content=md_content.encode("utf-8"),
        media_type="text/markdown",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
