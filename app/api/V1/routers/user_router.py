from fastapi import APIRouter
from app.api.V1.endpoints.user_endpoint import router as user_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users",tags=["users"])