import time

from google import genai

from .config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini and automatically retry
    on temporary server failures.
    """

    delays = [1, 2, 4]

    for attempt, delay in enumerate(delays, start=1):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )

            return response.text

        except Exception as error:

            message = str(error)

            if "503" in message or "UNAVAILABLE" in message:

                print(
                    f"Gemini temporarily unavailable "
                    f"(attempt {attempt}/{len(delays)}). "
                    f"Retrying in {delay} second(s)..."
                )

                time.sleep(delay)
                continue

            raise

    raise RuntimeError("Gemini is unavailable after multiple retry attempts.")
