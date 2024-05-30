import requests
import json

BASE_URL = "http://127.0.0.1:8000/operation"

data = {
    "id": 0,
    "type": 1,
    "description": "salary from balance",
    "amount": 20000,
    "date": "2024-08-24",
    "user_id": 0
}


def test_add_operation():
    response = requests.post(BASE_URL, data=json.dumps(data))
    assert response.status_code == 200


def test_add_operation_user_not_exist():
    data['user_id'] = 100
    response = requests.post(BASE_URL, data=json.dumps(data))
    assert response.status_code == 404


def test_add_operation_wrong_type():
    data['amount'] = 2000
    data['type'] = 8
    response = requests.post(BASE_URL, data=json.dumps(data))
    assert response.status_code == 422


def test_add_operation_amount_less_then_0():
    data['user_id'] = 0
    data['amount'] = -20
    response = requests.post(BASE_URL, data=json.dumps(data))
    assert response.status_code == 422


new_data = {
    "id": 0,
    "type": 1,
    "description": "salary from balance plus bonus",
    "amount": 30000,
    "date": "2024-05-15",
    "user_id": 0
}


def test_update_operation():
    operation_id = 0
    response = requests.put(BASE_URL + f"/{operation_id}", data=json.dumps(new_data))
    assert response.status_code == 200


def test_update_operation_id_not_exist():
    operation_id = 100
    response = requests.put(BASE_URL + f"/{operation_id}", data=json.dumps(new_data))
    assert response.status_code == 404


def test_update_operation_amount_less_then_0():
    operation_id = 0
    new_data['amount'] = -20
    response = requests.put(BASE_URL + f"/{operation_id}", data=json.dumps(new_data))
    assert response.status_code == 422


def test_get_balance():
    user_id = 0
    response = requests.get(BASE_URL + f"/balance/{user_id}")
    assert response.json() == 30000 and response.status_code == 200


def test_get_balance_user_not_exist():
    user_id = 100
    response = requests.get(BASE_URL + f"/balance/{user_id}")
    assert response.status_code == 404


def test_get_all_user_spending():
    user_id = 0
    response = requests.get(BASE_URL + f"/spending/{user_id}")
    assert response.status_code == 200 and response.json() == []


def test_get_all_user_spending_user_not_exist():
    user_id = 100
    response = requests.get(BASE_URL + f"/spending/{user_id}")
    assert response.status_code == 404


def test_get_all_user_revenues():
    user_id = 0
    response = requests.get(BASE_URL + f"/revenues/{user_id}")
    assert response.json() == [
        {
            "id": 0,
            "type": 1,
            "description": "salary from balance plus bonus",
            "amount": 30000,
            "date": "2024-08-24",
            "user_id": 0
        }
    ]


def test_get_all_user_revenues_user_not_exist():
    user_id = 100
    response = requests.get(BASE_URL + f"/revenues/{user_id}")
    assert response.status_code == 404


def test_delete_operation():
    operation_id = 0
    response = requests.delete(BASE_URL + f"/{operation_id}")
    assert response.status_code == 200


def test_delete_operation_user_not_exist():
    operation_id = 100
    response = requests.delete(BASE_URL + f"/{operation_id}")
    assert response.status_code == 404
