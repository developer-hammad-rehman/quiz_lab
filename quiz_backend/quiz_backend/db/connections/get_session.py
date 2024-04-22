from sqlmodel import Session
from quiz_backend.db.connections.engine import engine

def get_session():
    with Session(engine) as session :
        yield session