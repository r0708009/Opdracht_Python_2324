from soldaat_controller import SoldaatController
from wapen_controller import WapenController
from soldaat import Soldaat
from wapen import Dienstwapen

import random
import string

def genereer_serienummer(eenheid, wapen_naam):
    eenheid_afkorting = eenheid[:3].upper()
    wapen_afkorting = ''.join(filter(str.isalpha, wapen_naam)).upper()
    willekeurig_getal = ''.join(random.choices(string.digits, k=5))
    serienummer = f"{eenheid_afkorting}{wapen_afkorting}{willekeurig_getal}"
    return serienummer

db_name = "soldaat_database.db"
soldaat_controller = SoldaatController(db_name)
wapen_controller = WapenController(db_name)

soldaten_gegevens = [
    ("Bogdan Vincent", "12-02-1999", "Sergeant", "Infanterie"),
    ("Julia De Vries", "05-09-1997", "Sergeant", "Paracommando"),
    ("Max van der Berg", "18-06-1995", "Adjudant-Chef", "Genie"),
    ("Sophie Jansen", "23-11-1998", "Luitenant", "Logistiek"),
    ("Liam Bakker", "30-04-1996", "Sergeant", "Infanterie"),
    ("Emma Visser", "14-08-1993", "Eerste Soldaat", "Paracommando"),
    ("Finn de Boer", "09-10-1994", "Adjudant", "Genie"),
    ("Mila Smit", "27-03-2000", "Soldaat", "Logistiek"),
    ("Noah Mulder", "08-12-1992", "Sergeant", "Infanterie"),
    ("Zoë van Dijk", "03-07-1991", "Korporaal", "Paracommando"),
    ("Luuk Hoekstra", "19-05-1990", "Sergeant", "Genie"),
    ("Eva Veenstra", "25-10-1997", "Luitenant", "Logistiek"),
    ("Daan Kuijpers", "20-01-1993", "Sergeant-Chef", "Infanterie"),
    ("Lisa de Graaf", "10-11-1996", "Korporaal", "Paracommando"),
    ("Sem Hendriks", "15-06-1998", "Sergeant-majoor", "Genie")
]

for gegevens in soldaten_gegevens:
    soldaat = Soldaat(None, *gegevens)
    soldaat_controller.voeg_soldaat_toe(soldaat)

wapens_gegevens = [
    ("FN Scar-SC", "Infanterie"),
    ("FN Scar-L", "Paracommando"),
    ("FN Scar-H", "Genie"),
    ("FN 5.7", "Logistiek")
    
]

for gegevens in wapens_gegevens:
    wapen_naam, eenheid = gegevens
    serienummer = genereer_serienummer(eenheid, wapen_naam)
    wapen = Dienstwapen(None, wapen_naam, eenheid, serienummer)
    wapen_controller.voeg_wapen_toe(wapen)
