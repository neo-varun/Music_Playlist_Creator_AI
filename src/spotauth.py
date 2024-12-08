import os
import requests
from flask import Flask, request, session

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")  # Make sure this is set in your environment
SCOPES = "playlist-modify-public playlist-modify-private"

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Get the authorization code from URL
    code = request.args.get('code')

    if not code:
        return "Error: No code found in the URL"

    # Exchange the authorization code for an access token and refresh token
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens['access_token']
        refresh_token = tokens['refresh_token']

        # Store the access token and refresh token in the session
        session['access_token'] = access_token
        session['refresh_token'] = refresh_token
        return f"{access_token}"
    else:
        return f"Error fetching access token: {response.json()}"
    
def refresh_access_token():
    refresh_token = session.get('refresh_token')
    
    if not refresh_token:
        return None

    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        new_access_token = response.json()['access_token']

        # Store the new access token in session
        session['access_token'] = new_access_token
        return new_access_token
    else:
        return None