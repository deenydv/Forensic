import os

image_path = "disk_image.dd"
output_folder = "extracted_files"

print("[INFO] Extracting files from disk image...")
os.system(f"foremost -i {image_path} -o {output_folder}")

print(f"[INFO] Files extracted to '{output_folder}'"
