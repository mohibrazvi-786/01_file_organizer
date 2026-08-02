def build_classification_prompt(filename: str) -> str:
    """
    Build a prompt for Gemini.
    """

    return f"""
You are an expert file organizer.

Classify this file.

Filename:
{filename}

Choose ONE category from:

Documents
Images
Videos
Music
Archives
Programming
Finance
Education
Personal
Applications
Others

Return ONLY valid JSON.

Example:

{{
    "category": "Images",
    "confidence": 0.98,
    "reason": "PNG image"
}}
"""
