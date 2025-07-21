from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

@app.route('/')
def index():
    return "Backend is running"

@app.route('/process_audio', methods=['POST'])
def process_audio():
    data = request.get_json()
    transcript = data.get("transcript", "")

    # Simple intent handling
    if "password" in transcript.lower():
        intent = "Password Reset"
        answer = "To reset your password, click 'Forgot Password' on login."
    else:
        intent = "Unknown"
        answer = "I'm not sure how to help with that."

    return jsonify({"intent": intent, "answer": answer})

@app.route('/intent', methods=['POST'])
def handle_intent():
    data = request.get_json()
    transcript = data.get("transcript", "")

    if "password" in transcript.lower():
        intent = "Password Reset"
        answer = "Go to settings to reset your password."
    else:
        intent = "Unknown"
        answer = "I'm not sure how to help."

    return jsonify({"intent": intent, "answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
