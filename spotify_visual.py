import configparser

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from plotly import offline

config = configparser.ConfigParser()
config.read('config.cfg')

cid = config.get('SPOTIFY', 'CLIENT_ID')
secret = config.get('SPOTIFY', 'CLIENT_SECRET')
scope = 'user-library-read'
redirect_url = 'http://localhost:8000/callback/'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope,
                                               redirect_uri=redirect_url))
# sp = SpotifyOAuth(client_id=cid, client_secret=secret, scope=scope, redirect_uri=redirect_url, open_browser=False, show_dialog=True)
# access_token = sp.get_access_token(check_cache=False, as_dict=False)
# sp = spotipy.Spotify(auth=access_token)

tracks = []
for i in range(0, 5000, 50):
    all_tracks = sp.current_user_saved_tracks(limit=50, offset=i)
    for index, t in enumerate(all_tracks['items']):
        tracks.append(t)

# Count the number of tracks by each artist
artist_counts = {}
for track in tracks:
    artists = track['track']['artists']
    for artist in artists:
        artist_name = artist['name']
        if artist_name in artist_counts:
            artist_counts[artist_name][1] += 1
        else:
            artist_counts[artist_name] = [artist['external_urls']['spotify'], 1]

name = f'<a href="{sp.current_user()["external_urls"]["spotify"]}">{sp.current_user()["display_name"]}'
cap = 20
sorted_artists = dict(sorted(artist_counts.items(), key=lambda x: x[1][1])[::-1])
artists_names = [f'<a href="{sorted_artists[name][0]}">{name}</a>' for name in sorted_artists][:cap]
tracks_count = [num[1] for num in sorted_artists.values()][:cap]

data = [{
    'type': 'bar',
    'x': artists_names,
    'y': tracks_count,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 24, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': f'Top {cap} Artists by liked Song Amount for {name}',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Artists',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
    'yaxis': {'title': 'Track Count',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'Top {cap} Artists by Liked Song Amount.html')
