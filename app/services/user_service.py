from app.db_management.config_db import usersDB
from app.models.user_model import User
from app.models.user_details_model import UserDetails
from fastapi import HTTPException


async def signup(user: User):
    """
    A function to add new user to the users collection in the database
    :param user: a user to insert
    :return:the new user when the add was successful
    """
    if usersDB.find_one({"name": user.name, "password": user.password}) is not None:
        raise HTTPException(status_code=409, detail="the user is  exist")
    users = list(usersDB.find())
    if len(users) == 0:
        user.id = 0
    else:
        user.id = int(users[len(users) - 1]['id']) + 1
    usersDB.insert_one(user.__dict__)
    return user


async def login(user_details: UserDetails):
    """
    A function to check if the user who wants to connect exists according to the received details
    :param user_details: the username and his password
    :return:the user id if the user exist
    """
    user = usersDB.find_one(user_details.__dict__)
    if user is None:
        raise HTTPException(status_code=404, detail="the user is not exist")
    return user['id']


async def update_details(user_id, user: User):
    """
    A function to edit user information
    :param user_id:the id of the user
    :param user:the new details of the user
    :return:the updated user
    """
    if not await is_exist(user_id):
        raise HTTPException(status_code=404, detail="the user is not exist")
    user.id = int(user_id)
    usersDB.update_one({"id": int(user_id)}, {"$set": user.__dict__})
    return user


async def is_exist(user_id):
    """
    A function to check if user is existed
    :param user_id: the id of the user
    :return:True if existed, False if not
    """
    if usersDB.find_one({"id": int(user_id)}) is None:
        return False
    return True


async def get_all_users():
    """
    A function to get all the users
    :return: a list of all the users
    """
    users = list(usersDB.find())
    [u.pop('_id') for u in users]
    return users
