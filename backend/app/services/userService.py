from fastapi import HTTPException
from typing import List
from sqlmodel import Session, select

from app.models.userModel import User
from app.schemas.userScheme import UserCreate, UserUpdate
from app.db.database import engine
from app.services.authService import get_password_hash

def create_user(user: UserCreate) -> User:
    with Session(engine) as session:
        statement = select(User).where(User.username == user.username)
        existing_user = session.exec(statement).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")

        hashed = get_password_hash(user.password)
        new_user = User(username=user.username, password=hashed, email=user.email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

def get_users() -> List[User]:
    with Session(engine) as session:
        users = session.query(User).all()
        return users

def get_user(user_id: int) -> User:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

def update_user(user_id: int, user_update: UserUpdate) -> User:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if user_update.username is not None:
            user.username = user_update.username
        if user_update.password is not None:
            user.password = user_update.password
        if user_update.email is not None:
            user.email = user_update.email

        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def delete_user(user_id: int) -> None:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        session.delete(user)
        session.commit()
