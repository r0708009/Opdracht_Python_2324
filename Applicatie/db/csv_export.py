import sqlite3
import csv

conn = sqlite3.connect('soldaten_database.db')
cursor = conn.cursor()

query = """
    SELECT s.voornaam, s.familienaam, s.geboortedatum, s.stamnummer, s.rang, s.component, w.serienummer
    FROM soldaten s
    INNER JOIN wapens w ON s.wapen_serienummer = w.serienummer
"""

cursor.execute(query)

data = cursor.fetchall()

csv_file_path = './exported_data/soldaten_en_wapens_csv.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow([i[0] for i in cursor.description])
    
    csv_writer.writerows(data)


conn.close()

print(f"Gegevens zijn succesvol naar '{csv_file_path}' geschreven.")
