from fastapi import FastAPI
from app.api.V1.routers.user_router import api_router as user_api_router
from app.api.V1.routers.department_router import api_router as department_api_router
from app.core.database import engine, Base
from app.models.user import User
from app.models.department import Department

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Frist_Step")
app.include_router(user_api_router, prefix="/api/V1")
app.include_router(department_api_router, prefix="/api/V1")