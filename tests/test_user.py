import app.services.user_service as user_service
from app.models.user_model import User


def test_signup():
    assert user_service.signup(User(**{"id": 0, "name": "", "age": "", "city": "", "email": "", "password": ""}))!=1
