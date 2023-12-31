1. Kloon de githubrepo.
2. Creëer een virtuele omgeving.
3. Installeer in de virtuele omgeving de nodige packages van de requirement.txt , met het command pip install -r requirements.txt.
4. Bestudeer je README.md.
5. Run het project.

---------------------------------------------------------------------------------------------
1. run 'python initialaze_database.py' die zich in de map 'Applicatie' bevindt om de database te initialiseren.
2. run daarna 'python cli.py' om de applicatie te starten.









Het doel van de applicatie is om soldaten en hun wapens toe te voegen aan de database met een overzichtige cli. 

Als eerst ziet men een hoofdmenu. Het is de bedoeling om soldaten toe te voegen. 
Als men op '1' drukt komen we in een ander menu om de soldaten te beheren. Hier kan men soldaten toevoegen, verwijderen, aanpassen of alle soldaten uit de database in een lijst weergeven.

Bij het toevoegen van soldaten moet men gegevens invullen. Niet alle gegevens worden handmatig ingegeven. Bij voorbeeld het stamnummer van de soldaat wordt via de voornaam, familienaam en geboortedatum berekend en automatisch ingevuld.Indien er al iemand met dat stamnummer in de database zit, worden er 3 karakters willekeurig toegevoegd. Daarnaast krijgt de soldaat een wapen toegekend naargelang zijn component. Bij het toekennen wordt het wapen ook aangemaakt, deze krijgt ook naargelang het meegegeven component een serienummer die wordt berekend voor ons.




