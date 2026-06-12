# Restful Booker API – Automated Testing (Python)
![API Tests](https://github.com/28mirceas/Proiect-Restful-Booker-API-Tests/actions/workflows/api_tests.yml/badge.svg)
## Project Overview
This project contains automated API tests for the Restful Booker application (public demo API).
The tests are implemented in Python, using Pytest and Requests, and cover positive, negative, and edge case scenarios.

The goal of this project is to demonstrate:
- API Automation Testing skills
- Clear and maintainable project structure
- Token-based authentication handling
- Negative testing and real defect identification
- QA best practices

---

## Technologies Used
- Python 3
- Pytest
- Requests
- Pytest Fixtures
- REST API Testing
- Postman
- GitHub Actions
- HTML Reporting (pytest-html)


---

## Tested API
- **Base URL:** `https://restful-booker.herokuapp.com`

---

## Project Structure
```
Proiect-Restful-Booker-API-Tests/
│
├── api/
│   ├── create_token.py
│   └── restful_booker_requests.py
│
├── tests/
│   └── test_restful_booking.py
│
├── utils/
│   └── logger.py
│
├── config.py
├── conftest.py
├── requirements.txt
├── README.md
└── test.log

```

---
## Framework Features

- Pytest Fixtures
- Session Management using requests.Session()
- Centralized Configuration (config.py)
- Authentication Token Fixture
- Logging using Python logging module
- Positive and Negative API Tests

## Session Management

The framework uses a shared requests.Session()
fixture to reuse HTTP connections between API calls,
improving efficiency and reflecting real-world
automation framework practices.

## Logging

The framework uses Python logging to record:

- API actions
- Response status codes
- Created Booking IDs

Logs are stored in:

test.log


## Reporting

Generate HTML report:
```bash
pytest tests/test_restful_booking.py -v --html=restful_booker_report.html --self-contained-html
```

## Continuous Integration

The project uses GitHub Actions to automatically:

- Install project dependencies
- Execute automated API tests
- Generate test execution reports
- Validate code on every push and pull request



## Authentication
Authentication is performed using the endpoint:
```
POST /auth
```

The token is:
- generated once per session using a Pytest fixture
- sent in requests via header:
```
Cookie: token=<auth_token>
```

---

## Test Coverage

### Positive Tests
- Retrieve booking IDs list
- Create booking
- Retrieve booking by ID
- Update booking (PUT)
- Partial update booking (PATCH)
- Delete booking (DELETE)

### Negative Tests
- Get booking with non-existing ID → 404
- Create booking with empty body → BUG (500 instead of 400)

---

## Identified Defects (Known Issues)

| Scenario | Actual Response | Expected Response |
|--------|---------------|-----------------|
| Create booking with empty body | 500 Internal Server Error | 400 Bad Request |


---

## ▶Test Execution

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest -v
```

---

## Postman Collection
Included file:
```
Restful_Booker.postman_collection.json
```
---

## Author
**QA Tester**
