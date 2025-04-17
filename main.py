from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections
from pairs import pair

app = Flask(__name__)
chat = Chat(pair, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    if user_input.lower() == "exit":
        response = "Good Bye"
    else:
        response = chat.respond(user_input.lower())
        if not response:
            response = "I'm not sure how to respond to that."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)