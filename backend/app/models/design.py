from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime


class NodePosition(BaseModel):
    x: float
    y: float


class DiagramNode(BaseModel):
    id: str
    type: str
    label: str
    description: str
    tech: str


class DiagramEdge(BaseModel):
    id: str
    source: str
    target: str
    label: str = ""
    animated: bool = False


class Architecture(BaseModel):
    nodes: List[DiagramNode]
    edges: List[DiagramEdge]
    tech_stack: List[str]
    summary: str


class ComponentExplanation(BaseModel):
    component_id: str
    what: str
    why: str
    alternatives: List[str]
    trade_offs: str


class DesignCreate(BaseModel):
    problem_statement: str
    clarifications: Optional[Dict[str, str]] = None


class DesignInDB(BaseModel):
    user_id: str
    problem_statement: str
    requirements: List[str] = []
    architecture: Optional[Dict[str, Any]] = None
    explanations: Dict[str, Any] = {}
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class DesignResponse(BaseModel):
    id: str
    problem_statement: str
    architecture: Optional[Dict[str, Any]]
    explanations: Dict[str, Any]
    status: str
    created_at: datetime


class ClarifyingQuestionsResponse(BaseModel):
    design_id: str
    questions: List[str]


class ClarificationSubmit(BaseModel):
    clarifications: Dict[str, str]
