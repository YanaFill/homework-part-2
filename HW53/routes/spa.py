from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from jinja2 import Template
import base64

router = APIRouter()

security = HTTPBasic()

# Dummy user data
SUPERUSER = {
    "username": "superuser",
    "password": "itstep"
}


# Функція для базової авторизації
def authenticate(credentials: HTTPBasicCredentials):
    correct_username = credentials.username == SUPERUSER["username"]
    correct_password = credentials.password == SUPERUSER["password"]

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True


# Головна сторінка SPA
@router.get("/spa", response_class=HTMLResponse)
def get_spa(credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)
    with open("templates/index.html") as f:
        template = Template(f.read())
    return template.render()


# Додати новий користувач
@router.get("/spa/addnew", response_class=HTMLResponse)
def add_new(credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)
    with open("templates/addnew.html") as f:
        template = Template(f.read())
    return template.render()


# Редагування користувача
@router.get("/spa/edit", response_class=HTMLResponse)
def edit_user(credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)
    with open("templates/edit.html") as f:
        template = Template(f.read())
    return template.render()
