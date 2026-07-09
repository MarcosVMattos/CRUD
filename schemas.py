from typing import Optional

from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None

class TaskId(TaskCreate):
    id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = None
