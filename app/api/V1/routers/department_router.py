from fastapi import APIRouter
from app.api.V1.endpoints.department_endpoint import router as department_router

api_router = APIRouter()
api_router.include_router(department_router, prefix="/departments",tags=["departments"])