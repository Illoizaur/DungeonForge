from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.models.userModel import User
import app.services.statsService as services
from app.services.authService import get_current_user
from app.schemas.statsScheme import StatsCreate, StatsUpdate, StatsResponse

router = APIRouter(prefix="/stats", tags=["Stats"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/{adventurer_id}", response_model=StatsResponse)
def create_stats(adventurer_id: int, stats_data: StatsCreate, current_user: User = Depends(get_current_user)):
    return services.create_stats(stats_data, adventurer_id)

@router.get("/{adventurer_id}", response_model=StatsResponse)
def get_stats(adventurer_id: int, current_user: User = Depends(get_current_user)):
    return services.get_stats(adventurer_id)

@router.put("/{adventurer_id}", response_model=StatsResponse)
def update_stats(adventurer_id: int, update_data: StatsUpdate, current_user: User = Depends(get_current_user)):
    return services.update_stats(adventurer_id, update_data)

@router.delete("/{adventurer_id}", response_model=dict)
def delete_stats(adventurer_id: int, current_user: User = Depends(get_current_user)):
    services.delete_stats(adventurer_id)
    return {"detail": "Stats deleted successfully"}
