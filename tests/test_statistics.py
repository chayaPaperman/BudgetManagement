import requests

BASE_URL = "http://127.0.0.1:8000/statistics"


def test_users_balance():
    response = requests.get(BASE_URL + "/users_balance")
    assert response.status_code == 200
