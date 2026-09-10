# -*- coding: utf-8 -*-
"""De conversielaag: koppen, leads, tussenkoppen en CTA's.

De feiten komen onveranderd uit `inhoud_jboom.py` en dus uit `jboom/bron/`.
Hier staat alleen de formulering. Waar een bronalinea inhoudelijk klopte maar
zwak communiceerde, staat de herschreven versie hier en schuift de bronalinea
naar het uitlegblok verderop de pagina; er verdwijnt dus geen tekst.

Nagerekend: elk inhoudelijk woord in deze laag is teruggezocht in `jboom/bron/`.
Wat overblijft zijn werkwoorden en voegwoorden. Er staat hier geen dienst,
cijfer, certificering, garantie of bedrijfsclaim die niet uit de bron komt.

DE LEZER
  Particulieren en Verenigingen van Eigenaren in Purmerend en omstreken. Geen
  inkopers en geen vakgenoten: mensen die een keer in de vijftien jaar
  verbouwen en die vooral willen weten of ze de goede partij bellen. De toon is
  daarop afgestemd: nuchter, concreet, zonder bouwjargon waar het niet hoeft en
  met uitleg waar het jargon wel nodig is.

DRIE BEWUSTE KEUZES

  1. De H1 van een dienstpagina is de dienstnaam zelf ("Dakopbouw en dakkapel"),
     niet de belofte. Dat houdt de kop gelijk aan het menu en aan waar mensen op
     zoeken; het voordeel staat in de eerste H2 eronder. Alleen de homepage, de
     dienstenpagina, de projectenpagina en over-ons hebben een H1 die wel een
     belofte is.

  2. De bron zegt op drie plekken iets anders over de leeftijd van het bedrijf
     ("Bijna 80 jaar", "ruim 80 jaar", "ruim 79 jaar"). Die pagina's zijn rond
     2018 geschreven. Hier staat het jaartal: sinds 1935, vierde generatie.

  3. De bron gebruikt vaak de gebiedende wijs ("Huur ons in", "Laat ons uw huis
     opknappen"). Dat is een sterke stem en die blijft, maar niet in elke kop:
     zes keer achter elkaar leest het als een folder.
"""
import inhoud_jboom as D


