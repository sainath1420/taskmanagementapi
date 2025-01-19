from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field

class Status(str, Enum):
    pending = "Pending"
    in_progress = "In Progress"
    completed = "Completed"

class TaskRequest(BaseModel):
    id: int = Field(description="id of task")
    title: str = Field(description="title of task", max_length=100)
    description: Optional[str] = Field(default=None, description="description of task")
    status: Status = Field(description="status of task")

class TaskUpdate(BaseModel):
    title: str = Field(description="title of task", max_length=100)
    description: Optional[str] = Field(default=None, description="description of task")
    status: Status = Field(description="status of task")

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: Status

    class Config:
        from_attributes = True

class TasksResponse(BaseModel):
    tasks: List[Task]

class TaskResponse(BaseModel):
    details: str