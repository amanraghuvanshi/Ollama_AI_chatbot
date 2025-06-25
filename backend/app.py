import os
import subprocess
from flask import Flask, request, jsonify


# Configuration variables
OLLAMA_MODEL = "deepseek-r1:1.5b"
OLLAMA_PATH = os.getenv("OLLAMA_PATH", "ollama")

# 