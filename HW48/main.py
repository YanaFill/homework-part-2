from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models import Base, Article
from database import engine, get_db

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
async def read_articles(request: Request, db: Session = Depends(get_db)):
    articles = db.query(Article).order_by(Article.id.desc()).all()
    return templates.TemplateResponse("index.html", {"request": request, "articles": articles})

@app.post("/create")
async def create_article(request: Request, title: str = Form(...), author: str = Form(...), year: int = Form(...), db: Session = Depends(get_db)):
    new_article = Article(title=title, author=author, year=year)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return RedirectResponse(url=app.url_path_for("read_articles"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/create")
async def create_article_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.get("/update/{article_id}")
async def update_article_form(request: Request, article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    return templates.TemplateResponse("update.html", {"request": request, "article": article})

@app.post("/update/{article_id}")
async def update_article(request: Request, article_id: int, title: str = Form(...), author: str = Form(...), year: int = Form(...), db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    article.title = title
    article.author = author
    article.year = year
    db.commit()
    return RedirectResponse(url=app.url_path_for("read_articles"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/delete/{article_id}")
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    db.delete(article)
    db.commit()
    return RedirectResponse(url=app.url_path_for("read_articles"), status_code=status.HTTP_303_SEE_OTHER)
