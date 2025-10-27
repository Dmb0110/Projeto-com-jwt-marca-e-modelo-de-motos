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
https://projeto3-autenticacao-5higfpodp-dmb0110s-projects.vercel.app/
'''