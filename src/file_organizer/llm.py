from google import genai

from .config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return the response text."""

    response = client.models.generate_content(
       model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text