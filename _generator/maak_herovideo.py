#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zet de aangeleverde herofilm om naar het bestand dat de homepage laadt.

    python3 maak_herovideo.py

    jboom/video/hero-bron.mp4  ->  assets/video/jboom-hero-1280.mp4

Er komt ook een stilstaand beeld uit: het EERSTE beeldje van de film, dat in de
hero onder de film ligt.

    jboom/video/hero-eerste-beeld.png  ->  assets/foto/jboom-hero-stilstaand-*

Dat beeld moet er liggen. Speelt de film niet -- `prefers-reduced-motion`,
Save-Data of geen JavaScript, want dan hangt site.js hem niet in -- dan zag je
daarvoor het antraciet uit `.hero` en was de hero een zwart vlak. Nu zie je
hetzelfde beeld, alleen stil. Omdat het het eerste beeldje is, is er geen sprong
op het moment dat de film erin vervaagt.

Niet als `poster`-attribuut op het video-element: `.hero--video` staat op
opacity 0 tot de film echt loopt, dus een poster zou net zo onzichtbaar zijn als
de film zelf. Vandaar een echte <img> eronder.

Het beeld is gedeclareerd in beeldplan.json (sleutel `jboom-hero-stilstaand`,
met een `bronpad`), dus `maak_assets.py` bouwt de ladder voortaan zelf mee.

DE FILM IS GEEN OPNAME VAN J. BOOM
Aangeleverd als `hero-logistiek_20260910102219.mp4` (10 september 2026) en
stockmateriaal: een grijze bestelbus in een woonstraat, een monteur die een
kozijn stelt, en een woning met een dakkapel. Het wérk in beeld is wat J. Boom
doet; de bus en de monteur zijn niet van J. Boom -- de bussen van J. Boom zijn
geel en staan op de foto in de hero eronder. Daarom:

  * het beeld is decoratief (het staat in `.hero--beeld`, aria-hidden);
  * er staat geen tekst bij die de film aan het bedrijf toeschrijft;
  * de film draagt geen enkele bewering. Wat de hero beweert, staat in de kop
    en de lead, en dat komt uit inhoud_copy.py.

WAAROM DEZE INSTELLINGEN
  -an            de bron heeft een geluidsspoor. Een achtergrondfilm die
                 automatisch speelt mag geen geluid hebben, en zonder spoor
                 hoeft de browser het ook niet op te halen.
  -crf 27        1,4 MB voor tien seconden 1280x720. site.js rekent op
                 ongeveer anderhalve megabyte.
  +faststart     zet de moov-atom vooraan, zodat de browser kan beginnen te
                 spelen voordat het hele bestand binnen is.
  yuv420p        de pixelindeling die elke browser leest.

Eén breedte en geen ladder: op een staande telefoon wordt van dit 16:9-beeld
maar het middelste kwart gebruikt, dus een smallere versie zou daar juist het
eerst onscherp worden. Dat staat ook zo in de toelichting bij `[data-herovideo]`
in site.js.

De bron blijft in jboom/video/ staan zodat dit script opnieuw kan draaien.
"""
import pathlib
import shutil
import subprocess
import sys

HIER = pathlib.Path(__file__).resolve().parent
BRON = HIER / 'jboom' / 'video' / 'hero-bron.mp4'
UIT = HIER.parent / 'assets' / 'video' / 'jboom-hero-1280.mp4'
STIL = HIER / 'jboom' / 'video' / 'hero-eerste-beeld.png'


def main():
    if shutil.which('ffmpeg') is None:
        sys.exit('ffmpeg niet gevonden. Nodig om de herofilm om te zetten.')
    if not BRON.exists():
        sys.exit(f'Bronfilm ontbreekt: {BRON}')

    UIT.parent.mkdir(parents=True, exist_ok=True)

    # Het eerste beeldje, voor het stilstaande beeld onder de film. De ladder
    # eromheen maakt maak_assets.py, via de "bronpad" in beeldplan.json.
    subprocess.run(['ffmpeg', '-v', 'error', '-i', str(BRON),
                    '-vframes', '1', '-q:v', '1', '-y', str(STIL)], check=True)
    print(f'  {STIL.name:34s} eerste beeldje ({STIL.stat().st_size/1024:.0f} kB)')
    print('  -> draai maak_assets.py voor de webp/avif-ladder')

    subprocess.run([
        'ffmpeg', '-v', 'error', '-i', str(BRON),
        '-an',
        '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.0',
        '-crf', '27', '-preset', 'slower', '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart',
        '-y', str(UIT),
    ], check=True)

    kb = UIT.stat().st_size / 1024
    print(f'  {UIT.name:34s} {kb:7.1f} kB')
    if kb > 1800:
        print('  LET OP: groter dan 1,8 MB. site.js rekent op ongeveer 1,5 MB.')


if __name__ == '__main__':
    main()
