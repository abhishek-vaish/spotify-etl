import requests

class SpotifyAPI:
    __BASE_URL = "https://api.spotify.com/"

    def __init__(self, access_token):
        self.access_token = access_token

    def get