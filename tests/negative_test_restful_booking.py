from api.restful_booker_requests import (get_booking_ids,get_booking,create_booking,
                                         update_booking,partial_update_booking,delete_booking)


def test_negative_get_booking(api_session, base_url):
    invalid_booking_id = 6000
    response = get_booking(api_session, base_url, invalid_booking_id)
    assert response.status_code == 404, "Expected 404 for non-existent booking ID"



def test_create_booking_missing_firstname_and_lastname(api_session, base_url, headers_params, request_body):
    """
    KNOWN ISSUE:
    API returns 500 Internal Server Error when mandatory fields
    (firstname, lastname) are missing.
    Expected behavior: 400 Bad Request.
    """
    new_body = request_body.copy()
    del new_body["firstname"]
    del new_body["lastname"]
    response = create_booking(api_session, base_url, headers_params, new_body)
    assert response.status_code == 500  # BUG: should be 400


