import os
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def batch_convert_heic_to_jpg(src_dir, dest_dir):
    src_path = Path(src_dir)
    dest_path = Path(dest_dir)

    if not dest_path.exists():
        dest_path.mkdir(parents=True, exist_ok=True)
        print(f"Directory created: {dest_path}")

    heic_files = list(src_path.glob('*.[hH][eE][iI][cC]'))
    
    if not heic_files:
        print(f"No HEIC files found in {src_path}")
        return

    print(f"Found {len(heic_files)} files. Starting conversion...")

    for file in heic_files:
        try:
            image = Image.open(file)
            target_file = dest_path / f"{file.stem}.jpg"
            image.save(target_file, "JPEG", quality=95)
            print(f"✅ Success: {file.name} -> {target_file.name}")
            
        except Exception as e:
            print(f"❌ Failed: {file.name} - Error: {e}")

if __name__ == "__main__":
    SOURCE = "./HEIC"
    DESTINATION = "./JPG"
    
    batch_convert_heic_to_jpg(SOURCE, DESTINATION)
    print("\nAll tasks are completed!")
