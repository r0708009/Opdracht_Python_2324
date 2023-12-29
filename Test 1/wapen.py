class Dienstwapen:
    def __init__(self, wapen_id, wapen_naam, eenheid, serienummer):
        self.wapen_id = wapen_id
        self.wapen_naam = wapen_naam
        self.eenheid = eenheid
        self.serienummer = serienummer

    def __str__(self):
        return f"Wapen ID: {self.wapen_id}, Naam: {self.wapen_naam}, Eenheid: {self.eenheid}, Serienummer: {self.serienummer}"
