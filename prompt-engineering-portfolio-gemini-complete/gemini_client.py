import os
from pathlib import Path
import time

from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

MODEL = "gemini-3.8-flash"
MAX_ATTEMPTS = 3

def generate(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Set it in your terminal before running the app."
        )

    client = genai.Client(api_key=api_key)
    for attempt in range(MAX_ATTEMPTS):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
            )
            break
        except APIError as error:
            if error.code != 503:
                raise
            if attempt == MAX_ATTEMPTS - 1:
                raise RuntimeError(
                    "Gemini is temporarily busy. Please wait a minute and try again."
                ) from error
            time.sleep(2**attempt)

    return response.text or "No response was generated."
