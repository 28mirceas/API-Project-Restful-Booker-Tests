import pytest
import requests
from api.create_token import create_token
from config import BASE_URL


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def auth_token():
    return create_token()


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture
def headers_params(auth_token):
    return {
        "Cookie": f"token={auth_token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def request_body():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        },
        "additionalneeds": "Breakfast"
    }