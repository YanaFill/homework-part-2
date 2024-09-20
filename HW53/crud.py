from sqlalchemy.orm import Session
from models.user import User
from models.post import Post
from schemas.user import UserCreate
from schemas.post import PostCreate
import bcrypt
import uuid

# Створення користувача
def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password.decode('utf-8')
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Отримання користувача за email
def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

# CRUD для постів
def create_post(db: Session, post: PostCreate, author_id: uuid.UUID) -> Post:
    db_post = Post(
        title=post.title,
        content=post.content,
        author_id=author_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: uuid.UUID) -> Post:
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session):
    return db.query(Post).all()

def update_post(db: Session, post_id: uuid.UUID, post: PostCreate) -> Post:
    db_post = get_post(db, post_id)
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

def delete_post(db: Session, post_id: uuid.UUID) -> Post:
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
        return db_post
    return None
