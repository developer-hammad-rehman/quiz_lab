from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from quiz_backend.db.connections.get_session import get_session
from quiz_backend.db.models.quiz_models import Chocies


def add_chocie(input_choice :Chocies , session:Annotated[Session , Depends(get_session)]):
    session.add(input_choice)
    session.commit()
    session.refresh(input_choice)
    return input_choice