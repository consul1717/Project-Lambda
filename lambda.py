from pathlib import Path
import hashlib
import sys

LAB = Path(__file__).resolve().parent / "demo_lab"
FILES = LAB / "files"
BACKUPS = LAB / "backups"
MARKER = LAB / ".practice_lab"

SAMPLES = {
    "employees.txt": "Alex: IT\nBob: HR\nCharlie: Finance\nDavid: IT\nEve: HR\nFrank: Finance\nGrace: IT\nHeidi: HR\nIvan: Finance\nJudy: IT\n",
    "budget.txt": "January: 10000\nFebruary: 12000\nMarch: 9000\nApril: 11000\nMay: 13000\nJune: 9500\nJuly: 10500\nAugust: 11500\nSeptember: 12500\nOctober: 13500\nNovember: 14500\nDecember: 15500\n",
    "project.txt": "Project A: In Progress\nProject B: Completed\nProject C: Not Started\nProject D: In Progress\nProject E: Completed\nProject F: Not Started\nProject G: In Progress\nProject H: Completed\nProject I: Not Started\nProject J: In Progress\n"
}

def fingerprint(file):
    if not file.is_file():
        return None
    return hashlib.sha256(file.read_bytes()).hexdigest()

def setup():
    if LAB.exists() or LAB.is_symlink():
        print("Lab already exists. Please remove it before setting up again.")
        return

    FILES.mkdir(parents=True)
    BACKUPS.mkdir()
    MARKER.write_text("Lambda Practice Lab", encoding="utf-8")

    for name, text in SAMPLES.items():
        (FILES / name).write_text(text, encoding="utf-8")
        (BACKUPS / name).write_text(text, encoding="utf-8")
    print("Files and backups created.")

def detect():
    if (LAB.is_symlink() or not MARKER.is_file() or MARKER.is_symlink()
            or not FILES.is_dir() or FILES.is_symlink()
            or not BACKUPS.is_dir() or BACKUPS.is_symlink()):
        print("Run setup first, or check the folder.")
        return

    for name, original in SAMPLES.items():
        file = FILES / name
        backup = BACKUPS / name
        if file.is_symlink() or backup.is_symlink():
            print("Unsafe shortcut found. Terminating Lambda.")
            return
        if not backup.is_file() or backup.read_text(encoding="utf-8") != original:
            print("Backup missing or changed. Terminating Lambda.")
            return
        if file.exists() and not file.is_file():
            print("Unexpected practice file. Terminating Lambda.")
            return

    for name in SAMPLES:
        if fingerprint(FILES / name) != fingerprint(BACKUPS / name):
            print("LAMBDA ALERT:", name, "changed or missing")
        else:
            print("OK:", name)

if len(sys.argv) != 2:
    print("Use: python lambda.py setup | detect")
elif sys.argv[1] == "setup":
    setup()
elif sys.argv[1] == "detect":
    detect()
else:
    print("Unknown command.")