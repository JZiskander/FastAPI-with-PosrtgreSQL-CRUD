from typing import List

from sqlalchemy.orm import Session

from app.models import department
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentBase
from datetime import datetime

def creat_department(db: Session, department_in: DepartmentCreate) -> Department:
    db_department = Department(**department_in.dict())
    db_department.created_at = datetime.now()
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def update_department(db: Session, department_in: DepartmentUpdate, id:int):
    db_department = db.query(Department).filter(Department.id == id, Department.deleted_at.is_(None)).first()
    if db_department:
        if department_in.name != None :
            db_department.name = department_in.name
        if department_in.description != None :
            db_department.description = department_in.description
        db_department.updated_at = datetime.now()
        db.commit()
        db.refresh(db_department)
    return db_department


def soft_delete_department(db: Session, Id: int) :
    db_department = db.query(Department).filter(Department.id == Id, Department.deleted_at.is_(None)).first()
    if db_department:
        db_department.deleted_at = datetime.now()
        db.commit()
        db.refresh(db_department)
    return db_department

def hard_delete_department(db: Session, Id: int):
    db_department = db.query(Department).filter(Department.id == Id, Department.deleted_at.is_not(None)).first()
    if db_department:
        db.delete(db_department)
        db.commit()
        db.refresh(db_department)
    return db_department

def get_all(db: Session):
    return db.query(Department).filter(Department.deleted_at.is_(None)).all()

def get_by_id(db: Session, id: int) :
    return db.query(Department).filter(Department.id == id, Department.deleted_at.is_(None)).first()

def get_all_SoftDeleted(db : Session) :
    return db.query(Department).filter(Department.deleted_at.is_not(None)).all()

def get_by_id_SoftDeleted(db: Session, Id: int):
    return db.query(Department).filter(Department.id == Id, Department.deleted_at.is_not(None)).first()

def restore_all(db: Session) :
    departments = db.query(Department).filter(Department.deleted_at.is_not(None)).all()
    if departments:
        for department in departments:
            department.deleted_at = None
            department.updated_at = datetime.now()
            db.commit()
            db.refresh(department)
    return departments

def restore_by_id(db: Session, id: int) :
    db_department = db.query(Department).filter(Department.id == id, Department.deleted_at.is_not(None)).first()
    if db_department:
        db_department.deleted_at = None
        db_department.updated_at = datetime.now()
        db.commit()
        db.refresh(db_department)
    return db_department