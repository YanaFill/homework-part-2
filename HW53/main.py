from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router as user_router
from routes.post import router as post_router
from routes.spa import router as spa_router
from database import Base, engine

# Ініціалізація FastAPI
app = FastAPI()

# Додавання CORS (опціонально)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення маршрутів
app.include_router(user_router)
app.include_router(post_router)
app.include_router(spa_router)

# Створення таблиць в базі даних
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
