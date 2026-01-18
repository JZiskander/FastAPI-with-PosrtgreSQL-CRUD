from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentBase
from app.repositories.department_repository import creat_department, update_department, soft_delete_department, hard_delete_department, get_by_id, get_all, get_all_SoftDeleted, get_by_id_SoftDeleted, restore_all, restore_by_id

def create_department_serv(db: Session, department_data: DepartmentCreate):
    department = creat_department(db, department_data)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "status": "409_CONFLICT",
                "message": "Department already exists",
                "data": department_data
            },
        )
    return department

def update_department_serv(db: Session, department_in: DepartmentUpdate, id:int):
    department = get_by_id(db, id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": "404_NOT_FOUND",
                "message": "Department not found",
                "data": get_by_id(db, id)
            },
        )
    return update_department(db, department_in, id)

def soft_delete_department_serv(db: Session, Id: int):
    department = get_by_id(db, Id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": "404_NOT_FOUND",
                "message": "Department not found",
                "data": department
            },
        )
    return soft_delete_department(db, Id)

def hard_delete_department_serv(db: Session, Id: int):
    department = get_by_id_SoftDeleted(db, Id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": "404_NOT_FOUND",
                "message": "Department not Soft Deleted",
                "data": department
            },
        )
    return hard_delete_department(db, Id)

def get_all_departments_serv(db: Session):
    department = get_all(db)
    return department

def get_by_id_department_serv(db: Session, department_id: int):
    department = get_by_id(db, department_id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": "404_NOT_FOUND",
                "message": "Department not found",
                "data": department_id
            }
        )
    return department

def get_all_soft_deleted_departments_serv(db: Session):
    department = get_all_SoftDeleted(db)
    return department

def get_by_id_soft_deleted_department_serv(db: Session, department_id: int):
    department = get_by_id_SoftDeleted(db, department_id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": "404_NOT_FOUND",
                "message": "Department not soft deleted",
                "data": department_id
            },
        )
    return department

def restore_all_departments_serv(db: Session):
    return restore_all(db)

def restore_by_id_department_serv(db: Session, department_id: int):
    department = get_by_id_soft_deleted_department_serv(db, department_id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "status": "404_NOT_FOUND",
                "message": "Department not soft deleted",
                "data": department_id
            },
        )
    return restore_by_id(db, department_id)