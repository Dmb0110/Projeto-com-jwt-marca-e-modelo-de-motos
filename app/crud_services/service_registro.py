from sqlalchemy.orm import Session
from app.models.models_user import User
from app.schemas.schemas import CriarUsuario
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class RegistroService:
    @staticmethod
    def registrar_usuario(request,db: Session) -> dict:
        usuario_existente = db.query(User).filter(User.username == request.username).first()
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Usuário já existe")

        # Criptografa a senha
        senha_hash = pwd_context.hash(request.password)

        # Cria e salva o novo usuário
        novo_usuario = User(username=request.username, hashed_password=senha_hash)
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)  # garante que atributos gerados (ex: id) sejam carregados

        return {"mensagem": "Usuário registrado com sucesso"}