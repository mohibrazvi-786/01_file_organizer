from pathlib import Path

from .models import FileClassification

EXTENSION_MAP = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".py": "Programming",
    ".js": "Programming",
    ".java": "Programming",
    ".cpp": "Programming",
    ".c": "Programming",
}


def classify_by_extension(file: Path) -> FileClassification | None:
    """
    Classify using the file extension.

    Returns None if the extension is unknown.
    """

    extension = file.suffix.lower()

    category = EXTENSION_MAP.get(extension)

    if category is None:
        return None

    return FileClassification(
        category=category,
        confidence=1.0,
        reason=f"Matched extension '{extension}'.",
    )
