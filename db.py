import sqlite3
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS plate_reads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plate_text TEXT,
        confidence REAL,
        timestamp TEXT,
        track_id TEXT,
        image_path TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_to_db(item):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO plate_reads (plate_text, confidence, timestamp, track_id, image_path)
        VALUES (?, ?, ?, ?, ?)
    """, (item["plate_text"], item["confidence"], item["timestamp"],
          item["track_id"], item["image_path"]))
    conn.commit()
    conn.close()
