from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from quiz_backend.db.connections.get_session import get_session
from quiz_backend.db.models.quiz_models import Quizlevel

def is_exist(session:Session, name:str , catagory_id:int):
    statment = (select(Quizlevel).where(catagory_id == Quizlevel.category_id).where(name == Quizlevel.name))
    result = session.exec(statment).first()
    print(result)
    if result:
        return True 
    else:
        return False

def add_quiz_level(input_level : Quizlevel , session : Annotated[Session , Depends(get_session)]):
    if is_exist(session , input_level.name , input_level.category_id):
        raise HTTPException(status_code=404 , detail="Quiz level already exist")
    else:
        session.add(input_level)
        session.commit()
        session.refresh(input_level)
        return input_level