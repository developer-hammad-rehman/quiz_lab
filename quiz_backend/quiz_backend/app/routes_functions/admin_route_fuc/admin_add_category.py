
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlmodel import Session ,select
from quiz_backend.db.connections.get_session import get_session
from quiz_backend.db.models.quiz_models import Category


def is_name(session:Session , name:str):
    statment = select(Category).where(name == Category.name)
    result = session.exec(statment).first()
    if result:
       return True if result.name.lower() == name.lower() else False
    else:
       return False
 

def add_category(input_category:Category , session:Annotated[Session , Depends(get_session)]):
    if is_name(session , input_category.name):
        raise HTTPException(status_code=404 , detail="Category Already Exist")
    else:
     session.add(input_category)
     session.commit()
     session.refresh(input_category)
     return input_category