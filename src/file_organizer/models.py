from dataclasses import dataclass


@dataclass(slots=True)
class FileClassification:
    """
    Represents the AI's classification result.
    """

    category: str
    confidence: float
    reason: str
