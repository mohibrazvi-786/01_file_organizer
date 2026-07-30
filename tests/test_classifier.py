from pathlib import Path

from src.file_organizer.classifier import get_category


def test_pdf():
    assert get_category(Path("resume.pdf")) == "Documents"


def test_png():
    assert get_category(Path("photo.png")) == "Images"


def test_mp4():
    assert get_category(Path("movie.mp4")) == "Videos"


def test_mp3():
    assert get_category(Path("song.mp3")) == "Music"


def test_unknown():
    assert get_category(Path("abc.xyz")) == "Others"