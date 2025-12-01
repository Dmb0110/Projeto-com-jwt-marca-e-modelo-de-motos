from sqlalchemy.orm import Session
from app.models.models_user import User
from app.schemas.schemas import CriarUsuario
from fastapi import HTTPException
from passlib.context import CryptContext

# Uso do Passlib com bcrypt é uma boa prática para hashing seguro de senhas.
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class RegistroService:
    @staticmethod
    def registrar_usuario(request: CriarUsuario, db: Session) -> dict:
        # Verifica se já existe um usuário com o mesmo username.
        usuario_existente = db.query(User).filter(User.username == request.username).first()
        if usuario_existente:
            # Tratamento de erro adequado com HTTPException e status 400.
            raise HTTPException(status_code=400, detail="Usuário já existe")

        # Criptografa a senha antes de salvar no banco.
        senha_hash = pwd_context.hash(request.password)

        # Cria e persiste o novo usuário.
        novo_usuario = User(username=request.username, hashed_password=senha_hash)
        db.add(novo_usuario)
        db.commit()
        # Refresh garante que atributos gerados pelo banco (ex: id) sejam carregados.
        db.refresh(novo_usuario)

        # Retorno simples com mensagem. Poderia retornar também os dados do usuário criado
        # (excluindo a senha) para consistência com outras rotas.
        return {"mensagem": "Usuário registrado com sucesso"}
