def generate_song_artist_dict(playlist):
    
    # Split the response into a list of songs
    songs = playlist.strip().split("\n")

    # Create a dictionary to store song details
    song_artist_dict = {}

    # Loop through each song and extract details
    for song in songs:

        parts = song.split(" - ")
        if len(parts) == 4:
            song_title, album, artist, year = [part.strip() for part in parts]
            song_artist_dict[song_title] = {
                "album": album,
                "artist": artist,
                "year": year,
            }

    return song_artist_dict