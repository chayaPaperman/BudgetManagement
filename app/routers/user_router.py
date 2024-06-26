from fastapi import APIRouter, Request
import app.services.user_service as user_service
from app.models.user_model import User
from app.models.user_details_model import UserDetails
from app.utils.logger import log_request

user_router = APIRouter()


@user_router.get("/")
@log_request
async def get_all_users(request: Request):
    return await user_service.get_all_users()


@user_router.post("/signup")
@log_request
async def signup(user: User, request: Request):
    return await user_service.signup(user)


@user_router.post("/login")
@log_request
async def login(details: UserDetails, request: Request):
    return await user_service.login(details)


@user_router.put("/{user_id}")
@log_request
async def update_details(user_id, user: User, request: Request):
    return await user_service.update_details(user_id, user)
