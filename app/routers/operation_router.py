from fastapi import APIRouter
from app.models.operation_model import Operation
import app.services.operation_service as operation_service

operation_router = APIRouter()


@operation_router.get("/getBalance/{user_id}")
async def get_balance(user_id):
    return await operation_service.get_balance(user_id)


@operation_router.get("/getAllRevenues/{user_id}")
async def get_all_revenues(user_id):
    return await operation_service.get_all_user_revenues(user_id)


@operation_router.get("/getAllSpending/{user_id}")
async def get_all_spending(user_id):
    return await operation_service.get_all_user_spending(user_id)


@operation_router.post("/add")
async def add(operation: Operation):
    return await operation_service.add_operation(operation)


@operation_router.put("/update/{operation_id}")
async def update(operation_id, operation: Operation):
    return await operation_service.update_operation(operation_id, operation)


@operation_router.delete("/delete/{operation_id}")
async def delete(operation_id):
    return await operation_service.delete_operation(operation_id)
