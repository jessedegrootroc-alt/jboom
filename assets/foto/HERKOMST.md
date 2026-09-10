# assets/foto: herkomst van het beeld

Alle foto's in deze map komen van **www.jboom.nl** en zijn eigendom van
Aannemersbedrijf J. Boom v.o.f. Ze zijn opgehaald van het eigen domein van het
bedrijf op 10 september 2026; de onbewerkte bestanden staan in
`_generator/jboom/beeld/`.

`_generator/maak_assets.py` heeft ze omgezet naar WebP en AVIF in meerdere
breedtes. Welk bronbestand welke sleutel kreeg en welke alt-tekst erbij hoort,
staat in `_generator/beeldplan.json`; de gemaakte breedtes staan in
`_generator/beeldmaten.json`.

## Er is niet opgeschaald

De grootste trede is de bronbreedte zelf. De bronsite levert brede banden van
1920 tot 2000 pixels en projectfoto's van 600 tot 1024 pixels; een foto van 800
pixels krijgt hier dus geen variant van 1600. Wat er niet is, wordt niet
verzonnen.

Eén beeld is daardoor kleiner dan de plek waar het staat: `jboom-historie`, de
zwart-witfoto uit het familiearchief, is 436 pixels breed. Die staat daarom op
zijn eigen maat met een bijschrift ernaast en niet over de volle breedte. Zie
`CONTENT-TODO.md`.

## Er staat geen stockbeeld op deze site

Elke foto op elke pagina komt van J. Boom zelf. Het merkpatroon achter de
paginakoppen zonder foto is de enige uitzondering: dat komt uit de
oorspronkelijke template en is omgekleurd naar de merklaag. Zie
`assets/patronen/HERKOMST.md`.

## Rechten

Deze beelden zijn van J. Boom. Voor gebruik buiten deze website is toestemming
van Aannemersbedrijf J. Boom v.o.f. nodig. Op een aantal foto's staan
medewerkers en bedrijfsbussen; die stonden ook op de bronsite.
