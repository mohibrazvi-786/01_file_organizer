import json
from pathlib import Path

from .llm import ask_gemini
from .models import FileClassification
from .prompts import build_classification_prompt


def classify_file(file: Path) -> FileClassification:
    """
    Classify a file using Gemini.
    """

    prompt = build_classification_prompt(file.name)

    try:
        response = ask_gemini(prompt)

        print("\n========== GEMINI RESPONSE ==========")
        print(response)
        print("=====================================\n")

        data = json.loads(response)

        return FileClassification(
            category=data["category"],
            confidence=float(data["confidence"]),
            reason=data["reason"],
        )

    except Exception as error:
        print("\n========== AI ERROR ==========")
        print(error)
        print("==============================\n")

        return FileClassification(
            category="Others",
            confidence=0.0,
            reason="AI classification failed.",
        )
