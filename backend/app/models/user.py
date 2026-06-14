from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    image: Optional[str] = None


class UserInDB(BaseModel):
    name: str
    email: EmailStr
    image: Optional[str] = None
    role: Literal["student", "admin"] = "student"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    design_count: int = 0
    quiz_count: int = 0


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    image: Optional[str] = None
    role: str
    created_at: datetime
    design_count: int
    quiz_count: int
