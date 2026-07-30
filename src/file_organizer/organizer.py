from pathlib import Path

from .classifier import get_category
from .mover import move_file


def scan_directory(folder: Path) -> None:
    """
    Scan a directory and organize files.
    """

    total = 0

    print("\nScanning folder...\n")

    for item in folder.iterdir():

        if not item.is_file():
            continue

        category = get_category(item)

        print(f"{item.name:<35} -> {category}")

        move_file(item, category)

        total += 1

    print("-" * 50)
    print(f"Files Organized : {total}")