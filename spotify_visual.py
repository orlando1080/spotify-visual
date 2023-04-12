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
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope,
                                               redirect_uri=redirect_url))

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

# Print the number of tracks by each artist
# for artist, count in artist_counts.items():
#     print(f"{artist}: {count}")
# print(len(tracks))
artists_names = [name for name in artist_counts]
tracks_count = [num for num in artist_counts.values()]

fig, ax = plt.subplots()
ax.barh(artists_names[: 6], tracks_count[: 6])

plt.show()
print(artist_counts.get('Eminem'))
