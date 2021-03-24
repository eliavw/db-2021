## 4. Hoe en wat in te dienen?

Nu je alle queries ingevuld (en getest) hebt, ben je klaar om je taak in te dienen. **De deadline wordt gecommuniceerd via Toledo.**

1. **Maak een leeg bestand** aan, en geef het de bestandsnaam met formaat: `achternaam_voornaam_studentennummer.py`.
    - `achternaam` verwijst naar je achternaam, bijvoorbeeld `Lemaître`
    - `voornaam`  verwijst naar je voornaam, bijvoorbeeld `Georges`
    - `studentennummer` is je studentennummer zoals vermeld op je studentenkaart, bijvoorbeeld `r0123456`
    -  Een goede bestandsnaam is dus bijvoorbeeld: `lemaitre_georges_r0123456.py`  
    
2. Kopieer **ALLE INGEVULDE FUNCTIES EN NIETS ANDERS** naar dit bestand. Het bevat dus _enkel en alleen_ de functies: `query_01`, `query_02`, etc.  

3. **TIP**: om te testen dat je oplossing deftig runt, kan je gebruik maken van de `verification.ipynb` notebook!
    - Eerst worden je functies ingelezen vanuit het zonet aangemaakte python bestand (e.g. `lemaitre_georges_r0123456.py`).
    - Die functies worden dan automatisch gerund op je database, met verschillende parameters.
    - De resultaten worden uitgeschreven als `.csv` files (in de `out` folder)
    - Dit helpt om zeker te zijn dat je `achternaam_voornaam_studentennummer.py` bestand correct werkt.
        - Als een query crasht, zal er dus geen resultaat worden uitgeschreven!
        - Als een query niet crasht, kan je de resultaten inspecteren.  
        
4. **TIP**: voor de eerste query kan je je oplossing zelfs _evalueren_ via de `verification.ipynb` notebook!
    - De output `.csv` file van jouw oplossing wordt vergeleken met de `.csv` van de modeloplossing (te vinden in de `solution` folder).
    - Jouw oplossing krijgt een score toegekend. Cf. https://en.wikipedia.org/wiki/F1_score. 
    - Al dan niet correct sorteren is verantwoordelijk voor 10% van je score.
    - Een kort rapport wordt weergegeven. Dit vertelt je wat er eventueel mis is met je oplossing. 
        - TP: True Positives
        - TN: True Negatives
        - FP: False Positives
    - Dit kan je helpen om je oplossing te debuggen.
    - Voor de andere queries houden we de modeloplossingen geheim tot na de deadline.
        - Hier moet je dus zelf de resultaten inspecteren om jezelf ervan te overtuigen dat deze inderdaad correct zijn.  
        
5. Als je oplossing definitief is, submit je je `achternaam_voornaam_studentennummer.py` bestand via Toledo.  

6. Nogmaals, als finale submissie verwachten we dus _enkel_ een python bestand (e.g., `achternaam_voornaam_studentennummer.py`) dat jullie ingevulde functies bevat en niks anders.
    - Wij evalueren jullie ingediende python bestanden ook via de `verification.ipynb` notebook
    - Zoals zonet uitgelegd laat de `verification.ipynb` notebook je toe om zelf te checken dat je bestand deftig runt zonder te crashen etc. **Als op het op je eigen machine al niet werkt, is de kans miniem dat het bij ons wel zo zal zijn.**