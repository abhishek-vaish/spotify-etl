import requests


class SpotifyAPI:
    __BASE_URL = "https://api.spotify.com/v1/"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self):
        uri = "https://accounts.spotify.com/api/token"
        response = requests.post(uri, data={"grant_type": "client_credentials",
                                            "client_id": self.client_id,
                                            "client_secret": self.client_secret
                                            }, headers={
            "Content-Type": "application/x-www-form-urlencoded"
        })
        return response.json()['access_token']

    def get_api_response(self, endpoints, access_token, key=None):
        uri = self.__BASE_URL + f"{endpoints}" + f"/{key}" if key \
            else self.__BASE_URL + f"{endpoints}"
        try:
            response = requests.get(uri, headers={"Authorization": f"Bearer {access_token}"})
            if response.status_code == 200:
                return response.json()
            else:
                raise requests.RequestException
        except requests.ConnectionError:
            raise requests.ConnectionError
