from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.login import Login
from app.services.login_service import login as check_user
from app.db.session import get_db

import jwt
import datetime
from typing import Optional
from pydantic import BaseModel
import bcrypt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

router = APIRouter()

@router.post("/login")
def login(user: Login, db: Session = Depends(get_db)):
    user_exists = check_user(db=db, email=user.email, password=user.password)

    if user_exists is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_jwt_token(email=user_exists.email)
    return {"access_token": token, "token_type": "bearer"}

def create_jwt_token(email: str, expires_delta: Optional[datetime.timedelta] = None) -> str:
    to_encode = {"exp": datetime.datetime.utcnow() + (expires_delta or datetime.timedelta(hours=1)),
                "sub": email}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
