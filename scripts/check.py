import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_step(title: str, command: list[str]) -> None:
    """Run a development tool and stop on failure."""

    print(f"\n{'=' * 60}")
    print(f"Running {title}")
    print(f"{'=' * 60}")

    result = subprocess.run(command, cwd=PROJECT_ROOT)

    if result.returncode != 0:
        print(f"\n❌ {title} failed.")
        sys.exit(result.returncode)

    print(f"\n✅ {title} passed.")


def main() -> None:
    run_step(
        "Black",
        [sys.executable, "-m", "black", "."],
    )

    run_step(
        "Ruff",
        [sys.executable, "-m", "ruff", "check", "."],
    )

    run_step(
        "Pytest",
        [sys.executable, "-m", "pytest"],
    )

    print("\n" + "=" * 60)
    print("🎉 All quality checks passed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
