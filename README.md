1. Kloon de githubrepo.
2. Creëer een virtuele omgeving.
3. Installeer in de virtuele omgeving de nodige packages van de requirement.txt , met het command pip install -r requirements.txt.
4. Bestudeer je README.md.
5. Run het project.

---------------------------------------------------------------------------------------------
1. run 'python initialaze_database.py' die zich in de map 'Applicatie' bevindt om de database te initialiseren.
2. run daarna 'python cli.py' om de applicatie te starten.



-------------------------------------------------------------------------------------------

Het doel van de applicatie is om soldaten en hun wapens toe te voegen aan de database met behulp van een overzichtelijke CLI.

Bij het openen van de applicatie verschijnt eerst een hoofdmenu.

Door op '1' te drukken komt men in een ander menu om de soldaten te beheren. Hier kan men soldaten toevoegen, verwijderen, aanpassen of alle soldaten uit de database in een lijst weergeven.

Bij het toevoegen van soldaten moeten gegevens worden ingevoerd. Niet alle gegevens worden handmatig ingevoerd. Zo wordt bijvoorbeeld het stamnummer van de soldaat automatisch berekend op basis van de voornaam, achternaam en geboortedatum. Als er al iemand met dat stamnummer in de database staat, worden er 3 willekeurige karakters toegevoegd. Daarnaast wordt aan de soldaat een wapen toegewezen op basis van zijn component. Bij het toekennen wordt het wapen ook aangemaakt; deze krijgt een serienummer dat wordt berekend op basis van het meegegeven component. Als u achteraf het component wijzigt, wordt ook gevraagd of u uw huidige wapen wilt behouden of een wapen van het nieuwe component wilt.

Terugkeren naar het hoofdmenu kan door op '0' te drukken, waarna de optie '2. Wapens beheren' gekozen kan worden. Hier kan men handelingen uitvoeren met de tabel 'wapens' in de database.

Het gebruik van het menu spreekt voor zich. Bij het toevoegen van een nieuw wapen wordt gevraagd om de naam en het passende component in te voeren zodat het serienummer kan worden berekend. Bij het updaten van een wapen kan alleen de naam worden gewijzigd. Dit is om veiligheidsredenen; het wijzigen van het serienummer zou wapens kunnen 'verloren' laten gaan.

Daarnaast biedt het hoofdmenu de optie 'Opzoekingen uitvoeren', waar men specifieke zaken kan opzoeken. Zo kan een soldaat worden gevonden op basis van zijn naam (voor- en achternaam), stamnummer, of het serienummer van een wapen. Deze laatste optie is handig als een wapen onderhouden wordt en de juiste persoon moet worden gevonden om het wapen terug te ontvangen.

Uiteindelijk kan hier een csv-bestand worden opgevraagd met via het csv_export-bestand. De output van dit bestand kan op zijn beurt worden omgezet naar een excel-bestand.
