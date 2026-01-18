from typing import List

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate, UserBase
from datetime import datetime
from app.repositories.department_repository import get_by_id as get_by_id_dep

def create_user(db: Session, data: UserCreate) -> User:
    user = User(**data.dict())
    user.created_at = datetime.now()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_in: UserUpdate, id:int):
    db_user = db.query(User).filter(User.id == id, User.deleted_at.is_(None)).first()
    if db_user:
        if user_in.first_name != None:
            db_user.first_name = user_in.first_name
        if user_in.last_name != None:
            db_user.last_name = user_in.last_name
        if user_in.email != None:
            db_user.email = user_in.email
        if user_in.department_id != None:
            db_user.department_id = user_in.department_id
        db_user.updated_at = datetime.now()
        db.commit()
        db.refresh(db_user)
    return db_user

def soft_delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id, User.deleted_at.is_(None)).first()
    if db_user:
        db_user.deleted_at = datetime.now()
        db.commit()
        db.refresh(db_user)
    return db_user

def hard_delete_user(db: Session, Id: int):
    db_user = db.query(User).filter(User.id == Id, User.deleted_at.is_not(None)).first()
    db.delete(db_user)
    db.commit()
    return db_user

def get_all(db: Session):
    users = db.query(User).all()
    print(f"repo got {len(users)} users")
    return users

def get_by_id(db: Session, user_id: int) :
    return db.query(User).filter(User.id == user_id, User.deleted_at.is_(None)).first()

def get_by_email(db: Session, email: str) :
    return db.query(User).filter(User.email == email).first()

def get_all_softdeleted(db: Session) :
    users = db.query(User).filter(User.deleted_at.isnot(None)).all()
    return users if not users is None else []

def get_by_id_softdeleted(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id, User.deleted_at.is_not(None)).first()
    return user if not user is None else []


def restore_all(db: Session):
    users = db.query(User).filter(User.deleted_at.is_not(None)).all()
    for user in users:
        user.deleted_at = None
        user.updated_at = datetime.now()
    if users:
        db.commit()
    return users

def restore_by_id(db: Session, user_id : int) :
    user = db.query(User).filter(User.id == user_id, User.deleted_at.is_not(None)).first()
    user.updated_at = datetime.now()
    user.deleted_at = None
    db.commit()
    db.refresh(user)
    return user


