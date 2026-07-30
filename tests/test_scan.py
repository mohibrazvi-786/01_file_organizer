from pathlib import Path

def scan_directory(folder: Path) -> None:
    print(folder)

    for item in folder.iterdir():
        print(item)
        print("Is File:", item.is_file())