from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schema import user_schema
from models import user_model
from utils import db
from core.security import auth, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get current user by decoding JWT
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = jwt.verify_token(token)
    if token_data is None:
        raise credentials_exception
    user = db.query(user_model.User).filter(user_model.User.username == token_data["sub"]).first()
    if user is None:
        raise credentials_exception
    return user


# User registration
@router.post("/register", response_model=user_schema.UserResponse)
def register_user(user: user_schema.UserCreate, db: Session = Depends(db.get_db)):
    hashed_password = auth.get_password_hash(user.password)
    db_user = user_model.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# User login and token generation
@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
    user = db.query(user_model.User).filter(user_model.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route for any authenticated user
@router.get("/me", response_model=user_schema.UserResponse)
def read_users_me(current_user: user_model.User = Depends(get_current_user)):
    return current_user

