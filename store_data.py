import sqlite3

def create_connection():
    conn = sqlite3.connect('air_quality_data.db')
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS measurements (
        id INTEGER PRIMARY KEY,
        city TEXT NOT NULL,
        parameter TEXT NOT NULL,
        value REAL NOT NULL,
        unit TEXT NOT NULL,
        date_utc TEXT NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL
    )
    """)

    conn.commit()

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    conn.close()