# ---------------------------------------------------------------------------
#  Homepage
# ---------------------------------------------------------------------------
# De bron heeft op de homepage vier blokken: de introductie, "Huur ons in voor",
# "Bouwadvies", "Strakke planning, snel klaar" en "Bijna 80 jaar bouwplezier".
# Die vier komen hieronder terug, verdeeld over de secties van dit template.
HOME = {
    'eyebrow': 'Aannemer in Purmerend sinds 1935',
    'h1': 'Bouwen en verbouwen in Purmerend, door twee vakmensen die er zelf bij staan',
    # Eén alinea, 26 woorden. De tweede alinea die hier stond ("Martin en Mario
    # voeren het gesprek...") is eruit: de kop zegt al dat u met twee vakmensen
    # te maken heeft die er zelf bij staan, en de planningsbelofte staat verderop
    # op deze pagina en op werkwijze.html. Er is dus niets weggevallen wat de
    # bezoeker hier nog niet wist of straks niet leest.
    #
    # Wat deze alinea wel moet doen, doet de kop niet: zeggen wát er gebouwd
    # wordt en voor wie. Vandaar de drie werkzaamheden en de twee doelgroepen.
    # "Wij" en niet de bedrijfsnaam: die staat in het logo erboven en in de
    # eyebrow, en driemaal dezelfde naam in één hero leest als een formulier.
    'lead': [
        'Wordt uw huis te klein? Wij bouwen de aanbouw, dakkapel of verbouwing die '
        'dat oplost &mdash; voor particulieren en Verenigingen van Eigenaren in '
        'Purmerend en omstreken.',
    ],
    'cta_primair': ('Vraag een offerte aan', 'offerte.html'),
    'cta_secundair': ('Bekijk onze diensten', 'diensten.html'),

    'statement_kop': 'Gespecialiseerd in aanbouw, verbouw, dakkapellen en kunststof kozijnen',
    'statement': [
        'Wij zijn gespecialiseerd in aanbouw, verbouw, dakkapellen, dakopbouw en '
        'kunststof kozijnen. Daarnaast zijn we in te huren voor tal van andere '
        'bouwwerkzaamheden, van nieuwbouw tot renovatie.',
        'Ieder project weer zorgen onze jarenlange ervaring, persoonlijke aanpak en ons '
        'perfectionisme voor tevreden klanten en prachtige resultaten. Uiteraard '
        'voorzien we u, indien gewenst, ook van bouwadvies en verzorgen we de '
        'technische tekeningen.',
    ],
    'statement_cta': ('Meer over onze diensten', 'diensten.html'),

    'werkzaamheden_kop': 'Waarvoor u ons inhuurt',
    'werkzaamheden_lead': (
        'Van een dakkapel tot een complete nieuwbouwwoning. Drie richtingen waarin de '
        'meeste projecten vallen, met de werkzaamheden die daaronder horen.'),
    'losse_kop': 'En verder',
    'losse_lead': (
        'Twee werkzaamheden die net zo goed op zichzelf staan: de gevel en de '
        'kozijnen.'),

    'projecten_kop': 'Werk dat er al staat',
    'projecten_cta': ('Bekijk alle projecten', 'projecten.html'),

    'planning_kop': 'Strakke planning, snel klaar',
    'planning': [
        'Start met de realisatie van uw droomhuis en laat de bouw of verbouwing '
        'uitvoeren door Aannemersbedrijf J. Boom. In no time kunt u genieten van uw '
        'nieuwe woonruimte.',
        'Wij houden namelijk van een strakke planning. Hierdoor weet u van tevoren '
        'altijd wat u kunt verwachten en wanneer uw woning klaar is voor gebruik. Onze '
        'werktijden zijn flexibel. Is er nood aan de man? Dan staan wij zo op de stoep.',
    ],

    'over_kop': 'Sinds 1935 bouwplezier in en rondom Purmerend',
    'over': [
        'Al sinds 1935 wordt er door de aannemers van J. Boom met veel plezier gebouwd '
        'en verbouwd. Inmiddels staat de vierde generatie aan het roer.',
        'De zwagers Martin en Mario werken voornamelijk in Purmerend en omstreken en '
        'nemen hoofdzakelijk opdrachten van particulieren aan. Ze werken snel en '
        '&mdash; vanzelfsprekend &mdash; zorgvuldig.',
    ],
    'over_cta': ('Over Aannemersbedrijf J. Boom', 'over-ons.html'),

    'slot_kop': 'Huur een aannemer van J. Boom in',
    'slot': (
        'Hoe groot of klein uw project ook is, wij gaan graag voor u aan de slag. Bel '
        f'{D.TELEFOON_WEERGAVE}, mail ons of vraag vrijblijvend een orientatiegesprek '
        'aan.'),
}


# ---------------------------------------------------------------------------
#  Dienstenoverzicht
# ---------------------------------------------------------------------------
DIENSTEN_OVERZICHT = {
    'h1': 'Allround aannemer in Purmerend',
    'lead_kop': 'Dakkapel of aanbouw laten bouwen?',
    'lead': [
        'Hoewel we gespecialiseerd zijn in aanbouw, verbouw, dakkapellen, dakopbouw en '
        'kunststof kozijnen, zijn we ook in te huren voor tal van andere '
        'bouwwerkzaamheden. Van nieuwbouw tot aanbouw en renovatie: Aannemersbedrijf '
        'J. Boom staat voor u klaar.',
    ],
    'lead_cta': ('Direct een offerte aanvragen', 'offerte.html'),

    'kies_kop': 'Welke vraag heeft u?',
    'kies_lead': (
        'Drie vragen waarmee mensen bellen, en de werkzaamheden die daarbij horen. '
        'Weet u het niet zeker? Dan komen we er in het orientatiegesprek uit.'),
    # (vraag, welke dienst, bestand)
    'kies': [
        ('&ldquo;Ons huis is te klein geworden.&rdquo;',
         'Ruimte erbij, aan de woning of op het dak.', 'aanbouw-en-uitbouw.html'),
        ('&ldquo;De indeling klopt niet meer.&rdquo;',
         'Dezelfde meters anders gebruiken.', 'verbouw.html'),
        ('&ldquo;De woning is aan een opknapbeurt toe.&rdquo;',
         'Dak, gevel, kozijnen en afwerking.', 'renovatie.html'),
    ],

    'hoofd_kop': 'De drie richtingen waarin de meeste projecten vallen',
    'hoofd_lead': (
        'Onder elke richting hangen de werkzaamheden die daarbij horen. Op elke pagina '
        'staat wat het inhoudt, hoe het traject loopt en wat u van ons krijgt.'),
    'losse_kop': 'Gevel en kozijnen',
    'losse_lead': (
        'Twee werkzaamheden die net zo goed op zichzelf staan, en die vaak meelopen met '
        'een verbouwing of een aanbouw.'),

    'samen_kop': 'De krachten gebundeld',
    'samen': [
        'Om uw bouw- of verbouwproject perfect op te leveren werken wij al jaren samen '
        'met een vast aantal bedrijven. Een goede planning betekent voor ons namelijk '
        'ook een goede samenwerking met andere bedrijven.',
        'Daarom werkt Aannemersbedrijf J. Boom altijd met dezelfde stukadoors, '
        'metselaars en elektriciens. Door deze vertrouwde samenwerking weten we wat we '
        'van elkaar kunnen verwachten en zijn we perfect op elkaar ingespeeld. Het werk '
        'ligt daarom nooit stil, niemand loopt elkaar in de weg en u bent verzekerd van '
        'goed werk.',
    ],
    'samen_lijst_kop': 'De bedrijven die aan uw project bijdragen',

    'slot_kop': 'Meer weten over de mogelijkheden?',
    'slot': (
        'Wilt u meer weten over onze diensten of over de mogelijkheden voor de bouw of '
        'verbouwing van uw woning? Wij beantwoorden al uw vragen graag.'),
}


