from pydantic import BaseModel, conint, constr, ValidationError


class User(BaseModel):
    id: int
    name: constr(min_length=3, max_length=15)
    age: conint(gt=0)
    city: str
    email: constr(pattern=r'^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$')
    password: constr(min_length=6, max_length=10)
