from pathlib import Path

from src.file_organizer.organizer import scan_directory


def test_scan_directory():
    folder = Path("sample_files")

    scan_directory(folder)

    assert folder.exists()