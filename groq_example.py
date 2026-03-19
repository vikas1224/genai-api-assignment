from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

prompt = input("Enter prompt: ")

try:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )
    print("\nResponse:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)