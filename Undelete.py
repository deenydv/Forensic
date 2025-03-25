import os

partition = "/dev/sda1"
output_folder = "recovered_files"

print("[INFO] Recovering deleted files...")
os.system(f"photorec /cmd {partition} recovered_files options,enable,search")

print(f"[INFO] Recovered files saved to '{output_folder}'"
