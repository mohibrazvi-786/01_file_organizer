from pathlib import Path

from src.file_organizer.classifier import get_category


def main() -> None:
    print(get_category(Path("resume.pdf")))
    print(get_category(Path("photo.jpg")))
    print(get_category(Path("movie.mp4")))
    print(get_category(Path("song.mp3")))
    print(get_category(Path("unknown.xyz")))


if __name__ == "__main__":
    main()