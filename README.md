Spotify Top Artists
This script retrieves the user's saved tracks from their Spotify account and counts the number of tracks saved by each artist. It then creates a bar chart to display the top N artists by the number of saved tracks for each artist.

Prerequisites
Spotify account
Spotify Developer account
Python 3.x
configparser library (pip install configparser)
spotipy library (pip install spotipy)
plotly library (pip install plotly)
Installation
Clone this repository or download the spotify_top_artists.py file.
Create a config file named config.cfg in the same directory as the spotify_top_artists.py file. Add the following lines to the config file, replacing YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your Spotify client ID and client secret, respectively:
makefile
Copy code
[SPOTIFY]
CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET
Install the required Python libraries using pip:
Copy code
pip install configparser spotipy plotly
Usage
Run the script from the command line:
Copy code
python spotify_top_artists.py
The script will prompt you to log in to your Spotify account and authorize the script to access your saved tracks.
The script will generate a bar chart in HTML format that displays the top N artists by the number of saved tracks for each artist, where N is a user-defined variable. The chart will be saved as an HTML file with a filename that includes the number of artists displayed.
Customization
You can customize the number of top artists displayed by changing the value of the cap variable in the script.
You can customize the chart title and axis labels by modifying the my_layout dictionary in the script.
Limitations
This script is limited to retrieving the user's saved tracks, so it may not be representative of the user's overall music preferences.
The script may take a long time to run if the user has a large number of saved tracks. To avoid rate limiting by the Spotify API, the script retrieves the tracks in batches of 50. If the user has more than 5000 saved tracks, some tracks may not be counted.