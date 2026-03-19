import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("models/gemini-flash-latest")

prompt = input("Enter prompt: ")

try:
    response = model.generate_content(prompt)
    print("\nResponse:\n")
    print(response.text)
except Exception as e:
    print("Error:", e)