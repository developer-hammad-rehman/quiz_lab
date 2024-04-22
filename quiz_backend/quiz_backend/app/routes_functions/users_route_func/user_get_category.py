from typing import Annotated , Literal

from fastapi import Depends, Response
from sqlmodel import Session, select
from quiz_backend.db.connections.get_session import get_session
from quiz_backend.db.models.quiz_models import Category
from quiz_backend.helpers.decode_token_helper import decode_refresh_token
from quiz_backend.helpers.ouath2_helper import ouath2_schema

def get_category(token : Annotated[str , Depends(ouath2_schema)] , session : Annotated[Session , Depends(get_session)] , type:Literal['acces_token' , "refresh_token"] , response:Response):
    if type == 'refresh_token':
        token = decode_refresh_token(token)
        response.set_cookie(key='acces_token' , value=token , max_age=500)
        return session.exec(select(Category)).all()
    else:
        return session.exec(select(Category)).all()