#!/usr/bin/env python3
"""Zet het bronmateriaal van www.jboom.nl om naar de assets van deze site.

Vier dingen gebeuren hier:

1. Het logo. Het bestand op de bronsite is 300 x 88 en staat op een
   doorzichtige achtergrond. De header vraagt twee varianten: de gekleurde voor
   de witte balk, en een witte voor de balk die over een donkere hero ligt. De
   witte variant is hetzelfde merk met alle dekkende pixels op wit; het rood
   verdwijnt daar dus, want een rood woordmerk op een donkere foto komt niet los.

2. Het beeldmerk en de deelafbeelding. De favicon is het vierkant met de B uit
   het logo, uitgesneden op de kleurgrens en niet op een geraden getal. De
   deelafbeelding (1200 x 630) is het logo op het antraciet uit de merklaag.

3. De foto's. De template vraagt per beeld meerdere breedtes in WebP en AVIF
   (zie foto() in schil.py). De ladder hangt af van hoe groot het bronbestand
   is: de bronsite levert brede banden van 1920-2000px en projectfoto's van
   600-1024px, en er wordt niet opgeschaald. Wat er niet is, wordt niet
   verzonnen: een foto van 800px krijgt geen 1600px-variant.

4. Het merkpatroon. Het patroon is van de oorspronkelijke template en loopt
   daar van geel via petrol naar donkerpaars. Die kleuren zijn niet van J. Boom.
   De vorm van het patroon blijft (dat is template), de kleuren gaan naar de
   merklaag: van Boom Goud naar het antraciet uit het logo.

Draaien:  python3 maak_assets.py

Het verwacht de bronbestanden in `jboom/beeld/`. Staan die er niet, dan stopt
het script met een melding in plaats van met halve bestanden.
"""
import json
import pathlib
import shutil
import subprocess
import sys

from PIL import Image

HIER = pathlib.Path(__file__).resolve().parent
WORTEL = HIER.parent
BRON = HIER / 'jboom' / 'beeld'
FOTO = WORTEL / 'assets' / 'foto'
LOGO = WORTEL / 'assets' / 'logo'
FAVICON = WORTEL / 'assets' / 'favicon'
SOCIAL = WORTEL / 'assets' / 'social'
PATRONEN = WORTEL / 'assets' / 'patronen'

ANTRACIET = (26, 23, 27)      # --color-text / --color-groen
GOUD = (212, 184, 28)         # --color-secondary, Boom Goud

# Kwaliteit. WebP op 82 en AVIF op 60 leveren bij deze foto's visueel hetzelfde
# beeld; AVIF is bij die instelling ruwweg een derde kleiner.
WEBP_Q = 82
AVIF_Q = 60


def eis_bron():
    if not BRON.exists():
        sys.exit(f'Bronbeeld ontbreekt: {BRON}\n'
                 'Zet de foto\'s van www.jboom.nl daar neer en draai opnieuw.')


# ---------------------------------------------------------------------- ladder
def ladder(breedte):
    """De breedtes die van dit beeld gemaakt worden.

       Er wordt nooit opgeschaald: de grootste trede is de bronbreedte zelf.
       De treden erboven vallen weg, zodat srcset geen maat aanbiedt die in
       werkelijkheid een uitvergroting is."""
    kandidaten = [420, 640, 800, 1024, 1280, 1600, 1920]
    uit = [b for b in kandidaten if b < breedte]
    uit.append(breedte)
    # Twee treden onder elkaar die minder dan 15% schelen leveren de browser
    # niets op en kosten wel twee bestanden.
    gefilterd = []
    for b in uit:
        if not gefilterd or b >= gefilterd[-1] * 1.15:
            gefilterd.append(b)
        else:
            gefilterd[-1] = b
    return gefilterd


def schrijf(im, doel, breedte):
    """Eén breedte wegschrijven in WebP en AVIF."""
    hoogte = round(im.height * breedte / im.width)
    klein = im if breedte == im.width else im.resize((breedte, hoogte), Image.LANCZOS)
    klein.save(doel.with_name(f'{doel.stem}-{breedte}.webp'), 'WEBP',
               quality=WEBP_Q, method=6)
    klein.save(doel.with_name(f'{doel.stem}-{breedte}.avif'), 'AVIF',
               quality=AVIF_Q, speed=4)
    return hoogte


def maak_fotos(plan):
    FOTO.mkdir(parents=True, exist_ok=True)
    maten = {}
    for sleutel, r in plan.items():
        if sleutel.startswith('_'):
            continue
        bronpad = next(BRON.glob(f'*{r["bron"]}.*'), None)
        if bronpad is None:
            sys.exit(f'{sleutel}: bronbestand met nummer {r["bron"]} niet gevonden in {BRON}')
        im = Image.open(bronpad).convert('RGB')
        breedtes = ladder(im.width)
        hoogte = None
        for b in breedtes:
            h = schrijf(im, FOTO / f'{sleutel}.webp', b)
            if b == breedtes[-1]:
                hoogte = h
        maten[sleutel] = {'breed': breedtes[-1], 'hoog': hoogte,
                          'breedtes': breedtes, 'alt': r['alt'], 'bron': bronpad.name}
        print(f'  {sleutel:34s} {im.width:5d}px -> {breedtes}')
    return maten


