
Music Playlist Creator
------------------------------

Project Overview:
-----------------
The **Music Playlist Creator** is a web-based application that allows users to generate personalized music playlists based on their preferences. The application leverages Spotify's API and OpenAI's GPT model to interact with users and gather information such as preferred languages, genres, artists, music eras, and feelings. The chatbot then creates a playlist tailored to the user's preferences. Here’s how it works:

1. User Login & Authorization:
   - The user is redirected to Spotify's authorization page to log in and grant necessary permissions for creating and modifying playlists.

2. Chatbot Interaction:
   - The user interacts with a chatbot that asks for details like language, genre, artists, era, and mood. This information helps curate a personalized playlist.

3. Playlist Generation:
   - Based on the user’s input, the app uses OpenAI GPT to generate a list of recommended songs, which are then searched on Spotify using its Web API.
   - A new playlist is created on the user’s Spotify account with the selected tracks.

4. Playlist Link:
   - The user is provided with a link to the newly created playlist on Spotify.

Features of the Music Playlist Creator
--------------------------------------
1. Interactive Chatbot:
   - Users provide their preferences through a conversational chatbot, making the playlist creation process fun and dynamic.

2. Spotify API Integration:
   - The app creates playlists and adds tracks to Spotify using the Spotify Web API.
   - Tracks are fetched based on user preferences.

3. Personalized Playlists:
   - The app generates playlists based on criteria like language, genre, artists, mood, and era.

4. OpenAI GPT Integration:
   - GPT-3 powers the chatbot, making the interaction natural and responsive to user input.

5. Link to Generated Playlist:
   - After playlist creation, the user receives a link to their custom Spotify playlist, which can be shared or saved.

Prerequisites:
--------------
Before running the project, make sure you have the following:
1. Python 3.x installed.
2. Spotify Developer account (to access the Spotify API).
3. OpenAI API key (for playlist generation with GPT).
4. Your machine should have `pip` (Python package installer) installed.

Steps to Set Up:
----------------

1. **Create a Virtual Environment** (Optional but recommended):
   - Navigate to your project directory in the terminal/command prompt.
   - Create a new virtual environment using the following command:
     ```
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On MacOS/Linux:
       ```
       source venv/bin/activate
       ```

2. **Install Required Dependencies**:
   - Make sure your virtual environment is activated, then install the required dependencies by running the following command:
     ```
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**:
   - You'll need to set up environment variables for your Spotify and OpenAI credentials. Create a `.env` file in your project directory and add the following lines:
     ```
     SPOTIFY_CLIENT_ID=your_spotify_client_id
     SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
     SPOTIFY_REDIRECT_URI=your_spotify_redirect_uri
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Install the Package**:
   - Install the package using the following command:
     ```
     python setup.py install
     ```

5. **Run the Application**:
   - Once everything is set up, you can run the application with:
     ```
     python app.py
     ```

6. **Interact with the Chatbot**:
   - After running the app, navigate to `http://127.0.0.1:8000/` in your web browser. You’ll be able to interact with the chatbot, providing responses to questions such as:
     - Preferred languages for songs
     - Music genres
     - Favorite artists
     - Music era preferences
     - Your current mood
   - The chatbot will guide you through the entire process of playlist creation.

7. **Spotify Authentication**:
   - When the chatbot starts asking for input, you may need to authenticate with Spotify. If not already logged in, you will be redirected to the Spotify login page. Grant access to the application to allow it to create playlists on your behalf.

8. **Generate Your Playlist**:
   - After you’ve provided all the necessary information, the chatbot will create a playlist based on your preferences and add tracks from Spotify. A link to the newly created playlist will be displayed in the chat interface.

Troubleshooting:
----------------
- **Missing Environment Variables**: Make sure all required API keys are set in the `.env` file.
- **Dependencies**: If any dependencies fail to install, try running `pip install --upgrade pip` before installing again.
- **Spotify Authentication Issues**: Ensure that your `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `SPOTIFY_REDIRECT_URI` are correctly configured in your environment variables.

Contribution:
-------------
Feel free to fork the repository, report issues, and submit pull requests. Contributions are welcome!

Contact:
--------
For any issues or inquiries, contact the author at:
- Email: darklususnaturae@gmail.com