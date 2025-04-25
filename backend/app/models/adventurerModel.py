from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Adventurer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Foreign Keys
    user_id: int = Field(foreign_key="users.id")
    #room_id: Optional[int] = Field(default=None, foreign_key="rooms.id")

    name: str
    avatar_url: str
    exp: int
    level: int
    sex: str
    age: int
    race: str
    adv_class: str
    alignment: str

    # Relationships (реалізую пізніше)
    user: Optional["User"] = Relationship(back_populates="adventurers")
    #room: Optional["Room"] = Relationship(back_populates="adventurers")
