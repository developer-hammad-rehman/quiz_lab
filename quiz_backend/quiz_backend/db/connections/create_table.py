from sqlmodel import SQLModel
from quiz_backend.db.connections.engine import engine

def create_table():
    SQLModel.metadata.create_all(engine)