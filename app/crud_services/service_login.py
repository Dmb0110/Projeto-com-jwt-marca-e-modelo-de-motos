from sqlalchemy.orm import Session
from app.schemas.schemas import LoginUsuario
from app.database.session import get_db
from app.autenticacao2.authjwt2 import authenticate_user, create_token
from fastapi import Depends, HTTPException

class LoginService:

    @staticmethod
    def login(request: LoginUsuario, db: Session = Depends(get_db)):
        # Boa prática: usar schema Pydantic (LoginUsuario) para validar entrada.
        username = request.username
        password = request.password

        # Autenticação delegada para função externa (authenticate_user).
        # Isso mantém a responsabilidade separada e facilita testes.
        user = authenticate_user(db, username, password)
        if not user:
            # Tratamento de erro adequado com HTTPException e status 401.
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        # Criação de token JWT com claim "sub" (subject).
        # Sugestão: incluir mais claims (ex: roles, id do usuário) para suportar autorização.
        token = create_token({"sub": username})

        # Retorno simples e claro em formato JSON.
        # Sugestão: padronizar resposta (ex: {"access_token": token, "token_type": "bearer"})
        return {"access_token": token}
