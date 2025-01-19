import uuid as uuid_pkg
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str = Field(description="password of user")


