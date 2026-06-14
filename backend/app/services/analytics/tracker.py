"""Aggregate analytics queries for user dashboard and admin panel."""
from datetime import datetime, timedelta
from app.core.database import get_db


async def get_user_stats(user_id: str) -> dict:
    db = get_db()
    designs = await db.designs.count_documents({"user_id": user_id})
    quizzes = await db.quiz_attempts.count_documents({"user_id": user_id})

    # Recent designs (last 5)
    cursor = db.designs.find(
        {"user_id": user_id},
        {"problem_statement": 1, "status": 1, "created_at": 1},
    ).sort("created_at", -1).limit(5)
    recent_designs = [
        {
            "id": str(d["_id"]),
            "problem_statement": d["problem_statement"],
            "status": d["status"],
            "created_at": d["created_at"].isoformat(),
        }
        async for d in cursor
    ]

    # Quiz scores
    cursor = db.quiz_attempts.find(
        {"user_id": user_id},
        {"topic": 1, "score": 1, "completed_at": 1},
    ).sort("completed_at", -1).limit(10)
    quiz_history = [
        {
            "topic": q["topic"],
            "score": q["score"],
            "completed_at": q["completed_at"].isoformat(),
        }
        async for q in cursor
    ]

    avg_score = (
        sum(q["score"] for q in quiz_history) / len(quiz_history)
        if quiz_history else 0
    )

    return {
        "total_designs": designs,
        "total_quizzes": quizzes,
        "avg_quiz_score": round(avg_score, 1),
        "recent_designs": recent_designs,
        "quiz_history": quiz_history,
    }


async def get_admin_stats() -> dict:
    db = get_db()
    total_users = await db.users.count_documents({})
    total_designs = await db.designs.count_documents({})
    total_quizzes = await db.quiz_attempts.count_documents({})

    # Active users last 7 days
    week_ago = datetime.utcnow() - timedelta(days=7)
    active_users = await db.designs.distinct("user_id", {"created_at": {"$gte": week_ago}})

    # Designs per day (last 7 days)
    pipeline = [
        {"$match": {"created_at": {"$gte": week_ago}}},
        {"$group": {
            "_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$created_at"}},
            "count": {"$sum": 1},
        }},
        {"$sort": {"_id": 1}},
    ]
    daily_designs = [
        {"date": d["_id"], "count": d["count"]}
        async for d in db.designs.aggregate(pipeline)
    ]

    return {
        "total_users": total_users,
        "total_designs": total_designs,
        "total_quiz_attempts": total_quizzes,
        "active_users_7d": len(active_users),
        "daily_designs_7d": daily_designs,
    }
