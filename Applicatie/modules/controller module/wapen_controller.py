from soldaat import Soldaat
from soldaat_controller import SoldaatController

from wapen import Wapen


import sqlite3
import random
import string

class WapenController:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def genereer_serienummer(component, wapen_naam):
        component_afkorting = component[:3].upper()
        wapen_afkorting = ''.join(filter(str.isalpha, wapen_naam)).upper()
        willekeurig_getal = ''.join(random.choices(string.digits, k=5))
        serienummer = f"{component_afkorting}{wapen_afkorting}{willekeurig_getal}"
        return serienummer

    def voeg_wapen_toe(self, wapen):
        query = "INSERT INTO wapens (naam, serienummer) VALUES (?, ?)"
        self.cursor.execute(query, (wapen.naam, wapen.serienummer))
        self.conn.commit()

    def verwijder_wapen(self, wapen_id):
        query = "DELETE FROM wapens WHERE id = ?"
        self.cursor.execute(query, (wapen_id,))
        self.conn.commit()

    def update_wapen(self, wapen_id, nieuwe_naam):
        query = "UPDATE wapens SET naam = ? WHERE id = ?"
        self.cursor.execute(query, (nieuwe_naam, wapen_id))
        self.conn.commit()

    def wijs_wapen_toe(self, soldaat_id, serienummer):
        query = "UPDATE soldaten SET wapen_serienummer = ? WHERE id = ?"
        self.cursor.execute(query, (serienummer, soldaat_id))
        self.conn.commit()

    def krijg_serienummer_van_wapen(self, wapen_id):
        query = "SELECT serienummer FROM wapens WHERE id = ?"
        self.cursor.execute(query, (wapen_id,))
        serienummer = self.cursor.fetchone()
        return serienummer

    def krijg_wapen_by_id(self, wapen_id):
        query = "SELECT * FROM wapens WHERE id = ?"
        self.cursor.execute(query, (wapen_id,))
        wapen_info = self.cursor.fetchone()

        if wapen_info:
            wapen = Wapen(*wapen_info)
            return wapen
        else:
            return None

    def krijg_wapen_via_serienummer(self, serienummer):
        query = "SELECT * FROM wapens WHERE serienummer = ?"
        self.cursor.execute(query, (serienummer,))
        wapen_info = self.cursor.fetchone()

        if wapen_info:
            wapen = Wapen(*wapen_info)
            return wapen
        else:
            return None

    def krijg_wapens_van_eenheid(self, eenheid):
        query = "SELECT * FROM wapens WHERE eenheid = ?"
        self.cursor.execute(query, (eenheid,))
        wapens = self.cursor.fetchall()
        return wapens
    
    def krijg_alle_wapens(self):
        query = "SELECT * FROM wapens"
        self.cursor.execute(query)
        wapens = self.cursor.fetchall()
        return wapens

    def check_component_wapen(component):
        if component.lower() == 'landmacht':
            return 'FN SCAR-L'
        elif component.lower() == 'zeemacht':
            return 'FN P90'
        elif component.lower() == 'luchtmacht':
            return 'FN 5.7'
        elif component.lower() == 'medisch component':
            return 'FN 5.7'

    
