from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    city: str
    email: str
    password: str
