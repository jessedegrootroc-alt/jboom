# -*- coding: utf-8 -*-
"""De feiten: alles wat deze site over Aannemersbedrijf J. Boom beweert.

Eén bron van waarheid. Elk gegeven hieronder is terug te vinden in
`jboom/bron/` — de tekst van de zeven pagina's van www.jboom.nl. Bij elk blok
staat uit welke pagina het komt.

WAT HIER WEL IN STAAT
  Bedrijfsgegevens, de negen diensten die de bron noemt, de twee fotoseries,
  de zeven referenties met naam en datum, de vaste samenwerkingspartners, en de
  historie van 1935 tot nu.

WAT HIER NIET IN STAAT, EN OOK NERGENS ANDERS
  Doorlooptijden, prijzen, garanties, aantallen projecten, certificeringen,
  keurmerken, teamgroottes anders dan de twee die de bron zelf noemt, en
  klantnamen buiten de zeven ondertekende referenties. De bron noemt die niet,
  dus deze site ook niet.

TWEE DINGEN DIE BEWUST ANDERS ZIJN GEFORMULEERD DAN OP DE BRON
  1. De bron zegt op drie plekken iets anders over de leeftijd van het bedrijf:
     "Bijna 80 jaar", "Al ruim 80 jaar" en "ruim 79 jaar". Die pagina's zijn
     rond 2018 geschreven en lopen dus achter. Hier staat overal het jaartal
     zelf (1935) en "vierde generatie"; dat is wat de bron feitelijk zegt en
     het veroudert niet.
  2. De bron schrijft het bedrijf soms als "J. Boom" midden in een zin met een
     hoofdletter op de verkeerde plek ("HUUR EEN AANNEMER VAN J. Boom IN").
     Dat is een zetfout, geen naam; de naam is Aannemersbedrijf J. Boom v.o.f.

De herschreven koppen, leads en CTA's staan niet hier maar in `inhoud_copy.py`.
De verhaallaag onder de dienstpagina's staat in `inhoud_dienst_verhaal.py`.
"""
import re

MARKERING = '[CONTENT NODIG]'


# ---------------------------------------------------------------------------
#  Bedrijf en contact          bron: footer op elke pagina + contact.txt
# ---------------------------------------------------------------------------
NAAM = 'J. Boom'
NAAM_VOLUIT = 'Aannemersbedrijf J. Boom v.o.f.'
NAAM_KORT = 'Aannemersbedrijf J. Boom'
TAGLINE = 'Aanbouw &middot; Verbouw &middot; Dakkapellen &middot; Kunststof kozijnen'  # uit het logo

STRAAT = 'Pascalstraat 24'
POSTCODE = '1446 TX'
PLAATS = 'Purmerend'
POSTCODE_PLAATS = f'{POSTCODE} {PLAATS}'
ADRES = f'{STRAAT}, {POSTCODE_PLAATS}'

TELEFOON_WEERGAVE = '0299 - 43 34 98'
TELEFOON_LINK = '+31299433498'
EMAIL = 'info@jboom.nl'
KVK = '36019793'

FACEBOOK = 'https://www.facebook.com/AannemersbedrijfJ.Boom'
# De routelink van de bronsite, met de ampersand als entiteit. In een href hoort
# een losse & geëscaped te zijn; de URL zelf is onveranderd.
ROUTE = 'https://www.google.com/maps?&amp;daddr=52.5156457,4.991863'
PRIVACY_PDF = ('https://www.jboom.nl/uploads/c3ajfmR2/'
               'PrivacyencookiestatementvolgensminisiterieEZJBoomAannemersbedrijfVOF.pdf')
OUDERE_REFERENTIES_PDF = 'https://www.jboom.nl/uploads/VthRNIs0/OuderereferentiesJBoom.pdf'

OPRICHTING = '1935'
GENERATIE = 'vierde'
WERKGEBIED = 'Purmerend en omstreken'
# De bron noemt op de homepage twee mensen bij naam, met hun relatie en rol.
VAKMENSEN = [
    ('Mario Boom', 'Zoon van J. Boom sr.'),
    ('Martin Babel', 'Zwager van Mario'),
]
# De bron noemt op de homepage en op /diensten voor wie er gewerkt wordt.
DOELGROEPEN = ['Particulieren', 'Verenigingen van Eigenaren']

