# -*- coding: utf-8 -*-
"""Bouwt de hele site opnieuw op uit de content van www.jboom.nl.

    python3 bouw_alles.py

De HTML in de hoofdmap is gegenereerd; pas je daar met de hand iets aan, dan is
dat weg zodra dit script draait. Feiten wijzig je in inhoud_jboom.py, de
formulering in inhoud_copy.py, de uitleg onder de dienstpagina's in
inhoud_dienst_verhaal.py, en de indeling in de bouwscripts.

De afbeeldingen worden hier NIET opnieuw omgezet; dat doet maak_assets.py en dat
hoeft alleen als er beeld bijkomt of verandert.
"""
# Eerst minificeren, dan pas de pagina's schrijven. De verwijzingen in de HTML
# krijgen een hash van het bestand dat de browser ophaalt, en die bestanden
# moeten er dus al staan; bouw_jboom_home schrijft index.html al bij het
# importeren, vandaar dat dit hierboven staat en niet onderaan.
import minify
minify.main()

import bouw_jboom_home            # noqa: F401  (schrijft index.html bij import)
import bouw_jboom_dienst
import bouw_jboom_projecten
import bouw_jboom_bedrijf
import bouw_jboom_contact
import bouw_jboom_sitemap

bouw_jboom_dienst.main()
bouw_jboom_projecten.main()
bouw_jboom_bedrijf.main()
bouw_jboom_contact.main()
bouw_jboom_sitemap.main()
print('klaar')
