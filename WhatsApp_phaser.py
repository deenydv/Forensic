import sqlite3

db_path = "msgstore.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT key_remote_jid, data, timestamp FROM messages")

for row in cursor.fetchall():
    print(f"Chat ID: {row[0]}, Message: {row[1]}, Timestamp: {row[2]}")

conn.close(
