import requests

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-small"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

prompt = input("Enter prompt: ")

try:
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    print("Status:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("\nResponse:\n", data)
    else:
        print("\nError:\n", response.text)

except Exception as e:
    print("Error:", e)