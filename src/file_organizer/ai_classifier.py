import json
from pathlib import Path

from .file_preview import get_file_preview
from .llm import ask_gemini
from .models import FileClassification
from .prompts import build_classification_prompt


def classify_file(file: Path) -> FileClassification:
    """
    Classify a file using Gemini.
    """

    preview = get_file_preview(file)

    prompt = build_classification_prompt(
        filename=file.name,
        preview=preview,
    )

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
