#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zet het merkpatroon uit bron/ om naar de WebP-ladder die de site gebruikt.

    python3 maak_patroon.py

Dit script TEKENT niets en HERTINT niets: het schaalt alleen en comprimeert.
De bronbestanden zijn de aangeleverde export van Jesse (10 september 2026,
`Group 12.png` en `Group 13.png`), een geel vlak met een raster van witte
driehoekjes dat naar onderen dichter wordt.

  bron/HERO.SECTION.png          1440 x 940   het aangeleverde heropatroon
  bron/CTA.SECTION.BACKGROUND.png 2880 x 760  de aangeleverde brede band
  bron/HERO.SECTION2.png         1440 x 1440  hieruit opgebouwd: het heropatroon
                                              onderaan, daarboven de egale
                                              grondkleur #FFC801. De bovenhelft
                                              van het bronbeeld is pixel voor
                                              pixel diezelfde kleur, dus dat
                                              voegt niets toe wat er niet al was.

LET OP: maak_patronen() in maak_assets.py doet iets anders met dezelfde
bestanden. Die hertint ze van antraciet naar goud, wat klopte voor het vorige
patroon maar dit gele beeld juist kapotmaakt. Draai voor het patroon dus dit
script en niet die functie.
"""
import pathlib, subprocess
from PIL import Image

HIER    = pathlib.Path(__file__).resolve().parent
PATROON = HIER.parent / 'assets' / 'patronen'
BRON    = PATROON / 'bron'

# bronbestand -> (stam van de webp-naam, breedtes)
VLAKKEN = [
    ('HERO.SECTION.png',           'hero-patroon',        [720, 1000, 1440]),
    ('HERO.SECTION2.png',          'hero-patroon-mobiel', [720, 800, 1440]),
    ('CTA.SECTION.BACKGROUND.png', 'cta-patroon',         [1440, 2880]),
]


def main():
    for bestand, stam, breedtes in VLAKKEN:
        pad = BRON / bestand
        if not pad.exists():
            print(f'  {bestand} ontbreekt, overgeslagen')
            continue
        im = Image.open(pad).convert('RGB')
        for breedte in breedtes:
            hoogte = round(im.height * breedte / im.width)
            tmp = BRON / f'_tmp-{stam}-{breedte}.png'
            im.resize((breedte, hoogte), Image.LANCZOS).save(tmp)
            uit = PATROON / f'{stam}-{breedte}.webp'
            subprocess.run(['cwebp', '-q', '88', '-m', '6', str(tmp), '-o', str(uit)],
                           check=True, capture_output=True)
            tmp.unlink()
            print(f'  {uit.name:34s} {uit.stat().st_size/1024:6.1f} kB')


if __name__ == '__main__':
    main()
