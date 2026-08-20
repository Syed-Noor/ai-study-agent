import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. Check your .env file."
    )

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.1-flash-lite"


def ask_llm(messages):

    prompt_parts = []

    for message in messages:

        role = message.get("role", "user")
        content = message.get("content", "")

        if role == "system":
            prompt_parts.append(
                f"SYSTEM:\n{content}"
            )

        elif role == "user":
            prompt_parts.append(
                f"USER:\n{content}"
            )

        elif role == "assistant":
            prompt_parts.append(
                f"ASSISTANT:\n{content}"
            )

    prompt = "\n\n".join(prompt_parts)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text