"""Simple script to build an executable for the current platform."""

import subprocess
import sys
import platform


def main():
    # Ensure PyInstaller is available
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    target_name = "square_cli"
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name",
        target_name,
        "square.py",
    ]
    subprocess.run(cmd, check=True)
    if platform.system() == "Windows":
        suffix = ".exe"
    else:
        suffix = ""
    print(f"Executable created: dist/{target_name}{suffix}")


if __name__ == "__main__":
    main()
