import requests
import json

BASE_URL = "http://127.0.0.1:8000/user"

data = {
    "id": 0,
    "name": "chaya",
    "age": 20,
    "city": "modiinElit",
    "email": "fcsdc@dfh.com",
    "password": "12345678"
}


def test_signup():
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 200


def test_signup_small_age():
    data['age'] = 0
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422


def test_signup_wrong_email():
    data['age'] = 20
    data['email'] = "43545654"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422


def test_signup_wrong_password():
    data['email'] = "fcsdc@dfh.com"
    data['password'] = "123456789012"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422


def test_signup_wrong_name():
    data['password'] = "12345678"
    data['name'] = "ch"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422


def test_signup_exist_name():
    data['name'] = "chaya"
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 409


login_data = {
    "name": "chaya",
    "password": "12345678"
}


def test_login():
    response = requests.post(BASE_URL + "/login", data=json.dumps(login_data))
    assert response.json() == 0


def test_login_wrong_password():
    login_data['password'] = "123456789012"
    response = requests.post(BASE_URL + "/login", data=json.dumps(login_data))
    assert response.status_code == 404


def test_login_wrong_name():
    login_data['password'] = "12345678"
    login_data['name'] = "ch"
    response = requests.post(BASE_URL + "/login", data=json.dumps(login_data))
    assert response.status_code == 404


new_data = {
    "id": 0,
    "name": "chaya",
    "age": 20,
    "city": "modiinElit",
    "email": "fcsdc@dfhfgfh.com",
    "password": "12345678"
}


def test_update_details():
    userid = 0
    response = requests.put(BASE_URL + f"/{userid}", data=json.dumps(new_data))
    assert response.status_code == 200


def test_update_details_user_not_exist():
    userid = 100
    response = requests.put(BASE_URL + f"/{userid}", data=json.dumps(new_data))
    assert response.status_code == 404


def test_update_details_wrong_name():
    userid = 0
    new_data['name'] = "ch"
    response = requests.put(BASE_URL + f"/{userid}", data=json.dumps(new_data))
    assert response.status_code == 422


def test_get_all_users():
    response = requests.get(BASE_URL)
    assert response.json() == [{
        "id": 0,
        "name": "chaya",
        "age": 20,
        "city": "modiinElit",
        "email": "fcsdc@dfhfgfh.com",
        "password": "12345678"
    }]
