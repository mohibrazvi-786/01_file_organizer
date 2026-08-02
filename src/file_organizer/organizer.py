from collections import Counter
from pathlib import Path

from .ai_classifier import classify_file
from .mover import move_file

SKIP_FOLDERS = {
    "Documents",
    "Images",
    "Music",
    "Videos",
    "Programming",
    "Finance",
    "Archives",
    "Others",
    "organized_files",
}


def scan_directory(folder: Path) -> None:
    """
    Scan a directory and organize files.
    """

    total = 0
    summary = Counter()

    print("\nScanning folder...\n")

    for item in folder.rglob("*"):

        if not item.is_file():
            continue

        if any(parent.name in SKIP_FOLDERS for parent in item.parents):
            continue

        classification = classify_file(item)

        destination = move_file(item, classification.category)

        print(f"📄 File        : {item.name}")
        print(f"📂 Category    : {classification.category}")
        print(f"🎯 Confidence  : {classification.confidence:.0%}")
        print(f"💡 Reason      : {classification.reason}")
        print(f"📦 Destination : {destination}")
        print("-" * 50)

        summary[classification.category] += 1
        total += 1

    print("\n========== SUMMARY ==========\n")

    for category, count in sorted(summary.items()):
        print(f"{category:<15} : {count}")

    print("\n------------------------------")
    print(f"Total Files Organized : {total}")
