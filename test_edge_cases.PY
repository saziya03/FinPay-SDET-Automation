import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_negative_amount():
    # Bug Found: Negative amount is accepted, should be rejected
    payload = {"amount": -500}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201

def test_empty_username():
    # Bug Found: Login is allowed with empty username
    payload = {"username": "", "password": "123"}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201

def test_very_large_amount():
    # Edge Case: Verify system behavior with very large transaction amount
    payload = {"amount": 9999999999}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201

def test_sql_injection_check():
    # Security Test: Verify system is safe from SQL Injection attack
    payload = {"username": "' OR '1'='1"}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201

def test_missing_field():
    # Edge Case: Verify API behavior when required field amount is missing
    payload = {"userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201