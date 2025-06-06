import os
import shutil
import argparse
import json
from pathlib import Path

# Define categories and extensions
CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Zip Files": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
}

EXTENSION_TO_CATEGORY = {
    ext: category for category, extensions in CATEGORIES.items() for ext in extensions
}

LOG_FILENAME = ".organizer_log.json"

# Organise Downloads folder function
# Additional option to do a dry run showing all the changes that will be made before you commit
def organize_downloads(dry_run=False):
    downloads_path = Path.home() / "Downloads"
    log_path = downloads_path / LOG_FILENAME
    move_log = []

    for category in list(CATEGORIES.keys()) + ["Other"]:
        category_path = downloads_path / category
        category_path.mkdir(parents=True, exist_ok=True)

    for item in downloads_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            category = EXTENSION_TO_CATEGORY.get(ext, "Other")
            destination = downloads_path / category / item.name

            counter = 1
            while destination.exists():
                destination = downloads_path / category / f"{item.stem}_{counter}{item.suffix}"
                counter += 1

            if dry_run:
                print(f"[Dry Run] Would move: {item.name} -> {category}/")
            else:
                shutil.move(str(item), str(destination))
                move_log.append({
                    "from": str(item.resolve()),
                    "to": str(destination.resolve())
                })
                print(f"Moved: {item.name} -> {category}/")

    if not dry_run and move_log:
        with open(log_path, "w") as log_file:
            json.dump(move_log, log_file, indent=2)

# Function to revert the effects of the organise_downloads function
def undo_moves():
    downloads_path = Path.home() / "Downloads"
    log_path = downloads_path / LOG_FILENAME

    if not log_path.exists():
        print("No move log found. Nothing to undo.")
        return

    with open(log_path, "r") as log_file:
        move_log = json.load(log_file)

    for entry in move_log:
        src = Path(entry["to"])
        dst = Path(entry["from"])

        if src.exists():
            dst_parent = dst.parent
            dst_parent.mkdir(parents=True, exist_ok=True)

            counter = 1
            original_dst = dst
            while dst.exists():
                dst = original_dst.with_name(f"{original_dst.stem}_undo{counter}{original_dst.suffix}")
                counter += 1

            shutil.move(str(src), str(dst))
            print(f"Restored: {src.name} -> {dst}")

        else:
            print(f"Skipped missing file: {src}")

    log_path.unlink()
    print("🗑️ Undo complete. Log file deleted.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize Downloads Folder")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without moving files")
    parser.add_argument("--undo", action="store_true", help="Undo last file organization")
    args = parser.parse_args()

    if args.undo:
        undo_moves()
    else:
        organize_downloads(dry_run=args.dry_run)
