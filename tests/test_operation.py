import requests
import json

BASE_URL = "http://127.0.0.1:8000/operation"


def test_add_operation():
    data = {
        "id": 0,
        "type": 1,
        "description": "salary from balance",
        "amount": 20000,
        "date": "15/05/2024",
        "user_id": 0
    }
    response = requests.post(BASE_URL, data=json.dumps(data))
    assert response.status_code == 200
    data['user_id'] = 100
    response = requests.post(BASE_URL , data=json.dumps(data))
    assert response.status_code == 404
    data['user_id'] = 0
    data['amount'] = -20
    response = requests.post(BASE_URL , data=json.dumps(data))
    assert response.status_code == 422
    data['amount'] = 2000
    data['type'] = 8
    response = requests.post(BASE_URL, data=json.dumps(data))
    assert response.status_code == 422


def test_update_operation():
    operation_id = 0
    data = {
        "id": 0,
        "type": 1,
        "description": "salary from balance plus bonus",
        "amount": 30000,
        "date": "15/05/2024",
        "user_id": 0
    }
    response = requests.put(BASE_URL + f"/{operation_id}", data=json.dumps(data))
    assert response.status_code == 200
    operation_id = 100
    response = requests.put(BASE_URL + f"/{operation_id}", data=json.dumps(data))
    assert response.status_code == 404
    operation_id = 0
    data['amount'] = -20
    response = requests.put(BASE_URL + f"/{operation_id}", data=json.dumps(data))
    assert response.status_code == 422


def test_get_balance():
    user_id = 0
    response = requests.get(BASE_URL + f"/balance/{user_id}")
    assert response.json() == 30000
    assert response.status_code == 200
    user_id = 100
    response = requests.get(BASE_URL + f"/balance/{user_id}")
    assert response.status_code == 404


def test_get_all_user_spending():
    user_id = 0
    response = requests.get(BASE_URL + f"/spending/{user_id}")
    assert response.status_code == 200
    assert response.json() == []
    user_id = 100
    response = requests.get(BASE_URL + f"/spending/{user_id}")
    assert response.status_code == 404


def test_get_all_user_revenues():
    user_id = 0
    response = requests.get(BASE_URL + f"/revenues/{user_id}")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 0,
            "type": 1,
            "description": "salary from balance plus bonus",
            "amount": 30000,
            "date": "15/05/2024",
            "user_id": 0
        }
    ]
    user_id = 100
    response = requests.get(BASE_URL + f"/revenues/{user_id}")
    assert response.status_code == 404


def test_delete_operation():
    operation_id = 0
    response = requests.delete(BASE_URL + f"/{operation_id}")
    assert response.status_code == 200
    operation_id = 100
    response = requests.delete(BASE_URL + f"/{operation_id}")
    assert response.status_code == 404
