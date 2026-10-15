#!/usr/bin/env python3
"""One-time setup after cloning: enable the repo's git hooks.

    python bootstrap.py            enable hooks, check the trackers
    python bootstrap.py --install  also pip install -r requirements.txt

Needs only the standard library.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(*cmd):
    subprocess.run(cmd, cwd=ROOT, check=True)


def main():
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10+ is required.")
    run("git", "config", "core.hooksPath", ".githooks")
    hook = ROOT / ".githooks" / "pre-commit"
    try:
        hook.chmod(hook.stat().st_mode | 0o111)
    except OSError:
        pass
    print("git hooks enabled: README.md refreshes on every commit.")
    if "--install" in sys.argv:
        run(sys.executable, "-m", "pip", "install", "-r", "requirements.txt")
    run(sys.executable, "master.py", "--check")
    print("Setup OK. Run `pytest` to check the tests.")


if __name__ == "__main__":
    main()