# De bron noemt geen reactietermijn. Op de contactpagina staat alleen dat je kunt
# bellen, mailen of het formulier invullen; hier wordt dus geen aantal dagen
# beloofd dat J. Boom nooit heeft toegezegd.
REACTIETIJD = 'zo snel mogelijk'


# ---------------------------------------------------------------------------
#  Diensten                    bron: diensten.txt + het lijstje op home.txt
# ---------------------------------------------------------------------------
# De bron noemt op /diensten negen werkzaamheden met een eigen kopje, en op de
# homepage hetzelfde rijtje als opsomming onder "Huur ons in voor". Die negen
# staan hieronder, één op één.
#
# De indeling in drie hoofddiensten met werkzaamheden eronder is van deze site
# en niet van de bron: die zet alle negen als losse kopjes onder elkaar. De
# groepering is geen nieuwe bewering over J. Boom maar een ordening, en elke
# koppeling is terug te lezen in de brontekst zelf:
#
#   Aanbouw en uitbouw  <- Deuren en puien: "wilt u zelf een deur of pui kiezen
#                          voor uw aanbouw of nieuwbouwhuis?"
#   Verbouw             <- Renovatie en Dakopbouw en dakkapel: de bron noemt ze
#                          alle drie als manieren om een bestaande woning aan te
#                          passen
#   Nieuwbouw           <- Bouwadvies en bouwtekening: "Op basis van uw wens
#                          maken we graag een bouwtekening voor u"
#
# (bestand, titel, beeldsleutel)
HOOFDDIENSTEN = [
    ('aanbouw-en-uitbouw.html', 'Aanbouw en uitbouw', 'jboom-aanbouw-18'),
    ('verbouw.html', 'Verbouw', 'jboom-aanbouw-13'),
    ('nieuwbouw.html', 'Nieuwbouw', 'jboom-aanbouw-08'),
]

# (bestand, titel, hoofddienst of None, beeldsleutel)
DIENSTEN = [
    ('deuren-en-puien.html', 'Deuren en puien', 'Aanbouw en uitbouw', 'jboom-dakkapel-32'),
    ('dakopbouw-en-dakkapel.html', 'Dakopbouw en dakkapel', 'Verbouw', 'jboom-dakkapel-03'),
    ('renovatie.html', 'Renovatie', 'Verbouw', 'jboom-aanbouw-32'),
    ('bouwadvies.html', 'Bouwadvies en bouwtekening', 'Nieuwbouw', 'jboom-aanbouw-16'),
    ('kunststof-kozijnen.html', 'Kunststof kozijnen en voorgevels', None, 'jboom-voorgevel-kozijnen'),
    ('gevelbekleding.html', 'Gevelbekleding', None, 'jboom-aanbouw-24'),
]

ALLE_DIENSTEN = ([(b, t, None, beeld) for b, t, beeld in HOOFDDIENSTEN]
                 + list(DIENSTEN))
LOSSE_DIENSTEN = [d for d in DIENSTEN if d[2] is None]


def kinderen(hoofddienst_titel):
    """De werkzaamheden onder een hoofddienst, in de volgorde van de tabel."""
    return [d for d in DIENSTEN if d[2] == hoofddienst_titel]


def dienst_titel(bestand):
    return next(t for b, t, *_ in ALLE_DIENSTEN if b == bestand)


def dienst_beeld(bestand):
    return next(r[-1] for r in ALLE_DIENSTEN if r[0] == bestand)


def is_hoofddienst(bestand):
    return bestand in [h[0] for h in HOOFDDIENSTEN]


def ouder(bestand):
    return next((r[2] for r in ALLE_DIENSTEN if r[0] == bestand), None)


