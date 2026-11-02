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

