from pathlib import Path
import shutil


def move_file(file: Path, category: str) -> None:
    """
    Move a file into its category folder.
    """

    destination_folder = file.parent / category
    destination_folder.mkdir(exist_ok=True)

    destination = destination_folder / file.name

    shutil.move(str(file), str(destination))

    print(f"Moved: {file.name} -> {category}/")