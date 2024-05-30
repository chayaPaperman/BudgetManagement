from fastapi import APIRouter, Request
from app.services import statistics_service
from app.utils.logger import log_request

statistics_router = APIRouter()


@statistics_router.get("/balance")
@log_request
async def get_users_balance(request: Request):
    return await statistics_service.get_users_balance()


@statistics_router.get("/balance/{user_id}")
@log_request
async def get_user_balance(user_id, request: Request):
    return await statistics_service.get_user_balance(user_id)
