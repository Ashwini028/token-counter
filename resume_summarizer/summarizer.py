import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(api_version="v1beta"),
)
MODEL = "gemini-3.5-flash-lite"

# path of the folder where this script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESUME_PATH = os.path.join(BASE_DIR, "resume.txt")


def read_resume(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


resume_text = read_resume(RESUME_PATH)
if not resume_text.strip():
    raise SystemExit("resume.txt is empty. Please add some text and run again.")
PROMPT = """You are a helpful resume assistant.
Summarize the resume below in exactly 3 bullet points for a recruiter.
Use only the information in the resume. Do not add anything that is not written there.
Return only the bullet points.

Resume:
\"\"\"
{resume}
\"\"\"
"""


def summarize(text):
    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT.format(resume=text),
        config=types.GenerateContentConfig(temperature=0.2),
    )
    return response.text


def summarize_with_retry(text, tries=3):
    for attempt in range(tries):
        try:
            result = summarize(text)
            if not result or not result.strip():
                return "The model returned an empty answer. Please try again."
            return result
        except Exception as e:
            wait = 2 ** attempt
            print("Error:", str(e)[:200])
            if attempt < tries - 1:
                print("Retrying in", wait, "seconds...")
                time.sleep(wait)
    return "Sorry, I could not get a summary. Please try again later."


summary = summarize_with_retry(resume_text)
print("Summary:")
print(summary)