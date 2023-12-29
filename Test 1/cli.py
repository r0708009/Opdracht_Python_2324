from soldaat import Soldaat
from wapen import Dienstwapen
from soldaat_controller import SoldaatController
from wapen_controller import WapenController

import random
import string

def toon_soldaten(soldaten):
    if not soldaten:
        print("Geen soldaten gevonden.\n")
    else:
        for soldaat in soldaten:
            print(soldaat)

def toon_wapens(wapens):
    if not wapens:
        print("Geen wapens gevonden.\n")
    else:
        for wapen in wapens:
            print(wapen)

def genereer_serienummer(eenheid, wapen_naam):
                eenheid_afkorting = eenheid[:3].upper()
                wapen_afkorting = ''.join(filter(str.isalpha, wapen_naam)).upper()
                willekeurig_getal = ''.join(random.choices(string.digits, k=5))
                serienummer = f"{eenheid_afkorting}{wapen_afkorting}{willekeurig_getal}"
                return serienummer

def main():
    db_name = "soldaat_database.db"
    soldaat_controller = SoldaatController(db_name)
    wapen_controller = WapenController(db_name)

    while True:
        print("\n1. Voeg soldaat toe")
        print("2. Verwijder soldaat")
        print("3. Update soldaat")
        print("4. Toon alle soldaten")
        print("5. Zoek soldaat op naam")
        print("6. Soldaten van een bepaalde eenheid")
        print("7. Voeg wapen toe")
        print("8. Verwijder wapen")
        print("9. Update wapen")
        print("10. Zoek wapen van eenheid")
        print("11. Toon alle wapens.")
        print("0. Exit\n")

        keuze = input("Voer een optie in: ")

        def geldige_invoer(tekst):
            while True:
                invoer = input(tekst).strip(": ")
                if not invoer:
                    print(f"Voer een geldige {tekst.lower().strip(': ')} in.")
                else:
                    return invoer

        if keuze == "1":
            while True:
                naam = geldige_invoer("Voor- en achternaam: ").title()
                if len(naam.split()) >= 2:
                    geboortedatum = geldige_invoer("Geboortedatum (dd-mm-jjjj): ")
                    rang = geldige_invoer("Rang: ").capitalize()
                    eenheid = geldige_invoer("Eenheid: ").capitalize()
                    soldaat = Soldaat(None, naam, geboortedatum, rang, eenheid)
                    soldaat_controller.voeg_soldaat_toe(soldaat)
                    print("Soldaat toegevoegd.")
                    break
                else:
                    print("Voer een voor- en achternaam in.\n")
                    
        elif keuze == "2":
            while True:
                soldaat_id = input("Soldaat ID om te verwijderen: ")
                soldaat = soldaat_controller.krijg_soldaat_by_id(soldaat_id)
                if soldaat:
                    soldaat_controller.verwijder_soldaat(soldaat_id)
                    print("Soldaat verwijderd.")
                    break
                else:
                    print("Ongeldige Soldaat ID. Probeer opnieuw.\n")

        elif keuze == "3":
            soldaat_id = input("Soldaat ID om bij te werken: ")
            soldaat = soldaat_controller.krijg_soldaat_by_id(soldaat_id)
            while True:
                if soldaat:
                    print("\nVoor- en achternaam moeten ingevuld worden voor veiligheidsredenen.")
                    print("Druk enter indien u niet wenst te wijzigen.")
                    nieuwe_naam = geldige_invoer(f"(Update) voor- en achternaam ({soldaat.naam}): ") or soldaat.naam
                    if len(nieuwe_naam.split()) >= 2:
                        nieuwe_geboortedatum = input(f"Update geboortedatum ({soldaat.geboortedatum}): ") or soldaat.geboortedatum
                        nieuwe_rang = input(f"Update rang ({soldaat.rang}): ") or soldaat.rang
                        nieuwe_eenheid = input(f"Update eenheid ({soldaat.eenheid}): ") or soldaat.eenheid
                        soldaat_controller.update_soldaat(soldaat_id, nieuwe_naam, nieuwe_geboortedatum, nieuwe_rang, nieuwe_eenheid)
                        print("Soldaat bijgewerkt.\n")
                        break
                    else:
                        print("Voer een voor- en achternaam in.")
                else:
                    print("Ongeldige Soldaat ID. Probeer opnieuw.\n")


        elif keuze == "4":
            soldaten = soldaat_controller.krijg_alle_soldaten()
            toon_soldaten(soldaten)

        elif keuze == "5":
            while True:
                zoek_naam = input("Naam om te zoeken (voor- en achternaam): ")
                if len(zoek_naam) <= 2:
                    print("Voer een voor- en achternaam in.")
                else:
                    soldaten = soldaat_controller.zoek_soldaat_op_naam(zoek_naam)
                    if soldaten:
                        toon_soldaten(soldaten)
                        break
                    else:
                        print("Geen soldaten gevonden met die naam.\n")
                        doorgaan = input("Wil je opnieuw zoeken? (ja/nee): ")
                        if doorgaan.lower() != 'ja':
                            break

        elif keuze == "6":
            zoek_eenheid = input("Eenheid om te zoeken: ").capitalize()
            soldaten = soldaat_controller.krijg_soldaten_van_eenheid(zoek_eenheid)
            toon_soldaten(soldaten)

        elif keuze == "7":
            wapen_naam = input("Naam van het wapen: ").upper()
            eenheid = input("Eenheid waar het wapen toe behoort: ").capitalize()
            serienummer = genereer_serienummer(eenheid, wapen_naam).upper()
            print(f"Uw verkregen serienummer: {serienummer}")
            wapen = Dienstwapen(None, wapen_naam, eenheid, serienummer)
            wapen_controller.voeg_wapen_toe(wapen)
            print("Wapen toegevoegd.")

        elif keuze == "8":
            while True:
                wapen_id = input("Wapen ID om te verwijderen: ")
                wapen = wapen_controller.krijg_wapen_by_id(wapen_id)
                if wapen:
                    wapen_controller.verwijder_wapen(wapen_id)
                    print("Wapen verwijderd.")
                    break
                else:
                    print("Ongeldige Wapen ID. Probeer opnieuw.\n")

        elif keuze == "9":
            wapen_id = input("Wapen ID om bij te werken: ")
            wapen = wapen_controller.krijg_wapen_by_id(wapen_id)
            nieuwe_naam = input(f"Nieuw naam van het wapen ({wapen.wapen_naam}): ")
            nieuwe_eenheid = input("Nieuwe eenheid van het wapen: ")
            nieuw_serienummer = genereer_serienummer(nieuwe_eenheid, nieuwe_naam)
            wapen_controller.update_wapen(wapen_id, nieuwe_naam, nieuwe_eenheid, nieuw_serienummer)
            print("Wapen bijgewerkt.")

        elif keuze == "10":
            zoek_wapen = input("Naam van de eenheid: ")
            wapen = wapen_controller.krijg_wapens_van_eenheid(zoek_wapen)
            toon_wapens(wapen)

        elif keuze == "11":
            wapens = wapen_controller.krijg_alle_wapens()
            toon_wapens(wapens)

        elif keuze == "0":
            break
        else:
            print("Ongeldige optie. Probeer opnieuw.")

if __name__ == "__main__":
    main()
