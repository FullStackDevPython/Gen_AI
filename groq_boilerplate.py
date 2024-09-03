#Installing the package via PIP
# !pip install groq

from groq import Groq

groq_api_key = "Enter Your Key"
model_name = "llama-3.1-8b-instant"

client = Groq(api_key=groq_api_key)
user_question = "What are the 7 wonders of world ?"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_question,
        }
    ],
    model=model_name,
)

print(chat_completion.choices[0].message.content)

print(chat_completion)