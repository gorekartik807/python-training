import os
from groq import Groq

# API key environment se lega
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Test prompt
prompt = "Give me 2 practical study tips for DBMS in 2 lines max"

# Groq API call
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Result print
print("🤖 AI Response:")
print(response.choices[0].message.content)