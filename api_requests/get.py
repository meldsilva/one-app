import base64
import requests as api
import json
from api_requests.auth import get_auth_token
import os

base_url = os.environ.get('BASE_URL')
user_authorization_code = "AQBS-OlqT05FfxuZSyhP90EnDWDr1c5i30Jht_FdgOWN5qrre2Yxl0-dBboLcJyXWWc-g_K9uT_lat0xYnQeMfaT_mfKw8X47qb9lshRrgqy2S3wCfZaoaunVVSL4oM1d62e6XmVGTKeBuvfCc0mRFJHqjsfUpHb6s476gtM3SrrK_ql98HoL_jHMc-tNYbsRJbuSIV3"
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

def get_playlists():
    auth_token = get_auth_token()
    # print(f"Auth token = {auth_token}")
    encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": user_authorization_code,
        "redirect_uri": "http://localhost:3000/callback/"
    }

    r = api.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers) 
    # token = json.loads(r.text)
    print(r)
    # print(token)

    