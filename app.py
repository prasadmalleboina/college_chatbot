from flask import Flask, render_template, request, jsonify
import re
app = Flask(__name__)

def get_response(msg):
    import json

with open("data.json") as f:
    data = json.load(f)

def get_response(msg):
    msg = msg.lower()

    if "course" in msg:
        return ", ".join(data["courses"].keys())

    elif "fee" in msg:
        if "cse" in msg:
            return data["fees"]["cse"]
        elif "ece" in msg:
            return data["fees"]["ece"]
        else:
            return str(data["fees"])

    elif "placement" in msg:
        return data["placement"]

    elif "hostel" in msg:
        return data["hostel"]

    else:
        return "Ask about courses, fees, placement, or hostel."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_response(user_msg)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
