from fastapi import APIRouter
from app.api.v1.endpoints import get_time

api_router = APIRouter()
api_router.include_router(get_time.router, prefix="/time", tags=["get_time"])
