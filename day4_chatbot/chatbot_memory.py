import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version="v1beta"),
)
MODEL = "gemini-2.5-flash"

chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction="You are a patient Python tutor. Use simple English and keep answers short."
    ),
)


def ask_llm(text):
    response = chat.send_message(text)
    return response.text


while True:
    user_text = input("You: ")
    if not user_text.strip():
        continue
    if user_text.lower() in ["quit", "exit"]:
        break
    try:
        print("Bot:", ask_llm(user_text))
    except Exception as e:
        print("Something went wrong:", e)