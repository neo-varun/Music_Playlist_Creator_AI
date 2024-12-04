from openai import OpenAI

client=OpenAI() # Retrieves the key from os.environ.get('OPENAI_API_KEY').

class OpenaiResponse:

    def __init__(self):
        pass

    def openai_response(self,prompt):

        completion=client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[{"role":"user","content":prompt}],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.8,
        )

        return completion.choices[0].message.content