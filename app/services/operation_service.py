from fastapi import HTTPException

from app.db_management.config_db import operationsDB
from app.models.operation_model import Operation, OperationType
from app.services.user_service import is_exist


async def get_balance(user_id):
    """
    A function to get the account balance of the user
    :param user_id: the id of the user
    :return: the balance amount of the user
    """
    if not await is_exist(user_id):
        raise HTTPException(status_code=404, detail="the user is not exist")
    sum_revenues = sum(r['amount'] for r in await get_all_user_revenues(user_id))
    sum_spending = sum(r['amount'] for r in await get_all_user_spending(user_id))
    return sum_revenues - sum_spending


async def get_all_user_revenues(user_id):
    """
    A function to get all the user's revenues
    :param user_id: the id of the user
    :return: a list of all the user's revenues
    """
    if not await is_exist(user_id):
        raise HTTPException(status_code=404, detail="the user is not exist")
    revenues = list(operationsDB.find({'user_id': int(user_id), 'type': OperationType.REVENUE}))
    [r.pop('_id') for r in revenues]
    return revenues


async def get_all_user_spending(user_id):
    """
    A function to get all the user's spending
    :param user_id: the id of the user
    :return: a list of all the user's spending
    """
    if not await is_exist(user_id):
        raise HTTPException(status_code=404, detail="the user is not exist")
    spending = list(operationsDB.find({'user_id': int(user_id), 'type': OperationType.SPENDING}))
    [s.pop('_id') for s in spending]
    return spending


async def add_operation(operation: Operation):
    """
     A function to add new operation - revenue or spending - to the operations collection in the database
    :param operation: an operation to insert
    :return: the new operation when the add was successful
    """
    if not await is_exist(operation.user_id):
        raise HTTPException(status_code=404, detail="the user is not exist")
    operations = list(operationsDB.find())
    if len(operations) == 0:
        operation.id = 0
    else:
        operation.id = int(operations[len(operations) - 1]['id']) + 1
    operationsDB.insert_one(operation.__dict__)
    return operation


async def update_operation(operation_id, operation: Operation):
    """
    A function to edit operation information
    :param operation_id: the id of operation
    :param operation: the new details of the operation
    :return: the updated operation
    """
    if operationsDB.find_one({"id": int(operation_id)}) is None:
        raise HTTPException(status_code=404, detail="the operation is not exist")
    operationsDB.update_one({"id": int(operation_id)},
                            {"$set": {"description": operation.description, "amount": operation.amount}})
    return "Editing of the description and amount was done successfully "


async def delete_operation(operation_id):
    """
    A function to delete operation from the operations collection in the database
    :param operation_id:the id of operation
    :return: message if the deletion was successful
    """
    if operationsDB.find_one({"id": int(operation_id)}) is None:
        raise HTTPException(status_code=404, detail="the operation is not exist")
    operationsDB.delete_one({"id": int(operation_id)})
    return "Delete operation" + operation_id + "passed successfully"
