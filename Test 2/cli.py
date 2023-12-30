import random
import string
import sys
sys.path.append('modules/view module')
sys.path.append('modules/controller module')


from datetime import datetime

from soldaat import Soldaat
from wapen import Wapen
from component import Component

from soldaat_controller import SoldaatController
from wapen_controller import WapenController
from component_controller import ComponentController

def genereer_random_karakters():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

def soldaten_beheren(soldaat_controller, wapen_controller):
    while True:
        print("\n1. Voeg soldaat toe")
        print("2. Verwijder soldaat")
        print("3. Update soldaat")
        print("4. Toon alle soldaten")
        print("0. Terug naar hoofdmenu\n")

        keuze = input("Voer een optie in: ")

        if keuze == "1":
            while True:
                voornaam = input("Voornaam: ").strip()
                while not voornaam:
                    print("Voornaam mag niet leeg zijn.")
                    voornaam = input("Voornaam: ").strip()
                voornaam = voornaam.capitalize()

                familienaam = input("Familienaam: ").strip()
                while not familienaam:
                    print("Familienaam mag niet leeg zijn.")
                    Familienaam = input("Familienaam: ").strip()
                familienaam = familienaam.capitalize()

                while True:
                    geboortedatum = input("Geboortedatum (dd-mm-jjjj): ")
                    try:
                        datetime.strptime(geboortedatum, "%d-%m-%Y")
                        break
                    except ValueError:
                        print("Voer een geldige geboortedatum in (dd-mm-jjjj).")

                stamnummer = f"{voornaam[0]}{familienaam[0]}{geboortedatum[::-1]}".replace("-","")

                if soldaat_controller.controleer_stamnummer(stamnummer):
                    print("Stamnummer bestaat al. Het wordt aangepast met 3 willekeurige karakters.")
                    stamnummer += genereer_random_karakters().upper()
                    print(f"Nieuw stamnummer: {stamnummer}")
                else:
                    print(f"Verkregen stamnummer: {stamnummer}")

                rang = input("Rang: ").capitalize()
                while not rang:
                    print("Rang mag niet leeg zijn.")
                    rang = input("Rang: ").strip()
                rang = rang.capitalize()

                component = input("Component: ").lower()

                while not component:
                    print("Component mag niet leeg zijn.")
                    component = input("Component: ").strip()

                while component not in ['landmacht', 'zeemacht', 'luchtmacht', 'medisch component']:
                    print("Ongeldige invoer. U kunt alleen kiezen tussen landmacht, zeemacht, luchtmacht of medisch component.")
                    component = input("Component: ").lower()

                component = component.capitalize()

                wapen_naam = WapenController.check_component_wapen(component)

                serienummer = WapenController.genereer_serienummer(component, wapen_naam)
                # serienummer = "test"

                wapen = Wapen(None, wapen_naam, serienummer)
                wapen_controller.voeg_wapen_toe(wapen)

                soldaat = Soldaat(None, voornaam, familienaam, geboortedatum, stamnummer, rang, component, serienummer)
                soldaat_controller.voeg_soldaat_toe(soldaat)
                print("Soldaat toegevoegd.")
                break



        elif keuze == "2":
            while True:
                soldaat = soldaat_controller.krijg_soldaat_by_id(input("Soldaat ID om te verwijderen: "))
                if soldaat:
                    test = input(f"Bent u zeker dat u {soldaat.rang} {soldaat.voornaam[0]}.{soldaat.familienaam} ({soldaat.stamnummer}) wilt verwijderen?\n")
                    if test == "ja":
                        soldaat_controller.verwijder_soldaat(soldaat.soldaat_id)
                        print("Soldaat verwijderd.")
                        break
                    else:
                        continue
                else:
                    print("Ongeldige Soldaat ID. Probeer opnieuw.\n")

        elif keuze == "3":
            # Implementeer bijwerken van een soldaat
            print("3")

        elif keuze == "4":
            # Implementeer weergeven van alle soldaten
            print("4")

        elif keuze == "0":
            break
        else:
            print("Ongeldige optie. Probeer opnieuw.")

def wapens_beheren(wapen_controller):
    while True:
        print("\n1. Voeg wapen toe")
        print("2. Verwijder wapen")
        print("3. Update wapen")
        print("4. Toon alle wapens")
        print("0. Terug naar hoofdmenu\n")

        keuze = input("Voer een optie in: ")

        if keuze == "1":
            # Implementeer toevoegen van een wapen
            print("1")

        elif keuze == "2":
            # Implementeer verwijderen van een wapen
            print("2")

        elif keuze == "3":
            # Implementeer bijwerken van een wapen
            print("3")

        elif keuze == "4":
            # Implementeer weergeven van alle wapens
            print("4")

        elif keuze == "0":
            break
        else:
            print("Ongeldige optie. Probeer opnieuw.")

def opzoekingen_uitvoeren(soldaat_controller, wapen_controller):
    while True:
        print("\n1. Zoek soldaat op naam")
        print("2. Zoek wapen van een bepaalde eenheid")
        print("3. Toon soldaten van een eenheid")
        print("0. Terug naar hoofdmenu\n")

        keuze = input("Voer een optie in: ")

        if keuze == "1":
            # Implementeer zoeken van een soldaat op naam
            print("1")

        elif keuze == "2":
            # Implementeer zoeken van een wapen van een bepaalde eenheid
            print("2")

        elif keuze == "3":
            # Implementeer weergeven van soldaten van een bepaalde eenheid
            print("3")

        elif keuze == "0":
            break
        else:
            print("Ongeldige optie. Probeer opnieuw.")

def hoofdmenu(soldaat_controller, wapen_controller, component_controller):
    while True:
        print("\nHoofdmenu:")
        print("1. Soldaten beheren")
        print("2. Wapens beheren")
        print("3. Opzoekingen uitvoeren")
        print("0. Afsluiten\n")

        keuze = input("Voer een optie in: ")

        if keuze == "1":
            soldaten_beheren(soldaat_controller, wapen_controller)

        elif keuze == "2":
            wapens_beheren(wapen_controller)

        elif keuze == "3":
            opzoekingen_uitvoeren(soldaat_controller, wapen_controller)

        elif keuze == "0":
            break
        else:
            print("Ongeldige optie. Probeer opnieuw.")

def main():
    db_name = "soldaten_database.db"
    soldaat_controller = SoldaatController(db_name)
    wapen_controller = WapenController(db_name)
    component_controller = ComponentController(db_name)
    
    hoofdmenu(soldaat_controller, wapen_controller, component_controller)

if __name__ == "__main__":
    main()
