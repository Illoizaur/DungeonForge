from typing import Optional
from sqlmodel import Field, SQLModel

class StatsCreate(SQLModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

class StatsUpdate(SQLModel):
    strength: Optional[int] = Field(default=None)
    dexterity: Optional[int] = Field(default=None)
    constitution: Optional[int] = Field(default=None)
    intelligence: Optional[int] = Field(default=None)
    wisdom: Optional[int] = Field(default=None)
    charisma: Optional[int] = Field(default=None)

class StatsResponse(SQLModel):
    id: int
    adventurer_id: int
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    class StatsResponseConfig:
        from_attributes = True
