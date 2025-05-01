from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.adventurerModel import Adventurer

class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    description: Optional[str] = Field(default=None, max_length=500)
    prime_stat: Optional[str] = Field(default=None, max_length=255)

    adventurers: List["Adventurer_Skill"] = Relationship(back_populates="skill")

class Adventurer_Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    adventurer_id: Optional[int] = Field(default=None, foreign_key="adventurer.id")
    skill_id: Optional[int] = Field(default=None, foreign_key="skill.id")

    skill: Optional[Skill] = Relationship(back_populates="adventurers")
    adventurer: Optional["Adventurer"] = Relationship(back_populates="skills")
