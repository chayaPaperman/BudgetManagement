from fastapi import APIRouter
import app.services.user_service as user_service
from app.models.user_model import User
from app.models.userDetails_model import UserDetails

user_router = APIRouter()


@user_router.post("/signup")
async def signup(user: User):
    return user_service.signup(user)


@user_router.post("/login")
async def login\
                (details: UserDetails):
    return user_service.login(details)


@user_router.put("/update_details")
async def update_details(user: User):
    return user_service.update_details(user)
