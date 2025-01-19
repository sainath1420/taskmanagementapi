import uuid as uuid_pkg
from typing import Optional

from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    uuid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True)
    id: int = Field(nullable=False, description="unique id of task")
    title: str = Field(nullable=False, description="title of task", max_length=100)
    description: Optional[str] = Field(default=None,description="description of task")
    status: str = Field(description="status of task")