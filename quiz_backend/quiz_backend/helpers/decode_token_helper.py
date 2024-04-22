from jose import jwt , JWTError
from quiz_backend.settings.jwt_env_settings.jwt_env_settings import token_algorithm , token_secret
def decode_refresh_token(token:str):
 try:
    token = jwt.decode(token=token , key=str(token_secret) , algorithms=str(token_algorithm))
    return jwt.encode(claims=token , key=str(token_secret) , algorithm=str(token_algorithm))
 except JWTError as je:
    return je