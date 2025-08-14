Gebruikersdocumentatie: APG IoT-bord Project
GitHub - Henok-cloud/Eind_ProjectAPGIoTboard
Opstartgedrag en Wisselen tussen programma’s
Bij het opstarten van het bordje (na voeding of rest):
-	Alle LEDs worden kort uitgeschakeld om de toestand te resetten.
-	De LEDs van 1 - 5 geven de verschillende programma’s aan, via de potentiometer kun je deze doorlopen.  
o	Stand 0: Eerste LED (groen) = Op_neer_teller_binary.
o	Stand 1: Tweede LED (rood) = licht_balk_verdrijver_links_rechhts.
o	Stand 2: Derde LED (oranje) = 4 x LED_lichtshow.
o	Stand 3: Vierde LED (oranje) = internal_temp.
o	Stand 4: Vijfde LED (oranje) = Reaction_game.
-	Druk op knop 1 om het geselecteerde programma te starten.
-	Knop 1 en knop 2 gezamenlijk lang indrukken stopt het programma en brengt je terug naar keuze meun.

 
Overzicht programma’s
1.  Binair op/neer Teller 
- Knop 1 verhoogt de teller.
- Knop 2 verlaagt de teller.
- Oranje LEDs tonen de binaire waarde (6 bits).
- Groene LED = positief; Rode LED = negatief.
- Lang drukken op beide knoppen stopt het programma en brengt je terug naar keuze meun.
2. Lichtbalk – Verkeer verdrijven
- Knop 1: start lichtbalk van rechts naar links (links verdrijven).
- Knop 2: start van links naar rechts (rechts verdrijven).
- Korte druk op beide knoppen: activeert STOP-patroon (alle LEDs knipperen).
- Lang drukken op beide knoppen: stopt het programma en brengt je terug naar keuze meun.
- Snelheid van de lichtbalk is instelbaar met de potentiometer.

3. LED Lichtshow
- Doorloopt 3 visuele LED-effecten:
	- scroll links
	- scroll rechts 
	- fade-wave 
	- regenval 
- Knop 1 volgende LED-effect
- Knop 2 vorige LED-effect
-  Potentiometer regelt snelheid.
- Lang drukken op beide knoppen stopt de show en brengt je terug naar keuze meun.

4. Temperatuurweergave 
- Meet interne temperatuur via ingebouwde sensor.
- Toont temperatuur (in °C) binaire weergegeven op LEDs (0–63°C).
- Groene LED = temperatuur binnen bereik (0–63).
- Rode LED = buiten bereik.
- Lang drukken op beide knoppen stopt het programma en brengt je terug naar keuze meun.




5. Reactiespel 
-  Willekeurige LEDs 3 – 5(Links) of 6 – 8(Rechts) (oranje) licht op.
- Druk snel op de juiste knop (links = knop 1, rechts = knop 2).
- Herhaal voor 5 rondes.
- Aan het eind wordt de gemiddelde reactietijd getoond op LED 1 en 2.
- Groene LED = goede score, rode LED = trager.
- Lang drukken op beide knoppen stopt het spel op elk moment en brengt je terug naar keuze meun.


