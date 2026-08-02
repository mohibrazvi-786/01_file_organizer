import sys
from pathlib import Path

from .organizer import scan_directory


def main() -> None:
    print("=" * 50)
    print("Smart File Organizer")
    print("=" * 50)

    # Developer mode
    if len(sys.argv) > 1:
        folder = Path(sys.argv[1])

    # Interactive mode
    else:
        folder = Path(input("\nEnter folder path: ").strip())

    if not folder.exists():
        print("\nFolder does not exist.")
        return

    scan_directory(folder)


if __name__ == "__main__":
    main()
