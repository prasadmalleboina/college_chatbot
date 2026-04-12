from flask import Flask, render_template, request, jsonify
import re
app = Flask(__name__)

def get_response(msg):
    msg = msg.lower()

    import re

def get_response(msg):
    msg = msg.lower()

    # greetings
    if re.search(r"\b(hi|hello|hey)\b", msg):
        return "Hello! 👋 How can I assist you today?"

    # courses
    elif re.search(r"\b(course|branch|department)\b", msg):
        return "We offer CSE, ECE, EEE, Mechanical, Civil."

    # fees
    elif re.search(r"\b(fee|fees|cost|tuition)\b", msg):
        return "Fees depend on course. Approx ₹50,000–₹1,00,000 per year."

    # admission
    elif re.search(r"\b(admission|apply|join)\b", msg):
        return "Admissions are open! Apply online or visit campus."

    # placement
    elif re.search(r"\b(placement|job|package)\b", msg):
        return "We have 90% placement rate. Top companies visit every year."

    # hostel
    elif re.search(r"\b(hostel|accommodation)\b", msg):
        return "Hostel facilities available for boys and girls."

    # contact
    elif re.search(r"\b(contact|phone|number)\b", msg):
        return "📞 9876543210 | 📍 College Office"

    else:
        return "🤔 I’m not sure. Try asking about courses, fees, placements, or hostel."

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