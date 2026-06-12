import requests
from config import BASE_URL, USERNAME, PASSWORD

BASE_URL = "https://restful-booker.herokuapp.com"

def create_token():
    endpoint = f"{BASE_URL}/auth"
    request_body = {
                     "username" : USERNAME,
                     "password" : PASSWORD
                    }

    response = requests.post(endpoint, json=request_body) 
    token = response.json()['token']
    return token

