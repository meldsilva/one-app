import requests
import os
import json

auth_url = 'https://accounts.spotify.com/api/token'
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')


data = {
    'grant_type': 'client_credentials',
    'client_id':client_id,
    'client_secret': client_secret,
}

def get_auth_token():

    auth_response = requests.post(auth_url, data=data)
    response_dict = json.loads(auth_response.text)

    for key, value in response_dict.items():
        if key == "access_token":
            # print(f"{key}: {value}")
            return value
            # print(value)
            


def is_token_valid(token):
    pass
