# -*- coding: utf-8 -*-
"""sitemap.xml en robots.txt, uit dezelfde paginalijst als de rest.

Zo kan een pagina niet in de sitemap ontbreken of erin blijven staan nadat hij
weg is: de lijst komt uit inhoud_jboom.py, niet uit een los bestand.
"""
import pathlib
import sys
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import BASIS
import inhoud_jboom as D

UIT = pathlib.Path(__file__).resolve().parent.parent


def paginas():
    """Elke pagina met zijn gewicht.

       De homepage, het dienstenoverzicht en de offertepagina staan hoog: dat
       zijn de ingangen. De twee tekstpagina's staan laag; die worden gezocht,
       niet gevonden."""
    rijen = [('index.html', '1.0'),
             ('diensten.html', '0.9'),
             ('offerte.html', '0.9'),
             ('contact.html', '0.8')]
    rijen += [(b, '0.8') for b, _, _ in D.HOOFDDIENSTEN]
    rijen += [(b, '0.7') for b, _, _, _ in D.DIENSTEN]
    rijen += [('projecten.html', '0.8')]
    rijen += [(s['bestand'], '0.7') for s in D.PROJECTSERIES]
    rijen += [('referenties.html', '0.7'), ('over-ons.html', '0.7'),
              ('werkwijze.html', '0.6'), ('historie.html', '0.5')]
    rijen += [('privacybeleid.html', '0.2'), ('cookies.html', '0.2')]
    return rijen


def main():
    vandaag = date.today().isoformat()
    regels = "\n".join(
        f'  <url>\n    <loc>{BASIS}/{b}</loc>\n'
        f'    <lastmod>{vandaag}</lastmod>\n'
        f'    <priority>{gewicht}</priority>\n  </url>'
        for b, gewicht in paginas())
    (UIT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'{regels}\n</urlset>\n', encoding='utf-8')

    (UIT / 'robots.txt').write_text(
        'User-agent: *\n'
        'Allow: /\n\n'
        f'Sitemap: {BASIS}/sitemap.xml\n', encoding='utf-8')
    print(f'sitemap.xml ({len(paginas())} pagina\'s) en robots.txt geschreven')
    return [b for b, _ in paginas()]


if __name__ == '__main__':
    main()
