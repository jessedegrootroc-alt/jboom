# Wat er nog van J. Boom nodig is

Deze site is gevuld met de content van www.jboom.nl. Er staan **geen**
`[CONTENT NODIG]`-markeringen meer op de pagina's: waar de bron iets niet zegt,
staat er niets in plaats van een leeg vak. Wat hieronder staat is dus geen fout
op de site, maar wat de site beter zou maken zodra J. Boom het aanlevert.

Op volgorde van hoeveel het uitmaakt.

---

## 1. Het formulier verstuurt niets

`ENDPOINT` in `contactformulier.js` is leeg, dus er gaat nog geen bericht de
deur uit. Het formulier zegt dat nu ook: bij verzenden meldt het dat het nog
niet is aangesloten, dat het bericht dus niet verstuurd is, en het wijst naar
het e-mailadres en het telefoonnummer. De ingevulde tekst blijft staan zodat
hij te kopiëren is. Er wordt dus geen succes meer gemeld dat er niet is.

**Wat er nodig is:** een adres waar de inzending naartoe mag. Dat kan een eigen
backend zijn of een formulierdienst; zet het in `ENDPOINT` bovenin
`contactformulier.js`. Zodra dat er staat, verdwijnt de melding vanzelf en komt
de gewone bevestiging ervoor terug — er hoeft niets anders te wijzigen.

Tot dat geregeld is werken het telefoonnummer en het e-mailadres wél: die staan
op elke pagina in de voet, op de contactpagina in de vlakkenrij en als knop in
elk slotblok.

---

## 2. Foto's van Martin en Mario

Het hele verhaal van deze site is dat u met twee vakmensen te maken heeft die
zelf op de bouw staan. Op `over-ons.html` staan hun namen in twee panelen, maar
er is geen foto van ze: de bronsite heeft er geen.

Twee portretten, of één foto van ze samen op een project, maken die pagina
aanzienlijk sterker. Het beeldveld staat er al klaar voor; het is één regel in
`beeldplan.json` plus een keer `maak_assets.py` draaien.

---

## 3. De archieffoto op ware grootte

De zwart-witfoto uit het familiearchief (`jboom-historie`) is het beeld dat de
historie draagt. Het bestand op de bronsite is **436 pixels breed** en meer is
er niet. Daarom staat hij op `index.html` en `historie.html` op zijn eigen maat
met een bijschrift ernaast, en niet over de volle breedte: uitvergroot wordt het
een wazige vlek.

Is er een scan van het origineel, dan kan hij over de volle inhoudsbreedte en
wordt het een van de sterkste beelden van de site.

---

## 4. Projectgegevens

De bronsite heeft twee fotoseries — 46 en 33 beelden — en verder niets: geen
opdrachtgever, plaats, jaartal, opgave, aanpak of resultaat per project.

Daarom staan er op deze site geen losse projectpagina's maar twee
seriepagina's. Het template heeft een volwaardige case-studytemplate met een
opgave, een uitdaging, een aanpak en een resultaat, en die zou hier goed staan
— maar alleen met echte gegevens. Ze verzinnen zou betekenen dat er over werk
bij echte mensen thuis iets wordt beweerd wat J. Boom nooit heeft gezegd.

**Wat er nodig is voor één echte case study:** per project de plaats, het jaar,
wat de vraag was, wat er is gedaan en wat het opleverde. Drie of vier van dat
soort projecten wegen zwaarder dan de hele fotoserie.

Let op: voor het noemen van een opdrachtgever bij naam is toestemming van die
partij nodig.

---

## 5. Openingstijden

Staan niet op de bronsite en staan dus nergens op deze site. Wat er wel staat
is wat de bron zelf zegt: "onze werktijden zijn flexibel" en "is er nood aan de
man? Dan staan wij zo op de stoep".

Zodra ze bekend zijn: in `bouw_jboom_contact.py`, in de lijst `gegevens`,
achter het telefoonnummer aan het telefoonvlak toevoegen. Dan blijft de rij op
vier vlakken; een vijfde vlak begint de kleurenreeks opnieuw en breekt het
ritme.

---

## 6. De privacy- en cookieverklaring

`privacybeleid.html` verwijst naar de PDF die J. Boom zelf heeft gepubliceerd
(het privacy- en cookiestatement volgens de richtlijnen van het ministerie van
Economische Zaken) en beschrijft daarnaast wat het formulier op deze site
verzamelt. `cookies.html` beschrijft wat deze site plaatst.

Twee dingen om na te lopen:

- **De PDF staat nog op het oude domein.** De link wijst naar
  `https://www.jboom.nl/uploads/...`. Gaat die site uit de lucht, dan moet de
  PDF meeverhuizen naar deze map en de link mee.
- **De verklaring beschrijft de oude site.** Zodra hier statistiek wordt
  aangezet of het formulier gekoppeld is, hoort de verklaring daarop te worden
  bijgewerkt. Dat is een juridische tekst: die moet van J. Boom komen.

---

## 7. Statistiek

`analytics.js` staat klaar en luistert naar de keuze uit de cookiemelding, maar
er is geen statistiekpakket aan gekoppeld. Wordt dat er wel aan gehangen, dan
hoort de opsomming in `cookies.html` uitgebreid te worden met de naam, het doel
en de bewaartermijn van de cookies die dat pakket plaatst.

---

## 8. Twee dingen die de bron zelf tegenspreekt

De bronsite zegt op drie plekken iets anders over de leeftijd van het bedrijf:
"Bijna 80 jaar", "Al ruim 80 jaar" en "ruim 79 jaar". Die pagina's zijn rond
2018 geschreven en lopen dus achter.

Op deze site staat daarom overal het jaartal zelf — sinds 1935 — en "vierde
generatie". Dat is wat de bron feitelijk zegt en het veroudert niet. Klopt 1935
niet, dan is het één regel: `OPRICHTING` in `inhoud_jboom.py`.

Hetzelfde geldt voor het moment waarop het bedrijf naar twee man ging. De bron
zegt "vijfenzestig jaar na oprichting" en noemt geen jaartal; dat staat op
`historie.html` dus ook zo.

---

## 9. Het merkpatroon op mobiel

Het patroon achter de paginakoppen zonder foto komt uit de oorspronkelijke
template en is hier omgekleurd naar Boom Goud en het antraciet uit het logo. De
bredeschermversie is een verloop van stralen; de mobiele versie is in het
aangeleverde bestand een vlak veld met een fijne stip. Dat is geen fout, maar
een ray-verloop zou daar net zo goed werken.

Aanleveren als vierkant bronbestand in `assets/patronen/bron/`, daarna
`maak_assets.py` draaien; het omkleuren en de contrastmeting gaan vanzelf.
