from google import genai
from src.file_organizer.config import GEMINI_API_KEY


def main() -> None:
    client = genai.Client(api_key=GEMINI_API_KEY)

    print("\nAvailable Gemini Models\n")
    print("-" * 60)

    for model in client.models.list():
        print(model.name)


if __name__ == "__main__":
    main()
