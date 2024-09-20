from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserInDB
from crud import create_user, get_user_by_email
from database import get_db

router = APIRouter()

@router.post("/users/", response_model=UserInDB)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/{email}", response_model=UserInDB)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
