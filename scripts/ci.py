import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_script(script_name: str) -> None:
    """
    Execute another developer script.
    """

    print("\n" + "=" * 60)
    print(f"Running {script_name}")
    print("=" * 60)

    result = subprocess.run(
        [
            sys.executable,
            f"scripts/{script_name}",
        ],
        cwd=PROJECT_ROOT,
    )

    if result.returncode != 0:
        print(f"\n❌ {script_name} failed.")
        sys.exit(result.returncode)

    print(f"\n✅ {script_name} completed.")


def main() -> None:
    run_script("check.py")
    run_script("dev.py")

    print("\n" + "=" * 60)
    print("🚀 Development pipeline completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
