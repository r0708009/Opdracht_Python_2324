from wapen import Dienstwapen

import sqlite3

class WapenController:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def voeg_wapen_toe(self, wapen):
        query = "INSERT INTO Dienstwapens (wapen_naam, eenheid, serienummer) VALUES (?, ?, ?)"
        self.cursor.execute(query, (wapen.wapen_naam, wapen.eenheid, wapen.serienummer))
        self.conn.commit()

    def verwijder_wapen(self, wapen_id):
        query = "DELETE FROM Dienstwapens WHERE wapen_id = ?"
        self.cursor.execute(query, (wapen_id,))
        self.conn.commit()

    def update_wapen(self, wapen_id, nieuwe_naam, nieuwe_eenheid, nieuw_serienummer):
        query = "UPDATE Dienstwapens SET wapen_naam = ?, eenheid = ?, serienummer = ? WHERE wapen_id = ?"
        self.cursor.execute(query, (nieuwe_naam, nieuwe_eenheid, nieuw_serienummer, wapen_id))
        self.conn.commit()

    def krijg_wapen_by_id(self, wapen_id):
        query = "SELECT * FROM Dienstwapens WHERE wapen_id = ?"
        self.cursor.execute(query, (wapen_id,))
        wapen_info = self.cursor.fetchone()

        if wapen_info:
            wapen = Dienstwapen(*wapen_info)
            return wapen
        else:
            return None

    def krijg_serienummer_van_wapen(wapen_id):
        query = "SELECT serienummer FROM Dienstwapens WHERE wapen_id = ?"
        self.cursor.execute(query, (wapen_id,))
        wapen = self.cursor.fetchone()

    def krijg_wapens_van_eenheid(self, eenheid):
        query = "SELECT wapen_naam FROM Dienstwapens WHERE eenheid = ?"
        self.cursor.execute(query, (eenheid,))
        wapens = self.cursor.fetchall()
        return wapens
    
    def krijg_alle_wapens(self):
        query = "SELECT * FROM Dienstwapens"
        self.cursor.execute(query)
        wapens = self.cursor.fetchall()
        return wapens

