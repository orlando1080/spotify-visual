from collections import defaultdict
import configparser
import json
import requests

import matplotlib.pyplot as plt

import spotipy
from spotipy.oauth2 import SpotifyOAuth

config = configparser.ConfigParser()
config.read('config.cfg')

cid = config.get('SPOTIFY', 'CLIENT_ID')
secret = config.get('SPOTIFY', 'CLIENT_SECRET')
scope = 'user-library-read'
redirect_url = 'http://localhost:8000/callback/'
sp = SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope, redirect_uri=redirect_url, open_browser=False, show_dialog=True)
#
# # Function to write tokens to a file
# def write_tokens(tokens):
#     with open(f"{sp.current_user()['display_name']}_tokens.json", "w") as f:
#         json.dump(tokens, f)
#
#
# # Function to read tokens from a file
# def read_tokens():
#     with open(f"{sp.current_user()['display_name']}_tokens.json", "r") as f:
#         tokens = json.load(f)
#     return tokens
#
# # Check if tokens are stored in file
# try:
#     tokens = read_tokens()
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret,
#                                                    scope=scope, redirect_uri=redirect_url,
#                                                    access_token=tokens["access_token"],
#                                                    refresh_token=tokens["refresh_token"]))
# except:
#     # auth_url = sp.get_authorize_url()
#     # print(f'{auth_url}')
#     # url = input('paste: ')
#     # code = sp.parse_auth_response_url(url)
access_token = sp.get_access_token(check_cache=False, as_dict=False)
# access_token = tokens['access_token']
# refresh_token = tokens['refresh_token']
sp = spotipy.Spotify(auth=access_token)

#     # Store tokens in a dictionary and write to file
#     tokens = {
#         "access_token": access_token,
#         "refresh_token": refresh_token
#     }
#     write_tokens(tokens)
# finally:
#     if isinstance(sp._session, requests.Session):
#         sp._session.close()

name = sp.current_user()['display_name']

tracks = []
for i in range(0, 5000, 50):
    all_tracks = sp.current_user_saved_tracks(limit=50, offset=i)
    for index, t in enumerate(all_tracks['items']):
        tracks.append(t)

# Count the number of tracks by each artist
artist_counts = defaultdict(int)
for track in tracks:
    artists = track['track']['artists']
    for artist in artists:
        artist_name = artist['name']
        artist_counts[artist_name] += 1

sorted_artists = dict(sorted(artist_counts.items(), key=lambda x: x[1])[::-1])

# Print the number of tracks by each artist
for artist, count in sorted_artists.items():
    print(f"{artist}: {count}")
artists_names = [name for name in sorted_artists]
tracks_count = [num for num in sorted_artists.values()]
fig, ax = plt.subplots()
ax.barh(artists_names[:10], tracks_count[:10])
ax.set_xlabel('Artists')
ax.set_ylabel('Number Of Songs')
ax.set_title(f'Top 10 Artists by Saved Tracks for {name}')
plt.show()
