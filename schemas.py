from typing import Optional
from pydantic import BaseModel

# Modelo para criação de usuário
class CriarUsuario(BaseModel):
    username: str
    password: str

# Modelo para requisição de login
class LoginRequest(BaseModel):
    username: str
    password: str
#############################################################
# Modelo para criação de moto
class CriarMoto(BaseModel):
    marca: str
    modelo: str

# Modelo de saída da moto (inclui ID)
class MotoOut(BaseModel):
    id: int
    marca: str
    modelo: str

    # Permite criar o modelo a partir de atributos ORM
    model_config = {
        'from_attributes': True
    }

# Modelo para atualização parcial da moto
class Atualizar(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None

# Modelo para resposta de exclusão
class Deletar(BaseModel):
    mensagem: bool
