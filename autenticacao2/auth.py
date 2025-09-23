''''# auth/auth.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models import Moto
from crud import get_db

SECRET_KEY = "sua_chave_secreta"  # Troque por uma chave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    moto = db.query(Moto).filter(Moto.username == username).first()
    if not moto or not verify_password(password, moto.password):
        return None
    return moto
'''
     #if not moto:
    #return False
   #if not verify_password(password, moto.password):
      #return False
    #return moto
'''

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    moto = db.query(Moto).filter(Moto.username == username).first()
    if moto is None:
        raise credentials_exception
    return moto
'''
###########################################################################

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models import User
from crud import get_db

#Chave secreta usada para assinar e verificar os tokens JWT
######################
SECRET_KEY = "sua_chave_secreta"
######################
ALGORITHM = "HS256"
######################
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#######################
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#######################
#  verifica se a senha digitada e igual a que esta no banco
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

########################################
#  criptografa a senha antes de salvar no banco
def get_password_hash(password):
    return pwd_context.hash(password)

#########################################
#  confirma se o usuario existe e se a senha esta correta
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

#########################################
#  criar um token para autenticar o usuario
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

########################################
#  identifica quem e o usuario que esta fazendo a requisiçao
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        ############################
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    ###############################
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user



