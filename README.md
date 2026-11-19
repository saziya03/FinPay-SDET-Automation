# FinPay – SDET API Automation Testing

## Project Overview

FinPay SDET API Automation is a Python-based API testing project designed to practice software testing concepts for a fintech payment application.

The project uses **Pytest and Python Requests** to test API operations, validate HTTP responses, and explore positive, negative, and edge-case scenarios.

## Tech Stack

- Python
- Pytest
- Requests Library
- REST API
- JSON
- Postman (API testing practice)

## Project Structure

```text
FinPay-SDET-Automation/
│
├── test_finpay.py
├── test_edge_cases.py
└── README.md
```

## Test Scenarios

### 1. Functional API Testing

- Login API testing with sample credentials
- Successful payment request
- Failed payment scenario
- Invalid transaction ID
- Transaction history retrieval
- HTTP status code validation
- JSON response validation

### 2. Negative & Edge Case Testing

- Zero payment amount
- Negative payment amount
- Empty username
- Very large transaction amount
- SQL injection input
- Missing required fields

## Installation

Clone the repository:

```bash
git clone https://github.com/saziya03/FinPay-SDET-Automation.git
```

Navigate to the project:

```bash
cd FinPay-SDET-Automation
```

Install dependencies:

```bash
pip install pytest requests
```

## Run Automation Tests

Run all tests:

```bash
pytest -v
```

Run functional tests:

```bash
pytest -v test_finpay.py
```

Run edge-case tests:

```bash
pytest -v test_edge_cases.py
```

## Learning Outcomes

- Understanding REST API testing
- Writing automated test cases using Pytest
- Sending GET and POST requests
- Validating HTTP status codes
- Working with JSON responses
- Understanding negative and boundary testing
- Exploring basic API security test scenarios

## Important Note

This is a learning and practice project using the JSONPlaceholder testing API. It does not connect to a real banking or payment gateway.

## Author

**Saziya Alvi**

GitHub: https://github.com/saziya03
