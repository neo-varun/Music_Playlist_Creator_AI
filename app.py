from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import requests
from urllib.parse import urlencode
from src.songlist import generate_song_artist_dict
from src.songbot import generate_playlist
from src.songsearch import search_spotify_tracks
from src.playlist import create_spotify_playlist

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SCOPES = "playlist-modify-public playlist-modify-private"

def get_authorization_url():
    
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
    }
    return f"{auth_url}?{urlencode(params)}"

@app.route('/')
def home():
    
    access_token = session.get('access_token')
    
    if not access_token:
        return redirect(url_for('authorize'))

    return render_template('index.html')

@app.route('/authorize')
def authorize():
    
    return redirect(get_authorization_url())

@app.route('/callback')
def callback():
    
    code = request.args.get('code')

    if not code:
        return "Error: No code found in the URL"

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
        access_token = response.json()['access_token']
        refresh_token = response.json()['refresh_token']

        # Store the access token and refresh token in session
        session['access_token'] = access_token
        session['refresh_token'] = refresh_token  # Store the refresh token for future use

        # After successful token retrieval, redirect to the /submit route
        return redirect(url_for('submit'))
    else:
        return f"Error fetching access token: {response.json()}"

def refresh_access_token():
    
    token_url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": session.get('refresh_token'),
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        new_access_token = response.json()['access_token']
        session['access_token'] = new_access_token
        return new_access_token
    else:
        return None

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    
    # If the request method is GET, just show the form or message
    if request.method == 'GET':
        return render_template('index.html')

    language = request.form['language']
    genre = request.form['genre']
    artists = request.form['artist']
    era = request.form['era']
    feeling = request.form['feeling']

    # Get the access token from session
    access_token = session.get('access_token')

    if not access_token:
        return redirect(url_for('authorize'))

    # Call the OpenAI handler to generate the playlist
    playlist = generate_playlist(language, genre, artists, era, feeling)

    # Call the function to generate the song-artist dictionary
    song_artist_dict = generate_song_artist_dict(playlist)

    # Call search_spotify_tracks to get track IDs from Spotify
    track_id_list = search_spotify_tracks(song_artist_dict)

    # Call create_spotify_playlist to create the playlist on Spotify
    result = create_spotify_playlist(track_id_list, access_token=access_token, playlist_name="My Chill Vibes", description="A playlist of my favorite chill tracks.")

    # Return playlist result
    return jsonify({
            "message": "Here is a playlist tailored just for you:",
            "playlist_url": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)