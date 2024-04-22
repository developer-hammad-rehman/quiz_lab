from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config('.env')

except FileNotFoundError:
    config = Config()

token_secret = config('SECRET_KEY' , cast=Secret)
token_algorithm = config('ALGORITHM' , cast=Secret)