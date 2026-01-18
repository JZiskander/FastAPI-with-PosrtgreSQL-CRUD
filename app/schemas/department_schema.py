from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    name: str
    description: str

class DepartmentCreate(DepartmentBase):
    name: str
    description: str

class DepartmentUpdate(DepartmentBase):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes= True

class DepartmentDelete(DepartmentBase):
    pass
