from src.file_organizer.llm import ask_gemini


def main() -> None:
    response = ask_gemini("Say hello in exactly three words.")
    print(response)


if __name__ == "__main__":
    main()