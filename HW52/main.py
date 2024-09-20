from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from routes.user import router as user_router
from routes.post import router as post_router

# Налаштування бази даних
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Створення FastAPI додатку
app = FastAPI()

# Додавання CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Зміни на свої дозволені домени
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутерів
app.include_router(user_router)
app.include_router(post_router)

# Створення таблиць
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Основний маршрут
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
