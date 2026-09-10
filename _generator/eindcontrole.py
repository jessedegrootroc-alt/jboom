# -*- coding: utf-8 -*-
"""Controleert de gegenereerde pagina's op fouten die je met het oog mist.

    python3 _generator/eindcontrole.py

Draai dit na `bouw_alles.py`. Het kijkt niet of de site mooi is; het kijkt of er
niets kapot of dubbel is. Wat het nagaat:

  - kapotte interne links
  - precies één <h1> per pagina, en geen sprong in de koppenniveaus
  - unieke <title> en meta-omschrijving, en geen lege
  - resten van het oude template en van de vorige inhoud
  - oude contactgegevens, oude diensten, oude merkkleuren en oude lettertypen
  - verwijzingen naar beeld, stylesheets of scripts die er niet zijn
  - lege alinea's, afbeeldingen zonder alt en alinea's die elkaar herhalen
  - dubbele labels in de navigatie
  - hoeveel [CONTENT NODIG]-markeringen er staan (die horen er te zijn)
"""
import collections
import pathlib
import re
import sys

WORTEL = pathlib.Path(__file__).resolve().parent.parent
PAGINAS = sorted(WORTEL.glob('*.html'))

# Dingen die er niet meer in mogen staan. De eerste drie zijn resten van de
# oorspronkelijke template, de rest is van de vorige inhoud (Duyts
# Bouwconstructies uit Amsterdam) en van het merk daarvoor (Madegro).
VERBODEN = [
    (r'(?i)madegro', 'madegro'),
    (r'(?i)lorem ipsum', 'lorem'),
    (r'(?i)duyts', 'oude bedrijfsnaam (Duyts)'),
    (r'(?i)\bassistant\b|\bkarla\b|inter.tight', 'oud lettertype'),
    (r'(?i)funderingsherstel|constructieberekening|registerconstructeur', 'oude dienst'),
    (r'020[\s-]?\d{3}[\s-]?\d{4}|0182[\s-]?\d{6}', 'oud telefoonnummer'),
    (r'(?i)gouda|moordrecht|jacob van lennepkade', 'oud adres'),
    (r'(?i)#017E84|#0d7377|rgba\(1,\s*126,\s*132', 'oude merkkleur (petrol)'),
    (r'(?i)#463878|#143369|#C7D8E0|rgba\(70,\s*56,\s*120', 'oude merkkleur (indigo)'),
    # Het merk van J. Boom heeft geen blauw; dat was de standaardknopkleur van
    # het sitebuilder-thema van de bronsite. Zie brand-style.md.
    (r'(?i)#2178C4', 'geschrapt bronblauw'),
]

# Naast de pagina's ook de bestanden die niet gegenereerd worden: daar bleef bij
# de vorige migratie een oude naam in staan zonder dat het opviel.
EXTRA_BESTANDEN = ['styleguide.css', 'site.js', 'contactformulier.js', 'index.css',
                   'cases.css', 'service.css', 'contact.css', 'tekstpagina.css',
                   'cookiebalk.css', 'transitions.css', 'sitemap.xml', 'robots.txt']


LEEGTAGS = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source', 'area', 'base',
            'col', 'embed', 'param', 'track', 'wbr'}


def _nesting(pad):
    """Tags die niet gesloten worden of in de verkeerde volgorde sluiten."""
    import html.parser

    class Controle(html.parser.HTMLParser):
        def __init__(zelf):
            super().__init__(convert_charrefs=False)
            zelf.stapel, zelf.fouten = [], []

        def handle_starttag(zelf, tag, attrs):
            if tag not in LEEGTAGS:
                zelf.stapel.append(tag)

        def handle_endtag(zelf, tag):
            if tag in LEEGTAGS:
                return
            if not zelf.stapel or tag not in zelf.stapel:
                zelf.fouten.append(f'</{tag}> zonder open')
                return
            while zelf.stapel and zelf.stapel[-1] != tag:
                zelf.fouten.append(f'<{zelf.stapel.pop()}> niet gesloten')
            zelf.stapel.pop()

    c = Controle()
    c.feed(pad.read_text(encoding='utf-8'))
    rest = [t for t in c.stapel if t not in ('html', 'body', 'head')]
    return [f'{pad.name}: {x}' for x in c.fouten + [f'<{t}> blijft open' for t in rest]]


def tekst(el):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', el)).strip()