# De tekst die de bron zelf bij elke dienst zet. Letterlijk overgenomen; deze
# alinea's komen op de dienstpagina terug in het uitlegblok. Wat de bron per
# dienst schrijft is één alinea, dus dat is wat er staat.
#
#   bron: diensten.txt, de kopjes onder "Allround aannemer in Purmerend"
#   bron van Aanbouw en uitbouw: het kopje "Aan- of uitbouw"
#   bron van Bouwadvies: het blok "Bouwadvies" op home.txt
BRONTEKST = {
    'nieuwbouw.html': [
        'Heeft u er altijd al van gedroomd om uw eigen huis te ontwerpen en '
        'laten bouwen? De aannemers van J. Boom zijn ook in te huren voor '
        'nieuwbouwprojecten op maat. Op basis van uw wens maken we graag een '
        'bouwtekening voor u. Wij coordineren het gehele project. Indien '
        'gewenst van de eerste tekening tot de finishing touch.',
    ],
    'verbouw.html': [
        'Fantaseert u van een open keuken of wilt u van twee kamers graag een '
        'maken? Heeft u altijd al gedroomd van een open haard of wilt u het '
        'plafond laten verlagen? J. Boom realiseert al uw verbouwplannen.',
    ],
    'dakopbouw-en-dakkapel.html': [
        'Heeft u een zolder met schuine muren en komt u ruimte tekort? Of wilt '
        'u uw slaapkamer vergroten? Kies voor een dakopbouw of dakkapel en '
        'creeer meer ruimte en lichtinval.',
    ],
    'aanbouw-en-uitbouw.html': [
        'Heeft u een fijn huis maar wilt u eigenlijk een grotere slaapkamer of '
        'een ruimere woonkamer? Laat u verrassen door de extra woonruimte die '
        'een aan- of uitbouw u biedt.',
    ],
    'renovatie.html': [
        'Is uw dak aan vervanging toe of kan uw huiskamer wel een nieuw laagje '
        'stucwerk gebruiken? Laat ons uw huis opknappen.',
    ],
    'gevelbekleding.html': [
        'Met gevelbekleding geeft u uw huis in een handomdraai een nieuwe '
        'uitstraling. Kies uit verschillende kleuren en materialen.',
    ],
    'deuren-en-puien.html': [
        'Tijd voor een nieuwe deur? Of wilt u zelf een deur of pui kiezen voor '
        'uw aanbouw of nieuwbouwhuis? Kies bijvoorbeeld voor openslaande '
        'deuren, een schuifpui of een andere pui naar wens. Ons aanbod in '
        'deuren en puien is heel divers.',
    ],
    'kunststof-kozijnen.html': [
        'Kunststof kozijnen en voorgevels zijn qua uiterlijk tegenwoordig bijna '
        'niet meer van houten te onderscheiden. Wat betreft functionaliteit '
        'biedt kunststof alleen maar voordelen. U bespaart op energiekosten '
        'door goede isolatie en kunststof is onderhoudsarm. Zo blijft uw '
        'kunststof kozijn of voorgevel lang mooi.',
    ],
    'bouwadvies.html': [
        'Uiteraard voorzien we u, indien gewenst, ook van bouwadvies en '
        'verzorgen we de technische tekeningen. Benieuwd hoe we uw plannen '
        'kunnen vertalen naar uw ideale huis? Vraag vrijblijvend een '
        'orientatiegesprek aan of laat een offerte opstellen.',
    ],
}


# ---------------------------------------------------------------------------
#  Vaste partners              bron: diensten.txt, "De krachten gebundeld"
# ---------------------------------------------------------------------------
# De bron noemt deze zes bedrijven bij naam als vaste samenwerkingspartners,
# met een link erbij waar die er was. Dit zijn dus geen opdrachtgevers en ook
# geen klantenlogo's: het zijn de partijen waarmee J. Boom een project
# uitvoert. Ze staan als woordmerk in de band en niet als logo, want er is geen
# enkel logobestand van ze en er is ook geen toestemming om dat te voeren.
#
# De links staan op de bron als http; ze zijn hier op https gezet omdat alle
# vijf dat ondersteunen. Nagelopen op 10 september 2026:
#   ewp.nl, smitheiwerken.nl                 werken onveranderd op https
#   deheer-elektrotechniek.nl                stuurt door naar de versie zonder www
#   sandersloodgieters.nl                    heeft geen certificaat voor www,
#                                            dus staat hier zonder www
#   selectwindows.nl                         stuurt door naar kozijncollectief.nl;
#                                            de naam die J. Boom noemt is Select
#                                            Windows, dus die blijft staan
PARTNERS = [
    ('EWP', 'Ontwerp, constructie en bouwadvies', 'https://ewp.nl/'),
    ('Select Windows', 'Leverancier van de kunststof kozijnen', 'https://www.selectwindows.nl/'),
    ('Smit Heiwerken', 'Heiwerken', 'https://www.smitheiwerken.nl/'),
    ('De Heer Elektrotechniek', 'Elektrotechnische installatie', 'https://deheer-elektrotechniek.nl/'),
    ('Sanders', 'Loodgieterswerk', 'https://sandersloodgieters.nl/'),
    ('Peter Helmich', 'Stuc- en spuitwerk', None),
]

