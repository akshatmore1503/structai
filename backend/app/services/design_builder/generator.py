"""Generate the architecture JSON using GPT-4o + RAG context."""
import json
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from app.core.config import settings

_llm = ChatOpenAI(model="gpt-4o", temperature=0.2, openai_api_key=settings.OPENAI_API_KEY)

GENERATE_SYSTEM = """You are a world-class system design architect.
Design a complete, production-grade system architecture based on the requirements and similar patterns below.

Return ONLY valid JSON (no markdown fences) matching this exact schema:
{
  "nodes": [
    {
      "id": "<kebab-case unique id>",
      "type": "<one of: client|api_gateway|load_balancer|web_server|database|nosql_database|cache|message_queue|cdn|object_storage|auth_service|monitoring|ml_service>",
      "label": "<display name>",
      "description": "<one-line description>",
      "tech": "<recommended technology, e.g. Redis, PostgreSQL, Nginx>"
    }
  ],
  "edges": [
    {
      "id": "<unique id>",
      "source": "<node id>",
      "target": "<node id>",
      "label": "<protocol or relationship, e.g. HTTPS, TCP, async>",
      "animated": <true for real-time or async flows, false otherwise>
    }
  ],
  "tech_stack": ["<technology>", ...],
  "summary": "<2–3 sentence architecture overview>"
}

Rules:
- Include all components needed for a production system (auth, monitoring, caching, etc.)
- Every edge must reference valid node ids
- Prefer battle-tested technologies unless the requirements suggest otherwise
- Include at least 6 nodes for any non-trivial system"""


async def generate_architecture(
    requirements: dict,
    clarifications: dict,
    rag_context: str,
) -> dict:
    prompt = f"""REQUIREMENTS:
{json.dumps(requirements, indent=2)}

CLARIFICATIONS:
{json.dumps(clarifications or {}, indent=2)}

SIMILAR ARCHITECTURE PATTERNS FOR REFERENCE:
{rag_context}

Design the architecture now."""

    messages = [
        SystemMessage(content=GENERATE_SYSTEM),
        HumanMessage(content=prompt),
    ]
    response = await _llm.ainvoke(messages)
    return json.loads(response.content)
