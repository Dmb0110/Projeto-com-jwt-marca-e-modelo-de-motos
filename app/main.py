from fastapi import FastAPI, HTTPException
from app.models.models_moto import Base
from app.autenticacao2.authjwt2 import router as auth_router
from app.router import api_router
from app.database.session import engine
import time

#  Cria instância da aplicação FastAPI com metadados úteis para documentação.
app = FastAPI(
    title='API de marca e modelo de motos',
    description='Gerenciamento de motos',
    version='1.0.0',
    docs_url='/docs',   # Documentação interativa padrão
    redoc_url='/redoc'  # Documentação alternativa ReDoc
)

# Isso é útil para inicializar o banco automaticamente, mas em produção é melhor usar migrations (Alembic).
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

#  Inclui rotas públicas e privadas na aplicação.
app.include_router(api_router)