import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def test_signup():
    data = {
        "id": 0,
        "name": "chaya",
        "age": 20,
        "city": "modiinElit",
        "email": "fcsdc@dfh.com",
        "password": "12345678"
    }
    response = requests.post(BASE_URL+"/user/signup", data=json.dumps(data))
    status_response = response.status_code
    assert status_response == 200
    data['age'] = 0
    response = requests.post(BASE_URL+"/user/signup", data=json.dumps(data))
    status_response = response.status_code
    assert status_response == 422
    data['age'] = 20
    data['email'] = "43545654"
    response = requests.post(BASE_URL+"/user/signup", data=json.dumps(data))
    status_response = response.status_code
    assert status_response == 422
    data['email'] = "fcsdc@dfh.com"
    data['password'] = "123456789012"
    response = requests.post(BASE_URL+"/user/signup", data=json.dumps(data))
    status_response = response.status_code
    assert status_response == 422
    data['password'] = "12345678"
    data['name'] = "ch"
    response = requests.post(BASE_URL+"/user/signup", data=json.dumps(data))
    status_response = response.status_code
    assert status_response == 422
    data['name'] = "chaya"
    response = requests.post(BASE_URL+"/user/signup", data=json.dumps(data))
    status_response = response.status_code
    assert status_response == 409
