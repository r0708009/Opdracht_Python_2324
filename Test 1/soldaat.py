class Soldaat:
    def __init__(self, soldaat_id, naam, geboortedatum, rang, eenheid):
        self.soldaat_id = soldaat_id
        self.naam = naam
        self.geboortedatum = geboortedatum
        self.rang = rang
        self.eenheid = eenheid

    def __str__(self):
        return f"ID: {self.soldaat_id}, Naam: {self.naam},Geboortedatum: {self.geboortedatum}, Rang: {self.rang}, Eenheid: {self.eenheid}"
