import sys
sys.path.append('modules/database module')


from database import create_connection, create_tables

def main():
    database = "db/soldaten_database.db"
    conn = create_connection(database)
    if conn is not None:
        create_tables(conn)
        print("Tabellen zijn aangemaakt.")
    else:
        print("Er is een fout opgetreden.")

if __name__ == '__main__':
    main()
