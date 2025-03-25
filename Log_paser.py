import re

log_file = "/var/log/auth.log"
pattern = r"Failed password|Accepted password"

with open(log_file, "r") as file:
    for line in file:
        if re.search(pattern, line):
            print(line.strip()
