import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE = PROJECT_ROOT / "sample_files"
WORKSPACE = PROJECT_ROOT / "test_workspace"


def main():

    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)

    shutil.copytree(SOURCE, WORKSPACE)

    print("Workspace prepared successfully!")
    print(f"Source    : {SOURCE}")
    print(f"Workspace : {WORKSPACE}")


if __name__ == "__main__":
    main()
