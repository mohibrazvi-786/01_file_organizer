from pathlib import Path

from docx import Document
from pypdf import PdfReader

TEXT_EXTENSIONS = {
    ".txt",
    ".md",
    ".py",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
    ".html",
    ".css",
    ".js",
}


def _read_text_file(file: Path, max_chars: int) -> str:
    """Read plain text files."""

    return file.read_text(
        encoding="utf-8",
        errors="ignore",
    )[:max_chars]


def _read_pdf(file: Path, max_chars: int) -> str:
    """Read text from a PDF."""

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

        if len(text) >= max_chars:
            break

    return text[:max_chars]


def _read_docx(file: Path, max_chars: int) -> str:
    """Read text from a Word document."""

    document = Document(file)

    text = "\n".join(paragraph.text for paragraph in document.paragraphs)

    return text[:max_chars]


def get_file_preview(
    file: Path,
    max_chars: int = 1000,
) -> str:
    """
    Return a preview of a supported file.
    """

    suffix = file.suffix.lower()

    try:

        if suffix in TEXT_EXTENSIONS:
            return _read_text_file(file, max_chars)

        if suffix == ".pdf":
            return _read_pdf(file, max_chars)

        if suffix == ".docx":
            return _read_docx(file, max_chars)

    except Exception:
        pass

    return ""
