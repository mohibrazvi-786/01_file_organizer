def build_classification_prompt(
    filename: str,
    preview: str,
) -> str:
    """
    Build the prompt sent to Gemini.
    """

    return f"""
You are an intelligent file classifier.

Classify the following file into ONE category.

Allowed categories:

- Documents
- Images
- Videos
- Music
- Programming
- Finance
- Archives
- Others

Filename:
{filename}

Content Preview:
{preview}

Respond ONLY with valid JSON.

Example:

{{
    "category": "Programming",
    "confidence": 0.98,
    "reason": "Python source code."
}}
"""
