# from api-requests import Get
from api_requests import get as g
from api_requests import authorize as authr


def main():
    # print("*** Running app.py ***")
    # Use get_user_authorization_code to obtain auth code in browser window
    # authr.get_user_authorization_code()
    g.get_playlists()

if __name__ == "__main__":
    main()