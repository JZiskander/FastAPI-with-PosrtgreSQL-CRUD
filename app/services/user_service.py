from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.user_repository import create_user, update_user, soft_delete_user, hard_delete_user, get_all, get_by_id, get_all_softdeleted, get_by_id_softdeleted, restore_all, restore_by_id, get_by_email
from app.repositories.department_repository import get_by_id as get_department_by_id
from app.schemas.user_schema import UserCreate, UserUpdate, UserBase

def create_user_serv(db : Session, user_data: UserCreate) :
    dept = get_department_by_id(db, user_data.department_id)
    if not dept:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": 404,
                "message": "Department not found",
                "data": f"department id :{user_data.department_id}"
            }
        )
    get_by_email_serv(db, user_data.email)
    return create_user(db, user_data)

def update_user_serv(db : Session, user_data: UserUpdate, id: int) :
    user = get_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": 404,
                "message": "User not found",
                "data": f"user id :{id}"
            }
        )
    if user_data.department_id != None:
        dep = get_department_by_id(db, user_data.department_id)
        if not dep:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "status": 404,
                    "message": "Department not found",
                    "data": f"department id :{id}"
                }
            )
    if user_data.email != None:
        get_by_email_serv(db, user_data.email)
    return update_user(db, user_data, id)


def soft_delete_user_serv(db : Session, Id : int) :
    db_user = get_by_id(db, Id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": 404,
                "message": "User not found",
                "data": f"user id :{Id}"
            }
        )
    soft_delete_user(db, db_user.id)
    return db_user

def hard_delete_user_serv(db : Session, Id : int) :
    db_user = get_by_id_softdeleted(db, Id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": 404,
                "message": "User not soft deleted",
                "data": f"user id :{Id}"
            }
        )
    hard_delete_user(db, db_user.id)
    return db_user

def get_all_users_serv(db : Session):
    users = get_all(db)
    return users

def get_by_id_user_serv(db: Session, user_id: int):
    user = get_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": 404,
                "message": "User not found",
                "data": f"user id :{user_id}"
            }
        )
    return user

def get_by_email_serv(db: Session, email: str):
    user = get_by_email(db, email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "status": 409,
                "message": "User with this mail address already exists",
                "data": f"mail address :{email}"
            }
        )

def get_all_soft_delete_users_serv(db : Session):
    return get_all_softdeleted(db)

def get_by_id_soft_delete_user_serv(db : Session, user_id: int):
    user = get_by_id_softdeleted(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": 404,
                "message": "User not soft deleted",
                "data": f"user id :{user_id}"
            }
        )
    return user

def restore_user_by_id_serv(db : Session, user_data: UserBase) :
    user = restore_by_id(db, user_data.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'status': 404,
                'message': 'User not soft deleted',
                'data': f"user id :{user_data.id}"
            }

        )
    return user

def restore_all_users_serv(db : Session):
    return restore_all(db)