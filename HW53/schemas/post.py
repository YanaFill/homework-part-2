from pydantic import BaseModel
from uuid import UUID
from enum import Enum
import datetime

class PostStatus(str, Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"

class PostBase(BaseModel):
    title: str
    content: str
    published: PostStatus

class PostCreate(PostBase):
    pass

class PostInDB(PostBase):
    id: UUID
    author_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
