from api.restful_booker_requests import (get_booking_ids,get_booking,create_booking,
                                         update_booking,partial_update_booking,delete_booking)
from utils.logger import logger


def test_get_booking_ids(api_session, base_url):
    response = get_booking_ids(api_session, base_url)
    assert response.status_code == 200, "Unexpected status code"



def test_create_booking(api_session, base_url, headers_params, request_body):
    logger.info("Creating booking")
    response = create_booking(api_session, base_url, headers_params, request_body)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200, "Unexpected status code"
    assert "bookingid" in response.json()
    booking_id = response.json()["bookingid"]
    logger.info(f"Booking ID created: {booking_id}")



def test_get_booking(api_session, base_url, request_body, headers_params):
    create_response = create_booking(api_session, base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]
    logger.info(f"Getting booking with id {booking_id}")
    response = get_booking(api_session, base_url, booking_id)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jim"



def test_update_booking(api_session, base_url, headers_params, request_body):
    create_response = create_booking(api_session, base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]

    updated_body = request_body.copy()
    updated_body["firstname"] = "John"
    updated_body["lastname"] = "Doe"
    updated_body["totalprice"] = 200

    logger.info(f"Updating booking {booking_id}")
    response = update_booking(api_session, base_url, booking_id, headers_params, updated_body)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    logger.info(f"Firstname changed to {response.json()['firstname']}")
    assert response.json()["firstname"] == "John"



def test_partial_update_booking(api_session, base_url, headers_params, request_body):
    create_response = create_booking(api_session, base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]

    logger.info(f"Partially updating booking {booking_id}")
    response = partial_update_booking(api_session, base_url, booking_id, headers_params, {"firstname": "Dan"})
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200

    assert response.json()["firstname"] == "Dan"



def test_delete_booking(api_session, base_url, headers_params, request_body):
    create_response = create_booking(api_session, base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]

    logger.info(f"Deleting booking {booking_id}")
    response = delete_booking(api_session, base_url, headers_params, booking_id)
    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 201

