from soldaat import Soldaat

import sqlite3


class SoldaatController:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def voeg_soldaat_toe(self, soldaat):
        query = "INSERT INTO Soldaten (naam, geboortedatum, rang, eenheid) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (soldaat.naam, soldaat.geboortedatum, soldaat.rang, soldaat.eenheid))
        self.conn.commit()

    def verwijder_soldaat(self, soldaat_id):
        query = "DELETE FROM Soldaten WHERE soldaat_id = ?"
        self.cursor.execute(query, (soldaat_id,))
        self.conn.commit()

    def update_soldaat(self, soldaat_id, nieuwe_naam, nieuwe_geboortedatum, nieuwe_rang, nieuwe_eenheid):
        query = "UPDATE Soldaten SET naam = ?, geboortedatum = ?, rang = ?, eenheid = ? WHERE soldaat_id = ?"
        self.cursor.execute(query, (nieuwe_naam,nieuwe_geboortedatum, nieuwe_rang, nieuwe_eenheid, soldaat_id))
        self.conn.commit()

    def krijg_soldaat_by_id(self, soldaat_id):
        query = "SELECT * FROM Soldaten WHERE soldaat_id = ?"
        self.cursor.execute(query, (soldaat_id,))
        soldaat_info = self.cursor.fetchone()

        if soldaat_info:
            soldaat = Soldaat(*soldaat_info)
            return soldaat
        else:
            return None

    def krijg_alle_soldaten(self):
        query = "SELECT * FROM Soldaten"
        self.cursor.execute(query)
        soldaten = self.cursor.fetchall()
        return soldaten

    def zoek_soldaat_op_naam(self, naam):
        query = "SELECT * FROM Soldaten WHERE naam = ?"
        self.cursor.execute(query, (naam,))
        soldaten = self.cursor.fetchall()
        return soldaten

    def krijg_soldaten_van_eenheid(self, eenheid):
        query = "SELECT * FROM Soldaten WHERE eenheid = ?"
        self.cursor.execute(query, (eenheid,))
        soldaten = self.cursor.fetchall()
        return soldaten
