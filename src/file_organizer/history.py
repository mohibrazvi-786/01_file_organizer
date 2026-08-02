import json
from pathlib import Path

from .models import FileClassification

HISTORY_DIR = Path("history")
HISTORY_FILE = HISTORY_DIR / "organization_history.json"


def save_history(
    filename: str,
    classification: FileClassification,
    destination: Path,
) -> None:
    """
    Save an organization event.
    """

    HISTORY_DIR.mkdir(exist_ok=True)

    history = []

    if HISTORY_FILE.exists():
        history = json.loads(HISTORY_FILE.read_text())

    history.append(
        {
            "filename": filename,
            "category": classification.category,
            "confidence": classification.confidence,
            "reason": classification.reason,
            "destination": str(destination),
        }
    )

    HISTORY_FILE.write_text(
        json.dumps(
            history,
            indent=4,
        )
    )
