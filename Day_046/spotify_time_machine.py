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

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
print(sp.current_user())
