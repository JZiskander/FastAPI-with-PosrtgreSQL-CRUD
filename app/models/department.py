from sqlalchemy import Column, Integer, String, Date, DATE
from sqlalchemy.orm import relationship

from app.core.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    created_at = Column(DATE)
    updated_at = Column(DATE)
    deleted_at = Column(DATE)