from collections import defaultdict

import spotipy

from spotipy.oauth2 import SpotifyOAuth


cid = 'e7bebd4ec3744b08afc1e80f13008e6f'
secret = 'b216f07725ca42c6b7ac6b845f55e684'

username = 'imn69hydyq5jbt4laxi523rko'
scope = 'user-library-read'
authorisation_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_url = 'http://localhost:8000/callback/'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_url,
                                               scope=scope, username=username))

tracks = []
results = sp.current_user_saved_tracks()
tracks.extend(results['items'])
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

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