# De bron noemt daarnaast, zonder bedrijfsnaam, met welke vakmensen er vast
# gewerkt wordt: "dezelfde stukadoors, metselaars en elektriciens".
VASTE_VAKMENSEN = ['stukadoors', 'metselaars', 'elektriciens']


# ---------------------------------------------------------------------------
#  Referenties                 bron: klanten-over-j-boom.txt
# ---------------------------------------------------------------------------
# Zeven ondertekende referenties, met de naam en de maand die de klant er zelf
# bij zette. Ze zijn ingekort waar ze over de post of over Facebook gingen; er
# is geen woord bij geschreven en geen oordeel aangescherpt. De volledige tekst
# staat in jboom/bron/klanten-over-j-boom.txt.
#
# (kop, citaat, naam, datum, waar het over ging, beeldsleutel)
REFERENTIES = [
    ('Prachtige nieuwe slaapkamer',
     'Wij slapen volgende week weer boven, maar dan in onze prachtige nieuwe '
     'slaapkamer.',
     'Ron &amp; Jos Teunis', 'mei 2014', 'Dakopbouw', 'jboom-dakkapel-05'),

    ('In een week de dakopbouw klaar',
     'Onvoorstelbaar snel is door jullie deze verbouwing gerealiseerd. In een '
     'week tijd veranderde onze slaapkamer met een behoorlijk schuin dak in een '
     'prachtige grote ruimte met openslaande deuren en grote zijramen. '
     'Complimenten voor de strakke planning, het meedenken, de netheid van '
     'werken, het dagelijks opruimen van de binnen- en buitenruimte.',
     'Ron &amp; Jos Teunis', 'oktober 2013', 'Dakopbouw', 'jboom-aanbouw-23'),

    ('Kunststof ramen en een nieuwe voordeur',
     'De vele reacties van familie, vrienden en buurtbewoners zijn erg positief; '
     'ze vonden de materiaalkeuze en de kleuren van binnen en van buiten erg '
     'mooi. Hierbij wil ik Martin en Mario hartelijk bedanken voor de goede '
     'afspraken, het advies, de planning en de mooie afwerking. Ik voel mij trots '
     'en prettig als ik weer thuiskom.',
     'Wilma Altena van Beetz', 'oktober 2013', 'Kunststof kozijnen', 'jboom-dakkapel-23'),

    ('Nooit lang hoeven wachten',
     'Door hun ervaring kwamen wij tot een wensenlijst waarop zij hun offerte af '
     'konden stemmen. De firma Boom staat voor kwaliteit. Je kunt hen '
     'vertrouwen: afspraak is afspraak, en mocht iets wijzigen ten opzichte van '
     'de gemaakte afspraak dan wordt er goed gecommuniceerd en een alternatief '
     'of oplossing geboden. Je wordt tijdens de verbouwing ontzorgd.',
     'Sabine Mulders en Jos Spork', 'september 2013', 'Opbouw en uitbouw',
     'jboom-aanbouw-18'),

    ('Uitbouw na de geboorte van onze zoon',
     'Jullie kwamen ervaren en betrouwbaar over en gaven ons ook het vertrouwen. '
     'Alles was goed achter elkaar gepland waardoor voor ons gevoel vaart werd '
     'gemaakt en geen onnodige tijd werd verspild. Waar we ons over verbazen en '
     'wat we zeer waarderen is de netheid van onze tuin na een werkdag.',
     'Jenny &amp; Chau', None, 'Uitbouw', 'jboom-aanbouw-14'),

    ('Dat wauw-gevoel',
     'Ondanks dat het alweer een paar maanden geleden is sinds de verbouwing, heb '
     'ik nog altijd dat wauw-gevoel als ik mijn woonkamer binnenkom. Wat een '
     'ruimte! Helemaal gelukkig ben ik met onze kunststof schuifpui waar we na '
     'goed advies van de mannen voor gekozen hebben. De verbouwing zelf liep '
     'vlekkeloos.',
     'Familie Bollen', 'augustus 2013', 'Verbouw en schuifpui', 'jboom-aanbouw-04'),

    ('Onderscheidend in dienstverlening',
     'Dat we voor de tweede keer zo&rsquo;n grote klus door jullie laten '
     'uitvoeren zegt eigenlijk al genoeg. Natuurlijk vooral vanwege jullie '
     'vakmanschap en nette afwerking. Maar waar jullie je minstens zo veel in '
     'onderscheiden is op het gebied van dienstverlening.',
     'Bob van Kampen en Ren&eacute;e Korthout', 'augustus 2013', 'Verbouw',
     'jboom-aanbouw-32'),
]


