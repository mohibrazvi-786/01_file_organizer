from pathlib import Path

FILE_CATEGORIES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    ".mp3": "Music",
    ".wav": "Music",

    ".zip": "Archives",
    ".rar": "Archives",

    ".exe": "Applications",

    ".py": "Python",
}


def get_category(file: Path) -> str:
    """
    Return the category of a file based on its extension.
    """

    extension = file.suffix.lower()

    return FILE_CATEGORIES.get(extension, "Others")