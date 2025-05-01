from sqlmodel import SQLModel
from typing import Optional

class SkillCreate(SQLModel):
    name: str
    description: Optional[str]
    prime_stat: Optional[str]

class SkillUpdate(SQLModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    prime_stat: Optional[str]

class SkillResponse(SQLModel):
    id: int
    name: str
    description: Optional[str]
    prime_stat: Optional[str]

class AdventurerSkillCreate(SQLModel):
    adventurer_id: int
    skill_id: int
    level: int

class AdventurerSkillUpdate(SQLModel):
    id: int
    adventurer_id: Optional[int]
    skill_id: Optional[int]

class AdventurerSkillResponse(SQLModel):
    id: int
    adventurer_id: int
    skill_id: int
