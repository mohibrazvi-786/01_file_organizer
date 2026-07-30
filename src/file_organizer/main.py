from pathlib import Path

from src.file_organizer.organizer import scan_directory


def print_banner() -> None:
    """Display application banner."""

    print("=" * 50)
    print("🚀 Smart File Organizer")
    print("=" * 50)
    print()


def get_target_directory() -> Path:
    """Read folder from user."""

    folder = input("📂 Enter folder path: ").strip()

    return Path(folder)


def main() -> None:
    """Application entry point."""

    print_banner()

    directory = get_target_directory()

    if not directory.exists():
        print("\n❌ Folder does not exist.")
        return

    if not directory.is_dir():
        print("\n❌ This is not a directory.")
        return

    print("\nScanning folder...\n")

    files = scan_directory(directory)

    for file in files:
        print(f"📄 {file.name}")

    print("\n" + "-" * 40)
    print(f"Total files : {len(files)}")


if __name__ == "__main__":
    main()