from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.services.authService import get_current_user
from app.models.userModel import User
from app.schemas.skillScheme import (
    SkillCreate, SkillUpdate, SkillResponse,
    AdventurerSkillCreate, AdventurerSkillUpdate, AdventurerSkillResponse
)
import app.services.skillService as services

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

router = APIRouter(prefix="/skills", tags=["Skills"])

# --- Skill CRUD ---

@router.post("/", response_model=SkillResponse)
def create_skill(skill: SkillCreate, current_user: User = Depends(get_current_user)):
    return services.create_skill(skill)

@router.get("/", response_model=list[SkillResponse])
def get_skills(current_user: User = Depends(get_current_user)):
    return services.get_skills()

@router.get("/{skill_id}", response_model=SkillResponse)
def get_skill(skill_id: int, current_user: User = Depends(get_current_user)):
    return services.get_skill(skill_id)

@router.put("/", response_model=SkillResponse)
def update_skill(skill: SkillUpdate, current_user: User = Depends(get_current_user)):
    return services.update_skill(skill)

@router.delete("/{skill_id}")
def delete_skill(skill_id: int, current_user: User = Depends(get_current_user)):
    return services.delete_skill(skill_id)

# --- Adventurer_Skills CRUD ---

@router.post("/belong", response_model=AdventurerSkillResponse)
def assign_skill_to_adventurer(data: AdventurerSkillCreate, current_user: User = Depends(get_current_user)):
    return services.assign_skill_to_adventurer(data)

@router.put("/belong", response_model=AdventurerSkillResponse)
def update_adventurer_skill(data: AdventurerSkillUpdate, current_user: User = Depends(get_current_user)):
    return services.update_adventurer_skill(data)

@router.delete("/belong/{link_id}")
def delete_adventurer_skill(link_id: int, current_user: User = Depends(get_current_user)):
    return services.delete_adventurer_skill(link_id)
