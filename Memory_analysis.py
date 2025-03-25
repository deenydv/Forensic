import os

memory_dump = "memory.dmp"

print("[INFO] Extracting running processes from memory dump...")
os.system(f"volatility -f {memory_dump} --profile=Win7SP1x64 pslist"
