from collections import defaultdict

import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyOAuth

cid = 'e7bebd4ec3744b08afc1e80f13008e6f'
secret = 'b216f07725ca42c6b7ac6b845f55e684'

scope = 'user-library-read'
redirect_url = 'http://localhost:8000/callback/'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope, redirect_uri=redirect_url))

tracks = []
# print(sp.current_user_saved_tracks()['items'])
for i in range(0, 5000, 50):
    all_tracks = sp.current_user_saved_tracks(limit=50, offset=i)
    for i, t in enumerate(all_tracks['items']):
        tracks.append(t)
print(tracks)

# Count the number of tracks by each artist
artist_counts = defaultdict(int)
for track in tracks:
    artists = track['track']['artists']
    for artist in artists:
        artist_name = artist['name']
        artist_counts[artist_name] += 1

# Print the number of tracks by each artist
for artist, count in artist_counts.items():
    print(f"{artist}: {count}")
print(len(tracks))
