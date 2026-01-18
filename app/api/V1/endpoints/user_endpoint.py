from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.schemas.user_schema import UserCreate, UserUpdate, UserBase
from app.services.user_service import create_user_serv, update_user_serv, soft_delete_user_serv, hard_delete_user_serv, get_all_users_serv, get_by_id_user_serv, get_all_soft_delete_users_serv, get_by_id_soft_delete_user_serv, restore_all_users_serv, restore_user_by_id_serv
from app.core.database import get_db

router = APIRouter()

@router.post('/create_user', status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    create_user_serv(db, user)
    return {
        'status': 201,
        'message': 'User created successfully',
        'user': user
    }

@router.patch('/update_user/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    update_user_serv(db, user, id)
    return {
        'status': 201,
        'message': 'User updated successfully',
        'user': user
    }

@router.get('/user', status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    data = get_all_users_serv(db)
    if len(data) == 0:
        return {
            'status': 200,
            'message': 'No users found'
        }
    return {
        'status': 200,
        'message': 'Users retrieved successfully',
        'users': data
    }

@router.get('/get_soft_deleted_users', status_code=status.HTTP_200_OK)
def get_soft_deleted_users(db: Session = Depends(get_db)):
    data = get_all_soft_delete_users_serv(db)
    if len(data) == 0:
        return {
            'status': 200,
            'message': 'No users Soft Deleted'
        }
    return {
        'status': 200,
        'message': 'Users restrived successfully',
    }

@router.patch('/restore', status_code=status.HTTP_202_ACCEPTED)
def restore_users(db: Session = Depends(get_db)):
    data = restore_all_users_serv(db)
    if len(data) == 0:
        return {
            'status': 200,
            'message': 'No users soft deleted to restore'
        }
    return {
        'status': 200,
        'message': 'Users restored successfully',
        'data': data
    }

@router.get('/user/{user_id}', status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    data = get_by_id_user_serv(db, user_id)
    return {
        'status': 200,
        'message': 'User retrieved successfully',
        'data': data
    }

@router.delete('/soft_delete_user/{user_id}', status_code=status.HTTP_200_OK)
def soft_delete_user(user_id: int, db: Session = Depends(get_db)):
    data = soft_delete_user_serv(db, user_id)
    return {
        'status': 200,
        'message': 'User deleted successfully',
        'data': data
    }

@router.delete('/hard_delete_user/{user_id}', status_code=status.HTTP_200_OK)
def hard_delete_user(user_id: int, db: Session = Depends(get_db)):
    hard_delete_user_serv(db, user_id)
    return {
        'status': 200,
        'message': 'Users hard deleted successfully',
    }

@router.get('/get_soft_deleted_users/{user_id}', status_code=status.HTTP_200_OK)
def get_soft_deleted_users(user_id: int, db: Session = Depends(get_db)):
    data = get_by_id_soft_delete_user_serv(db, user_id)
    return {
        'status': 200,
        'message': 'User restrived successfully',
        'data': data
    }

@router.patch('/restore/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def restore_user(user_id: int, db: Session = Depends(get_db)):
    data = restore_user_by_id_serv(db, user_id)
    return {
        'status': 200,
        'message': 'User restored successfully',
        'data': data
    }
