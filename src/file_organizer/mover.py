import shutil
from pathlib import Path


def move_file(file: Path, category: str) -> Path:
    """
    Move a file into its category folder.

    Returns:
        The destination path.
    """

    destination_folder = Path("organized_files") / category
    destination_folder.mkdir(parents=True, exist_ok=True)

    destination = destination_folder / file.name

    shutil.move(str(file), str(destination))

    return destination