# ------------------------------------------------------------------------ logo
def maak_logos():
    bron = next(BRON.glob('*001.png'), None)
    if bron is None:
        sys.exit(f'Logo (…001.png) niet gevonden in {BRON}')
    LOGO.mkdir(parents=True, exist_ok=True)
    im = Image.open(bron).convert('RGBA')
    vak = im.getbbox()
    im = im.crop(vak)

    # De gekleurde variant gaat onveranderd mee: dit is het merk zoals het is.
    im.save(LOGO / 'jboom-logo.png')
    im.save(LOGO / 'jboom-logo.webp', 'WEBP', lossless=True, method=6)

    # De witte variant, voor de balk die over een donkere hero ligt.
    #
    # Alles wit maken werkt hier niet. Het beeldmerk is een rode B in een
    # antraciet vierkant; wordt alles wit, dan wordt het vierkant een wit blok
    # en verdwijnt de B daarin. Het merk valt dan uit elkaar.
    #
    # Daarom twee gebieden, gescheiden op dezelfde kleurgrens die de favicon
    # gebruikt:
    #   links van de grens (het vierkant) is de B het merk. Zijn dekking wordt
    #   de roodheid van de pixel — R min de sterkste van G en B — zodat het
    #   vierkant doorzichtig wordt en alleen de letter overblijft.
    #   rechts van de grens staan het woordmerk (rood) en het regeltje eronder
    #   (bijna zwart) al op een doorzichtige ondergrond; daar blijft de dekking
    #   zoals hij is.
    # Beide gebieden worden daarna wit ingekleurd.
    grens = _merkgrens(im)
    alfa = im.getchannel('A').load()
    pix = im.convert('RGB').load()
    wit = Image.new('RGBA', im.size, (255, 255, 255, 0))
    doel = wit.load()
    for y in range(im.height):
        for x in range(im.width):
            a = alfa[x, y]
            if a == 0:
                continue
            if x < grens:
                r, g, b = pix[x, y]
                rood = max(0, r - max(g, b))
                a = round(a * min(1.0, rood / 140))
            doel[x, y] = (255, 255, 255, a)
    wit.save(LOGO / 'jboom-logo-wit.png')
    wit.save(LOGO / 'jboom-logo-wit.webp', 'WEBP', lossless=True, method=6)

    print(f'  logo {im.size[0]}x{im.size[1]} (kleur + wit, PNG + lossless WebP)')
    return im


def _merkgrens(logo):
    """De rechterrand van het antraciete vierkant met de B.

       Gezocht en niet geschat: het is de eerste kolom waarin minder dan de
       helft van de pixels nog donker is. Zo blijft de uitsnede kloppen als het
       logobestand ooit in een andere maat wordt aangeleverd."""
    rgb = logo.convert('RGB').load()
    for x in range(logo.width):
        donker = sum(1 for y in range(logo.height)
                     if max(rgb[x, y]) < 90)
        if donker < logo.height * 0.5:
            return x
    return logo.width


