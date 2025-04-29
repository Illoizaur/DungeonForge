from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

#from app.schemas.adventurerScheme import AdventurerResponseWithStats
from app.models.userModel import User
import app.services.adventurerService as services
from app.services.authService import get_current_user
from app.schemas.adventurerScheme import AdventurerCreate, AdventurerUpdate, AdventurerResponse

router = APIRouter(prefix="/adv", tags=["adventurers"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/", response_model=AdventurerResponse)
def create_adventurer(adventurer_data: AdventurerCreate, current_user: User = Depends(get_current_user)):
    return services.create_adventurer(adventurer_data, current_user)

@router.get("/", response_model=List[AdventurerResponse])
def get_adventurers(current_user: User = Depends(get_current_user)):
    return services.get_adventurers(current_user)

@router.get("/{adventurer_id}", response_model=AdventurerResponse)
def get_adventurer(adventurer_id: int, current_user: User = Depends(get_current_user)):
    return services.get_adventurer(adventurer_id, current_user)

@router.put("/{adventurer_id}", response_model=AdventurerResponse)
def update_adventurer(adventurer_id: int, update_data: AdventurerUpdate, current_user: User = Depends(get_current_user)):
    return services.update_adventurer(adventurer_id, update_data, current_user)

@router.delete("/{adventurer_id}", response_model=dict)
def delete_adventurer(adventurer_id: int, current_user: User = Depends(get_current_user)):
    services.delete_adventurer(adventurer_id, current_user)
    return {"detail": "Adventurer deleted successfully"}

#Ідея на майбутнє, яка буде реалізована пізніше... напевно, але можливо і ні
#@router.get("/{adventurer_id}/stats", response_model=AdventurerResponseWithStats)
#def get_adventurer_with_stats(adventurer_id: int, current_user: User = Depends(get_current_user)):
#    return services.get_adventurer_with_stats(adventurer_id, current_user)
