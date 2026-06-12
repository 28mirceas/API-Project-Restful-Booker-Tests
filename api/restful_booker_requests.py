import requests


def get_booking_ids(session, base_url):
    endpoint = f"{base_url}/booking"
    response = session.get(endpoint)
    return response


def get_booking(session, base_url, booking_id):
    endpoint = f"{base_url}/booking/" + f"{booking_id}"
    response = session.get(endpoint)
    return response


def create_booking(session, base_url, headers_params, request_body):
    endpoint = f"{base_url}/booking"
    response = session.post(endpoint, headers=headers_params, json=request_body)
    return response


def update_booking(session, base_url, booking_id, headers_params, request_body):
    endpoint = f"{base_url}/booking/" + f"{booking_id}"
    response = session.put(endpoint, headers=headers_params, json=request_body)
    return response


def partial_update_booking(session, base_url, booking_id, headers_params, request_body):
    endpoint = f"{base_url}/booking/" + f"{booking_id}"
    response = session.patch(endpoint, headers=headers_params, json=request_body)
    return response


def delete_booking(session, base_url, headers_params, booking_id):
    endpoint = f"{base_url}/booking/" + f"{booking_id}"
    response = session.delete(endpoint, headers=headers_params)
    return response
