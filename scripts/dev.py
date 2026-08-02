import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE = PROJECT_ROOT / "sample_files"
WORKSPACE = PROJECT_ROOT / "test_workspace"


def prepare_workspace() -> None:
    """Create a fresh copy of the sample files."""

    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)

    shutil.copytree(SOURCE, WORKSPACE)

    print("\n✅ Workspace prepared")
    print(f"Source    : {SOURCE}")
    print(f"Workspace : {WORKSPACE}")


def run_application() -> None:
    """Launch the Smart File Organizer."""

    print("\n🚀 Starting Smart File Organizer...\n")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "src.file_organizer.main",
            str(WORKSPACE),
        ],
        cwd=PROJECT_ROOT,
    )


def main() -> None:
    prepare_workspace()
    run_application()


if __name__ == "__main__":
    main()
