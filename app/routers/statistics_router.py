from fastapi import APIRouter
from app.services import statistics_service

statistics_router = APIRouter()


@statistics_router.get("/users_balance")
async def balance_statistics():
    return await statistics_service.get_users_balance()

