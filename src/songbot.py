from openai import OpenAI

client=OpenAI() # Retrieves the key from os.environ.get('OPENAI_API_KEY').

def generate_playlist(language, genre, artists, era, feeling):

    # Construct the prompt based on the user's preferences
    prompt = f"Suggest a list of songs based on these preferences:\n"
    prompt += f"Language: {language}\n"
    prompt += f"Genre: {genre}\n"
    prompt += f"Artists: {artists}\n"
    prompt += f"Year/Era Preference: {era}\n"
    prompt += f"Mood/Feeling: {feeling}\n"

    print(prompt)

    try:
        # Sending the prompt to OpenAI's API and getting the response
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are a helpful music recommendation assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.8,
            )
        
        # Return the recommended songs from the OpenAI response
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating playlist: {str(e)}"