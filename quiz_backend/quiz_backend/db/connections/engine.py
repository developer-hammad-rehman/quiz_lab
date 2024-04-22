from sqlmodel import create_engine
from quiz_backend.settings.database_env.db_env_settings import DATABASE_URL

connection_string = str(DATABASE_URL).replace(
    'postgresql' , 'postgresql+psycopg2'
)

engine = create_engine(connection_string , connect_args={'sslmode':'require'} , pool_recycle=300 , echo=True)