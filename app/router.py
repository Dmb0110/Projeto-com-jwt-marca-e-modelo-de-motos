from fastapi import APIRouter
from app.routers.router_crud_moto import router as moto
from app.routers.router_moto_auth import router as moto_auth
from app.routers.router_registro import router as registro
from app.routers.router_login import router as login

api_router = APIRouter()

api_router.include_router(registro,prefix='/registro',tags=['registro'])
api_router.include_router(login,prefix='/login',tags=['login'])

api_router.include_router(moto_auth,prefix='/moto_auth',tags=['moto_auth'])

api_router.include_router(moto,prefix='/moto',tags=['moto'])



