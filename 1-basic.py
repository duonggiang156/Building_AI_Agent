import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

user_prompt = input("Hãy nhập câu hỏi: ")

completion = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system", "content":"You are a helpful assistant."},
        {
            "role":"user",
            "content" : "user_prompt"
        },
    ],
)

response = completion.choices[0].message.content

print(response)
