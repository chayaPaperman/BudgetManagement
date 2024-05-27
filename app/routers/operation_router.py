from fastapi import APIRouter, Request
from app.models.operation_model import Operation
import app.services.operation_service as operation_service
from utils.logger import log_request

operation_router = APIRouter()


@operation_router.get("/balance/{user_id}")
@log_request
async def get_balance(user_id, request: Request):
    return await operation_service.get_balance(user_id)


@operation_router.get("/revenues/{user_id}")
@log_request
async def get_all_revenues(user_id, request: Request):
    return await operation_service.get_all_user_revenues(user_id)


@operation_router.get("/spending/{user_id}")
@log_request
async def get_all_spending(user_id, request: Request):
    return await operation_service.get_all_user_spending(user_id)


@operation_router.post("/")
@log_request
async def add(operation: Operation, request: Request):
    return await operation_service.add_operation(operation)


@operation_router.put("/{operation_id}")
@log_request
async def update(operation_id, operation: Operation, request: Request):
    return await operation_service.update_operation(operation_id, operation)


@operation_router.delete("/{operation_id}")
@log_request
async def delete(operation_id, request: Request):
    return await operation_service.delete_operation(operation_id)