def main():
    print(f'EINDCONTROLE ({len(PAGINAS)} pagina\'s)\n')
    fouten = []
    bestanden = {p.name for p in PAGINAS}
    titels, omschrijvingen = collections.defaultdict(list), collections.defaultdict(list)
    markeringen = 0

    kapot, geen_h1, sprongen, leeg_alinea, geen_alt, dubbel_nav = [], [], [], [], [], []
    echo = []

    for p in PAGINAS:
        h = p.read_text(encoding='utf-8')

        # interne links
        for m in re.finditer(r'href="(?!https?:|mailto:|tel:|#)([^"#?]+)', h):
            doel = m.group(1)
            if doel.endswith('.html') and doel not in bestanden:
                kapot.append(f'{p.name} -> {doel}')

        # koppen
        h1 = re.findall(r'<h1\b', h)
        if len(h1) != 1:
            geen_h1.append(f'{p.name} ({len(h1)})')
        niveaus = [int(m.group(1)) for m in re.finditer(r'<h([1-6])\b', h)]
        vorig = 0
        for n in niveaus:
            if vorig and n > vorig + 1:
                sprongen.append(f'{p.name}: h{vorig} -> h{n}')
            vorig = n

        # title en omschrijving
        t = re.search(r'<title>(.*?)</title>', h, re.S)
        d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
        titels[tekst(t.group(1)) if t else ''].append(p.name)
        omschrijvingen[tekst(d.group(1)) if d else ''].append(p.name)

        # Lege alinea's. Een live region mag wél leeg zijn: die wordt door
        # JavaScript gevuld, en hij moet al in de DOM staan voordat er iets in
        # komt, anders kondigt een schermlezer de wijziging niet aan. Zo werkt
        # de tellerregel op projecten.html.
        for m in re.finditer(r'<p((?:[^>"]|"[^"]*")*)>\s*</p>', h):
            attr = m.group(1)
            if 'aria-live' in attr or 'role="status"' in attr:
                continue
            leeg_alinea.append(p.name)
        for m in re.finditer(r'<img\b((?:[^>"]|"[^"]*")*)>', h):
            if 'alt=' not in m.group(1):
                geen_alt.append(p.name)

        # dubbele labels in de balk
        nav = re.search(r'<nav class="submenu".*?</nav>', h, re.S)
        if nav:
            labels = [tekst(x.group(2)) for x in
                      re.finditer(r'<(a|button)[^>]*>(.*?)</\1>', nav.group(), re.S)]
            labels = [l for l in labels if l]
            for label, aantal in collections.Counter(labels).items():
                if aantal > 1:
                    dubbel_nav.append(f'{p.name}: "{label}" {aantal}x')

        # Twee alinea's die grotendeels hetzelfde zeggen. Dat gebeurt zodra een
        # herschreven lead te dicht bij de bronzin blijft: die bronzin staat
        # verderop ook nog in het uitlegblok, en dan leest de bezoeker hem twee
        # keer op één scherm.
        #
        # Alleen binnen <main>: de balk en de mobiele lade herhalen de menutekst
        # per definitie, en dat is geen dubbele content maar navigatie.
        #
        # Jaccard over de verzameling woorden en niet over de kortste van de
        # twee. Anders slaat hij aan op een samenvattende regel in een paneel
        # ("Eerst droog en heel, dan isolatie") die de stap erboven bewust kort
        # herhaalt; dat is de opzet van dat blok en geen fout.
        romp = re.search(r'<main\b.*?</main>', h, re.S)
        alineas = []
        if romp:
            for m in re.finditer(r'<p[^>]*>(.*?)</p>', romp.group(), re.S):
                t = tekst(m.group(1))
                if len(t) > 110:
                    alineas.append(t)
        for i, a in enumerate(alineas):
            wa = set(w for w in re.findall(r"[a-z']+", a.lower()) if len(w) > 3)
            for b in alineas[i + 1:]:
                wb = set(w for w in re.findall(r"[a-z']+", b.lower()) if len(w) > 3)
                if not wa or not wb:
                    continue
                overlap = len(wa & wb) / len(wa | wb)
                if overlap > 0.6:
                    echo.append(f'{p.name}: {a[:50]}...')
                    break

        markeringen += len(re.findall(r'\[CONTENT NODIG\]', h))

    def regel(naam, lijst, toon=3):
        vlag = 'FOUT' if lijst else 'ok  '
        extra = f'  {lijst[:toon]}' if lijst else ''
        print(f'  {vlag} {naam:34s} {len(lijst)}{extra}')
        if lijst:
            fouten.append(naam)

    regel('kapotte interne links', kapot)
    regel('pagina\'s zonder precies 1 h1', geen_h1)
    regel('sprongen in koppenniveaus', sprongen)
    regel('lege alinea\'s', leeg_alinea)
    regel('afbeeldingen zonder alt', sorted(set(geen_alt)))
    regel('dubbele labels in de navigatie', dubbel_nav)
    regel('alinea die zichzelf herhaalt', sorted(set(echo)))

    # Kolomklassen die de stylesheet niet kent. Die vallen niet op: de kolom
    # krijgt dan geen breedte, stapelt over de volle breedte en ziet eruit als
    # een bedoelde keuze. col-lg-5 en col-lg-7 stonden zo een tijd op
    # referenties.html.
    css = (WORTEL / 'styleguide.css').read_text(encoding='utf-8')
    bestaat = set(re.findall(r'\.(col-(?:lg|md|sm)?-?\d+)', css))
    onbekend = []
    for p in PAGINAS:
        for m in re.finditer(r'class="([^"]*\bcol-[^"]*)"', p.read_text(encoding='utf-8')):
            for k in m.group(1).split():
                if k.startswith('col-') and k not in bestaat:
                    onbekend.append(f'{p.name}: {k}')
    regel('kolomklasse die de stylesheet niet kent', sorted(set(onbekend)))

    # Losse ampersands. Een & die geen entiteit inleidt hoort in HTML als
    # &amp; te staan; browsers repareren dat meestal, maar een URL met &daddr=
    # erin is dan strikt genomen ongeldige HTML en een parser die niet
    # repareert leest het anders. Kwam voor in de routelink op contact.html.
    losse = []
    for p in PAGINAS:
        for m in re.finditer(r'&(?![a-zA-Z][a-zA-Z0-9]{1,8};|#\d{1,6};|#x[0-9a-fA-F]{1,5};)',
                             p.read_text(encoding='utf-8')):
            losse.append(f'{p.name}:{m.start()}')
    regel('losse ampersand', sorted(set(losse)))

    # Openstaande of verkeerd genestelde tags.
    nesting = []
    for p in PAGINAS:
        nesting += _nesting(p)
    regel('tag niet netjes gesloten', nesting)

    for veld, kaart in (('title', titels), ('omschrijving', omschrijvingen)):
        dubbel = {k: v for k, v in kaart.items() if k and len(v) > 1}
        leeg = kaart.get('', [])
        regel(f'dubbele {veld}', [f'{k[:30]}: {v}' for k, v in dubbel.items()], 1)
        regel(f'lege {veld}', leeg)

    tekstbestanden = list(PAGINAS) + [WORTEL / n for n in EXTRA_BESTANDEN
                                      if (WORTEL / n).exists()]
    for patroon, label in VERBODEN:
        treffers = [b.name for b in tekstbestanden
                    if re.search(patroon, b.read_text(encoding='utf-8'))]
        regel(label, treffers)

    # Verwijzingen naar bestanden die er niet zijn: beeld, stylesheets, scripts.
    ontbreekt = []
    for p in PAGINAS:
        h = p.read_text(encoding='utf-8')
        for m in re.finditer(r'(?:src|href)="(?!https?:|mailto:|tel:|data:|#)([^"?#]+)', h):
            doel = m.group(1)
            if doel.endswith('.html'):
                continue
            if not (WORTEL / doel).exists():
                ontbreekt.append(f'{p.name} -> {doel}')
        for m in re.finditer(r'srcset="([^"]+)"', h):
            for stuk in m.group(1).split(','):
                pad = stuk.strip().split(' ')[0]
                if pad and not pad.startswith('http') and not (WORTEL / pad).exists():
                    ontbreekt.append(f'{p.name} -> {pad}')
    regel('ontbrekende bestanden', sorted(set(ontbreekt)))

    # Openstaande punten in de bron. In de gegenereerde HTML mag er geen staan;
    # in de CSS en de JavaScript is een TODO een legitieme aantekening bij werk
    # dat nog moet gebeuren. Ze worden dus geteld en niet als fout gemeld, met
    # uitzondering van een TODO die in een pagina terechtkomt.
    in_html = [p.name for p in PAGINAS
               if 'TODO-CONTENT' in p.read_text(encoding='utf-8')]
    regel('TODO in een gegenereerde pagina', in_html)
    openstaand = [b.name for b in tekstbestanden
                  if b not in PAGINAS and 'TODO-CONTENT' in b.read_text(encoding='utf-8')]

    print(f'\n  [CONTENT NODIG]-markeringen: {markeringen} (bewust: ontbrekende brondata)')
    if openstaand:
        print(f'  openstaande TODO-CONTENT in de bron: {", ".join(openstaand)} '
              f'(zie CONTENT-TODO.md)')
    print('\nRESULTAAT: ' + ('ALLES OK' if not fouten else 'AANDACHT: ' + ', '.join(fouten)))
    return 1 if fouten else 0


if __name__ == '__main__':
    sys.exit(main())
