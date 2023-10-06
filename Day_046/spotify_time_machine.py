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

# year_select = input("What date would you like to travel to (YYY-MM-DD)?: ")
year_select = "2010-06-15"
year = year_select[:4]
print(year)

URL = f"https://www.billboard.com/charts/hot-100/{year_select}/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_names_spans = soup.select("li ul li h3")
# print(song_names_spans)

song_titles = []

for song in song_names_spans:
    song_title = song.getText().strip()
    song_titles.append(song_title)

print(song_titles)

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

track_uris = []

for title in song_titles:
    result = sp.search(q=f"track: {title} year:{year}", type="track", limit=1)
    try:
        track_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        continue

new_pl = sp.user_playlist_create(user=SPOTIPY_USER_ID, name=f"{year_select} Billboard 100", public=False,
                                 collaborative=False, description=f"The Billboard Top 100 for the date {year_select}.")

new_pl_id = new_pl["id"]

sp.playlist_add_items(playlist_id=new_pl_id, items=track_uris)
