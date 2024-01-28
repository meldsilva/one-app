# from api-requests import Get
from api_requests import get as g
from api_requests import authorize as authr


def main():
    # print("*** Running app.py ***")
    # g.get_playlists()
    authr.get_user_authorization_code()

    
    

if __name__ == "__main__":
    main()