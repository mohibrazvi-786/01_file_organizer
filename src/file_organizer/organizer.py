from pathlib import Path


def scan_directory(directory: Path) -> list[Path]:
    """
    Scan a directory and return all files.
    """

    files: list[Path] = []

    for item in directory.iterdir():
        if item.is_file():
            files.append(item)

    return files