import requests
import base64
import os

def spot_access_token():

    # Fetch Spotify credentials from environment variables
    client_id = os.getenv('SPOTIFY_CLIENT_ID')  # Make sure this is set in your environment
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')  # Make sure this is set in your environment

    if not client_id or not client_secret:
        print("Error: SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET not set in environment variables.")
        exit()

    # Encode the client credentials in base64
    client_credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(client_credentials.encode('utf-8')).decode('utf-8')

    # Request an access token
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, headers=headers, data=data)
    token_info = response.json()

    access_token = token_info['access_token']

    return access_token