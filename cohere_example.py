import cohere

co = cohere.Client("YOUR_API_KEY")

prompt = input("Enter prompt: ")

try:
    response = co.chat(
        model="command-r-plus-08-2024",
        message=prompt
    )

    print("\nResponse:\n")
    print(response.text)

except Exception as e:
    print("Error:", e)