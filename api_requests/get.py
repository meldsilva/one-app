import requests as api
import json
from api_requests.auth import get_auth_token
import os

base_url = os.environ.get('BASE_URL')


def get():
    print("START get.get()")

    response = api.get(url)

    # print(response.text)
   
    # print(json.dumps(response.text))
   
    with open("filename.json", "w") as write_file:
        json.dump(response.text, write_file, indent=4)


   
   
    # json_response = json.load(response)
    # s = json.dumps(json_response, indent=4)
    # # print(s)
    # print(json_response)

    print("END get.get()")


def get_playlists():
    # print("get_playlists")
    auth_token = get_auth_token()
    print(f"Auth token = {auth_token}")

    # print(base_url)

    # Call API for list of playlists
