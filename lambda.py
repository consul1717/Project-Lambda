from pathlib import Path
import hashlib
import sys

LAB = Path(__file__).resolve().parent / "demo_lab"
FILES = LAB / "files"
BACKUPS = LAB / "backups"
MARKER = LAB / ".practice_lab"