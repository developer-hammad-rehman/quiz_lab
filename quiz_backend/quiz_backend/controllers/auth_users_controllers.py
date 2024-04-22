from typing import Union
from sqlmodel import Session , select
from quiz_backend.db.models.user_auth_model import Users 
from passlib.context import CryptContext
from quiz_backend.settings.jwt_env_settings.jwt_env_settings import token_algorithm , token_secret
from jose import jwt
pwd_context = CryptContext(schemes="bcrypt")

def verfiy_email(session:Session , email:str):
    statment = select(Users).where(email == Users.email)
    result = session.exec(statment).first()
    if result:
        return True
    else:
        return False
    

def verify_password(session:Session , email:str , password:str):
    statment = select(Users).where(email == Users.email)
    result = session.exec(statment).first()  
    return pwd_context.verify(password , result.password)

def generate_token(data : dict[str , Union[str , int]]):
    token = jwt.encode(claims=data , key=str(token_secret) , algorithm=str(token_algorithm))
    return {
        'acces_token' : token,
        "refresh_token":token
    }