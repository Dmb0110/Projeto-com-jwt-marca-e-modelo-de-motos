from fastapi import APIRouter
from app.routers.router_crud_moto import router as moto
from app.routers.router_moto_auth import router as moto_auth
from app.routers.router_registro import router as registro
from app.routers.router_login import router as login

#ria um APIRouter principal para organizar e agrupar sub-rotas.
api_router = APIRouter()

# Inclui rotas de registro de usuário com prefixo e tag.
api_router.include_router(registro, prefix='/registro', tags=['registro'])

# Inclui rotas de login com prefixo e tag.
api_router.include_router(login, prefix='/login', tags=['login'])

# Inclui rotas protegidas de motos (autenticadas).
api_router.include_router(moto_auth, prefix='/moto_auth', tags=['moto_auth'])

# Inclui rotas públicas de motos (CRUD básico).
api_router.include_router(moto, prefix='/moto', tags=['moto'])
