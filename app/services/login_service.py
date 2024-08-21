from sqlalchemy.orm import Session
from app.models.user import User

def login(db: Session, email: str, password: str):
    return db.query(User).filter(User.email == email, User.password == password).first()
