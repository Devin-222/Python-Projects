import os
import shutil

# Set your folder paths here
jpeg_folder = r"C:\Users\devin\imagecomp\JPEGs"
raw_folder = r"C:\Users\devin\imagecomp\RAWs"
raw_delete_folder = r"C:\Users\devin\imagecomp\RawDelete"

# Create delete folder if it doesn't exist
os.makedirs(raw_delete_folder, exist_ok=True)

# Get set of all JPEG base filenames (without extension), lowercase for safety
jpeg_files = os.listdir(jpeg_folder)
jpeg_basenames = {os.path.splitext(f)[0].lower() for f in jpeg_files if f.lower().endswith(('.jpg', '.jpeg'))}

# Loop through all RAW files
for raw_file in os.listdir(raw_folder):
    raw_path = os.path.join(raw_folder, raw_file)
    if os.path.isfile(raw_path):
        raw_name, raw_ext = os.path.splitext(raw_file)
        raw_name_lower = raw_name.lower()
        
        # If no matching jpeg filename found, move the RAW file
        if raw_name_lower not in jpeg_basenames:
            print(f"Moving {raw_file} to delete folder")
            shutil.move(raw_path, os.path.join(raw_delete_folder, raw_file))
