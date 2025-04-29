from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.adventurerModel import Adventurer

class Stats(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    adventurer_id: Optional[int] = Field(foreign_key="adventurer.id", unique=True)

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    adventurer: Optional["Adventurer"] = Relationship(back_populates="stats")
