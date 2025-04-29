from sqlmodel import SQLModel, Field
from typing import Optional

class UserCreate(SQLModel):
    username: str
    password: str
    email: str

class UserResponse(SQLModel):
    id: int
    username: str
    email: str

    class UserResponseConfig:
        from_attributes = True

class UserUpdate(SQLModel):
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
