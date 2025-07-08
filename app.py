from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 🔑 Replace this with your real OpenAI API key
openai.api_key = "your-openai-api-key"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.json.get("message", "")
        if not user_input.strip():
            return jsonify({"reply": "Please ask something."})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
