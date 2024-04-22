from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from quiz_backend.db.connections.get_session import get_session
from quiz_backend.db.models.quiz_models import Quiz


def add_quiz(input_quiz:Quiz , session:Annotated[Session , Depends(get_session)]):
    session.add(input_quiz)
    session.commit()
    session.refresh(input_quiz)
    return input_quiz