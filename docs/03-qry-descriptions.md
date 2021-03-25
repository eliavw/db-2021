## 3.1 Query 01

**Beschrijving**

Voor elke manager, voor elke keer dat deze manager meer dan `X` games heeft, geef: het aantal wins, het aantal losses, het jaar, de gegeven naam en de achternaam van de manager, en het teamID.

Sorteer eerst aflopend op wins, dan oplopend op: losses, jaar, teamID, achternaam en gegeven naam.

## 3.2 Query 02

**Beschrijving**

Geef de voornaam en achternaam van alle spelers geboren in de jaren '60 van de vorige eeuw.

Sorteer achtereenvolgens alfabetisch oplopend op achternaam en voornaam.

## 3.3 Query 03

**Beschrijving**

Geef de namen en IDs van teams waarvan de naam een gegeven string `X` bevat. Het resultaat mag geen duplicaten bevatten.

Sorteer achtereenvolgens oplopend op teamID en dan op naam.


## 3.4 Query 04

**Beschrijving**

Geef voor elke manager, voor elk team waarmee de manager gewerkt heeft gedurende minstens `X` jaar: de achternaam en de voornaam van de manager, het ID van het team, het aantal jaren dat de manager het team heeft gemanaged, het gemiddeld aantal wins en gemiddelde rank.

Sorteer achtereenvolgens oplopend op gemiddelde rank, dan aflopend op: aantal jaar, aantal wins, teamID, achternaam en voornaam van de manager.


## 3.5 Query 05

**Beschrijving**

Geef voor een gegeven jaar `X`, voor elk team: de naam van dat team en de voornaam en de achternaam van de speler(s) met het hoogste totaal aantal homeruns in dat team in dat jaar, alsook dat aantal homeruns.

Sorteer achtereenvolgens alfabetisch oplopend op teamnaam, dan achternaam, dan voornaam.


## 3.6 Query 06

**Beschrijving**

Maak een lijst van spelers geboren op dezelfde datum als minstens 1 andere speler.
Geef de geboortedatum, alsook de voor en achternaam van de spelers.

Sorteer achtereenvolgens oplopend op geboortedatum, dan alfabetisch oplopend op achternaam en voornaam.

Zorg ervoor dat je resultaat geen data bevat die duidelijk geen geboortedatum van een speler kunnen zijn, e.g. data als _3000-1-1_ or _1950-80-3_.



## 3.7 Query 07

**Beschrijving**

Maak een lijst van alle speler geboren in een gegeven jaar `X`. 
Per speler, geef voornaam en achternaam, alsook de eventuele awards gewonnen als speler.
Voor elke award, geef de naam van die award en het jaar waarin de award gewonnen werd.

Sorteer achtereenvolgens alfabetisch oplopend op achternaam, voornaam, naam van award en tenslotte oplopend op jaar.


## 3.8 Query 08

**Beschrijving**

Maak een lijst van managers die een gegeven rank `R` minstens éénmaal hebben bereikt.
Voor elk van die managers, geef: voornaam, achternaam, leeftijd (in jaren) waarop ze de eerste keer die rank bereikt hebben en de naam van het team waarmee dit gebeurde, alsook het totale aantal keren dat ze die rank bereikt hebben.

Sorteer achtereenvolgens oplopend op leeftijd, dan alfabetich oplopend op: achternaam en voornaam.

Zorg ervoor dat je enkel managers beschouwt die, ten tijde van hun eerste rank `R`, niet meer dan een gegeven aantal `N` jaren ouder waren dan de leeftijd van de jongste manager die ooit rank `R` wist te bereiken.
