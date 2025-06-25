import os
from flask import Flask, request, jsonify


# Import modules
from backend.config import OLLAMA_PATH, MODEL_NAME
from backend.ollama_handler import query_model
from backend.preprocess import preprocess_text

app = Flask(__name__)

# Endpoint to check the backend status
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "running",
        "model": MODEL_NAME
    })


# Endpoint to query the model
@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        # Preprocess the prompt before sending it to the model
        prompt = data["prompt"]
        preprocessed_prompt = preprocess_text(prompt)

        # Query the model
        response = query_model(preprocessed_prompt, MODEL_NAME, OLLAMA_PATH)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to preprocess input (optional)
@app.route("/preprocess", methods=["POST"])
def preprocess():
    try:
        data = request.get_json()
        if not data or "input_text" not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        input_text = data["input_text"]
        preprocessed_text = preprocess_text(input_text)

        return jsonify({"preprocessed_text": preprocessed_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
