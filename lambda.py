from pathlib import Path
import hashlib
import sys

# Define directory paths relative to script's current location
LAB = Path(__file__).resolve().parent / "demo_lab"
FILES = LAB / "files"
BACKUPS = LAB / "backups"
MARKER = LAB / ".practice_lab"

# Sample text files for testing
SAMPLES = {
    "employees.txt": "Alex: IT\nBob: HR\nCharlie: Finance\nDavid: IT\nEve: HR\nFrank: Finance\nGrace: IT\nHeidi: HR\nIvan: Finance\nJudy: IT\n",
    "budget.txt": "January: 10000\nFebruary: 12000\nMarch: 9000\nApril: 11000\nMay: 13000\nJune: 9500\nJuly: 10500\nAugust: 11500\nSeptember: 12500\nOctober: 13500\nNovember: 14500\nDecember: 15500\n",
    "project.txt": "Project A: In Progress\nProject B: Completed\nProject C: Not Started\nProject D: In Progress\nProject E: Completed\nProject F: Not Started\nProject G: In Progress\nProject H: Completed\nProject I: Not Started\nProject J: In Progress\n"
}

# File corruption string simulation
DAMAGED = "FILE CORRUPTED.\n"

def safe_lab():
    # Verify environment, marker, and backups are intact
    # Check if the marker file and required directories exist
    if not MARKER.is_file() or not FILES.is_dir() or not BACKUPS.is_dir():
        print("Run `python lambda.py setup` first.")
        return False

    # Collect all symlinks to check for security issues
    paths = [LAB, FILES, BACKUPS, MARKER]
    paths += [folder / name for folder in (FILES, BACKUPS) for name in SAMPLES]
    if any(path.is_symlink() for path in paths):
        print("Unsafe shortcut found. Terminating LAMBDA.")
        return False

    # Check original backup files match sample text
    for name, text in SAMPLES.items():
        backup = BACKUPS / name
        file = FILES / name
        if not backup.is_file() or backup.read_text(encoding="utf-8") != text:
            print("Original backup is missing or changed. Terminating LAMBDA.")
            return False
        if file.exists() and not file.is_file():
            print("Unexpected file. Terminating LAMBDA")
            return False
    return True

def fingerprint(file):
    # Generate SHA-256 hash of file's contents
    if not file.is_file():
        return None
    return hashlib.sha256(file.read_bytes()).hexdigest()

def setup():
    # Create lab directory, populate sample files and backups
    if LAB.exists() or LAB.is_symlink():
        print("Lab already exists. Please remove it before setting up again.")
        return

    # Create directories and write lab marker
    FILES.mkdir(parents=True)
    BACKUPS.mkdir()
    MARKER.write_text("Lambda Practice Lab", encoding="utf-8")

    # Write sample contents to both files and backup directories
    for name, text in SAMPLES.items():
        (FILES / name).write_text(text, encoding="utf-8")
        (BACKUPS / name).write_text(text, encoding="utf-8")
    print("Files and backups created.")

def simulate():
    # Simulate file corruption, overwrite files with damaged data
    if not safe_lab():
        return

    # Verify files haven't been altered before simulation
    for name, original in SAMPLES.items():
        file = FILES / name
        if not file.is_file() or file.read_text(encoding="utf-8") != original:
            print("Files have changed. Terminating LAMBDA.")
            return

    # Overwrite each file with file corruption string simulation
    for name in SAMPLES:
        (FILES / name).write_text(DAMAGED, encoding="utf-8")
        print("SIMULATED DAMAGE:", name)

def detect():
    # Compare files against backups using SHA-256 hashes to detect changes
    if not safe_lab():
        return
    for name in SAMPLES:
        # Check if file has is different from backup
        if fingerprint(FILES / name) != fingerprint(BACKUPS / name):
            print("LAMBDA ALERT:", name, "changed or missing")
        else:
            print("OK:", name)

def recover():
    # Restore files from their clean backups
    if not safe_lab():
        return

    # Check files only contain original or known file corruption string simulation
    for name, original in SAMPLES.items():
        file = FILES / name
        if file.exists() and file.read_text(encoding="utf-8") not in (original, DAMAGED):
            print("Unexpected contents. Terminating LAMBDA.")
            return

    # Copy exact bytes from backup to files
    for name in SAMPLES:
        (FILES / name).write_bytes((BACKUPS / name).read_bytes())
        print("RESTORED:", name)
    detect()

# CLI dispatcher
if len(sys.argv) != 2:
    print("Lambda use: python lambda.py setup | simulate | detect")
elif sys.argv[1] == "setup":
    setup()
elif sys.argv[1] == "simulate":
    simulate()
elif sys.argv[1] == "detect":
    detect()
elif sys.argv[1] == "recover":
    recover()
else:
    print("Unknown command.")