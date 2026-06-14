"""Extract structured requirements from a free-text problem statement."""
import json
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings

_llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=settings.OPENAI_API_KEY)

EXTRACT_SYSTEM = """You are a senior system design architect.
Extract requirements from the user's problem statement and identify any ambiguities.

Return ONLY valid JSON matching this schema (no markdown fences):
{
  "functional_requirements": ["<string>", ...],
  "non_functional_requirements": ["<string>", ...],
  "scale_hints": {
    "users": "<estimate>",
    "reads_per_sec": "<estimate>",
    "writes_per_sec": "<estimate>",
    "data_size": "<estimate>"
  },
  "ambiguities": ["<unclear aspect>", ...]
}"""


async def extract_requirements(problem_statement: str) -> dict:
    messages = [
        SystemMessage(content=EXTRACT_SYSTEM),
        HumanMessage(content=problem_statement),
    ]
    response = await _llm.ainvoke(messages)
    return json.loads(response.content)


CLARIFY_SYSTEM = """You are a senior system design architect conducting a scoping session.
Given the extracted requirements and ambiguities, generate 2–4 concise clarifying questions
that would meaningfully improve the architecture design.

Return ONLY valid JSON (no markdown fences):
{"questions": ["<question>", ...]}"""


async def generate_clarifying_questions(requirements: dict) -> list[str]:
    if not requirements.get("ambiguities"):
        return []
    payload = json.dumps(requirements)
    messages = [
        SystemMessage(content=CLARIFY_SYSTEM),
        HumanMessage(content=payload),
    ]
    response = await _llm.ainvoke(messages)
    data = json.loads(response.content)
    return data.get("questions", [])
