from groq import Groq

client = Groq(api_key="YOUR_API_KEY")  

prompt = input("Enter prompt: ")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

print("\nResponse:\n")
print(response.choices[0].message.content)