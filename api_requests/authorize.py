import base64
from urllib.parse import urlencode
import webbrowser
import requests
import os

# URLS
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

def get_user_authorization_code():

    

    # Make a request to the /authorize endpoint to get an authorization code
    auth_code = requests.get(AUTH_URL, {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': 'http://localhost:8000/callback/',
        'scope': 'playlist-modify-private',
    })
    print("Auth code is {}".format(auth_code.text))

    r = webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    # # # # auth_header = base64.urlsafe_b64encode((client_id + ':' + client_secret).encode('ascii'))
    # auth_header = base64.urlsafe_b64encode((client_id + ':' + client_secret).encode())


    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Authorization': 'Basic %s' % auth_header.decode('ascii')
    # }

    # payload = {
    #     'grant_type': 'authorization_code',
    #     'code': auth_code,
    #     'redirect_uri': 'http://localhost:8000/callback/'
    # }

    # # # # # Make a request to the /token endpoint to get an access token
    # access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)
    # print("Access token request {}".format(access_token_request.text))

    # # # # convert the response to JSON
    # # # access_token_response_data = access_token_request.json()

    # # # print(access_token_response_data)

    # # # # save the access token
    # # # access_token = access_token_response_data['access_token']
    # # # print(access_token)
