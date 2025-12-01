from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field

# ✅ Modelo para criação de usuário
class CriarUsuario(BaseModel):
    # ⚠️ Boa prática: definir restrições de tamanho para username e password.
    # Sugestão: aumentar min_length da senha para algo mais seguro (ex: 6 ou 8).
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=2)

# ✅ Modelo para requisição de login
class LoginUsuario(BaseModel):
    username: str
    password: str

# ✅ Modelo para criação de moto
class CriarMoto(BaseModel):
    marca: str = Field(..., min_length=3, max_length=100)
    modelo: str = Field(..., min_length=3, max_length=100)

# ✅ Modelo de saída da moto (inclui ID)
class MotoOut(BaseModel):
    id: int
    marca: str
    modelo: str

    # ✅ Permite criar o modelo a partir de atributos ORM (SQLAlchemy).
    model_config = ConfigDict(
        from_attributes=True
    )

# ✅ Modelo para atualização parcial da moto
class Atualizar(BaseModel):
    # ⚠️ Usa Optional para permitir atualização parcial.
    # Sugestão: usar exclude_unset=True ao aplicar no serviço para atualizar apenas os campos enviados.
    marca: Optional[str] = Field(None, min_length=3, max_length=100)
    modelo: Optional[str] = Field(None, min_length=3, max_length=100)

# ✅ Modelo para resposta de exclusão
class Deletar(BaseModel):
    mensagem: str
