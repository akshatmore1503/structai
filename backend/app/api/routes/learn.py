"""Learn Mode routes — topics + dynamic quiz generation."""
import uuid
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.quiz import QuizGenerateRequest, QuizSubmitRequest
from app.services.learn_mode.topics import TOPICS, get_topic
from app.services.learn_mode.quiz_generator import generate_quiz, grade_quiz

router = APIRouter(prefix="/learn", tags=["learn"])

# In-memory quiz cache (quiz_id → questions list)
# In production this would be Redis, but for local dev this is fine
_quiz_cache: dict[str, list] = {}


@router.get("/topics")
async def list_topics():
    return TOPICS


@router.get("/topics/{topic_id}")
async def get_topic_detail(topic_id: str):
    topic = get_topic(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic


@router.post("/quiz/generate")
async def generate(
    payload: QuizGenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    result = await generate_quiz(payload.topic, payload.difficulty, payload.num_questions)
    _quiz_cache[result["quiz_id"]] = result["questions"]
    return result


@router.post("/quiz/submit")
async def submit_quiz(
    payload: QuizSubmitRequest,
    current_user: dict = Depends(get_current_user),
    db=Depends(get_db),
):
    questions = _quiz_cache.get(payload.quiz_id)
    if not questions:
        raise HTTPException(status_code=404, detail="Quiz session expired or not found")

    graded = grade_quiz(questions, [a.model_dump() for a in payload.answers])

    # Persist attempt
    attempt = {
        "user_id": str(current_user["_id"]),
        "quiz_id": payload.quiz_id,
        "topic": payload.topic,
        "score": graded["score"],
        "passed": graded["passed"],
        "completed_at": __import__("datetime").datetime.utcnow(),
    }
    await db.quiz_attempts.insert_one(attempt)
    await db.users.update_one(
        {"_id": current_user["_id"]},
        {"$inc": {"quiz_count": 1}},
    )

    # Clean up cache
    _quiz_cache.pop(payload.quiz_id, None)

    return graded
