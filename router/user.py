from typing import List
from fastapi import APIRouter, Depends, Response, status

from sqlalchemy.orm import Session


from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user
from auth.oauth2 import get_current_user


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, response: Response, db: Session = Depends(get_db)):
    response.status_code = status.HTTP_201_CREATED
    return db_user.create_user(db, request)


@router.get("/", response_model=List[UserDisplay])
def get_all_users(
    db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)
):
    return db_user.get_all_users(db)


@router.get("/{user_id}", response_model=UserDisplay)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.get_user(db, user_id)


@router.patch("/{id}/update")
def update_user(
    id: int,
    request: UserBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.update_user(db, id, request)


@router.delete("/{id}/delete")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.delete_user(db, id)
