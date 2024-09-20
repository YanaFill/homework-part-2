from pydantic import BaseModel
from guid import GUID
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

class PostCreate(PostBase):
    pass

class PostInDB(PostBase):
    id: GUID
    author_id: GUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
