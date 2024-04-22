from typing import Optional
from sqlmodel import SQLModel, Field


class Category(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    name : str


class Quizlevel(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    name:str
    category_id : int = Field(int , foreign_key='category.id')


class Quiz(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    question : str
    level_id : int = Field(int , foreign_key='quizlevel.id')


class Chocies(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    chocie : str
    quiz_id : int = Field(int , foreign_key='quiz.id') 
    status:bool