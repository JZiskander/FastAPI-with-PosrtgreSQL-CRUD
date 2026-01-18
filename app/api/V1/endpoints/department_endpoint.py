from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.core.database import get_db
from app.services.deparment_service import create_department_serv, update_department_serv, soft_delete_department_serv, hard_delete_department_serv, get_all_departments_serv, get_by_id_department_serv, get_all_soft_deleted_departments_serv, get_by_id_soft_deleted_department_serv, restore_all_departments_serv, restore_by_id_department_serv
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentBase
from app.core.config import settings

router = APIRouter()

@router.post('/create_department', status_code=status.HTTP_201_CREATED)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    create_department_serv(db, department)
    return {
        "status": 201,
        "message": "Department created successfully",
        "data": department
    }

@router.patch('/update_department/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_department(id: int, department: DepartmentUpdate, db: Session = Depends(get_db)):
    update_department_serv(db, department, id)
    return {
        "status": 200,
        "message": "Department updated successfully",
        "data": get_by_id_department_serv(db, id)
    }

@router.get('/department', status_code=status.HTTP_200_OK)
def get_all_departments(db: Session = Depends(get_db)):
    data = get_all_departments_serv(db)
    if len(data) == 0:
        return {
            "status": 200,
            "message": "No Departments found",
        }
    return {
        "status": 200,
        "message": "Departments retrieved successfully",
        "data": data
    }

@router.get('/get_soft_deleted', status_code=status.HTTP_200_OK)
def get_soft_deleted_departments(db: Session = Depends(get_db)):
    data = get_all_soft_deleted_departments_serv(db)
    if len(data) == 0:
        return {
            "status": 200,
            "message": "No Departments soft deleted",
        }
    return {
        "status": 200,
        "message": "Departments retrieved successfully",
        "data": data
    }

@router.patch('/restore')
def restore_department(db: Session = Depends(get_db)):
    data = restore_all_departments_serv(db)
    if len(data) == 0:
        return {
            "status": 200,
            "message": "No Departments restored"
        }
    return {
        "status": 200,
        "message": "Departments restored successfully",
        "data": data
    }

@router.get('/departments/{id}', status_code=status.HTTP_200_OK)
def get_department(id: int, db: Session = Depends(get_db)):
    data = get_by_id_department_serv(db, id)
    return{
        "status": 200,
        "message": "Department retrieved successfully",
        "data": data
    }

@router.delete(f'/departments/soft_delete_department/{id}', status_code=status.HTTP_202_ACCEPTED)
def soft_delete_department(id: int, db: Session = Depends(get_db)):
    data = soft_delete_department_serv(db, id)
    return {
        "status": 200,
        "message": "Department deleted successfully",
        "data": data
    }


@router.delete('/departments/hard_delete_department/{department_id}')
def hard_delete_department(department_id: int, db: Session = Depends(get_db)):
    data = hard_delete_department_serv(db, department_id)
    return {
        "status": 200,
        "message": "Department hard deleted successfully",
        "data": data
    }


@router.get('/departments/get_soft_deleted/{department_id}', status_code=status.HTTP_200_OK)
def get_soft_deleted_department_by_id(department_id: int, db: Session = Depends(get_db)):
    data = get_by_id_soft_deleted_department_serv(db, department_id)
    return{
        "status": 200,
        "message": "Departments retrieved successfully",
        "data": data
    }

@router.patch('/departments/restore/{department_id}')
def restore_department_by_id(department_id: int, db: Session = Depends(get_db)):
    data = restore_by_id_department_serv(db, department_id)
    return {
        "status": 200,
        "message": "Department restored successfully",
        "data": data
    }