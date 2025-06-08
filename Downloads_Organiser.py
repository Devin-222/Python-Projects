import os
import shutil
import argparse
import json
from pathlib import Path

# === CONFIG ===
CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Zip Files": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
}
LOG_FILENAME = ".organizer_log.json"

EXTENSION_TO_CATEGORY = {
    ext: category for category, extensions in CATEGORIES.items() for ext in extensions
}

def get_log_path():
    return Path.home() / "Downloads" / LOG_FILENAME

def load_log():
    log_path = get_log_path()
    if log_path.exists():
        with open(log_path, "r") as f:
            return json.load(f)
    return []

def save_log(log_data):
    log_path = get_log_path()
    with open(log_path, "w") as f:
        json.dump(log_data, f, indent=2)

def organize_downloads(dry_run=False):
    downloads_path = Path.home() / "Downloads"
    log = load_log()
    move_log = []

    # Create target folders
    for category in list(CATEGORIES.keys()) + ["Other"]:
        (downloads_path / category).mkdir(parents=True, exist_ok=True)

    for item in downloads_path.iterdir():
        if item.is_file():
            if item.name == LOG_FILENAME:
                continue  # Skip the log file itself

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

    # Save batch if real run
    if not dry_run and move_log:
        next_batch_id = (log[-1]["batch_id"] + 1) if log else 1
        log.append({"batch_id": next_batch_id, "moves": move_log})
        save_log(log)

def undo_moves():
    log = load_log()
    if not log:
        print("❌ Nothing to undo.")
        return

    last_batch = log.pop()
    print(f"⏪ Undoing batch #{last_batch['batch_id']}")

    for move in reversed(last_batch["moves"]):
        src = Path(move["to"])
        dst = Path(move["from"])

        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            counter = 1
            original_dst = dst
            while dst.exists():
                dst = original_dst.with_name(f"{original_dst.stem}_undo{counter}{original_dst.suffix}")
                counter += 1

            shutil.move(str(src), str(dst))
            print(f"✅ Restored: {src.name} -> {dst}")
        else:
            print(f"⚠️ File missing: {src} — cannot restore.")

    # Update or remove log
    if log:
        save_log(log)
    else:
        get_log_path().unlink()
        print("🗑️ All batches undone. Log file removed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize Downloads Folder")
    parser.add_argument("--dry-run", action="store_true", help="Preview of what would be moved")
    parser.add_argument("--undo", action="store_true", help="Undo the last organization batch")
    args = parser.parse_args()

    if args.undo:
        undo_moves()
    else:
        organize_downloads(dry_run=args.dry_run)
