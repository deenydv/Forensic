import hashlib

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

file_path = "evidence_file.txt"
hash_value = calculate_hash(file_path)
print(f"SHA-256 Hash: {hash_value}"
