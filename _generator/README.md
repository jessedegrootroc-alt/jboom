# _generator

De 22 HTML-pagina's in de hoofdmap worden hier gemaakt en zijn dus
**gegenereerde bestanden**. Pas je een pagina met de hand aan, dan is die
wijziging weg zodra hier iets opnieuw draait.

```
python3 bouw_alles.py
```

Dat schrijft alle pagina's opnieuw. `bouw_alles.py` roept de andere scripts aan:

| bestand | wat het maakt |
|---|---|
| `schil.py` | de gedeelde onderdelen: balk, voettekst, hero's, knoppen, kaarten, beeld |
| `bouw_jboom_home.py` | `index.html` |
| `bouw_jboom_dienst.py` | `diensten.html` en de negen dienstpagina's |
| `bouw_jboom_projecten.py` | `projecten.html` en de twee projectseries |
| `bouw_jboom_bedrijf.py` | over ons, historie, werkwijze, referenties |
| `bouw_jboom_contact.py` | contact, offerte, privacybeleid, cookies |
| `bouw_jboom_sitemap.py` | `sitemap.xml` en `robots.txt` |

## Waar de inhoud staat

| bestand | wat erin staat |
|---|---|
| `jboom/bron/` | de contentexport van www.jboom.nl: de zeven pagina's als platte tekst |
| `jboom/beeld/` | de 99 bronafbeeldingen, onbewerkt zoals ze op de bronsite stonden |
| `inhoud_jboom.py` | de feiten: bedrijfsgegevens, diensten, projectseries, referenties, partners |
| `inhoud_copy.py` | de herschreven koppen, leads, tussenkoppen en CTA's |
| `inhoud_dienst_verhaal.py` | de verhaallaag onder de dienstpagina's |

`inhoud_dienst_verhaal.py` bevat de enige tekst op deze site die niet van
www.jboom.nl komt: situaties, processtappen, wat de klant aanlevert, wat hij
krijgt en de veelgestelde vragen. Bovenaan dat bestand staat waar die vakinhoud
op gebaseerd is (de Omgevingswet, het Besluit bouwwerken leefomgeving en het
Omgevingsloket) en wat er bewust niet in staat.

`inhoud_copy.py` is de conversielaag. Hier staat per pagina de herschreven kop,
lead, tussenkop en CTA. De feiten komen onveranderd uit `inhoud_jboom.py`;
alleen de formulering is anders. De brontekst van www.jboom.nl schuift naar het
uitlegblok verderop de pagina, zodat er niets verdwijnt maar de pagina wel
begint met de reden in plaats van met een definitie.

Nagerekend: elk inhoudelijk woord in die laag is teruggezocht in `jboom/bron/`.
Er staat dus geen dienst, cijfer, certificering, garantie of doorlooptijd in die
niet uit de bron komt.

Drie bewuste keuzes in deze laag:

- De H1 van een dienstpagina is de dienstnaam zelf ("Dakopbouw en dakkapel"),
  niet de belofte. Dat houdt de kop gelijk aan het menu en aan waar mensen op
  zoeken; het voordeel staat in de eerste H2 eronder. Alleen de homepage, het
  dienstenoverzicht, het projectenoverzicht en over-ons hebben een H1 die wél
  een belofte is.
- De negen diensten zijn gegroepeerd onder drie hoofddiensten. De bronsite zet
  ze alle negen als losse kopjes onder elkaar; de groepering is dus een ordening
  en geen nieuwe bewering. Waarom elke koppeling klopt, staat in het commentaar
  bij `HOOFDDIENSTEN` in `inhoud_jboom.py`.
- Er zijn geen projectpagina's per project. Waarom niet, staat bovenin
  `bouw_jboom_projecten.py`.

## Beeld

`maak_assets.py` zet de afbeeldingen van de bronsite om naar responsive WebP en
AVIF, maakt de twee logovarianten, de favicon en de deelafbeelding, en kleurt
het merkpatroon om naar de merklaag. Dat hoeft alleen als er beeld bijkomt of
verandert:

```
python3 maak_assets.py
```

