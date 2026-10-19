"""Create an empty Mcode.db from schema.sql."""
import os
import sqlite3

if os.path.exists("Mcode.db"):
    raise SystemExit("Mcode.db already exists, delete it first to start over.")

with open("schema.sql", encoding="utf-8") as f:
    sqlite3.connect("Mcode.db").executescript(f.read())
print("Created an empty Mcode.db")
