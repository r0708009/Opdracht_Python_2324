from soldaat import Soldaat
import sqlite3

class SoldaatController:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def voeg_soldaat_toe(self, soldaat):
        query = "INSERT INTO soldaten (voornaam, familienaam, geboortedatum, stamnummer, rang, component, wapen_serienummer) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (soldaat.voornaam, soldaat.familienaam, soldaat.geboortedatum,soldaat.stamnummer, soldaat.rang, soldaat.component, soldaat.wapen_serienummer))
        self.conn.commit()

    def controleer_stamnummer(self, stamnummer):
        query = "SELECT COUNT(*) FROM soldaten WHERE stamnummer = ?"
        self.cursor.execute(query, (stamnummer,))
        result = self.cursor.fetchone()[0]
        return result > 0

    def verwijder_soldaat(self, soldaat_id):
        query = "DELETE FROM soldaten WHERE id = ?"
        self.cursor.execute(query, (soldaat_id,))
        self.conn.commit()

    def update_soldaat_met_stamnummer(self, nieuwe_voornaam, nieuwe_familienaam, nieuwe_geboortedatum, nieuw_stamnummer, nieuwe_rang, nieuwe_component, nieuw_serienummer, soldaat_id):
        query = "UPDATE soldaten SET voornaam = ?, familienaam = ?, geboortedatum = ?, stamnummer = ?, rang = ?, component = ?, wapen_serienummer = ? WHERE id = ?"
        self.cursor.execute(query, (nieuwe_voornaam, nieuwe_familienaam, nieuwe_geboortedatum, nieuw_stamnummer, nieuwe_rang, nieuwe_component, nieuw_serienummer, soldaat_id))
        self.conn.commit()

    def update_soldaat_zonder_stamnummer(self, nieuwe_voornaam, nieuwe_familienaam, nieuwe_geboortedatum, stamnummer, nieuwe_rang, nieuwe_component,nieuw_serienummer, soldaat_id):
        query = "UPDATE soldaten SET voornaam = ?, familienaam = ?, geboortedatum = ?, stamnummer = ?, rang = ?, component = ?, wapen_serienummer = ? WHERE id = ?"
        self.cursor.execute(query, (nieuwe_voornaam, nieuwe_familienaam, nieuwe_geboortedatum, stamnummer, nieuwe_rang, nieuwe_component, nieuw_serienummer, soldaat_id))
        self.conn.commit()

    def krijg_soldaat_by_id(self, soldaat_id):
        query = "SELECT * FROM soldaten WHERE id = ?"
        self.cursor.execute(query, (soldaat_id,))
        soldaat_info = self.cursor.fetchone()

        if soldaat_info:
            soldaat = Soldaat(*soldaat_info)
            return soldaat
        else:
            return None

    def krijg_alle_soldaten(self):
        query = "SELECT * FROM soldaten"
        self.cursor.execute(query)
        soldaten = self.cursor.fetchall()
        return soldaten

    def zoek_soldaat_op_naam(self, voornaam, familienaam):
        query = "SELECT * FROM soldaten WHERE voornaam = ? AND familienaam = ?"
        self.cursor.execute(query, (naam,))
        soldaten = self.cursor.fetchall()
        return soldaten

    def krijg_soldaten_van_component(self, comonent):
        query = "SELECT * FROM soldaten WHERE component = ?"
        self.cursor.execute(query, (component,))
        soldaten = self.cursor.fetchall()
        return soldaten

    def krijg_component_van_soldaat(self, voornaam, familienaam):
        query = "SELECT component FROM  soldaten WHERE voornaam = ? AND familienaam = ?"
        self.cursor.execute(query, (voornaam, familienaam))
        soldaat = self.cursor.fetchone()
        return soldaat

    def krijg_soldaten_via_wapen_naam(self, wapen_naam):
        query = "SELECT Soldaten.* FROM soldaten JOIN Wapens ON Soldaten.wapen_id = Wapens.wapen_id WHERE Wapens.naam = ?"
        self.cursor.execute(query, (wapen_naam,))
        soldaten = self.cursor.fetchall()
        return soldaten

    def check_wapen_voor_verwijdering(serienummer):
        query = "SELECT COUNT(*) FROM soldaten WHERE wapen_serienummer = ?"
        connection = sqlite3.connect("././db/soldaten_database.db")
        cursor = connection.cursor()
        cursor.execute(query, (serienummer,))
        count = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return count > 0
