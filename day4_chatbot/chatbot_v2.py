import os
import time    # for waiting between retries
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(
 api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version="v1beta"),
)
MODEL = "gemini-3.5-flash-lite"     #model name, check docs when it changes
MAX_MESSAGES = 6  # keep only the last 6 messages to save tokens)
# system prompt: the bot's role and style
CONFIG = types.GenerateContentConfig(
    system_instruction="You are a patient Python tutor. Use simple English and keep answers short."
)


def make_chat(history=None):
    return client.chats.create(model=MODEL, config=CONFIG, history=history)


chat = make_chat()




def ask_llm(text):
    global chat
    response = chat.send_message(text)
    usage = response.usage_metadata
    print("[Tokens] input:", usage.prompt_token_count,
          "| output:", usage.candidates_token_count,
          "| total:", usage.total_token_count)

    history = chat.get_history()  # creates a chat; history is optional, so I can restart it with trimmed history
    if len(history) > MAX_MESSAGES:
        chat = make_chat(history[-MAX_MESSAGES:])
    return response.text
def ask_with_retry(text, tries=3):   # tries up to 3 times, waiting 1, 2, 4 seconds (exponential backoff)
    for attempt in range(tries):
        try:
            return ask_llm(text)
        except Exception as e:
            wait = 2 ** attempt
            print("Error:", e)
            if attempt < tries - 1:
                print("Retrying in", wait, "seconds...")
                time.sleep(wait)
    return "Sorry, I could not get an answer. Please try again later."

while True:
    user_text = input("You: ")
    if not user_text.strip():
        continue
    if user_text.lower() in ["quit", "exit"]:
        break
    try:
        print("Bot:", ask_with_retry(user_text))
    except Exception as e:
        print("Something went wrong:", e)