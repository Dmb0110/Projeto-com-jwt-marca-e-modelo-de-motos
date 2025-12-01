# Importa os schemas que serão expostos por este módulo
from .schemas import CriarMoto, MotoOut, Atualizar, Deletar
# Atenção: aqui você não está importando CriarUsuario nem LoginUsuario,
# mas eles aparecem listados no __all__. Isso gera inconsistência.

# __all__ define quais nomes serão exportados quando alguém fizer:
#   from app.schemas import *
# É uma forma de controlar a API pública do pacote.
__all__ = [
    'CriarUsuario',   # Não foi importado acima, precisa ser incluído
    'LoginRequest',   # O nome correto no seu código é LoginUsuario, não LoginRequest
    'CriarMoto',
    'MotoOut',
    'Atualizar',
    'Deletar',
]