import argparse
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE = PROJECT_ROOT / "sample_files"
WORKSPACE = PROJECT_ROOT / "test_workspace"


def run(command: list[str]) -> None:
    """Run a command and stop if it fails."""

    result = subprocess.run(command, cwd=PROJECT_ROOT)

    if result.returncode != 0:
        sys.exit(result.returncode)


def prepare_workspace() -> None:
    """Create a fresh test workspace."""

    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)

    shutil.copytree(SOURCE, WORKSPACE)

    print("✅ Workspace prepared")


def clean_workspace() -> None:
    """Delete generated workspace."""

    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)

    print("✅ Workspace cleaned")


def check() -> None:
    print("\nRunning Black...")
    run([sys.executable, "-m", "black", "."])

    print("\nRunning Ruff...")
    run([sys.executable, "-m", "ruff", "check", "."])

    print("\nRunning Pytest...")
    run([sys.executable, "-m", "pytest"])

    print("\n🎉 All checks passed!")


def dev() -> None:
    prepare_workspace()

    run(
        [
            sys.executable,
            "-m",
            "src.file_organizer.main",
            str(WORKSPACE),
        ]
    )


def ci() -> None:
    check()
    dev()


def main() -> None:
    parser = argparse.ArgumentParser(description="Developer tasks")

    parser.add_argument(
        "task",
        choices=[
            "check",
            "prepare",
            "clean",
            "dev",
            "ci",
        ],
    )

    args = parser.parse_args()

    if args.task == "check":
        check()

    elif args.task == "prepare":
        prepare_workspace()

    elif args.task == "clean":
        clean_workspace()

    elif args.task == "dev":
        dev()

    elif args.task == "ci":
        ci()


if __name__ == "__main__":
    main()
