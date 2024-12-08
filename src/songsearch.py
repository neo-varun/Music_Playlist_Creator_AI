import requests
from src.spotapi import spot_access_token

def search_spotify_tracks(song_artist_dict):
    """
    Takes a dictionary with song titles as keys and details (album, artist, year) as values,
    searches for the tracks on Spotify, and returns a list of track IDs.
    """
    access_token_api = spot_access_token()  # Get Spotify access token

    # Set up the headers with the access token
    headers = {
        'Authorization': f'Bearer {access_token_api}'
    }

    # List to store track ids (only Track ID)
    track_ids = []

    for song_title, details in song_artist_dict.items():
        # Extract details
        artist_name = details["artist"]
        album_name = details["album"]
        year = details["year"]

        # Set up the parameters for the search request
        params = {
            'q': f"{song_title} {artist_name} {album_name} {year}",  # Include all relevant details
            'type': 'track',  # Search for tracks
            'limit': 1  # Number of results to return
        }

        # Make the search request
        search_url = 'https://api.spotify.com/v1/search'
        response = requests.get(search_url, headers=headers, params=params)

        # Handle API response
        if response.status_code == 200:
            data = response.json()

            # Check if any tracks were found
            if data['tracks']['items']:
                for track in data['tracks']['items']:
                    # Extract track ID and add it to the list
                    track_id = track['id']
                    track_ids.append(track_id)

                    # Optionally, print track ID for verification (this line can be removed if not needed)
                    print(f"{song_title}: {track_id}")
                    print("-" * 30)  # Separator between tracks
            else:
                print(f"No tracks found for {song_title}.")
                print("-" * 30)
        else:
            # Handle non-successful responses
            print(f"Error: Unable to search for {song_title}.")
            print(f"HTTP Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            print("-" * 30)

    return track_ids  # Return the list of track IDs