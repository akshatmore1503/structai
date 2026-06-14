"""Dynamic quiz generation via GPT-4o."""
import json
import uuid
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings

_llm = ChatOpenAI(model="gpt-4o", temperature=0.7, openai_api_key=settings.OPENAI_API_KEY)

QUIZ_SYSTEM = """You are a system design instructor creating quiz questions.
Generate a multiple-choice quiz on the given topic at the specified difficulty.

Return ONLY valid JSON (no markdown fences):
{
  "questions": [
    {
      "id": "<uuid>",
      "question": "<clear, specific question>",
      "options": [
        {"id": "a", "text": "<option text>"},
        {"id": "b", "text": "<option text>"},
        {"id": "c", "text": "<option text>"},
        {"id": "d", "text": "<option text>"}
      ],
      "correct_option_id": "<a|b|c|d>",
      "explanation": "<2–3 sentence explanation of why the correct answer is right>"
    }
  ]
}

Rules:
- Questions must be practical and scenario-based, not trivia
- Distractors must be plausible (common misconceptions, not obviously wrong)
- Explanations must be educational, not just restate the answer"""


async def generate_quiz(topic: str, difficulty: str, num_questions: int) -> dict:
    prompt = f"""Topic: {topic}
Difficulty: {difficulty}
Number of questions: {num_questions}

Generate the quiz now."""

    messages = [
        SystemMessage(content=QUIZ_SYSTEM),
        HumanMessage(content=prompt),
    ]
    response = await _llm.ainvoke(messages)
    data = json.loads(response.content)

    # Ensure each question has a UUID id
    for q in data["questions"]:
        if not q.get("id"):
            q["id"] = str(uuid.uuid4())

    return {
        "quiz_id": str(uuid.uuid4()),
        "topic": topic,
        "questions": data["questions"],
    }


def grade_quiz(questions: list[dict], answers: list[dict]) -> dict:
    """Grade a submitted quiz. Returns score and per-question results."""
    answer_map = {a["question_id"]: a["selected_option_id"] for a in answers}
    results = []
    correct_count = 0

    for q in questions:
        selected = answer_map.get(q["id"])
        is_correct = selected == q["correct_option_id"]
        if is_correct:
            correct_count += 1
        results.append({
            "question_id": q["id"],
            "correct": is_correct,
            "correct_option_id": q["correct_option_id"],
            "explanation": q["explanation"],
        })

    score = round((correct_count / len(questions)) * 100, 1) if questions else 0
    return {
        "score": score,
        "results": results,
        "passed": score >= 70,
    }
