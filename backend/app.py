import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration variables
OLLAMA_MODEL = "deepseek-r1:1.5b"
OLLAMA_PATH = os.getenv("OLLAMA_PATH", "ollama")

# Endpoint to check the backend status
@app.route("/status", methods = ["GET"])
def status():
    return jsonify({
        "status": "running",
        "model" : OLLAMA_MODEL
    })
    
# Endpoint for quering the model
@app.route("/query", methods = ["POST"])
def query_model():
    try: 
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({
                "error": "Invalid request payload"
            }), 400
        prompt = data["prompt"]
        
        # Run the OLLAMA CLI command
        command = [OLLAMA_PATH, "run", OLLAMA_MODEL, "--prompt", prompt]
        res = subprocess.run(command, stdout=subprocess.PIPE, text = True)
        
        if res.returncode != 0:
            return jsonify({
                "error" : "Faild to communicate with the model"
            }), 500
            
        return jsonify({
            "response" : res.stdout.strip()
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
    
# Endpoint for preprocessing the data
@app.route("/preprocess", methods = ["POST"])
def preprocess():
    try:
        data = request.get_json()
        if not data or "input_text" not in data:
            return jsonify({
                "error" : "Invalid Request Payload"
            }), 400
            
        input_text = data["input_text"]
        
        # preprocessing logic
        processed_text = input_text.strip().lower()
        return jsonify({
            "processed_text" : processed_text
        })
    except Exception as e:
        return jsonify({
            "error" : str(e)
        }), 500
        
        
if __name__ == "__main___":
    app.run(host = "0.0.0.0", port = 11499, debug = True)