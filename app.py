# SpotifyOAuth is needed to get access to private data

import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm

client_id = config.SPOTIPY_CLIENT_ID
client_secret = config.SPOTIPY_CLIENT_SECRET
redirect_uri = config.SPOTIPY_REDIRECT_URI

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Set the initial offset to 0
offset = 0

# Create a dictionary to store the genre counts
genre_counts = {}

# Get the total number of saved tracks
total_saved_tracks = sp.current_user_saved_tracks(limit=1, offset=0)['total']

# Retrieve the saved tracks using pagination
with tqdm(total=total_saved_tracks) as pbar:
    while True:

        # max_limit = 50
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        items = results['items']
        for item in items:
            track = item['track']

            # Retrieve the artist's genres
            artist_id = track['artists'][0]['id']
            artist_info = sp.artist(artist_id)
            genres = artist_info['genres']

            # Count the genres
            for genre in genres:
                if genre in genre_counts:
                    genre_counts[genre] += 1
                else:
                    genre_counts[genre] = 1

            pbar.update(1)

        # Check if there are more saved tracks to retrieve
        if results['next'] is not None:
            offset += 50
        else:
            break

# Sort the genre counts in descending order and print the top 10 genres
sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
print("Top 10 genres:")
for genre, count in sorted_genres[:10]:
    print(f"{genre}: {count}")