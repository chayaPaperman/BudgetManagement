from pymongo import MongoClient

client = MongoClient("")
db = client['BudgetManagementDB']
users = db['users']
operations = db['operations']


