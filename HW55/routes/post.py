from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from schemas.post import PostCreate, PostInDB
from crud import create_post, get_post, get_posts, update_post, delete_post
from database import get_db

router = APIRouter()

@router.post("/users/{author_id}/posts/", response_model=PostInDB)
def create_post_endpoint(post: PostCreate, author_id: UUID, db: Session = Depends(get_db)):
    return create_post(db=db, post=post, author_id=author_id)

@router.get("/posts/", response_model=list[PostInDB])
def read_posts(db: Session = Depends(get_db)):
    return get_posts(db=db)

@router.get("/posts/{post_id}", response_model=PostInDB)
def read_post(post_id: UUID, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/posts/{post_id}", response_model=PostInDB)
def update_post_endpoint(post_id: UUID, post: PostCreate, db: Session = Depends(get_db)):
    return update_post(db=db, post_id=post_id, post=post)

@router.delete("/posts/{post_id}", response_model=PostInDB)
def delete_post_endpoint(post_id: UUID, db: Session = Depends(get_db)):
    db_post = delete_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
