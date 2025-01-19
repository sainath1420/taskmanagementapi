from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(description="name of user", max_length=100)
    password: str = Field(description="password of user")

class UserResponse(BaseModel):
    details: str