Het leest `beeldplan.json` (welke bron, welke rol, welke alt-tekst) en schrijft
`beeldmaten.json`, dat `schil.py` weer inleest. Het verwacht de bronbestanden in
`jboom/beeld/`; staan die er niet, dan stopt het script met een melding in
plaats van met halve bestanden.

Er wordt nooit opgeschaald: de grootste trede is de bronbreedte zelf. De
bronsite levert brede banden van 1920 tot 2000px en projectfoto's van 600 tot
1024px, en een foto van 800px krijgt dus geen 1600px-variant.

De CSS, de JavaScript en alles in `assets/` worden **niet** gegenereerd; die
bewerk je rechtstreeks.

## Snelheid: wat er gedaan is en waarom

Gemeten met Lighthouse tegen een server die comprimeert en cache-headers stuurt,
zoals een echte host. Mobiel, mediaan van vijf runs:

| | voor | na |
|---|---|---|
| Performance | 77 | **98** |
| Accessibility | 98 | **100** |
| Best Practices | 100 | 100 |
| SEO | 100 | 100 |
| First Contentful Paint | 2,6 s | 0,8 s |
| Largest Contentful Paint | 4,4 s | 2,4 s |
| Speed Index | 5,2 s | 1,4 s |
| Total Blocking Time | 40 ms | 0 ms |
| Layout shift | 0 | 0 |

Desktop staat op 100 / 100 / 100 / 100.

Wat het opleverde, in volgorde van effect:

1. **Minificeren** (`minify.py`). styleguide.css was 116 kB en blokkeerde het
   tekenen 1661 ms. Geminificeerd 60 kB, met gzip 10,7 kB over de lijn. Alle
   stylesheets en scripts gaan hierdoor.

2. **Een terugvalletter met dezelfde metriek.** Dit was de verrassing. Met
   `font-display: swap` tekent de browser de tekst eerst in de systeemletter en
   daarna opnieuw in Open Sans, en die tweede tekening heeft andere
   regelafmetingen. Chrome zag dat als een nieuw grootste tekstblok en
   registreerde de LCP dus op de tweede tekening: 0,5 seconde later en drie
   punten lager. Het tweede `@font-face`-blok bovenaan `styleguide.css` zet
   dezelfde systeemletter op maat met `size-adjust` en de ascent/descent-
   overrides, zodat de wissel geen herschikking meer is. De getallen komen uit
   het fontbestand zelf; wordt het font vervangen, dan moeten ze opnieuw
   berekend worden.

3. **Twee stylesheets in de pagina** in plaats van als los bestand
   (`transitions.css` en de pagina-stylesheets). Die zijn 0,3 tot 6 kB, en het
   ophalen kostte per stuk 304 ms aan heen-en-weer. Zie `inline()` in
   `schil.py`. styleguide.css blijft wél een los bestand: 60 kB in elke pagina
   zetten is duurder dan het één keer ophalen.

4. **Lage prioriteit voor beeld onder de vouw.** Een lazy afbeelding is niet
   nodig om te tekenen, dus krijgt hij `fetchpriority="low"`. De browser gaf de
   ruim twee megabyte beeld op de homepage eerst evenveel bandbreedte als de
   stylesheet en het lettertype.

5. **De logo's naar lossless WebP.** 42,8 kB aan PNG werd 24 kB, pixel voor
   pixel identiek (nagerekend met een pixelvergelijking).

6. **De koppen in de voet van h4 naar h2.** Dat was een sprong van twee niveaus
   na de h2 van het slotblok, op 72 van de 73 pagina's, en de enige fout die
   Lighthouse op toegankelijkheid gaf.

### Wat bewust NIET is aangeraakt

**De herovideo is eruit.** Het template had een film in de hero; J. Boom heeft
er geen en er is er geen bij gemaakt. De hero staat nu op een foto. De code die
een film inhangt staat nog in `site.js` en `index.css`: die kijkt naar een
`data-herovideo`-attribuut dat er niet is en valt dus stil zonder fout.

