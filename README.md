# Aannemersbedrijf J. Boom: website

Statische site: HTML, CSS en vanilla JavaScript, geen build-stap en geen
npm-afhankelijkheden. Van een CDN komen alleen GSAP (met ScrollTrigger en
ScrollSmoother) en Barba.js; samen doen die de pagina-overgangen en het vloeiende
scrollen. Het lettertype staat lokaal in `assets/fonts/`.

## Lokaal draaien

Open `index.html` in de browser, of draai de meetserver vanuit deze map:

    python3 _generator/devserver.py 8099

Die comprimeert en stuurt cache-headers, zoals een echte host; `python3 -m
http.server` doet dat niet en meet daardoor ongeveer vijf Lighthouse-punten te
laag. Alle links zijn relatief, dus de map kan zonder aanpassing als eigen site
gepubliceerd worden.

## De pagina's zijn gegenereerd

De 22 HTML-bestanden in deze map worden gemaakt door de scripts in
`_generator/`. **Pas je een HTML-bestand met de hand aan, dan is die wijziging
weg zodra de generator opnieuw draait.**

    python3 _generator/bouw_alles.py

| bestand | wat het doet |
|---|---|
| `jboom/bron/` | de contentexport van www.jboom.nl: de zeven pagina's als platte tekst |
| `inhoud_jboom.py` | de feiten: bedrijfsgegevens, diensten, projectseries, referenties, partners |
| `inhoud_copy.py` | de conversielaag: koppen, leads, tussenkoppen en CTA's |
| `inhoud_dienst_verhaal.py` | de verhaallaag onder de dienstpagina's (situaties, aanpak, input, oplevering, vragen) |
| `schil.py` | de gedeelde onderdelen: balk, voettekst, hero's, knoppen, kaarten, beeld |
| `bouw_jboom_home.py` | `index.html` |
| `bouw_jboom_dienst.py` | `diensten.html` en de negen dienstpagina's |
| `bouw_jboom_projecten.py` | `projecten.html` en de twee projectseries |
| `bouw_jboom_bedrijf.py` | over ons, historie, werkwijze, referenties |
| `bouw_jboom_contact.py` | contact, offerte, privacybeleid, cookies |
| `bouw_jboom_sitemap.py` | `sitemap.xml` en `robots.txt` |
| `maak_assets.py` | zet het bronbeeld om naar responsive WebP en AVIF (alleen nodig bij nieuw beeld) |
| `maak_herovideo.py` | zet de aangeleverde herofilm om naar `assets/video/` (alleen nodig bij een nieuwe film) |

De CSS, de JavaScript en alles in `assets/` worden **niet** gegenereerd; die
bewerk je rechtstreeks.

## Controleren

    python3 _generator/eindcontrole.py

Kijkt niet of de site mooi is, maar of er niets kapot of dubbel is: kapotte
links, ontbrekende bestanden, koppenniveaus, dubbele titles, alinea's die
zichzelf herhalen, ontbrekende alt-teksten en resten van de vorige inhoud.
Draai dit na elke `bouw_alles.py`.

## De sitemap

| pagina | bestand |
|---|---|
| Home | `index.html` |
| Diensten | `diensten.html` |
| — Aanbouw en uitbouw | `aanbouw-en-uitbouw.html` |
| — Deuren en puien | `deuren-en-puien.html` |
| — Verbouw | `verbouw.html` |
| — Dakopbouw en dakkapel | `dakopbouw-en-dakkapel.html` |
| — Renovatie | `renovatie.html` |
| — Nieuwbouw | `nieuwbouw.html` |
| — Bouwadvies en bouwtekening | `bouwadvies.html` |
| — Kunststof kozijnen en voorgevels | `kunststof-kozijnen.html` |
| — Gevelbekleding | `gevelbekleding.html` |
| Projecten | `projecten.html` |
| — Aanbouw, opbouw en verbouw | `projecten-aanbouw-opbouw-verbouw.html` |
| — Dakkapellen, gevels, kozijnen en deuren | `projecten-dakkapellen-gevels-kozijnen-deuren.html` |
| Klanten over J. Boom | `referenties.html` |
| Over ons | `over-ons.html` |
| Historie | `historie.html` |
| Werkwijze | `werkwijze.html` |
| Offerte | `offerte.html` |
| Contact | `contact.html` |
| Privacybeleid | `privacybeleid.html` |
| Cookies | `cookies.html` |

## Waar de inhoud vandaan komt

Drie lagen, met verschillende verantwoordelijkheden:

- **De feiten** komen uit `_generator/jboom/bron/`, de tekst van de zeven
  pagina's van www.jboom.nl. Alles wat deze site over het bedrijf beweert staat
  daar. Er is geen dienst, cijfer, certificering, garantie of doorlooptijd
  toegevoegd die daar niet staat.
- **De formulering** is herschreven. De koppen, leads en CTA's staan in
  `inhoud_copy.py`; bovenin dat bestand staat welke keuzes daarin zijn gemaakt.
- **De vakinhoudelijke uitleg** onder de dienstpagina's staat in
  `inhoud_dienst_verhaal.py`. Dat is de enige tekst op deze site die niet uit de
  bron komt; bovenin dat bestand staat waar hij wél op gebaseerd is (de
  Omgevingswet, het Besluit bouwwerken leefomgeving, het Omgevingsloket) en wat
  er bewust niet in staat.

Op de homepage ligt in de hero nog een vierde laag: de **aangeleverde
herofilm**. Die is stockmateriaal en geen opname van J. Boom, dus hij draagt
geen enkele bewering: het beeld is decoratief, er staat geen tekst bij die de
film aan het bedrijf toeschrijft, en het stilstaande beeld eronder is de foto
van de eigen gele bedrijfsbussen. Wie de film niet krijgt — beweging uit,
databesparing, trage lijn, geen JavaScript — ziet dus J. Boom zelf en geen
stockbeeld. De afweging staat in `_generator/maak_herovideo.py`.

De merklaag — kleuren en typografie — komt uit `brand-style.md`. Layout,
componenten, spacing, radius, animaties en responsive gedrag komen uit de
template en zijn niet uit `brand-style.md` overgenomen.

Wat er nog van J. Boom nodig is, staat in `CONTENT-TODO.md`.
