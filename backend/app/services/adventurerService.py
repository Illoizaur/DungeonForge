from fastapi import HTTPException
from typing import List
from sqlmodel import Session, select

from app.models.adventurerModel import Adventurer
from app.schemas.adventurerScheme import AdventurerCreate, AdventurerUpdate
#from app.schemas.adventurerScheme import AdventurerResponseWithStats
#from app.schemas.statsScheme import StatsResponse
from app.db.database import engine
from app.models.userModel import User

def create_adventurer(adventurer_data: AdventurerCreate, current_user: User) -> Adventurer:
    if current_user.id is None:
            raise HTTPException(status_code=400, detail="User ID is required")

    with Session(engine) as session:
        adventurer = Adventurer(**adventurer_data.dict(), user_id=current_user.id)
        session.add(adventurer)
        session.commit()
        session.refresh(adventurer)
        return adventurer


def get_adventurers(current_user: User) -> List[Adventurer]:
    with Session(engine) as session:
        statement = select(Adventurer).where(Adventurer.user_id == current_user.id)
        return list(session.exec(statement))


def get_adventurer(adventurer_id: int, current_user: User) -> Adventurer:
    with Session(engine) as session:
        statement = (
            select(Adventurer)
            .where(Adventurer.id == adventurer_id)
            .where(Adventurer.user_id == current_user.id)
        )
        adventurer = session.exec(statement).first()

        if adventurer is None:
            raise HTTPException(status_code=404, detail="Adventurer not found")
        if adventurer.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="You can only access your own adventurers")
        return adventurer

#Ідея на майбутнє, яка буде реалізована пізніше... напевно, але можливо і ні
#def get_adventurer_with_stats(adventurer_id: int, current_user: User) -> AdventurerResponseWithStats:
#    with Session(engine) as session:
#       statement = select(Adventurer).where(Adventurer.id == adventurer_id)
#        adventurer = session.exec(statement).first()
#
#        if adventurer is None:
#            raise HTTPException(status_code=404, detail="Adventurer not found")
#        if adventurer.user_id != current_user.id:
#            raise HTTPException(status_code=403, detail="You can only access your own adventurers")

#        return AdventurerResponseWithStats.from_orm(adventurer)

def update_adventurer(adventurer_id: int, update_data: AdventurerUpdate, current_user: User) -> Adventurer:
    with Session(engine) as session:
        statement = select(Adventurer).where(Adventurer.id == adventurer_id)
        adventurer = session.exec(statement).first()

        if adventurer is None:
            raise HTTPException(status_code=404, detail="Adventurer not found")
        if adventurer.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="You can only update your own adventurers")

        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(adventurer, field, value)

        session.add(adventurer)
        session.commit()
        session.refresh(adventurer)
        return adventurer


def delete_adventurer(adventurer_id: int, current_user: User) -> None:
    with Session(engine) as session:
        statement = select(Adventurer).where(Adventurer.id == adventurer_id)
        adventurer = session.exec(statement).first()

        if adventurer is None:
            raise HTTPException(status_code=404, detail="Adventurer not found")
        if adventurer.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="You can only delete your own adventurers")

        session.delete(adventurer)
        session.commit()
