from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str
    completed: bool = False


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None