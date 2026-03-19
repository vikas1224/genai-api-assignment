import requests

prompt = input("Enter prompt: ")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

print("\nFull Response:\n", data)

if "response" in data:
    print("\nFinal Output:\n")
    print(data["response"])
else:
    print("\nError from Ollama:", data)