import sqlite3
import os

chrome_db = os.path.expanduser("~") + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

conn = sqlite3.connect(chrome_db)
cursor = conn.cursor()
cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")

for row in cursor.fetchall():
    print(f"URL: {row[0]}, Title: {row[1]}")

conn.close(
