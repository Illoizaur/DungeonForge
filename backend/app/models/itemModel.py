from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.adventurerModel import Adventurer

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(default=0.0)
    effects: Optional[str] = Field(default=None, max_length=500)

    #category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    #category: Optional["Category"] = Relationship(back_populates="items")
    adventurers: List["Adventurer_Items"] = Relationship(back_populates="item")

# На майбутнє
#class Category(SQLModel, table=True):
#    id: Optional[int] = Field(default=None, primary_key=True)
#    name: str = Field(max_length=255)
#    description: Optional[str] = Field(default=None, max_length=250)
#    items: List[Item] = Relationship(back_populates="category")

class Adventurer_Items(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    adventurer_id: Optional[int] = Field(default=None, foreign_key="adventurer.id")
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    quantity: int = Field(default=0)

    item: Optional[Item] = Relationship(back_populates="adventurers")
    adventurer: Optional["Adventurer"] = Relationship(back_populates="items")
