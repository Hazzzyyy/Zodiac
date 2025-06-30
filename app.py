from flask import Flask, render_template, request, jsonify # type: ignore

app = Flask(__name__)
# Dummy AI response
def ai_assistant_response(message):
    if "love" in message.lower():
        return "💖 Your love life looks promising under Venus this week."
    elif "career" in message.lower():
        return "💼 Your career path may shift positively. Be open to new opportunities."
    elif "lucky" in message.lower():
        return "🍀 Your lucky number today is 7."
    else:
        return "🌠 Ask me about your zodiac, love life, or daily fortune!"

@app.route("/")
def index():
    title = "🌌 Welcome to Zodiac Realm"
    content = "Explore the mysteries of the stars, signs, and cosmic paths. Discover yourself through astrology."
    return render_template("index.html", title=title, content=content)

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = ai_assistant_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
