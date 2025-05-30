from typing import Optional
from sqlmodel import SQLModel

#from app.schemas.statsScheme import StatsResponse

class AdventurerCreate(SQLModel):
    room_id: Optional[int] = None
    name: str
    avatar_url: str
    exp: int
    level: int
    sex: str
    age: int
    race: str
    adv_class: str
    alignment: str

class AdventurerUpdate(SQLModel):
    name: Optional[str] = None
    avatar_url: Optional[str] = None
    exp: Optional[int] = None
    level: Optional[int] = None
    sex: Optional[str] = None
    age: Optional[int] = None
    race: Optional[str] = None
    adv_class: Optional[str] = None
    alignment: Optional[str] = None
    room_id: Optional[int] = None  # на випадок, якщо треба перенести в іншу кімнату

class AdventurerResponse(SQLModel):
    id: int
    user_id: int
    room_id: Optional[int] = None
    name: str
    avatar_url: str
    exp: int
    level: int
    sex: str
    age: int
    race: str
    adv_class: str
    alignment: str

    class AdventurerResponseConfig:
        from_attributes = True

#Ідея на майбутнє, яка буде реалізована пізніше... напевно, але можливо і ні
#class AdventurerResponseWithStats(SQLModel):
#    id: int
#    user_id: int
#    room_id: Optional[int] = None
#    name: str
#    avatar_url: str
#    exp: int
#    level: int
#    sex: str
#    age: int
#    race: str
#    adv_class: str
#    alignment: str
#    stats: Optional[StatsResponse]

#    class AdventurerResponseWithStatsConfig:
#        from_attributes = True
