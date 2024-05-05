from pydantic import BaseModel
from enum import Enum

OperationType = Enum('OperationType', ['REVENUE', 'SPENDING'])


class Operation(BaseModel):
    type: OperationType
    description: str
    count: int
    date: str
