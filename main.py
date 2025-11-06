from fastapi import HTTPException
from fastapi import FastAPI
from models.models import Base, engine
from crud import router as crud_router
from autenticacao2.authjwt2 import router as auth_router
#from test_crud import router
import time

#  Cria instancia da aplicaçao FastAPI
app = FastAPI()


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

#  Cria tabelas no banco de dados
#Base.metadata.create_all(bind=engine)

#  Incluir rotas publicas e privadas na aplicaçao
app.include_router(auth_router)
app.include_router(crud_router)



'''

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: davi9090
      POSTGRES_DB: banco_dmb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  backend:  # renomeado de "web" para "backend" para refletir melhor o propósito
    build: .
    depends_on:
      - db
    ports:
      - "8000:8000"  # ajuste conforme a porta usada pela sua API
    environment:
      DATABASE_URL: postgresql://postgres:davi9090@db:5432/banco_dmb

volumes:
  pgdata:
'''




