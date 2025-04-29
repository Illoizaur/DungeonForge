from fastapi import HTTPException
from sqlmodel import Session, select
from app.db.database import engine
from app.models.itemModel import Item, Adventurer_Items
from app.schemas.itemScheme import (
    ItemCreate, ItemUpdate, ItemResponse,
    AdventurerItemCreate, AdventurerItemUpdate, AdventurerItemResponse
)

# --- Item Service Functions ---

def create_item(item_data: ItemCreate) -> ItemResponse:
    with Session(engine) as session:
        item = Item(**item_data.dict())
        session.add(item)
        session.commit()
        session.refresh(item)
        return ItemResponse.from_orm(item)

def get_item(item_id: int) -> ItemResponse:
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemResponse.from_orm(item)

def get_items() -> list[ItemResponse]:
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return [ItemResponse.from_orm(item) for item in items]

def update_item(item_data: ItemUpdate) -> ItemResponse:
    with Session(engine) as session:
        item = session.get(Item, item_data.id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

    item_data_dict = item_data.dict(exclude_unset=True)
    for key, value in item_data_dict.items():
        setattr(item, key, value)

    session.add(item)
    session.commit()
    session.refresh(item)
    return ItemResponse.from_orm(item)

def delete_item(item_id: int) -> None:
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()

# --- Adventurer Item Service Functions ---

def assign_item_to_adventurer(data: AdventurerItemCreate) -> AdventurerItemResponse:
    with Session(engine) as session:
        link = Adventurer_Items(**data.dict())
        session.add(link)
        session.commit()
        session.refresh(link)
        return AdventurerItemResponse.from_orm(link)

def update_adventurer_item(data: AdventurerItemUpdate) -> AdventurerItemResponse:
    with Session(engine) as session:
        link = session.get(Adventurer_Items, data.id)
        if not link:
            raise HTTPException(status_code=404, detail="Link not found")

        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(link, key, value)

        session.add(link)
        session.commit()
        session.refresh(link)
        return AdventurerItemResponse.from_orm(link)

def delete_adventurer_item(link_id: int) -> None:
    with Session(engine) as session:
        link = session.get(Adventurer_Items, link_id)
        if not link:
            raise HTTPException(status_code=404, detail="Link not found")
        session.delete(link)
        session.commit()
