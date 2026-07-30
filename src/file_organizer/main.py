from pathlib import Path

from src.file_organizer.organizer import scan_directory


def print_banner() -> None:
    """Display application banner."""

    print("=" * 50)
    print("Smart File Organizer")
    print("=" * 50)
    print()


def get_target_directory() -> Path:
    """Read folder from user."""

    folder = input("Enter folder path: ").strip()
    return Path(folder)


def main() -> None:
    """Application entry point."""

    print_banner()

    directory = get_target_directory()

    if not directory.exists():
        print("\nFolder does not exist.")
        return

    if not directory.is_dir():
        print("\nThis is not a directory.")
        return

    scan_directory(directory)


if __name__ == "__main__":
    main()
