"""Per-component click-to-explain using GPT-4o."""
import json
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings

_llm = ChatOpenAI(model="gpt-4o", temperature=0.3, openai_api_key=settings.OPENAI_API_KEY)

EXPLAIN_SYSTEM = """You are a senior system design mentor explaining architecture decisions to a student or developer.
Given an architecture component, explain it clearly and concisely.

Return ONLY valid JSON (no markdown fences):
{
  "what": "<1–2 sentence description of what this component is>",
  "why": "<2–3 sentences on why it was chosen for this specific system>",
  "alternatives": ["<alternative tech or pattern>", "<another>"],
  "trade_offs": "<2–3 sentences on key trade-offs: performance, cost, complexity>",
  "learn_more": "<one key concept the user should study to go deeper>"
}"""


async def explain_component(
    component_id: str,
    component_label: str,
    component_type: str,
    component_tech: str,
    architecture_summary: str,
) -> dict:
    prompt = f"""ARCHITECTURE CONTEXT:
{architecture_summary}

COMPONENT TO EXPLAIN:
- ID: {component_id}
- Name: {component_label}
- Type: {component_type}
- Technology: {component_tech}

Explain this component in the context of the overall architecture."""

    messages = [
        SystemMessage(content=EXPLAIN_SYSTEM),
        HumanMessage(content=prompt),
    ]
    response = await _llm.ainvoke(messages)
    return json.loads(response.content)
