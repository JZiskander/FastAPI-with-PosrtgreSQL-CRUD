from typing import Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    department_id: int

class UserCreate(UserBase):
    first_name: str
    last_name: str
    email: EmailStr
    department_id: int

class UserUpdate(UserBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    department_id: Optional[int] = None
    class Config:
        from_attributes = True