# ---------------------------------------------------------------------------
#  Projecten                   bron: de twee fotoseries van de bronsite
# ---------------------------------------------------------------------------
# De bronsite heeft geen projectpagina's met een verhaal erbij: er zijn twee
# categorieen met daarin een fotoserie, en verder niets. Er is dus per foto geen
# opdrachtgever, plaats, jaar, opgave, aanpak of resultaat bekend.
#
# Die worden hier ook niet verzonnen. Wat er wel is — de categorie, wat er te
# zien is, en welke dienst erbij hoort — staat hieronder, en de twee pagina's
# zijn daarmee volwaardige overzichten van uitgevoerd werk in plaats van
# verzonnen case studies.
#
# (bestand, slug op de bron, titel, beeldsleutel voor de hero, prefix van de
#  galerijsleutels, de diensten waar deze serie bij hoort)
PROJECTSERIES = [
    {
        'bestand': 'projecten-aanbouw-opbouw-verbouw.html',
        'bron': 'https://www.jboom.nl/projecten/aanbouw-opbouw--verbouw',
        'titel': 'Aanbouw, opbouw en verbouw',
        'kort': 'Aanbouw, opbouw &amp; verbouw',
        'hero': 'jboom-aanbouw-schuifpui',
        'prefix': 'jboom-aanbouw-',
        'diensten': ['aanbouw-en-uitbouw.html', 'verbouw.html',
                     'dakopbouw-en-dakkapel.html', 'renovatie.html'],
    },
    {
        'bestand': 'projecten-dakkapellen-gevels-kozijnen-deuren.html',
        'bron': 'https://www.jboom.nl/projecten/dakkapellen-gevels-kozijnen--deuren',
        'titel': 'Dakkapellen, gevels, kozijnen en deuren',
        'kort': 'Dakkapellen, gevels, kozijnen &amp; deuren',
        'hero': 'jboom-dakkapel-raampartij',
        'prefix': 'jboom-dakkapel-',
        'diensten': ['dakopbouw-en-dakkapel.html', 'kunststof-kozijnen.html',
                     'deuren-en-puien.html', 'gevelbekleding.html'],
    },
]


def serie(bestand):
    return next(s for s in PROJECTSERIES if s['bestand'] == bestand)


# ---------------------------------------------------------------------------
#  Tekstgereedschap
# ---------------------------------------------------------------------------
def splits_lang(alineas, maximum=55):
    """Een alinea van meer dan `maximum` woorden opknippen op zinsgrens.

       De woorden veranderen niet; er komt alleen een alineagrens waar toch al
       een punt stond. Een alinea van zeventig woorden leest op een scherm als
       een muur."""
    uit = []
    for a in alineas:
        if len(a.split()) <= maximum:
            uit.append(a)
            continue
        zinnen = re.split(r'(?<=[.!?])\s+', a.strip())
        blok = []
        for zin in zinnen:
            blok.append(zin)
            if sum(len(z.split()) for z in blok) >= maximum * 0.6:
                uit.append(' '.join(blok))
                blok = []
        if blok:
            if uit and len(' '.join(blok).split()) < 12:
                uit[-1] += ' ' + ' '.join(blok)
            else:
                uit.append(' '.join(blok))
    return uit


