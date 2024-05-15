from app.db_management.config_db import operationsDB
from app.models.operation_model import Operation, OperationType


async def get_balance(user_id):
    """
    A function to get the account balance of the user
    :param user_id: the id of the user
    :return: the balance amount of the user
    """


async def get_all_user_revenues(user_id):
    """
    A function to get all the user's revenues
    :param user_id: the id of the user
    :return: a list of all the user's revenues
    """
    revenues = list(operationsDB.find({'user_id': int(user_id), 'type': OperationType.REVENUE}))
    for r in revenues:
        r.pop('_id')
    return revenues


async def get_all_user_spending(user_id):
    """
    A function to get all the user's spending
    :param user_id: the id of the user
    :return: a list of all the user's spending
    """
    spending = list(operationsDB.find({'user_id': int(user_id), 'type': OperationType.SPENDING}))
    for r in spending:
        r.pop('_id')
    return spending


async def add_operation(operation: Operation):
    """
     A function to add new operation - revenue or spending - to the operations collection in the database
    :param operation: an operation to insert
    :return: the new operation when the add was successful
    """
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


async def delete_operation(operation_id):
    """
    A function to delete operation from the operations collection in the database
    :param operation_id:the id of operation
    :return: message if the deletion was successful
    """
