from sqlmodel import SQLModel
from typing import Optional

class ItemCreate(SQLModel):
    name: str
    description: Optional[str]
    price: float
    effects: Optional[str]

class ItemUpdate(SQLModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    effects: Optional[str]

class ItemResponse(SQLModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    effects: Optional[str]

class AdventurerItemCreate(SQLModel):
    adventurer_id: int
    item_id: int
    quantity: int

class AdventurerItemUpdate(SQLModel):
    id: int
    adventurer_id: Optional[int]
    item_id: Optional[int]
    quantity: Optional[int]

class AdventurerItemResponse(SQLModel):
    id: int
    adventurer_id: int
    item_id: int
    quantity: int
