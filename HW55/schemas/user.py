from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: UUID | None = Field(default_factory=uuid4)
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
