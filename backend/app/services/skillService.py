from fastapi import HTTPException
from sqlmodel import Session, select
from app.db.database import engine
from app.models.skillModel import Skill, Adventurer_Skill
from app.schemas.skillScheme import (
    SkillCreate, SkillUpdate, SkillResponse,
    AdventurerSkillCreate, AdventurerSkillUpdate, AdventurerSkillResponse
)

# --- Skill Service Functions ---

def create_skill(skill_data: SkillCreate) -> SkillResponse:
    with Session(engine) as session:
        skill = Skill(**skill_data.dict())
        session.add(skill)
        session.commit()
        session.refresh(skill)
        return SkillResponse.from_orm(skill)

def get_skill(skill_id: int) -> SkillResponse:
    with Session(engine) as session:
        skill = session.get(Skill, skill_id)
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")
        return SkillResponse.from_orm(skill)

def get_skills() -> list[SkillResponse]:
    with Session(engine) as session:
        skills = session.exec(select(Skill)).all()
        return [SkillResponse.from_orm(skill) for skill in skills]

def update_skill(skill_data: SkillUpdate) -> SkillResponse:
    with Session(engine) as session:
        skill = session.get(Skill, skill_data.id)
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")

    skill_data_dict = skill_data.dict(exclude_unset=True)
    for key, value in skill_data_dict.items():
        setattr(skill, key, value)

    session.add(skill)
    session.commit()
    session.refresh(skill)
    return SkillResponse.from_orm(skill)

def delete_skill(skill_id: int) -> None:
    with Session(engine) as session:
        skill = session.get(Skill, skill_id)
        if not skill:
            raise HTTPException(status_code=404, detail="Skill not found")
        session.delete(skill)
        session.commit()

# --- Adventurer Item Service Functions ---

def assign_skill_to_adventurer(data: AdventurerSkillCreate) -> AdventurerSkillResponse:
    with Session(engine) as session:
        link = Adventurer_Skill(**data.dict())
        session.add(link)
        session.commit()
        session.refresh(link)
        return AdventurerSkillResponse.from_orm(link)

def update_adventurer_skill(data: AdventurerSkillUpdate) -> AdventurerSkillResponse:
    with Session(engine) as session:
        link = session.get(Adventurer_Skill, data.id)
        if not link:
            raise HTTPException(status_code=404, detail="Link not found")

        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(link, key, value)

        session.add(link)
        session.commit()
        session.refresh(link)
        return AdventurerSkillResponse.from_orm(link)

def delete_adventurer_skill(link_id: int) -> None:
    with Session(engine) as session:
        link = session.get(Adventurer_Skill, link_id)
        if not link:
            raise HTTPException(status_code=404, detail="Link not found")
        session.delete(link)
        session.commit()
