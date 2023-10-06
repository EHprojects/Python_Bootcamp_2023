from pprint import pprint
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("../.idea/.env")

# [Spotify]
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_USER_ID = os.getenv("SPOTIPY_USER_ID")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIPY_USER_ID,
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

result = sp.search(q="track: young blood year:2010", type="track")
track_uri = result["tracks"]["items"][0]["uri"]
print(track_uri)

# user_playlist_create(user, name, public=True, collaborative=False, description='')
# Creates a playlist for a user
#
# Parameters:
# user - the id of the user
# name - the name of the playlist
# public - is the created playlist public
# collaborative - is the created playlist collaborative
# description - the description of the playlist

new_pl = sp.user_playlist_create(user=SPOTIPY_USER_ID, name="Test01", public=False,
                                 collaborative=False, description="This is a test playlist.")

new_pl_id = new_pl["id"]

sp.playlist_add_items(playlist_id=new_pl_id, items=[track_uri])

