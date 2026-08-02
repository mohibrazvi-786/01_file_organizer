import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def validate_config() -> None:
    """Validate required environment variables."""

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found.")
