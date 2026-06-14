from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class QuizOption(BaseModel):
    id: str
    text: str


class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[QuizOption]
    correct_option_id: str
    explanation: str


class QuizGenerateRequest(BaseModel):
    topic: str
    difficulty: str = "intermediate"
    num_questions: int = 5


class QuizGenerateResponse(BaseModel):
    quiz_id: str
    topic: str
    questions: List[QuizQuestion]


class QuizAnswer(BaseModel):
    question_id: str
    selected_option_id: str


class QuizSubmitRequest(BaseModel):
    quiz_id: str
    topic: str
    answers: List[QuizAnswer]


class QuizResult(BaseModel):
    question_id: str
    correct: bool
    correct_option_id: str
    explanation: str


class QuizSubmitResponse(BaseModel):
    score: float
    results: List[QuizResult]
    passed: bool


class QuizAttemptInDB(BaseModel):
    user_id: str
    quiz_id: str
    topic: str
    score: float
    passed: bool
    completed_at: datetime = Field(default_factory=datetime.utcnow)
