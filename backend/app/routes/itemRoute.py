from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.services.authService import get_current_user
from app.models.userModel import User
from app.schemas.itemScheme import (
    ItemCreate, ItemUpdate, ItemResponse,
    AdventurerItemCreate, AdventurerItemUpdate, AdventurerItemResponse
)
import app.services.itemService as services

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

router = APIRouter(prefix="/items", tags=["Items"])

# --- Item CRUD ---

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, current_user: User = Depends(get_current_user)):
    return services.create_item(item)

@router.get("/", response_model=list[ItemResponse])
def get_items(current_user: User = Depends(get_current_user)):
    return services.get_items()

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, current_user: User = Depends(get_current_user)):
    return services.get_item(item_id)

@router.put("/", response_model=ItemResponse)
def update_item(item: ItemUpdate, current_user: User = Depends(get_current_user)):
    return services.update_item(item)

@router.delete("/{item_id}")
def delete_item(item_id: int, current_user: User = Depends(get_current_user)):
    return services.delete_item(item_id)

# --- Adventurer_Items CRUD ---

@router.post("/belong", response_model=AdventurerItemResponse)
def assign_item_to_adventurer(data: AdventurerItemCreate, current_user: User = Depends(get_current_user)):
    return services.assign_item_to_adventurer(data)

@router.put("/belong", response_model=AdventurerItemResponse)
def update_adventurer_item(data: AdventurerItemUpdate, current_user: User = Depends(get_current_user)):
    return services.update_adventurer_item(data)

@router.delete("/belong/{link_id}")
def delete_adventurer_item(link_id: int, current_user: User = Depends(get_current_user)):
    return services.delete_adventurer_item(link_id)
