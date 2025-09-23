'''from io import StringIO
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Integer, String

####################
class CriarAluno(BaseModel):
    nome: str
    idade: int
    turma: str

class AlunoOut(BaseModel):
    id: int
    nome: str
    idade: int
    turma: str

    model_config = {
        'from_attributes': True
    }

class Atualizar(BaseModel):
    nome:Optional[str] = None
    idade: Optional[int] = None
    turma: Optional[str] = None

class Deletar(BaseModel):
    mensagem: bool
    
###################################################################
class CriarMoto(BaseModel):
    marca: str
    modelo: str

class MotoOut(BaseModel):
    id: int
    marca: str
    modelo: str
    username: str

    model_config = {
        'from_attributes': True
    }

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
###############################################################

from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
###############################################################
class CriarMoto(BaseModel):
    marca: str
    modelo: str

class MotoOut(CriarMoto):
    id: int

    class Config:
        orm_mode = True

class Atualizar(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
#################################################

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class CriarCliente(BaseModel):
    nome: str
    idade: int

class ClienteOut(BaseModel):
    id: int

    class Config:
        orm_mode = True

class Atualizar(BaseModel):
    nome:Optional[str] = None
    idade:Optional[int] = None

class Deletar(BaseModel):
    mensagem: bool
'''
from typing import Optional
from pydantic import BaseModel

class CriarUsuario(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str
#################################
class CriarMoto(BaseModel):
    marca: str
    modelo: str

class MotoOut(BaseModel):
    id: int
    marca: str
    modelo: str

    model_config = {
        'from_attributes': True
    }

class Atualizar(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None

class Deletar(BaseModel):
    mensagem: bool

'''
###################################
class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class CriarTv(BaseModel):
    marca: str
    polegadas: int

class TvOut(BaseModel):
    id: int
    marca: str
    polegadas: int

    class Config:
        orm_mode = True

class Atualizar(BaseModel):
    marca: Optional[str] = None
    polegadas: Optional[int] = None

class Deletar(BaseModel):
    mensagem: bool

'''
