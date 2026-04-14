from flask import Flask, render_template, request, jsonify
import json
import os
from openai import OpenAI

app = Flask(__name__)

# Load data
with open("data.json") as f:
    data = json.load(f)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(msg):
    msg = msg.lower().strip()

    # RULE-BASED RESPONSES
    if "course" in msg:
        return "Available courses: " + ", ".join(data["courses"].keys())

    elif "fee" in msg:
        if "cse" in msg:
            return "CSE Fee: " + data["fees"]["cse"]
        elif "ece" in msg:
            return "ECE Fee: " + data["fees"]["ece"]
        elif "eee" in msg:
            return "EEE Fee: " + data["fees"]["eee"]
        else:
            return "Fees: " + ", ".join([f"{k.upper()}: {v}" for k, v in data["fees"].items()])

    elif "placement" in msg:
        return data["placement"]

    elif "hostel" in msg:
        return data["hostel"]

    elif msg in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    # AI FALLBACK
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful college assistant."},
                    {"role": "user", "content": msg}
                ]
            )
            return response.choices[0].message.content

        except Exception as e:
            return "AI service is not available right now."

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    reply = get_response(user_msg)
    return jsonify({"response": reply})

# Run
if __name__ == "__main__":
    app.run()
