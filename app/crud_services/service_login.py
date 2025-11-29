from sqlalchemy.orm import Session
from app.schemas.schemas import LoginUsuario
from app.database.session import get_db
from app.autenticacao2.authjwt2 import authenticate_user, create_token
from fastapi import Depends, HTTPException

class LoginService:

    @staticmethod
    def login(request: LoginUsuario, db: Session = Depends(get_db)):
        username = request.username
        password = request.password

        user = authenticate_user(db, username, password)
        if not user:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        token = create_token({"sub": username})  # payload inclui o "sub" (subject) como username
        return {"access_token": token}
    