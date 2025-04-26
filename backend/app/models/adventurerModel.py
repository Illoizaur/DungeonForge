from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.statsModel import Stats
    from app.models.userModel import User

class Adventurer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Foreign Keys (room доробиться пізніше)
    user_id: Optional[int] = Field(foreign_key="users.id")
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
    stats: Optional["Stats"] = Relationship(back_populates="adventurer", sa_relationship_kwargs={"uselist": False})