**De ongebruikte CSS.** Lighthouse meldt dat er op de homepage 32 kB van
styleguide.css niet gebruikt wordt. Dat is inherent aan één gedeelde
stylesheet: wat de homepage niet gebruikt, gebruikt een dienstpagina wel.
Regels weghalen zou andere pagina's breken, en de kritieke CSS eruit halen en de
rest achteraf laden geeft een pagina die een moment zonder opmaak staat.

**"Properly size images".** Dat gaat vooral om de verborgen citaten in de
referentieslider. Die zijn seconden later in beeld, dus ze moeten geladen
worden; ze staan al op `loading="lazy"` en lage prioriteit.

**"Label in Name".** Deze audit weegt nul en de site voldoet aan het
onderliggende criterium: de zichtbare tekst zit in de toegankelijke naam
("Verbouwing" in "Verbouwing: Om de kwaliteit..."). WCAG 2.5.3 vraagt dat de
zichtbare naam erin zit, niet dat hij er gelijk aan is.

### Meten

```bash
python3 _generator/devserver.py 8099
npx lighthouse http://127.0.0.1:8099/index.html --view
```

Meet tegen `devserver.py` en niet tegen `python3 -m http.server`: die laatste
comprimeert niet en stuurt geen cache-headers, en dan meet je ongeveer vijf
punten te laag. `devserver.py` doet wat een echte host doet; de instellingen die
de host moet krijgen staan in `DEPLOY.md`.

Reken op een spreiding van vijf punten tussen runs. Neem de mediaan van vijf
runs, niet één meting: tijdens dit werk gaf dezelfde site achtereenvolgens 89,
93, 93, 96 en 90.

## Controleren

```bash
python3 _generator/eindcontrole.py
```

Kijkt niet of de site mooi is, maar of er niets kapot of dubbel is: kapotte
links, koppenniveaus, dubbele titles, dubbele labels in de navigatie, lege
alinea's, ontbrekende alt-teksten en resten van het oude template. Draai dit na
elke `bouw_alles.py`.

## Versiehash op CSS en JavaScript

Elke lokale stylesheet en elk lokaal script krijgt `?v=<acht tekens>` mee,
berekend uit de sha256 van de inhoud van dat bestand:

```html
<link rel="stylesheet" href="styleguide.css?v=424acdcc" />
<script src="site.js?v=f105a2ab"></script>
```

Waarom: de site heeft geen build-stap, dus de bestandsnamen liggen vast.
`styleguide.css` heet altijd `styleguide.css`, dus een browser die de site eerder
bezocht mag hem uit zijn cache halen en blijft na een update op de oude versie
hangen. Tijdens het bouwen gebeurde dat hier drie keer: een gewijzigde
stylesheet of `site.js` kwam niet door, en een wijziging leek niet te werken
terwijl het bestand op schijf al goed was.

Verandert een bestand, dan verandert de hash en haalt de browser hem opnieuw op.
Verandert het niet, dan blijft de cache gewoon werken; dat is het verschil met
een tijdstempel of een willekeurig getal.

Dat gebeurt in `v()` in `schil.py`. Aandachtspunten:

- **Alleen lokale bestanden.** GSAP en Barba komen van jsDelivr en hebben hun
  versienummer al in het pad.
- **Niet op de lettertypen.** Die worden aangeroepen uit `@font-face` in
  `styleguide.css`, en dat pad kan dit script niet bijwerken. Zou de
  `<link rel="preload">` in de kop wél een hash krijgen en de `@font-face` niet,
  dan zijn dat twee verschillende URL's en haalt de browser elk font twee keer op.
  Beide staan daarom zonder hash.
- **Bestaat het bestand niet, dan komt de naam onveranderd terug.** Een
  ontbrekend bestand moet als 404 in de netwerktab zichtbaar blijven, niet hier
  gemaskeerd worden.
- **De pagina-overgang kan hier tegen.** `page-transitions.js` kloont de
  `<link data-page-css>` uit het opgehaalde document en vergelijkt op de naam in
  `data-page-css`, niet op de href. De hash loopt dus automatisch mee.

## Let op: het uitvoerpad

De bouwscripts schrijven naar de map boven deze (`UIT = ...parent.parent`), dus
naar de hoofdmap van de site. Verplaats je `_generator/`, dan verhuist de
uitvoer mee.
