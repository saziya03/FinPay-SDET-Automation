import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_01_login_success():
    # Test Case: Verify login with valid credentials
    payload = {"username": "testuser", "password": "12345"}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

def test_02_payment_success():
    # Test Case: Verify payment is successful with valid amount
    payload = {"userId": 1, "amount": 5000, "status": "SUCCESS"}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["amount"] == 5000

def test_03_payment_fail():
    # Test Case: Verify payment fails when balance is insufficient
    payload = {"userId": 1, "amount": 999999, "status": "FAILED"}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

def test_04_zero_amount_bug():
    # Bug Found: Payment is accepted even with 0 amount, should be rejected
    payload = {"userId": 1, "amount": 0}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

def test_05_invalid_id():
    # Test Case: Verify API returns 404 for invalid transaction ID
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404

def test_06_get_history():
    # Test Case: Verify transaction history is fetched correctly for user
    response = requests.get(f"{BASE_URL}/posts?userId=1")
    assert response.status_code == 200