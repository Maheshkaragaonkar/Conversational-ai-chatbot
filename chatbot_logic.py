import requests

def get_response(user_input):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": user_input, "stream": False}
    )
    return response.json()["response"]