def maak_favicon(logo):
    """Het vierkant met de B, uitgesneden op de kleurgrens."""
    FAVICON.mkdir(parents=True, exist_ok=True)
    grens = _merkgrens(logo)
    merk = logo.crop((0, 0, grens, logo.height))
    # Op een vierkant zetten, met het antraciet als vulling: het beeldmerk is
    # een vlak en geen letter op een doorzichtige ondergrond.
    zijde = max(merk.size)
    vak = Image.new('RGBA', (zijde, zijde), ANTRACIET + (255,))
    vak.alpha_composite(merk, ((zijde - merk.width) // 2, (zijde - merk.height) // 2))
    for maat, naam in ((32, 'jboom-favicon-32.png'), (192, 'jboom-favicon-192.png'),
                       (180, 'jboom-apple-touch-icon.png')):
        vak.resize((maat, maat), Image.LANCZOS).convert('RGB').save(FAVICON / naam)
    vak.resize((48, 48), Image.LANCZOS).convert('RGB').save(
        FAVICON / 'jboom-favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    print(f'  favicon: beeldmerk {grens}x{logo.height} -> vierkant {zijde}px')


def maak_deelafbeelding(logo):
    """1200 x 630 voor Open Graph en Twitter.

       Wit vlak met het merk in kleur, en onderaan de gouden band uit de
       merklaag. Niet andersom: het logo op antraciet betekent de witte variant
       en dan is het rood weg, terwijl juist dat rood het merk herkenbaar maakt
       in een tijdlijn."""
    SOCIAL.mkdir(parents=True, exist_ok=True)
    kaart = Image.new('RGB', (1200, 630), (255, 255, 255))
    band = 56
    kaart.paste(Image.new('RGB', (1200, band), GOUD), (0, 630 - band))
    breed = 780
    merk = logo.resize((breed, round(logo.height * breed / logo.width)), Image.LANCZOS)
    kaart.paste(merk, ((1200 - merk.width) // 2, (630 - band - merk.height) // 2), merk)
    kaart.save(SOCIAL / 'jboom-deelafbeelding.png')
    print('  deelafbeelding 1200x630')


# ------------------------------------------------------------------- patroon
def _ramp(t):
    """Van antraciet (t=0) naar Boom Goud (t=1), in een rechte lijn."""
    return tuple(round(ANTRACIET[i] + (GOUD[i] - ANTRACIET[i]) * t) for i in range(3))


def hertint(im):
    """Het patroon in de merkkleuren zetten.

       De vorm blijft precies zoals hij is; alleen de kleur van elke pixel gaat
       naar de merklaag. De positie op de ramp is de relatieve helderheid van de
       bronpixel, uitgerekt over het bereik dat in het bestand voorkomt, zodat
       het lichtste vlak ook echt goud wordt en het donkerste antraciet."""
    grijs = im.convert('L')
    laag, hoog = grijs.getextrema()
    spanwijdte = max(1, hoog - laag)
    tabel = []
    for kanaal in range(3):
        tabel += [_ramp(min(1.0, max(0.0, (v - laag) / spanwijdte)))[kanaal]
                  for v in range(256)]
    return grijs.convert('RGB').point(tabel)


def maak_patronen():
    bron = PATRONEN / 'bron'
    opdrachten = [
        ('HERO.SECTION.png', 'hero-patroon', [720, 1000, 1440]),
        ('HERO.SECTION2.png', 'hero-patroon-mobiel', [720, 800, 1440]),
        ('CTA.SECTION.BACKGROUND.png', 'cta-patroon', [1440, 2880]),
    ]
    for bestand, naam, breedtes in opdrachten:
        pad = bron / bestand
        if not pad.exists():
            print(f'  patroon {bestand} ontbreekt, overgeslagen')
            continue
        im = hertint(Image.open(pad).convert('RGB'))
        for b in breedtes:
            h = round(im.height * b / im.width)
            im.resize((b, h), Image.LANCZOS).save(
                PATRONEN / f'{naam}-{b}.webp', 'WEBP', quality=88, method=6)
        print(f'  patroon {naam}: {breedtes}')
    meet_patroon_contrast()


def _lum(rgb):
    def k(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (k(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def meet_patroon_contrast():
    """Wat wit op het CTA-patroon haalt, gemeten op de bitmap zelf.

       De uitkomst staat als commentaar bij .cta-slot__hoofd in styleguide.css.
       Verandert het patroon, dan hoort dit getal daar bijgewerkt te worden;
       daarom staat de meting hier en niet in een losse notitie."""
    pad = PATRONEN / 'cta-patroon-1440.webp'
    if not pad.exists():
        return
    im = Image.open(pad).convert('RGB')
    waarden = sorted((_lum(p) + 0.05) for p in im.resize((360, 190)).getdata())
    ratio = [1.05 / v for v in waarden]          # wit is 1,0 + 0,05
    n = len(ratio)
    # ratio loopt van donkerste pixel (hoogste verhouding) naar lichtste.
    print(f'  CTA-patroon, wit erop: donkerst {ratio[0]:.2f}:1  '
          f'mediaan {ratio[n // 2]:.2f}:1  lichtst {ratio[-1]:.2f}:1')
    scrims = [0.0, 0.25, 0.40, 0.55, 0.70]
    for s in scrims:
        gemengd = [tuple(round(p[i] * (1 - s) + ANTRACIET[i] * s) for i in range(3))
                   for p in im.resize((120, 64)).getdata()]
        # De ongunstigste plek voor witte tekst is de lichtste pixel; dat is
        # de laagste verhouding, dus min() en niet max().
        slechtst = min(1.05 / (_lum(p) + 0.05) for p in gemengd)
        print(f'    waas {int(s * 100):3d}%: ongunstigste pixel {slechtst:.2f}:1')


# ----------------------------------------------------------------------- main
def main():
    eis_bron()
    plan = json.loads((HIER / 'beeldplan.json').read_text(encoding='utf-8'))
    print('logo')
    logo = maak_logos()
    maak_favicon(logo)
    maak_deelafbeelding(logo)
    print('patroon')
    maak_patronen()
    print('foto\'s')
    maten = maak_fotos(plan)
    (HIER / 'beeldmaten.json').write_text(
        json.dumps(maten, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'\n{len(maten)} beelden, maten in beeldmaten.json')


if __name__ == '__main__':
    main()
