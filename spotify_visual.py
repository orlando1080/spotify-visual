from collections import defaultdict
import configparser

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

access_token = sp.get_access_token(check_cache=False, as_dict=False)
sp = spotipy.Spotify(auth=access_token)

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

artists_names = [name for name in sorted_artists]
tracks_count = [num for num in sorted_artists.values()]
fig, ax = plt.subplots()
ax.barh(artists_names[:10], tracks_count[:10])
ax.set_xlabel('Artists')
ax.set_ylabel('Number Of Songs')
ax.set_title(f'Top 10 Artists by Saved Tracks for {name}')
plt.show()
