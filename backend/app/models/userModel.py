from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models.adventurerModel import Adventurer

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
    is_admin: bool = False
    adventurers: List["Adventurer"] = Relationship(back_populates="user")
