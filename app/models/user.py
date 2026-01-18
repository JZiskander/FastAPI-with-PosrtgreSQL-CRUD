from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    #dep_id
    department_id = Column(Integer, ForeignKey('departments.id'))
    created_at = Column(DATE)
    updated_at = Column(DATE)
    deleted_at = Column(DATE)