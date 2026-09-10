# Brand Style

Merklaag gedestilleerd uit **https://www.jboom.nl/** (Aannemersbedrijf J. Boom v.o.f., Purmerend).
Alleen kleur en typografie. Geen layout, componenten, spacing, borders, shadows of interacties.

Bronnen van deze analyse:
de theme-CSS die de site inline meestuurt (`<style>`-blok met `.headline`, `.bodytext`, `.button`,
`nav`, `.footertext`, rij-ID's `#r1074` / `#r2192`), de computed styles van de live pagina
(area-gewogen achtergrondkleuren en tekstkleur-frequentie), en een pixelanalyse van het logo
(`uploads/rmO5v7zE/AannemersbedrijfJ.Boom001.png`).

---

## Brand Direction

Nuchter, direct en ambachtelijk: een lokaal aannemersbedrijf dat zichtbaar wil zijn, niet subtiel.
Het merk leunt op twee kleuren uit het logo — een warm signaalrood en een bijna-zwart antraciet —
met wit als rustige drager en een okergouden band als herkenbaar merkvlak.
De typografie is één humanistische sans, zwaar gezet in koppen en rustig in lopende tekst.
Robuust en herkenbaar, met contrast als voorwaarde in plaats van als bijvangst.

---

## Color System

### Primary
- **Name:** Boom Red
- **HEX:** `#D42A24` (rgb 212 42 36)
- **Usage:** De signatuurkleur uit het logo. Primaire CTA-achtergrond met witte tekst, actieve
  navigatiestatus, belangrijke markeringen. Dit is de enige actiekleur in het systeem.
- **Bron:** `#E5322C` (logo + `nav > ul li a` + `.form input[type=submit]`), minimaal verdonkerd
  voor WCAG AA — zie Accessibility.

### Secondary
- **Name:** Boom Gold
- **HEX:** `#D4B81C` (rgb 212 184 28)
- **Usage:** Het ondersteunende merkvlak. Contrasterende secties en banden (op de bron: de
  navigatiebalk en de contactband). Uitsluitend als **achtergrond**, nooit als tekstkleur.
  Tekst op dit vlak is altijd `--color-text`.

### Accent
- **Name:** Gold Ink
- **HEX:** `#7C6C10` (rgb 124 108 16)
- **Usage:** De tekstveilige variant van de goudfamilie: links in lopende tekst, labels,
  subkoppen en kleine typografische highlights op lichte achtergronden. Bewust géén tweede
  merkkleur maar dezelfde familie als Secondary, alleen leesbaar gemaakt.
- **Bron:** `#857311` (`.subtitle`, `.bodytext a`, `.footertext a`), minimaal verdonkerd.

### Background
- **HEX:** `#FFFFFF`
- **Usage:** De dominante pagina-ondergrond. Op de bron veruit het grootste oppervlak
  (≈ 11.6 mln px² tegenover ≈ 0.31 mln px² geel en ≈ 0.05 mln px² goud).

### Background Subtle
- **HEX:** `#F4F3F0` (rgb 244 243 240)
- **Usage:** Rustige, licht warme afwisseling binnen de witte basis: blokken die iets moeten
  loskomen zonder een gekleurd merkvlak te worden. Vervangt de vijf bijna identieke grijzen
  van de bron.

### Text Primary
- **HEX:** `#1A171B` (rgb 26 23 27)
- **Usage:** Alle lopende tekst en koppen op lichte achtergronden, en de tekst op het gouden
  merkvlak. Rechtstreeks uit het logo; iets warmer en zachter dan puur zwart.

### Text Muted
- **HEX:** `#5C5960` (rgb 92 89 96)
- **Usage:** Ondersteunende tekst, metadata, bijschriften, formulierhulp. Duidelijk zachter dan
  `--color-text`, maar nog ruim leesbaar. Alleen op `--color-background` en
  `--color-background-subtle` gebruiken, niet op het gouden vlak.

### Border Soft
- **HEX:** `#E4E1DC` (rgb 228 225 220)
- **Usage:** Zachte, decoratieve scheidingen binnen de bestaande componenten. Uitsluitend
  decoratief; een rand die betekenis draagt (focus, fout, geselecteerde staat) gebruikt
  `--color-text-muted` of `--color-primary`.

---

## 60 30 10 Distribution

### 60%
- **Color:** `#FFFFFF` — Background
- **Usage:** Pagina-ondergrond, alle grote oppervlakken, de standaardbasis van elke sectie.
  Aangevuld met `#F4F3F0` voor rustige afwisseling binnen dezelfde 60%-laag.

### 30%
- **Color:** `#D4B81C` — Secondary (Boom Gold), ondersteund door `#1A171B` voor donkere vlakken
- **Usage:** De contrasterende merklaag: gekleurde banden en secties die de pagina ritme geven.
  Tekst op dit vlak is altijd `#1A171B` (9.03:1).

### 10%
- **Color:** `#D42A24` — Primary (Boom Red)
- **Usage:** De enige actiekleur: primaire CTA's, actieve staat, kleine nadrukken. Nooit als
  vlakvulling voor hele secties, anders verdwijnt de signaalwerking.

**Contrastvoorwaarde bij deze verhouding:** de rode CTA haalt tegen wit 5.05:1 en tegen
`#F4F3F0` 4.55:1, maar tegen het gouden vlak slechts 2.57:1. Op een gouden band is de knop
daarom antraciet (`#1A171B`, 9.03:1) met witte tekst, niet rood.

---

## Color Tokens

```css
:root {
  /* Merk */
  --color-primary:            #D42A24; /* Boom Red — CTA-vlak, actieve staat, nadruk */
  --color-secondary:          #D4B81C; /* Boom Gold — merkvlak/band, alleen achtergrond */
  --color-accent:             #7C6C10; /* Gold Ink — links, labels, subkoppen op licht */

  /* Oppervlakken */
  --color-background:         #FFFFFF; /* pagina-ondergrond (60%) */
  --color-background-subtle:  #F4F3F0; /* rustige afwisseling binnen de witte basis */

  /* Tekst */
  --color-text:               #1A171B; /* koppen en lopende tekst, ook op het gouden vlak */
  --color-text-muted:         #5C5960; /* ondersteunende tekst, alleen op licht */

  /* Lijnen */
  --color-border-soft:        #E4E1DC; /* decoratieve scheiding */
}
```

Optioneel, alleen als de template al met kanaalwaarden werkt:

```css
:root {
  --color-primary-rgb: 212 42 36;
  --color-text-rgb:    26 23 27;
}
```

Witte tekst op `--color-primary` en op `--color-text` is de vaste tekstkleur binnen die vlakken
(5.05:1 respectievelijk 17.76:1). Daar is geen apart token voor nodig.

---

## Contrast Matrix

| Element | Foreground | Background | Contrast | Status |
|---|---|---|---|---|
| Body text | `#1A171B` | `#FFFFFF` | 17.76:1 | AA Pass |
| Body text op subtiel vlak | `#1A171B` | `#F4F3F0` | 16.01:1 | AA Pass |
| Heading | `#1A171B` | `#FFFFFF` | 17.76:1 | AA Pass |
| Muted text | `#5C5960` | `#FFFFFF` | 6.88:1 | AA Pass |
| Muted text op subtiel vlak | `#5C5960` | `#F4F3F0` | 6.20:1 | AA Pass |
| Link | `#7C6C10` | `#FFFFFF` | 5.24:1 | AA Pass |
| Link op subtiel vlak | `#7C6C10` | `#F4F3F0` | 4.72:1 | AA Pass |
| Primary CTA (tekst) | `#FFFFFF` | `#D42A24` | 5.05:1 | AA Pass |
| CTA vs page | `#D42A24` | `#FFFFFF` | 5.05:1 | Pass (≥ 3:1) |
| CTA vs subtiel vlak | `#D42A24` | `#F4F3F0` | 4.55:1 | Pass (≥ 3:1) |
| Tekst op merkvlak | `#1A171B` | `#D4B81C` | 9.03:1 | AA Pass |
| Tekst op donker vlak | `#FFFFFF` | `#1A171B` | 17.76:1 | AA Pass |
| CTA op donker vlak (tekst) | `#FFFFFF` | `#D42A24` op `#1A171B` | 5.05:1 tekst / 3.52:1 vlak | AA Pass / Pass |
| Label (nadruk) | `#7C6C10` | `#FFFFFF` | 5.24:1 | AA Pass |

Combinaties die het **niet** halen en daarom uit het systeem zijn gesloten:

| Verboden combinatie | Contrast | Reden |
|---|---|---|
| `#FFFFFF` op `#D4B81C` | 1.97:1 | Wit op goud is onleesbaar — gebruik `#1A171B`. |
| `#7C6C10` op `#D4B81C` | 2.66:1 | Gouden ink op gouden vlak — gebruik `#1A171B`. |
| `#5C5960` op `#D4B81C` | 3.50:1 | Muted tekst hoort niet op het merkvlak. |
| `#D42A24` op `#D4B81C` | 2.57:1 | Rode CTA op gouden band — gebruik de antraciete knop. |

---

## Typography

### Heading Font
- **Font:** Open Sans
- **Fallback:** `"Open Sans", "Segoe UI", "Helvetica Neue", Arial, sans-serif`
- **Weights:** 700 (koppen, labels)
- **Usage:** Display, H1 t/m H3, labels, knoplabels, navigatie.

### Body Font
- **Font:** Open Sans
- **Fallback:** `"Open Sans", "Segoe UI", "Helvetica Neue", Arial, sans-serif`
- **Weights:** 400 (lopende tekst), 700 (inline nadruk)
- **Usage:** Body large, body, small, formuliertekst, bijschriften.

Eén fontfamilie voor het hele systeem. De bron gebruikt Open Sans voor vrijwel alle zichtbare
tekst; een tweede familie zou hier ruis toevoegen zonder merkwaarde. Hiërarchie komt uit
gewicht, regelafstand en letterspatiëring, niet uit een tweede letter.

---

## Typography Tokens

```css
:root {
  --font-heading: "Open Sans", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  --font-body:    "Open Sans", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}
```

Laad exact twee snitten: **400** en **700** (normal). Meer gewichten zijn niet nodig en maken
het beeld onrustiger.

---

## Type Hierarchy

Geen `font-size` in deze laag: de responsive type scale van de bestaande template blijft leidend.

### Display
- **Font:** `var(--font-heading)`
- **Weight:** 700
- **Line height:** 1.15
- **Letter spacing:** -0.02em

### H1
- **Font:** `var(--font-heading)`
- **Weight:** 700
- **Line height:** 1.2
- **Letter spacing:** -0.01em

### H2
- **Font:** `var(--font-heading)`
- **Weight:** 700
- **Line height:** 1.3
- **Letter spacing:** -0.005em

### H3
- **Font:** `var(--font-heading)`
- **Weight:** 700
- **Line height:** 1.35
- **Letter spacing:** 0

### Body Large
- **Font:** `var(--font-body)`
- **Weight:** 400
- **Line height:** 1.5
- **Letter spacing:** 0

### Body
- **Font:** `var(--font-body)`
- **Weight:** 400
- **Line height:** 1.6
- **Letter spacing:** 0

### Small
- **Font:** `var(--font-body)`
- **Weight:** 400
- **Line height:** 1.55
- **Letter spacing:** 0

### Label
- **Font:** `var(--font-heading)`
- **Weight:** 700
- **Line height:** 1.2
- **Letter spacing:** 0.06em

De bron zet knop- en labelteksten in kapitalen. Neem dat alleen over als de template dat al doet;
de letterspatiëring van 0.06em hoort bij die kapitalen en houdt ze leesbaar.

---

## Font Consolidation

**Gevonden op de bron**

| Font | Waar | Aandeel zichtbare tekst |
|---|---|---|
| Open Sans | koppen, subkoppen, body, navigatie, knoppen, footer | ≈ 2.968 tekens |
| Roboto | alleen de `body`-regel van het theme | ≈ 10 tekens |
| FontAwesome / Font Awesome 5 & 6 | icoonglyphs | n.v.t. |
| Fontello, Nationale | gedeclareerd, niet geladen, nergens zichtbaar | 0 |

**Behouden:** Open Sans, in 400 en 700.

**Niet meegenomen:**
- *Roboto* — staat wel op `body` maar wordt overal overschreven door Open Sans. Het is een
  restant van de themabasis, geen merkkeuze; meenemen zou twee bijna identieke sans-serifs
  opleveren.
- *FontAwesome / Font Awesome 5 en 6* — icoonfonts, geen typografie. Buiten scope.
- *Fontello, Nationale* — gedeclareerd maar nooit geladen (`unloaded`) en nergens in beeld.
- De gewichten *300* en *800* — 300 wordt niet geladen; 800 kwam in de meting op ≈ 17 tekens
  (alleen het actieve menu-item). Te weinig om een eigen niveau te rechtvaardigen, en 800 naast
  700 levert vooral onrust op.

**Waarom dit consistenter is:** één familie in twee gewichten dekt alle acht hiërarchieniveaus.
De bron wisselde nergens zichtbaar van letter, dus er gaat geen merkkarakter verloren; wat
verdwijnt is de administratieve rommel van het themasysteem.

---

## Color Consolidation

**Gevonden op de bron**

| Kleur | Waar gebruikt |
|---|---|
| `#E5322C` rood | logo (41% van de logopixels), navigatie-items, formulier-submit |
| `#1A171B` antraciet | logo (51% van de logopixels) |
| `#000000` zwart | body-tekst, koppen, actieve nav-achtergrond |
| `#FFCB34` geel | contactband `#r1074`, hover van knoppen en `.scrollIcon`, social, accordeon |
| `#D4B81C` goud | navigatieband `#r2192`, hover van links |
| `#857311` olijfgoud | `.subtitle` (H2), links in body en footer |
| `#C7AD88` zandtint | standaard linkkleur, pijlen, icoonlijsten |
| `#2178C4` blauw | `.headline` (H1), alle `.button`-achtergronden, `.custom1` |
| `#F3F3F3`, `#F1F1F1`, `#FAFAFA`, `#EAEAEA`, `#ECEDEE` | lichte blokken, modals, accordeon |
| `#333333`, `#454545`, `#A5A5A5`, `#C0C0C0`, `#CCCCCC` | randen, secundaire tekst, dividers |

**Samengevoegd**

- De goudfamilie `#FFCB34` / `#D4B81C` / `#857311` / `#C7AD88` is teruggebracht tot **twee**
  rollen: één merkvlak (`#D4B81C`) en één tekstveilige inkt (`#7C6C10`). `#FFCB34` en `#D4B81C`
  doen visueel hetzelfde werk op verschillende banden; `#C7AD88` is te licht om iets te dragen
  (2.15:1 op wit) en verdwijnt.
- De vijf lichtgrijzen zijn één tint geworden: `#F4F3F0`, met een spoor warmte zodat hij bij de
  goudlaag past in plaats van er koel naast te liggen.
- De vijf donkergrijzen zijn één muted tint geworden: `#5C5960`.
- `#000000` en `#1A171B` zijn samengevoegd tot `#1A171B` — dezelfde leesbaarheid (17.76:1 tegen
  21:1), maar het is de kleur die daadwerkelijk in het logo staat.

**Bewust verwijderd: het blauw `#2178C4`.**
Dit is de opvallendste ingreep, dus expliciet: blauw draagt op de bron de H1's en alle knoppen,
maar het staat niet in het logo, heeft geen relatie met rood of goud, en levert een derde
concurrerende signaalkleur op. Het is de standaardknopkleur van het gebruikte sitebuilder-thema,
niet een merkbeslissing. Rood is de kleur die het merk daadwerkelijk bezit — het staat in het
logo, in de navigatie en op de verzendknop — en is daarmee de sterkste kandidaat voor de enige
accentkleur. Koppen worden antraciet, CTA's worden rood.

**Basis van het systeem:** rood, goud, antraciet, wit. Vier kleuren met elk één taak, plus twee
neutrale afgeleiden (subtiel vlak, muted tekst) en één zachte lijn.

**Aangepast voor contrast:** `#E5322C → #D42A24` en `#857311 → #7C6C10` — zie hieronder.

---

## Accessibility

Getoetst aan **WCAG 2.2 AA**: 4.5:1 voor normale tekst, 3:1 voor grote tekst en voor
betekenisdragende UI-elementen. Alle onderstaande waarden zijn berekend over de relatieve
luminantie volgens de WCAG-formule.

### Direct voldoende, ongewijzigd overgenomen

- `#1A171B` op `#FFFFFF` → **17.76:1** → AA Pass (lopende tekst en koppen)
- `#1A171B` op `#F4F3F0` → **16.01:1** → AA Pass
- `#1A171B` op `#D4B81C` → **9.03:1** → AA Pass (tekst op het gouden merkvlak)
- `#1A171B` op `#FFCB34` → **11.71:1** → AA Pass (de gele band van de bron, mocht die blijven)
- `#FFFFFF` op `#1A171B` → **17.76:1** → AA Pass (tekst op donkere vlakken)
- `#D4B81C` op `#1A171B` → **9.03:1** → AA Pass (goud als tekst op antraciet, indien nodig)

### Onvoldoende contrast, minimaal gecorrigeerd

**1. Merkrood — origineel `#E5322C`, definitief `#D42A24`**
- Origineel: wit op `#E5322C` → **4.35:1** → *Fail* voor normale tekst (4.5:1 vereist).
- Waarom nodig: dit is de kleur van de primaire CTA en van de verzendknop; knoptekst is normale
  tekst en moet 4.5:1 halen.
- Correctie: uitsluitend de lichtheid met circa 4% verlaagd, tint en verzadiging behouden
  (HSL-hue blijft ≈ 2°). Visueel nagenoeg hetzelfde signaalrood.
- Definitief: wit op `#D42A24` → **5.05:1** → **AA Pass**. Tegen de witte pagina → **5.05:1**
  (≥ 3:1 voor het knopvlak zelf), tegen `#F4F3F0` → **4.55:1**.

**2. Gouden inkt — origineel `#857311`, definitief `#7C6C10`**
- Origineel: `#857311` op `#FFFFFF` → **4.71:1** → net Pass, maar op het subtiele vlak
  `#F4F3F0` → **4.28:1** → *Fail*.
- Waarom nodig: deze kleur draagt op de bron links en H2-subkoppen; die verschijnen ook in
  lichtgrijze blokken. Een kleur die alleen op puur wit haalt, is niet breed inzetbaar.
- Correctie: circa 3% lichtheid eraf, tint ongewijzigd.
- Definitief: op `#FFFFFF` → **5.24:1** → **AA Pass**; op `#F4F3F0` → **4.72:1** → **AA Pass**.

**3. Muted tekst — origineel `#A5A5A5` / `#C0C0C0` / `#CCCCCC`, definitief `#5C5960`**
- Origineel: `#A5A5A5` op wit → **2.46:1** → *Fail*. `#CCCCCC` op wit → **1.61:1** → *Fail*.
- Waarom nodig: de bron gebruikt deze tinten voor dividers en secundaire tekst. Voor functionele
  ondersteunende tekst is dat onleesbaar.
- Definitief: `#5C5960` op `#FFFFFF` → **6.88:1**, op `#F4F3F0` → **6.20:1** → **AA Pass**.
  Ruim binnen de norm en toch duidelijk zachter dan `#1A171B`.

### Afgewezen combinaties (niet gecorrigeerd, maar uitgesloten)

- `#FFFFFF` op `#D4B81C` → **1.97:1** → *Fail*. Goud is te licht om wit te dragen; er is geen
  correctie die het goud nog goud laat. Regel: tekst op goud is altijd `#1A171B`.
- `#7C6C10` op `#D4B81C` → **2.66:1** → *Fail*. Links binnen een gouden band worden `#1A171B`,
  eventueel onderstreept, of een antraciete knop.
- `#5C5960` op `#D4B81C` → **3.50:1** → *Fail* voor normale tekst. Muted tekst hoort niet op het
  merkvlak.
- `#D42A24` op `#D4B81C` → **2.57:1** → *Fail* voor een UI-vlak (3:1). Een rode CTA op een gouden
  band komt onvoldoende los; gebruik daar de antraciete knop (`#1A171B`, **9.03:1** tegen goud,
  witte tekst **17.76:1**).
- `#C7AD88` op `#FFFFFF` → **2.15:1** → *Fail*. Als linkkleur op de bron onbruikbaar; verwijderd.
- Ter referentie het verwijderde blauw: `#2178C4` op wit → **4.62:1** en wit op `#2178C4` →
  **4.62:1**. Dat haalt AA net; het blauw is dus niet om contrastredenen geschrapt maar omdat het
  een derde concurrerende accentkleur was zonder merkbasis.

### Randen en niet-tekstuele elementen

`--color-border-soft` (`#E4E1DC`) haalt **1.30:1** tegen wit. Dat is bewust: deze lijn is
decoratief en valt daarmee buiten de 3:1-eis. Een rand die wél betekenis draagt — focusring,
foutstaat, geselecteerde staat — gebruikt `--color-text-muted` (**6.88:1**) of
`--color-primary` (**5.05:1**), beide ruim boven 3:1.

### Hiërarchie zonder kleurafhankelijkheid

Kop, body, label en muted tekst verschillen ook zonder kleur: gewicht (700 tegen 400),
regelafstand (1.15–1.35 tegen 1.5–1.6) en letterspatiëring (negatief in koppen, +0.06em in
labels). Links zijn herkenbaar aan kleur **plus** onderstreping of gewicht, nooit aan kleur
alleen.

**Conclusie:** alle combinaties die dit systeem aanbeveelt halen WCAG 2.2 AA. De laagste
aanbevolen tekstwaarde is 4.55:1 (rood knopvlak tegen het subtiele vlak, een UI-eis van 3:1),
de laagste normale-tekstwaarde is 4.72:1 (link op het subtiele vlak).

---

## Implementation Rules

### DO

- Pas alleen de kleurtokens aan: `--color-primary`, `--color-secondary`, `--color-accent`,
  `--color-background`, `--color-background-subtle`, `--color-text`, `--color-text-muted`,
  `--color-border-soft`.
- Pas alleen de font-family tokens aan: `--font-heading`, `--font-body`.
- Beperk de geladen snitten tot Open Sans 400 en 700.
- Behoud de bestaande responsive type scale en alle bestaande `font-size`-waarden.
- Behoud bestaande componenten, markup en klassenamen.
- Behoud bestaande spacing, grid, container widths en responsive logica.
- Behoud bestaande interacties, transitions en animaties.
- Gebruik `#1A171B` als enige tekstkleur op het gouden merkvlak.
- Gebruik op een gouden band de antraciete knop in plaats van de rode.
- Geef leesbaarheid voorrang wanneer een bronkleur onvoldoende toegankelijk is.
- Houd WCAG 2.2 AA aan als harde ondergrens, niet als streven.

### DO NOT

- Geen buttonvormen aanpassen.
- Geen border radius aanpassen.
- Geen padding, margin of gap aanpassen.
- Geen grid of flex layouts aanpassen.
- Geen container widths aanpassen.
- Geen shadows uit de bron kopiëren.
- Geen cards restylen.
- Geen hover effects, animaties of transitions uit de bron kopiëren.
- Geen iconenstijl of navigatiegedrag overnemen.
- Geen component markup aanpassen.
- Geen bestaande responsive logica veranderen.
- Geen font sizes uit de bron overnemen.
- Geen `#E5322C`, `#857311` of `#A5A5A5` letterlijk overnemen — gebruik de gecorrigeerde tokens.
- Geen extra accentkleur toevoegen; het blauw `#2178C4` blijft buiten het systeem.
- Geen wit of gouden inkt op het gouden merkvlak.
- Geen muted tekst voor informatie die de lezer nodig heeft om de content te begrijpen.
