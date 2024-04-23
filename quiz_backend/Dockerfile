FROM python:3.12



RUN pip install poetry


WORKDIR /app


COPY . /app/


RUN poetry install


EXPOSE 8000

CMD ["poetry" , "run" , "uvicorn" , "quiz_backend.app.routes.main:app" , "--host" , "0.0.0.0" , "--reload"]