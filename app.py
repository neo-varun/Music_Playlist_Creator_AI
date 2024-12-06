from flask import Flask, render_template, request
from src.songbot import generate_playlist  # Import the function to interact with OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect form data
    language = request.form['language']
    genre = request.form['genre']
    artists = request.form['artists']
    era = request.form['era']
    feeling = request.form['feeling']

    # Call the OpenAI handler to generate the playlist
    playlist = generate_playlist(language, genre, artists, era, feeling)

    # Return the playlist recommendations to the user
    return f"Playlist Recommendations:\n{playlist}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)