from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from datetime import timedelta

from app.schemas.userScheme import UserCreate, UserResponse, UserUpdate
from app.schemas.tokenScheme import Token
from app.models.userModel import User
import app.services.userService as services
from app.services.authService import (
    authenticate_user,
    create_access_token,
    get_current_user,
)

router = APIRouter(prefix="/users", tags=["users"])

# ---- AUTH ----

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=10)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# ---- CRUD USERS ----

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return services.create_user(user)

@router.get("/", response_model=List[UserResponse])
def get_users():
    return services.get_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, current_user: User = Depends(get_current_user)):
    return services.get_user(user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, current_user: User = Depends(get_current_user)):
    return services.update_user(user_id, user_update)

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, current_user: User = Depends(get_current_user)):
    services.delete_user(user_id)
    return {"detail": "User deleted successfully"}
