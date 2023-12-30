import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS soldaten(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                voornaam TEXT,
                familienaam TEXT,
                geboortedatum DATE,
                stamnummer TEXT,
                rang TEXT,
                component TEXT,
                wapen_serienummer TEXT,
                FOREIGN KEY(component) REFERENCES component(name),
                FOREIGN KEY(wapen_serienummer) REFERENCES wapens(serienummer)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS wapens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT,
                serienummer TEXT
            )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(e)
