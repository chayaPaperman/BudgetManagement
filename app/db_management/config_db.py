from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1")
db = client['BudgetManagementDB']
usersDB = db['users']
operationsDB = db['operations']
