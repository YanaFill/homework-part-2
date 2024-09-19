from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas.user import UserCreate, UserUpdate, UserInDB
import crud
from auth import authenticate_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter()

# Створення користувача (POST)
@router.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# Оновлення користувача (PUT)
@router.put("/users/", response_model=UserInDB)
def update_user(user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user=user, db_user=db_user)

# Видалення користувача (DELETE)
@router.delete("/users/{email}", response_model=UserInDB)
def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, db_user=db_user)

# Аутентифікація (POST)
@router.post("/auth/")
def authenticate(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Authenticated successfully"}

app.include_router(router)
