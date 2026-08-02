from pathlib import Path

from .file_preview import get_file_preview
from .llm import ask_gemini
from .models import FileClassification
from .prompts import build_classification_prompt
from .rule_classifier import classify_by_extension


def classify_file(file: Path) -> FileClassification:
    """
    Hybrid classifier.

    1. Try rule-based classification.
    2. If unknown, ask Gemini.
    3. If Gemini fails, return a safe fallback.
    """

    # Step 1: Fast rule-based classification
    classification = classify_by_extension(file)

    if classification is not None:
        return classification

    # Step 2: AI classification
    preview = get_file_preview(file)
    prompt = build_classification_prompt(file.name, preview)

    try:
        return ask_gemini(prompt)

    except Exception as error:
        print("\n========== AI ERROR ==========")
        print(error)
        print("==============================")

        return FileClassification(
            category="Others",
            confidence=0.0,
            reason="AI classification failed.",
        )
