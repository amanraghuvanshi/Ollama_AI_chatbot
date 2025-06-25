import subprocess

def query_model(prompt, model="deepseek-r1:1.5b", ollama_path="ollama"):
    try:
        command = [ollama_path, "run", model, "--prompt", prompt]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception("Failed to execute Ollama CLI command.")
        return result.stdout.strip()
    except Exception as e:
        return str(e)
