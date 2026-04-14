from flask import Flask, render_template, request, jsonify
import json
from openai import OpenAI
import os

app = Flask(__name__)

# Load data from JSON file
with open("data.json") as f:
    data = json.load(f)

def get_response(msg):
    msg = msg.lower().strip()

    # Courses
    if "course" in msg:
        return "Available courses: " + ", ".join(data["courses"].keys())

    # Fees
    elif "fee" in msg:
        if "cse" in msg:
            return "CSE Fee: " + data["fees"]["cse"]
        elif "ece" in msg:
            return "ECE Fee: " + data["fees"]["ece"]
        elif "eee" in msg:
            return "EEE Fee: " + data["fees"]["eee"]
        else:
            return "Fees: " + ", ".join([f"{k.upper()}: {v}" for k, v in data["fees"].items()])

    # Placement
    elif "placement" in msg:
        return data["placement"]

    # Hostel
    elif "hostel" in msg:
        return data["hostel"]

    # Greeting
    elif msg in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    # Default
    else:
        return "I can help with courses, fees, placement, and hostel info."

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    reply = get_response(user_msg)
    return jsonify({"response": reply})

# Run app
if __name__ == "__main__":
    app.run()
