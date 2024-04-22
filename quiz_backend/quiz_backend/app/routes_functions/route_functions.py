from typing import Annotated
from quiz_backend.controllers.auth_users_controllers import verfiy_email , verify_password ,generate_token
from fastapi import Depends , HTTPException, Response
from quiz_backend.db.models.user_auth_model import Users
from sqlmodel import Session 
from quiz_backend.db.connections.get_session import get_session
from fastapi.security import OAuth2PasswordRequestForm
from quiz_backend.helpers.pwd_hash import hash_password

def route_route():
   return "Welocme to my app"

def login_route(form_data: Annotated[OAuth2PasswordRequestForm , Depends()] , session:Annotated[Session , Depends(get_session)] , response:Response):
    is_email = verfiy_email(session=session , email=form_data.username)
    if is_email:
        is_password = verify_password(session , form_data.username , form_data.password)
        if is_password:
         tokens = generate_token(data={
            "email" : form_data.username,
         })
         response.set_cookie(key="acces_token", value=tokens['acces_token'] , max_age=4000)
         response.set_cookie(key="refresh_token" , value=tokens['refresh_token'])
         return "You are Login"
        else:
           raise HTTPException(status_code=404 , detail= "Password is Invalid")
    else:
        raise HTTPException(status_code=404 , detail="Email is Invalid")
    

def sigin_up(form_data : Annotated[OAuth2PasswordRequestForm , Depends()] , session:Annotated[Session , Depends(get_session)]):
   is_email = verfiy_email(session=session , email=form_data.username)
   if is_email:
      raise HTTPException(status_code=404 , detail="Email Already Exist")
   else:
      hash_pass = hash_password(password=form_data.password)
      data = Users(email=form_data.username , password=hash_pass)
      session.add(data)
      session.commit()
      session.refresh(data)
      return "You are Register"