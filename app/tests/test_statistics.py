import requests

BASE_URL = "http://127.0.0.1:8000/statistics"


def test_users_balance():
    response = requests.get(BASE_URL + "/balance")
    assert response.status_code == 200


def test_user_balance(user_id):
    response = requests.get(BASE_URL + f"/balance/{user_id}")
    assert response.status_code == 200
