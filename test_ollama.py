from ollama import chat

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Suggest a cheap route from Tel Aviv to Buenos Aires"
        }
    ]
)

print(response["message"]["content"])