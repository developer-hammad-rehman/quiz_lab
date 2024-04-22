from typing import Annotated, Sequence
from fastapi import Depends, FastAPI
from quiz_backend.app.routes_functions.admin_route_fuc.admin_add_chocies import add_chocie
from quiz_backend.app.routes_functions.admin_route_fuc.admin_add_quiz import add_quiz
from quiz_backend.app.routes_functions.admin_route_fuc.admin_add_quiz_level import add_quiz_level
from quiz_backend.app.routes_functions.admin_route_fuc.admin_auth import Admin_Login, admin_login
from quiz_backend.app.routes_functions.route_functions import route_route , login_route , sigin_up
from contextlib import asynccontextmanager
from quiz_backend.app.routes_functions.users_route_func.user_get_category import get_category
from quiz_backend.app.routes_functions.users_route_func.user_get_questions import get_questions
from quiz_backend.db.connections.create_table import create_table
from quiz_backend.db.models.quiz_models import Category, Chocies, Quiz, Quizlevel
from quiz_backend.app.routes_functions.admin_route_fuc.admin_add_category import add_category 
from quiz_backend.app.routes_functions.users_route_func.user_get_question_level import quiz_level

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table()
    yield

app = FastAPI(title="QuizLab" , lifespan=lifespan)

@app.get('/')
def route(route_func = Depends(route_route)):
    return route_func


@app.post('/login')
def login(route_func = Depends(login_route)):
    return route_func


@app.post('/register')
def sign_up(route_func = Depends(sigin_up)):
    return route_func

@app.post('/admin_login')
def admin_login_route(route_func:Annotated[Admin_Login , Depends(admin_login)]):
    return route_func


@app.post('/admin_add_catgory')
def add_category(route_func : Annotated[Category , Depends(add_category)]):
    return route_func


@app.post('/admin_add_quiz_level')
def add_quiz_level_route(route_func:Annotated[Quizlevel , Depends(add_quiz_level)]):
    return route_func


@app.post('/admin_add_question')
def add_questions_route(route_func:Annotated[Quiz , Depends(add_quiz)]):
    return route_func


@app.post('/admin_add_chocies')
def chocies_route(route_func:Annotated[Chocies , Depends(add_chocie)]):
    return route_func


@app.get('/get_category')
def get_category_route(route_func:Annotated[Sequence[Category] , Depends(get_category)]):
    return route_func

@app.get('/get_quiz_level')
def quiz_level(route_func:Annotated[Sequence[Quizlevel], Depends(quiz_level)]):
    return route_func

@app.get('/get_question')
def quiz_route(route_func : Annotated[list[dict[str, str]] , Depends(get_questions)]):
    return route_func