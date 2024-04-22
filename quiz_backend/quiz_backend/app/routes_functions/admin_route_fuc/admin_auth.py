from typing import Annotated
from sqlmodel import SQLModel, Session
from quiz_backend.settings.admin_settings.admin_auth import admin_name , admin_pass
from quiz_backend.db.connections.get_session import get_session
from fastapi import Depends, HTTPException

class Admin_Login(SQLModel):
    admin_name:str
    admin_pass:str

def admin_login(admin_detail:Admin_Login):
    if admin_detail.admin_name == admin_name:
        if admin_detail.admin_pass == admin_pass:
            return admin_detail
        else:
            raise HTTPException(status_code=404 , detail="Password is Invalid")
    else:
        raise HTTPException(status_code=404 , detail="Email is Invalid")