def _tekens(t):
    """Losse aanhalings- en deeltekens netjes maken; de tekst zelf blijft."""
    if not t:
        return t
    return (t.replace('&', '\x00').replace('\x00amp;', '&amp;')
             .replace('\x00rsquo;', '&rsquo;').replace('\x00lsquo;', '&lsquo;')
             .replace('\x00ldquo;', '&ldquo;').replace('\x00rdquo;', '&rdquo;')
             .replace('\x00ndash;', '&ndash;').replace('\x00mdash;', '&mdash;')
             .replace('\x00middot;', '&middot;').replace('\x00hellip;', '&hellip;')
             .replace('\x00eacute;', '&eacute;').replace('\x00euml;', '&euml;')
             .replace('\x00iuml;', '&iuml;').replace('\x00ouml;', '&ouml;')
             .replace('\x00uuml;', '&uuml;').replace('\x00egrave;', '&egrave;')
             .replace('\x00sup2;', '&sup2;').replace('\x00euro;', '&euro;')
             .replace('\x00shy;', '&shy;').replace('\x00times;', '&times;')
             .replace('\x00', '&amp;')
             .replace('’', '&rsquo;').replace('‘', '&lsquo;')
             .replace('“', '&ldquo;').replace('”', '&rdquo;')
             .replace('–', '&ndash;').replace('—', '&mdash;')
             .replace('é', '&eacute;').replace('ë', '&euml;').replace('ï', '&iuml;')
             .replace('ö', '&ouml;').replace('ü', '&uuml;').replace('è', '&egrave;')
             .replace('á', '&aacute;').replace('í', '&iacute;').replace('ó', '&oacute;')
             .replace('ú', '&uacute;').replace('ç', '&ccedil;').replace('â', '&acirc;')
             .replace('ê', '&ecirc;').replace('î', '&icirc;').replace('û', '&ucirc;')
             .replace('²', '&sup2;').replace('€', '&euro;').replace('…', '&hellip;'))


# Nederlandse samenstellingen breken in een hero van 80px of in een kaart van
# een kwart pagina niet vanzelf goed af; de browser zet de streep dan op de
# verkeerde plek. Voor de woorden die op deze site in een kop staan geven we het
# afbreekpunt zelf op met een zacht afbreekstreepje. Dat is onzichtbaar zolang
# het woord past.
#
# Alleen voor zichtbare koppen. In een <title>, meta description of schema.org
# hoort geen zacht afbreekstreepje.
AFBREEKPUNTEN = [
    ('Dakopbouw', 'Dak&shy;opbouw'),
    ('dakopbouw', 'dak&shy;opbouw'),
    ('Gevelbekleding', 'Gevel&shy;bekleding'),
    ('gevelbekleding', 'gevel&shy;bekleding'),
    ('Bouwtekening', 'Bouw&shy;tekening'),
    ('bouwtekening', 'bouw&shy;tekening'),
    ('Bouwadvies', 'Bouw&shy;advies'),
    ('bouwadvies', 'bouw&shy;advies'),
    ('Voorgevels', 'Voor&shy;gevels'),
    ('voorgevels', 'voor&shy;gevels'),
    ('Aannemersbedrijf', 'Aannemers&shy;bedrijf'),
    ('Dakkapellen', 'Dak&shy;kapellen'),
    ('dakkapellen', 'dak&shy;kapellen'),
    ('Verenigingen', 'Ver&shy;enigingen'),
]


def afbreek(titel):
    """Zachte afbreekstreepjes in een zichtbare kop."""
    if not titel:
        return titel
    uit = titel
    for heel, gebroken in AFBREEKPUNTEN:
        uit = uit.replace(heel, gebroken)
    return uit
