import os
from dotenv import load_dotenv

from spotify_api import SpotifyAPI
from src.utility.spotify_config import config


load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_api = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
access_token = spotify_api.get_access_token()


def get_albums():
    key = config["albums"]
    response = spotify_api.get_api_response("albums", access_token, key)
    return response


def get_artists():
    key = config["artists"]
    response = spotify_api.get_api_response("artists", access_token, key)
    return response