# ---------------------------------------------------------------------------
#  Dienstpagina's
# ---------------------------------------------------------------------------
# Per dienst: de herschreven lead boven de brontekst, de tussenkop boven het
# uitlegblok, en de knop in het statementblok. De brontekst zelf schuift naar het
# uitlegblok en blijft daar onveranderd staan.
DIENST = {
    'aanbouw-en-uitbouw.html': {
        'lead': [
            'Een fijn huis, maar een te kleine woonkamer of een keuken die geen keuken '
            'meer is. Een aan- of uitbouw lost dat op zonder dat u hoeft te verhuizen.',
            'Wij verzorgen het hele traject: de bouwtekening, de constructieve '
            'uitwerking met ons vaste bureau EWP, de ruwbouw en de afbouw met onze '
            'vaste stukadoors, metselaars en elektriciens.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Uw plannen voor een aanbouw bespreken?',
    },
    'verbouw.html': {
        'lead': [
            'Twee kamers een maken, de keuken openbreken of het plafond verlagen: '
            'verbouwen is dezelfde vierkante meters anders laten werken.',
            'Wij realiseren uw verbouwplannen en houden de partijen op elkaar '
            'afgestemd, zodat het werk niet stilligt en u weet wanneer uw woning weer '
            'van u is.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Uw verbouwing bespreken?',
    },
    'nieuwbouw.html': {
        # De bronzin ("Heeft u er altijd al van gedroomd...") staat hieronder in
        # het uitlegblok. Hij stond hier eerder ook, en dan las de bezoeker hem
        # twee keer op één scherm.
        'lead': [
            'Een kavel, een idee en nog geen tekening. Wij maken de bouwtekening op '
            'basis van uw wensen en bouwen wat erop staat.',
            'Bij nieuwbouw is de afstemming tussen de partijen het grootste deel van '
            'het werk. Wij zijn daarin uw aanspreekpunt, van de fundering tot de '
            'laatste plint.',
        ],
        'cta': ('Bespreek uw nieuwbouwplan', 'contact.html'),
        'slot_kop': 'Een nieuwbouwplan bespreken?',
    },
    'dakopbouw-en-dakkapel.html': {
        'lead': [
            'Een zolder met schuine wanden waar u alleen in het midden kunt staan. Een '
            'dakkapel of dakopbouw maakt daar een kamer van, met stahoogte en daglicht '
            'erbij.',
            'Dakkapellen zijn een van onze specialismen. Het kozijnwerk wordt op maat '
            'voorbereid voordat het dak opengaat, zodat uw woning zo kort mogelijk open '
            'staat.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Een dakkapel of dakopbouw laten plaatsen?',
    },
    'renovatie.html': {
        'lead': [
            'Een dak dat op is, kozijnen die niet meer sluiten, stucwerk dat loslaat. '
            'Renovatie is geen nieuw huis maar hetzelfde huis, weer in orde.',
            'De volgorde is het halve werk: eerst wat de woning droog en heel houdt, '
            'dan de isolatie en de installaties, dan pas de afwerking. Zo doet u niets '
            'twee keer.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Uw woning laten opknappen?',
    },
    'deuren-en-puien.html': {
        'lead': [
            'Een voordeur die klemt, of een achtergevel die open moet naar de tuin. Het '
            'is het onderdeel van de gevel dat u elke dag aanraakt.',
            'Openslaande deuren, een schuifpui of een pui op maat: we adviseren over wat '
            'bij uw gevel past, meten exact in en zetten de pui bouwkundig aan.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Een deur of pui laten plaatsen?',
    },
    'kunststof-kozijnen.html': {
        'lead': [
            'Klaar met schilderen, en klaar met tocht langs de ramen. Kunststof is '
            'onderhoudsarm en isoleert, en het is aan de gevel nauwelijks nog van hout '
            'te onderscheiden.',
            'Wij werken met Select Windows als vaste leverancier en plaatsen de kozijnen '
            'zelf. Dat laatste is geen detail: de aansluiting op het metselwerk bepaalt '
            'of u er tocht voor terugkrijgt.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Kunststof kozijnen of een voorgevel laten plaatsen?',
    },
    'gevelbekleding.html': {
        'lead': [
            'Een verweerde gevel, een dakopbouw die moet aansluiten of isolatie die '
            'erbij moet: bekleding geeft uw woning een nieuw front en een tweede huid '
            'tegelijk.',
            'Het zichtbare deel is de bekleding; het werk zit in het regelwerk, de '
            'geventileerde spouw en de aansluitingen bij kozijnen, hoeken en dakrand.',
        ],
        'cta': ('Vraag een offerte aan', 'offerte.html'),
        'slot_kop': 'Uw gevel laten bekleden?',
    },
    'bouwadvies.html': {
        'lead': [
            'Soms is de eerste vraag niet wat het kost, maar of het mag en of het kan. '
            'Wij zetten uw plan op tekening en zeggen erbij waar het op vastloopt.',
            'Dat kan los van de uitvoering: u kunt vrijblijvend een orientatiegesprek '
            'aanvragen of alleen de tekening laten maken.',
        ],
        'cta': ('Vraag een orientatiegesprek aan', 'contact.html'),
        'slot_kop': 'Uw plannen laten uittekenen?',
    },
}

# Een regel per dienst, voor de kaart, het menu en de voettekst. Kort genoeg om
# op een kaart van een derde pagina op twee regels te passen.
DIENST_KORT = {
    'aanbouw-en-uitbouw.html': 'Extra woonruimte tegen de bestaande woning aan',
    'verbouw.html': 'Dezelfde meters anders indelen, van muurdoorbraak tot schuifpui',
    'nieuwbouw.html': 'Een woning of bijgebouw op maat, van tekening tot oplevering',
    'dakopbouw-en-dakkapel.html': 'Stahoogte en daglicht op de zolder',
    'renovatie.html': 'Dak, gevel en afwerking weer in orde',
    'deuren-en-puien.html': 'Voordeuren, openslaande deuren en schuifpuien',
    'kunststof-kozijnen.html': 'Onderhoudsarm, isolerend en bouwkundig aangezet',
    'gevelbekleding.html': 'Een nieuw front voor uw gevel, met isolatie erachter',
    'bouwadvies.html': 'Bouwtekeningen en advies over wat er kan en mag',
}


def dienst_kort(bestand):
    return DIENST_KORT[bestand]


# De tussenkop boven het blok waar de brontekst van www.jboom.nl in staat.
UITLEG_KOP = {
    'aanbouw-en-uitbouw.html': 'Wat een aan- of uitbouw is, en waar het op vastloopt',
    'verbouw.html': 'Waar het bij een verbouwing op aankomt',
    'nieuwbouw.html': 'Wat er bij nieuwbouw op maat komt kijken',
    'dakopbouw-en-dakkapel.html': 'Dakkapel of dakopbouw: wat is het verschil',
    'renovatie.html': 'Wat renovatie is, en waarom de volgorde ertoe doet',
    'deuren-en-puien.html': 'Wat er te kiezen valt, en wat de keuze bepaalt',
    'kunststof-kozijnen.html': 'Wat kunststof kozijnen doen, en waar u op let',
    'gevelbekleding.html': 'Hoe gevelbekleding is opgebouwd',
    'bouwadvies.html': 'Wat bouwadvies en een bouwtekening inhouden',
}


def dienst(bestand):
    return DIENST[bestand]


# ---------------------------------------------------------------------------
#  Projecten
# ---------------------------------------------------------------------------
PROJECTEN_OVERZICHT = {
    'h1': 'Opgeleverd werk in en om Purmerend',
    'kop': 'Opgeleverde bouwwerken in en rondom Purmerend',
    'lead': (
        'Bent u nog zoekende naar de juiste aannemer voor uw bouwplannen? Of zijn uw '
        'plannen nog niet concreet en wilt u inspiratie opdoen? Bekijk de bouwprojecten '
        'die wij gerealiseerd hebben; zo krijgt u een indruk van de mogelijkheden.'),
    'reeksen_kop': 'Twee reeksen',
    'reeksen_lead': (
        'Het werk valt uiteen in twee series: wat er aan een woning bij komt, en wat er '
        'aan de buitenkant verandert.'),
    'slot_kop': 'Nieuwsgierig hoe wij uw plannen vertalen?',
    'slot': (
        'Neem contact op met Aannemersbedrijf J. Boom. Hoe groot of klein uw project ook '
        'is, wij gaan graag voor u aan de slag.'),
}

PROJECTSERIE = {
    'projecten-aanbouw-opbouw-verbouw.html': {
        'h1': 'Aanbouw, opbouw en verbouw',
        'kop': 'Bouw en verbouwingen uitgevoerd door J. Boom',
        'lead': (
            'Hier vindt u foto&rsquo;s van eerder uitgevoerde projecten. Zo kunt u alvast '
            'inspiratie opdoen of een beeld vormen van de mogelijkheden. Heeft u iets '
            'anders in gedachten dan wat u hier ziet? Neem contact op &mdash; wij staan '
            'open voor ieder bouwproject.'),
        'wat_kop': 'Wat u op deze foto&rsquo;s ziet',
        'wat': [
            'Uitbouwen over de volle breedte van een achtergevel, aanbouwen aan de zijkant, '
            'aangebouwde garages en bergingen, dakopbouwen waarbij er een verdieping bij '
            'kwam, veranda&rsquo;s en overkappingen, en verbouwingen aan de binnenkant.',
            'Het zijn woningen in en rondom Purmerend, van rijtjeswoning tot vrijstaand. '
            'Bij elk project zit hetzelfde werk: een fundering, een opening in de bestaande '
            'gevel, een dak dat waterdicht moet aansluiten en een afwerking die niet mag '
            'laten zien waar het oude ophield.',
        ],
        'galerij_kop': 'De fotoserie',
        'galerij_lead': (
            'De volledige serie zoals die op www.jboom.nl staat. Er staat bewust geen '
            'opdrachtgever, plaats of jaartal bij: die gegevens horen bij een echt project '
            'en die kunnen alleen van J. Boom zelf komen.'),
        'diensten_kop': 'De werkzaamheden achter deze serie',
        'slot_kop': 'Iets anders in gedachten?',
        'slot': (
            'Wij staan open voor ieder bouwproject. Vertel wat u wilt bereiken; in het '
            'orientatiegesprek kijken we wat er kan.'),
    },
    'projecten-dakkapellen-gevels-kozijnen-deuren.html': {
        'h1': 'Dakkapellen, gevels, kozijnen en deuren',
        'kop': 'Realisaties door aannemer J. Boom',
        'lead': (
            'Bent u nieuwsgierig geworden naar onze gerealiseerde projecten? Hoe ziet een '
            'dakkapel, gevel of kozijn dat wij plaatsen eruit? Bekijk hier de '
            'foto&rsquo;s.'),
        'wat_kop': 'Wat u op deze foto&rsquo;s ziet',
        'wat': [
            'Dakkapellen op voor- en achterdakvlakken, in wit en in antraciet, en van '
            'binnenuit gezien zodat u ziet wat het aan ruimte en licht oplevert. Daarnaast '
            'voordeuren, tuindeuren en kozijnen in kunststof, van klassiek met '
            'roedeverdeling tot strak en modern.',
            'Het zijn de twee werkzaamheden die het gezicht van een woning het snelst '
            'veranderen. Wat je op een foto niet ziet is de aansluiting op het metselwerk '
            'en op het dakvlak; dat is precies waar het werk zit.',
        ],
        'galerij_kop': 'De fotoserie',
        'galerij_lead': (
            'De volledige serie zoals die op www.jboom.nl staat. Er staat bewust geen '
            'opdrachtgever, plaats of jaartal bij: die gegevens horen bij een echt project '
            'en die kunnen alleen van J. Boom zelf komen.'),
        'diensten_kop': 'De werkzaamheden achter deze serie',
        'slot_kop': 'Een dakkapel, kozijn of deur laten plaatsen?',
        'slot': (
            'Neem contact op met Aannemersbedrijf J. Boom. Vertel wat u in gedachten heeft; '
            'wij kijken wat er bij uw woning past.'),
    },
}


# ---------------------------------------------------------------------------
#  Bedrijfspagina's
# ---------------------------------------------------------------------------
BEDRIJF = {
    'over-ons.html': {
        # Het jaartal staat in het label boven de kop en in de lead eronder;
        # drie keer in beeld is een keer te veel.
        'h1': 'Een familiebedrijf uit Purmerend',
        'lead': [
            'Aannemersbedrijf J. Boom is een familiebedrijf uit Purmerend. Sinds 1935 '
            'wordt er onder deze naam gebouwd en verbouwd; inmiddels staat de vierde '
            'generatie aan het roer.',
            'Wat het bedrijf typeert is de schaal. Er werken twee mensen: de zwagers '
            'Mario Boom en Martin Babel. Dat is een bewuste keuze geweest, en het is de '
            'reden dat u met dezelfde mensen praat die het werk uitvoeren.',
        ],
        'wie_kop': 'Wie u aan de lijn krijgt',
        'wie_lead': (
            'Bij J. Boom is er geen projectleider tussen u en de bouw. De twee mensen die '
            'het gesprek voeren, zijn ook de twee die op de steiger staan.'),
        'werk_kop': 'Voor wie wij werken',
        'werk': [
            'Wij werken voor particulieren en voor Verenigingen van Eigenaren, '
            'voornamelijk in Purmerend en omstreken. Hoofdzakelijk nemen we opdrachten '
            'van particulieren aan.',
            'Hoe groot of klein uw project ook is: van een voordeur tot een complete '
            'nieuwbouwwoning, wij gaan graag voor u aan de slag.',
        ],
        'samen_kop': 'Nooit alleen op de bouw',
        'samen': [
            'Om een project perfect op te leveren werken wij al jaren samen met een vast '
            'aantal bedrijven. Altijd dezelfde stukadoors, metselaars en elektriciens.',
            'Door die vertrouwde samenwerking weten we wat we van elkaar kunnen '
            'verwachten en zijn we op elkaar ingespeeld. Het werk ligt daardoor nooit '
            'stil en niemand loopt elkaar in de weg.',
        ],
        'slot_kop': 'Kennismaken met Martin en Mario?',
    },
    'historie.html': {
        'h1': 'Van vader op zoon, sinds 1935',
        'lead': [
            'In 1935 begon de grootvader van J. Boom sr. in Purmerend met zijn '
            'aannemersbedrijf. Zijn werkzaamheden bestonden onder andere uit verbouwingen '
            'en renovaties.',
        ],
        'slot_kop': 'Ook uw project door J. Boom laten uitvoeren?',
    },
    'werkwijze.html': {
        'h1': 'Hoe wij werken',
        'lead': [
            'Verbouwen is intensief. Wat het draaglijk maakt, is dat u van tevoren weet '
            'wat er gaat gebeuren en dat de partijen elkaar op de bouw niet in de weg '
            'lopen.',
            'Daarom houden wij van een strakke planning en werken we met een vaste kring '
            'van bedrijven. Hieronder staat hoe een opdracht bij ons verloopt.',
        ],
        'slot_kop': 'Zullen we beginnen met een gesprek?',
    },
    'referenties.html': {
        # Kort genoeg om in de kop van de hero op twee regels te passen; de
        # volledige zin van de bron staat eronder als H2.
        'h1': 'Klanten over aannemer J. Boom',
        'kop': 'Geslaagde verbouwingen in en om Purmerend',
        'lead': [
            'Gaan wij binnenkort ook voor u aan de slag? Al velen gingen u voor. '
            'Natuurlijk kunnen wij zelf vertellen over onze bouwwerken en verbouwingen, '
            'maar onze klanten kunnen dat beter.',
            'Hieronder staan de reacties zoals ze zijn binnengekomen, met de naam en de '
            'maand die de schrijvers er zelf bij zetten.',
        ],
        'slot_kop': 'Schakel Martin en Mario in',
    },
}


# ---------------------------------------------------------------------------
#  Contact en offerte
# ---------------------------------------------------------------------------
CONTACT = {
    'h1': 'Contact met aannemer J. Boom',
    'kop': 'Snelle bouw of verbouwing in en om Purmerend',
    'lead': [
        'Zoek niet verder: u heeft de aannemer voor de bouw of verbouwing van uw droomhuis '
        'gevonden. Hoe groot of klein uw project ook is, wij gaan graag voor u aan de slag.',
        'Wilt u meer weten over onze diensten en de mogelijkheden? Of wilt u direct een '
        f'afspraak maken? Bel {D.TELEFOON_WEERGAVE}, stuur een e-mail of vul het '
        'formulier hieronder in.',
    ],
    'formulier_kop': 'Stel hier uw vraag',
    'formulier_lead': (
        'Vertel kort waar het over gaat. We nemen zo snel mogelijk contact met u op.'),
    'slot_kop': 'Liever meteen bellen?',
}

OFFERTE = {
    'h1': 'Offerte aanvragen',
    'kop': 'Vertel wat u wilt bouwen of verbouwen',
    'lead': [
        'Vraag vrijblijvend een offerte aan, of begin met een orientatiegesprek als uw '
        'plannen nog niet concreet zijn. Beide kan; u zit nergens aan vast.',
        'Hoe concreter uw omschrijving, hoe sneller we u een reeel beeld kunnen geven. '
        'Weet u het nog niet precies? Dan komen we er in het gesprek uit.',
    ],
    'helpt_kop': 'Wat helpt bij uw aanvraag',
    'helpt_lead': (
        'Niet verplicht, wel handig. Heeft u iets niet bij de hand, stuur dan gewoon wat '
        'u wel heeft.'),
    'helpt': [
        ('lijst', 'Wat u wilt bereiken',
         'Liever in functies dan in oplossingen: &lsquo;een werkkamer erbij&rsquo; zegt '
         'ons meer dan &lsquo;een dakkapel van drie meter&rsquo;.'),
        ('huis', 'Om welke woning het gaat',
         'Adres, type woning en bouwjaar. Daarmee weten we al veel over wat er kan.'),
        ('document', 'Tekeningen die er al zijn',
         'Een bouwtekening, de plattegrond uit de verkoopbrochure of een eerdere '
         'vergunning.'),
        ('klok', 'Wanneer het zou moeten',
         'Hangt er een verhuisdatum of een aanvraagmoment aan? Goed om vroeg te weten.'),
    ],
    'daarna_kop': 'Wat er daarna gebeurt',
    'daarna': [
        ('We nemen contact op',
         'Zo snel mogelijk, per telefoon of mail, om te horen wat u precies zoekt.', None),
        ('Orientatiegesprek bij u thuis',
         'We kijken naar de bestaande situatie en naar wat er kan. Vrijblijvend.', None),
        ('Tekening waar die nodig is',
         'Bij een aanbouw, dakopbouw of nieuwbouw maken we de bouwtekening, met een '
         'constructieve berekening van EWP als het plan de draagconstructie raakt.', None),
        ('Offerte',
         'Waarin staat wat er gebeurt en wat erin zit, in dezelfde taal als het gesprek.',
         'U zit nergens aan vast tot u de offerte tekent.'),
    ],
    'slot_kop': 'Liever eerst even bellen?',
}


# ---------------------------------------------------------------------------
#  Vaste teksten
# ---------------------------------------------------------------------------
SLOT_STANDAARD = (
    'Vertel kort wat u wilt bouwen of verbouwen. Wij nemen zo snel mogelijk contact met '
    'u op.')

PARTNERBAND_KOP = 'Met wie wij samenwerken'
