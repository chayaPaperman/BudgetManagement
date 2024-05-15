import requests
import json

BASE_URL = "http://127.0.0.1:8000/user"


def test_signup():
    data = {
        "id": 0,
        "name": "chaya",
        "age": 20,
        "city": "modiinElit",
        "email": "fcsdc@dfh.com",
        "password": "12345678"
    }
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 200
    data['age'] = 0
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data['age'] = 20
    data['email'] = "43545654"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data['email'] = "fcsdc@dfh.com"
    data['password'] = "123456789012"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data['password'] = "12345678"
    data['name'] = "ch"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data['name'] = "chaya"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 409


def test_login():
    data = {
        "name": "chaya",
        "password": "12345678"
    }
    response = requests.post(BASE_URL + "/login", data=json.dumps(data))
    assert response.json() == 0
    data['password'] = "123456789012"
    response = requests.post(BASE_URL + "/login", data=json.dumps(data))
    assert response.status_code == 404
    data['password'] = "12345678"
    data['name'] = "ch"
    response = requests.post(BASE_URL + "/login", data=json.dumps(data))
    assert response.status_code == 404


def test_update_details():
    userid = 0
    data = {
        "id": 0,
        "name": "chaya",
        "age": 20,
        "city": "modiinElit",
        "email": "fcsdc@dfhfgfh.com",
        "password": "12345678"
    }
    response = requests.put(BASE_URL + f"/update_details/{userid}", data=json.dumps(data))
    assert response.status_code == 200
    userid = 100
    response = requests.put(BASE_URL + f"/update_details/{userid}", data=json.dumps(data))
    assert response.status_code == 404
    userid = 0
    data['name'] = "ch"
    response = requests.put(BASE_URL + f"/update_details/{userid}", data=json.dumps(data))
    assert response.status_code == 422
