import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_PATH = os.getenv("OLLAMA_PATH", "ollama")
MODEL_NAME = "deepseek-r1:1.5b"
DEFAULT_PORT = 8000
DEBUG_MODE = True
