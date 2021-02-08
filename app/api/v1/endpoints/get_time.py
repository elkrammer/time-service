from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app.core.time_utils import get_time
from app.schemas.time import Time
from typing import Any

router = APIRouter()

# returns current timestamp
@router.get("/", response_model=schemas.Time)
async def get_current_time() -> Any:
    return {"message": "Automate all the things!", "timestamp": get_time()}


@router.get("/demo", response_model=schemas.Time)
async def get_current_time() -> Any:
    return {"message": "Demo Time!", "timestamp": get_time()}
