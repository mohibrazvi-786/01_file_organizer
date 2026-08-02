import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_FOLDER = PROJECT_ROOT / "organized_files"


def move_file(file: Path, category: str) -> None:
    """
    Move a file into the organized_files directory.
    """

    destination_folder = OUTPUT_FOLDER / category
    destination_folder.mkdir(parents=True, exist_ok=True)

    destination = destination_folder / file.name

    shutil.move(str(file), str(destination))

    print(f"Moved: {file.name} -> organized_files/{category}/")
