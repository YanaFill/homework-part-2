from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from enum import Enum
from typing import Optional
from datetime import datetime


class PostStatus(str, Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"

class PostBase(BaseModel):
    title: str
    content: str
    published: PostStatus
    year: int

class PostCreate(PostBase):
    pass

class PostInDB(PostBase):
    id: UUID = Field(default_factory=uuid4)
    author_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
