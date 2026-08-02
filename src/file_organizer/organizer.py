from pathlib import Path

from .ai_classifier import classify_file
from .mover import move_file

SKIP_FOLDERS = {
    "Documents",
    "Images",
    "Videos",
    "Music",
    "Archives",
    "Programming",
    "Finance",
    "Education",
    "Personal",
    "Applications",
    "Others",
}


def scan_directory(folder: Path) -> None:
    """
    Scan a directory recursively and organize files.
    """

    total = 0

    print("\nScanning folder...\n")

    for item in folder.rglob("*"):

        if not item.is_file():
            continue

        if item.parent.name in SKIP_FOLDERS:
            continue

        classification = classify_file(item)

        print(
            f"{item.name:<35} "
            f"-> {classification.category:<15} "
            f"({classification.confidence:.0%})"
        )

        print(f"Reason: {classification.reason}")

        move_file(item, classification.category)

        print()

        total += 1

    print("-" * 50)
    print(f"Files Organized : {total}")
