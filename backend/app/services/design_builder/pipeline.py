"""LangGraph state machine for end-to-end design generation."""
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from app.services.design_builder.extractor import extract_requirements, generate_clarifying_questions
from app.services.design_builder.generator import generate_architecture
from app.services.design_builder.rag import retrieve_similar_patterns


class DesignState(TypedDict):
    problem_statement: str
    requirements: dict
    clarifying_questions: list[str]
    clarifications: Optional[dict]
    rag_context: str
    architecture: Optional[dict]
    error: Optional[str]


# ── graph nodes ──────────────────────────────────────────────────────────────

async def node_extract(state: DesignState) -> dict:
    try:
        reqs = await extract_requirements(state["problem_statement"])
        return {"requirements": reqs}
    except Exception as e:
        return {"error": str(e)}


async def node_clarify(state: DesignState) -> dict:
    questions = await generate_clarifying_questions(state["requirements"])
    return {"clarifying_questions": questions}


async def node_retrieve(state: DesignState) -> dict:
    context = await retrieve_similar_patterns(state["problem_statement"])
    return {"rag_context": context}


async def node_generate(state: DesignState) -> dict:
    try:
        arch = await generate_architecture(
            state["requirements"],
            state.get("clarifications") or {},
            state["rag_context"],
        )
        return {"architecture": arch}
    except Exception as e:
        return {"error": str(e)}


# ── routing ───────────────────────────────────────────────────────────────────

def should_clarify(state: DesignState) -> str:
    """Route to clarification step only when ambiguities exist and no clarifications provided."""
    has_ambiguities = bool(state["requirements"].get("ambiguities"))
    already_clarified = bool(state.get("clarifications"))
    return "clarify" if has_ambiguities and not already_clarified else "retrieve"


# ── graph assembly ────────────────────────────────────────────────────────────

def build_pipeline():
    graph = StateGraph(DesignState)

    graph.add_node("extract", node_extract)
    graph.add_node("clarify", node_clarify)
    graph.add_node("retrieve", node_retrieve)
    graph.add_node("generate", node_generate)

    graph.set_entry_point("extract")
    graph.add_conditional_edges("extract", should_clarify, {
        "clarify": "clarify",
        "retrieve": "retrieve",
    })
    graph.add_edge("clarify", END)   # returns questions to caller; generation happens after answers
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()


pipeline = build_pipeline()


async def run_initial(problem_statement: str) -> DesignState:
    """First pass: extract requirements and return clarifying questions if needed."""
    state = await pipeline.ainvoke({
        "problem_statement": problem_statement,
        "requirements": {},
        "clarifying_questions": [],
        "clarifications": None,
        "rag_context": "",
        "architecture": None,
        "error": None,
    })
    return state


async def run_with_clarifications(problem_statement: str, requirements: dict, clarifications: dict) -> DesignState:
    """Second pass: run retrieve → generate with clarifications filled in."""
    context = await retrieve_similar_patterns(problem_statement)
    arch = await generate_architecture(requirements, clarifications, context)
    return {
        "problem_statement": problem_statement,
        "requirements": requirements,
        "clarifying_questions": [],
        "clarifications": clarifications,
        "rag_context": context,
        "architecture": arch,
        "error": None,
    }
