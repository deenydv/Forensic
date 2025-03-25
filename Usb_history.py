import os

print("[INFO] Extracting USB history...")
os.system("reg query HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USBSTOR /s"
