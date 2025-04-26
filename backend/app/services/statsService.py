from fastapi import HTTPException
from sqlmodel import Session, select

from app.db.database import engine
from app.models.statsModel import Stats
from app.models.adventurerModel import Adventurer
from app.schemas.statsScheme import StatsCreate, StatsUpdate

def create_stats(stats_data: StatsCreate, adventurer_id: int) -> Stats:
    with Session(engine) as session:
        adventurer = session.get(Adventurer, adventurer_id)
        if adventurer is None:
            raise HTTPException(status_code=404, detail="Adventurer not found")

        stats = Stats(**stats_data.dict(), adventurer_id=adventurer_id)
        session.add(stats)
        session.commit()
        session.refresh(stats)
        return stats

def get_stats(adventurer_id: int) -> Stats:
    with Session(engine) as session:
        statement = select(Stats).where(Stats.adventurer_id == adventurer_id)
        stats = session.exec(statement).first()

        if stats is None:
            raise HTTPException(status_code=404, detail="Stats not found for this adventurer")
        return stats

def update_stats(adventurer_id: int, update_data: StatsUpdate) -> Stats:
    with Session(engine) as session:
        statement = select(Stats).where(Stats.adventurer_id == adventurer_id)
        stats = session.exec(statement).first()

        if stats is None:
            raise HTTPException(status_code=404, detail="Stats not found for this adventurer")

        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(stats, field, value)

        session.add(stats)
        session.commit()
        session.refresh(stats)
        return stats

def delete_stats(adventurer_id: int) -> None:
    with Session(engine) as session:
        statement = select(Stats).where(Stats.adventurer_id == adventurer_id)
        stats = session.exec(statement).first()

        if stats is None:
            raise HTTPException(status_code=404, detail="Stats not found for this adventurer")

        session.delete(stats)
        session.commit()
