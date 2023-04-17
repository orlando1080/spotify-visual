from collections import defaultdict
import configparser
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from plotly import offline

config = configparser.ConfigParser()
config.read('config.cfg')

cid = config.get('SPOTIFY', 'CLIENT_ID')
secret = config.get('SPOTIFY', 'CLIENT_SECRET')
scope = 'user-library-read'
redirect_url = 'http://localhost:8000/callback/'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope, redirect_uri=redirect_url))
# sp = SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope, redirect_uri=redirect_url, open_browser=False, show_dialog=True)
# access_token = sp.get_access_token(check_cache=False, as_dict=False)
# sp = spotipy.Spotify(auth=access_token)

# with open('spotify.json', 'w') as file:
#     json.dump(sp.current_user_saved_tracks(), indent=4, fp=json)

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
        if artist_name in artist_counts:
            artist_counts[artist_name][1] += 1
        else:
            artist_counts[artist_name] = [artist['external_urls']['spotify'], 1]

sorted_artists = dict(sorted(artist_counts.items(), key=lambda x: x[1][1])[::-1])
# artists_names = [name for name in sorted_artists][:10]
# tracks_count = [num for num in sorted_artists.values()][:10]
#
# data = [{
#     'type': 'bar',
#     'x': artists_names,
#     'y': tracks_count,
#     'marker': {
#         'color': 'rgb(60, 100, 150)',
#         'line': {'width': 1.5, 'color': 'rgb(25, 24, 25)'}
#     },
#     'opacity': 0.6,
# }]
#
# my_layout = {
#     'title': f'Top 10 Most Songs for {name}',
#     'titlefont': {'size': 28},
#     'xaxis': {'title': 'Artists',
#               'titlefont': {'size': 24},
#               'tickfont': {'size': 14}
#               },
#     'yaxis': {'title': 'Track Count',
#               'titlefont': {'size': 24},
#               'tickfont': {'size': 14}
#               },
# }
#
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='Top 10 Artist by Song Count.html')