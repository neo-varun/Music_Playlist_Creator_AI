from flask import Flask, render_template, request, jsonify
from src.chatbot import OpenaiResponse

app = Flask(__name__)

# Initialize chatbot instance
chatbot = OpenaiResponse()

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Get user input from form (using request.form for POST data)
    user_input = request.form.get("user_input")
    
    if user_input:
        # Get the bot response by passing the user input to the chatbot
        bot_response = chatbot.openai_response(user_input)
        print(f"You: {user_input}")
        print(f"Bot: {bot_response}")
        # Return bot response as JSON to update the page dynamically
        return jsonify({"response": bot_response})
    else:
        return jsonify({"response": "Please provide some input."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)