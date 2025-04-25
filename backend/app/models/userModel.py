from sqlmodel import SQLModel, Field, Relationship
from typing import List

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    is_admin: bool = False
    adventurers: List["Adventurer"] = Relationship(back_populates="user")
