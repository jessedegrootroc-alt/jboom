# -*- coding: utf-8 -*-
"""De verhaallaag onder de dienstpagina's.

DIT IS DE ENIGE TEKST OP DEZE SITE DIE NIET UIT jboom/bron/ KOMT.

www.jboom.nl schrijft per dienst een alinea van drie tot vijf regels. Dat is te
weinig om iemand te helpen kiezen: er staat niet bij wanneer je zoiets nodig
hebt, hoe het traject loopt, wat je zelf moet aanleveren of wat je aan het eind
in handen hebt. Die uitleg staat hieronder.

WAT DE BRON IS
  Algemene vakkennis over bouwen en verbouwen in Nederland, en de regels die
  daarvoor gelden: de Omgevingswet en het Besluit bouwwerken leefomgeving
  (sinds 1 januari 2024), de vergunningcheck via het Omgevingsloket, en het
  gemeentelijk omgevingsplan met de welstandscriteria die gemeenten voor
  dakkapellen hanteren. Dat is uitleg over het vak, niet over J. Boom.

WAT HIER BEWUST NIET IN STAAT
  Geen doorlooptijden, geen prijzen, geen garantietermijnen, geen aantallen,
  geen certificeringen of keurmerken, geen capaciteiten. Alles wat een harde
  toezegging van J. Boom zou zijn, kan alleen van J. Boom zelf komen.

  Waar een termijn onvermijdelijk is om iets uit te leggen, staat er wat er
  wettelijk of gebruikelijk geldt en wie dat bepaalt (de gemeente, de
  leverancier) — nooit wat J. Boom belooft.

  De processtappen zijn per dienst anders. Een dakkapel plaatsen is geen
  nieuwbouwproject, en een kozijn vervangen is geen uitbouw; ze hebben hier dus
  ook niet dezelfde stappen gekregen.

WAT ER WEL UIT DE BRON KOMT, EN HIER ALLEEN ANDERS STAAT GEFORMULEERD
  Dat J. Boom bouwtekeningen verzorgt en het project coordineert, dat er met
  vaste partners wordt gewerkt, dat er vrijblijvend een orientatiegesprek of
  offerte kan worden aangevraagd, en dat er voor particulieren en VvE's wordt
  gewerkt. Dat staat allemaal op www.jboom.nl.
"""

# De iconen die de panelen gebruiken; de tekeningen staan in bouw_jboom_dienst.py.
# vinkje schild lijst trap klok mensen grafiek document huis liniaal zon blad

VERHAAL = {}


# ---------------------------------------------------------------------------
#  Aanbouw en uitbouw
# ---------------------------------------------------------------------------
VERHAAL['aanbouw-en-uitbouw.html'] = {
    'wanneer_kop': 'Wanneer een aanbouw de kortste route naar meer ruimte is',
    'wanneer_intro': (
        'Verhuizen is duur, en niet iedereen wil weg uit zijn straat. Een aanbouw '
        'lost het ruimteprobleem op de plek zelf op. Deze drie situaties komen het '
        'vaakst voor.'),
    'situaties': [
        ('De keuken en de woonkamer vechten om dezelfde meters',
         'De eettafel staat in de looproute en de keuken is een gang geworden. Een '
         'uitbouw over de volle breedte van de achtergevel geeft de keuken zijn '
         'eigen plek en maakt de woonkamer weer een woonkamer.'),
        ('Het gezin is gegroeid, het huis niet',
         'Er is een werkplek, een logeerkamer of een speelkamer bij nodig. Aan de '
         'begane grond aanbouwen is vaak eenvoudiger dan de zolder verbouwen, omdat '
         'de fundering en de gevel het werk doen in plaats van de bestaande '
         'draagconstructie.'),
        ('De tuin is groot genoeg, de woning te ondiep',
         'Bij een diepe achtertuin blijft er na een uitbouw van twee of drie meter '
         'nog ruim tuin over. Wat er precies mag hangt af van het achtererfgebied en '
         'van het omgevingsplan van uw gemeente.'),
    ],
    'uitleg_kop': 'Wat een aan- of uitbouw is, en waar het op vastloopt',
    'uitleg_extra': [
        'Een aanbouw is een bouwwerk dat tegen de bestaande woning aan komt en er '
        'constructief mee samenwerkt: de bestaande gevel wordt deels of helemaal '
        'weggehaald en er komt een nieuwe ruimte tegenaan. Een uitbouw is hetzelfde '
        'principe, meestal ondieper en over de volle breedte van de achtergevel.',
        'Drie dingen bepalen of een plan werkt. Ten eerste de fundering: een aanbouw '
        'weegt en moet zijn eigen gewicht kwijt in de grond, dus komt er een eigen '
        'fundering onder. Ten tweede de opening in de bestaande gevel: zodra er een '
        'dragende muur weggaat, moet de belasting daarboven door een stalen ligger '
        'worden overgenomen, en daar hoort een constructieve berekening bij. Ten '
        'derde de aansluiting op wat er al staat &mdash; het dak, de dakgoot, de '
        'riolering en de isolatie moeten op elkaar aansluiten, anders lekt of tocht '
        'het precies op de naad.',
        'Voor de vergunning geldt sinds 1 januari 2024 de Omgevingswet. Een '
        'bijbehorend bouwwerk in het achtererfgebied is onder voorwaarden '
        'vergunningvrij; of dat voor uw situatie geldt, hangt af van de diepte, de '
        'hoogte, de perceelgrens en van het omgevingsplan van uw gemeente. De '
        'vergunningcheck van het Omgevingsloket geeft daar uitsluitsel over.',
    ],
    'stappen_kop': 'Van eerste schets naar sleutelklare uitbouw',
    'stappen_intro': (
        'Een aanbouw raakt de fundering, de gevel en het dak van uw woning. Daarom '
        'begint het met opnemen wat er staat, en niet met tekenen wat er zou kunnen '
        'staan.'),
    'stappen': [
        ('Orientatiegesprek bij u thuis',
         'We kijken naar de bestaande situatie: waar staat de dragende muur, hoe '
         'ligt de tuin, waar zitten de meterkast, de riolering en de cv. Uw wensen '
         'gaan in dezelfde ronde mee.',
         'Vrijblijvend, en aan te vragen via het contactformulier of per telefoon.'),
        ('Bouwtekening en constructieve uitwerking',
         'Op basis van het gesprek maken wij de bouwtekening. Gaat er een dragende '
         'muur open, dan komt er een constructieve berekening bij; die maken we met '
         'EWP, ons vaste bureau voor ontwerp, constructie en bouwadvies.',
         None),
        ('Offerte en vergunning',
         'U krijgt een offerte waarin staat wat er wordt gebouwd en wat erbij '
         'inbegrepen is. Is er een omgevingsvergunning nodig, dan hoort de tekening '
         'die u van ons krijgt bij de aanvraag.',
         'De gemeente beslist over de vergunning, niet de aannemer. De '
         'behandeltermijn staat in de ontvangstbevestiging van uw aanvraag.'),
        ('Fundering en ruwbouw',
         'Grondwerk, fundering, metselwerk en de dakconstructie. Bij heiwerk halen '
         'we Smit Heiwerken erbij. De opening in de bestaande gevel gaat pas open '
         'als de nieuwe constructie de belasting kan overnemen.',
         None),
        ('Kozijnen, dak en dichtzetten',
         'Het kozijnwerk gaat erin, het dak wordt waterdicht en de aansluiting op de '
         'bestaande dakgoot en riolering wordt gemaakt. Vanaf dit punt staat uw huis '
         'weer dicht.',
         None),
        ('Afbouw en oplevering',
         'Stucwerk, elektra en loodgieterswerk lopen via de vaste partners waarmee '
         'we al jaren samenwerken. We lopen het werk met u na en nemen de punten mee '
         'die u nog ziet.',
         'Aan het eind van elke werkdag wordt er opgeruimd; dat is hoe we werken en '
         'wat klanten er zelf over schrijven.'),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Hoe scherper dit aan het begin ligt, hoe minder er tijdens de bouw nog '
        'gewijzigd hoeft te worden. Heeft u iets niet, dan komen we er samen uit.'),
    'input': [
        ('liniaal', 'De maten van uw woning',
         'Een bestaande bouwtekening, de plattegrond uit de verkoopbrochure of het '
         'bouwdossier van uw gemeente. Is er niets, dan meten wij zelf in.'),
        ('lijst', 'Waar de uitbouw voor is',
         'Keuken, werkkamer, speelkamer of gewoon meer woonkamer. Dat bepaalt de '
         'daglichtopening, de aansluitingen en de indeling.'),
        ('huis', 'Kadastrale gegevens bij twijfel',
         'Bij bouwen tegen de erfgrens of bij een VvE is duidelijk moeten zijn waar '
         'de grens ligt en wie waarover beslist.'),
        ('document', 'Wat er al vastligt',
         'Een eerdere tekening van een architect, een vergunning die al is verleend, '
         'of afspraken met de VvE of de buren.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('document', 'Een bouwtekening',
         'De tekening van de nieuwe situatie, bruikbaar voor de vergunningaanvraag '
         'als die nodig is.'),
        ('vinkje', 'Een offerte die klopt met de tekening',
         'Wat er gebouwd wordt en wat er in zit, in dezelfde taal als het gesprek dat '
         'we hadden.'),
        ('mensen', 'Een aanbouw die af is',
         'Ruwbouw, dak, kozijnen en afbouw, met de vaste stukadoors, metselaars en '
         'elektriciens waarmee we werken.'),
        ('schild', 'Een aansluiting die dicht is',
         'Dak, goot, riolering en isolatie sluiten aan op wat er al stond. Daar gaat '
         'het bij een uitbouw meestal mis.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Heb ik een vergunning nodig voor een uitbouw?',
         'Dat hangt af van de maten en van waar de uitbouw komt. Een bijbehorend '
         'bouwwerk in het achtererfgebied is onder de Omgevingswet in veel gevallen '
         'vergunningvrij, maar de diepte, de hoogte en de afstand tot de perceelgrens '
         'bepalen het, net als het omgevingsplan van uw gemeente. De vergunningcheck '
         'van het Omgevingsloket geeft uitsluitsel; wij maken de tekening die u bij '
         'een aanvraag nodig heeft.'),
        ('Wat is het verschil tussen een aanbouw en een uitbouw?',
         'In de praktijk lopen de woorden door elkaar. Een uitbouw is meestal een '
         'uitbreiding van een bestaande ruimte over de volle breedte van de gevel; een '
         'aanbouw is een aparte ruimte die tegen de woning aan wordt gezet, zoals een '
         'bijkeuken, een garage of een berging. Constructief is de aanpak dezelfde.'),
        ('Kan de dragende muur eruit?',
         'Bijna altijd, maar niet zomaar. De belasting die die muur draagt moet worden '
         'overgenomen, meestal door een stalen ligger op nieuwe steunpunten. Dat is '
         'geen inschatting maar een berekening, en die laten we maken voordat er iets '
         'opengaat.'),
        ('Kan ik in het huis blijven wonen tijdens de bouw?',
         'Meestal wel. De bestaande gevel gaat pas open als de nieuwe constructie zover '
         'is, zodat het huis zo kort mogelijk open staat. Er is overlast &mdash; er '
         'wordt verbouwd &mdash; maar er wordt dagelijks opgeruimd.'),
        ('Werken jullie ook voor Verenigingen van Eigenaren?',
         'Ja. Naast particulieren werken we voor VvE&rsquo;s. Bij een VvE ligt de '
         'besluitvorming anders: er is toestemming van de vergadering nodig en er zijn '
         'afspraken over wat gemeenschappelijk is en wat privé. Dat regelen we in het '
         'traject mee.'),
    ],
}


# ---------------------------------------------------------------------------
#  Verbouw
# ---------------------------------------------------------------------------
VERHAAL['verbouw.html'] = {
    'wanneer_kop': 'Wanneer verbouwen meer oplevert dan verhuizen',
    'wanneer_intro': (
        'Een verbouwing gaat zelden over de hele woning. Het gaat over die ene ruimte '
        'die niet werkt. Dit zijn de drie vragen waarmee mensen bellen.'),
    'situaties': [
        ('Twee kamers moeten er een worden',
         'De muur tussen de woonkamer en de achterkamer eruit, of de keuken open naar '
         'de eetkamer. Zodra die muur draagt, komt er een ligger voor in de plaats en '
         'hoort daar een berekening bij.'),
        ('De indeling klopt niet meer met hoe u woont',
         'Een slaapkamer erbij, een badkamer op de verdieping, het plafond verlaagd of '
         'een open haard erin. Verbouwen betekent hier: dezelfde vierkante meters '
         'anders indelen.'),
        ('Er komt licht en ruimte tekort',
         'Een grotere raampartij, een schuifpui naar de tuin of een vide. Dat raakt de '
         'gevel en dus de constructie, en vaak ook de isolatie en de ventilatie.'),
    ],
    'uitleg_kop': 'Waar het bij een verbouwing op aankomt',
    'uitleg_extra': [
        'Bij een verbouwing werkt u in een huis dat al staat. Dat is het verschil met '
        'nieuwbouw: de volgorde van het werk wordt niet bepaald door wat handig is, '
        'maar door wat er kan blijven staan terwijl er iets anders weggaat.',
        'Het eerste dat vastgesteld moet worden is welke muren dragen. In een '
        'doorsneewoning zijn dat de bouwmuren tussen de woningen en soms een muur '
        'middenin; in een oudere woning kan een balklaag ergens anders op steunen dan '
        'u verwacht. Gaat er een dragende muur weg, dan neemt een stalen ligger het '
        'over, en die ligger moet zijn belasting kwijt op steunpunten die het aankunnen '
        '&mdash; tot in de fundering aan toe.',
        'Daarnaast bepaalt de leeftijd van de woning wat er komt kijken. In woningen '
        'van voor 1994 kan asbest zitten, en dan hoort er voor de sloop een '
        'asbestinventarisatie te liggen. Verandert u een ruimte in een verblijfsruimte, '
        'dan gelden er eisen aan daglicht en ventilatie uit het Besluit bouwwerken '
        'leefomgeving. Dat zijn geen formaliteiten: het is precies wat een verbouwing '
        'later comfortabel of vochtig maakt.',
    ],
    'stappen_kop': 'Hoe een verbouwing bij ons loopt',
    'stappen_intro': (
        'Verbouwen is intensief. Wat het draaglijk maakt is een planning waarin de '
        'partijen elkaar niet in de weg lopen &mdash; en dat is precies waarvoor we met '
        'vaste bedrijven werken.'),
    'stappen': [
        ('Opname van de bestaande situatie',
         'Welke muren dragen, waar de leidingen lopen, wat de balklaag doet en wat de '
         'staat van het bestaande werk is. Pas daarna weten we wat er kan.',
         None),
        ('Plan, tekening en waar nodig een berekening',
         'We tekenen de nieuwe indeling. Gaat er een dragende muur open, dan komt de '
         'constructieve berekening van EWP erbij.',
         None),
        ('Offerte en planning',
         'In de offerte staat wat er gebeurt en wat erin zit. In de planning staat wie '
         'wanneer komt: de stukadoor, de metselaar, de elektricien en de loodgieter '
         'zijn vaste partijen, dus die planning houdt stand.',
         'Dat is waarom we met dezelfde bedrijven blijven werken: het werk ligt niet '
         'stil en niemand loopt elkaar in de weg.'),
        ('Sloop en constructief werk',
         'Wat eruit moet gaat eruit, met de tijdelijke ondersteuning die daarbij hoort. '
         'De ligger gaat erin voordat de muur eronder verdwijnt.',
         None),
        ('Afbouw',
         'Stucwerk, elektra, loodgieterswerk en timmerwerk, in de volgorde waarin ze '
         'elkaar niet in de weg zitten.',
         None),
        ('Nalopen en opleveren',
         'We lopen het werk met u na. Wat u ziet, nemen we mee.',
         'Ook na de oplevering zijn we bereikbaar voor vragen over het werk dat we '
         'gedaan hebben.'),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Bij een verbouwing zitten de verrassingen in wat er achter de muren zit. Alles '
        'wat u daarover heeft, helpt.'),
    'input': [
        ('document', 'Tekeningen van de woning',
         'Een bouwtekening, de plattegrond of het bouwdossier van de gemeente. Ook een '
         'oude tekening van een eerdere verbouwing is nuttig.'),
        ('lijst', 'Een wensenlijst',
         'Wat er weg moet, wat erbij komt en wat er beslist moet blijven. Ook wat u '
         'twijfelt: daar denken we in het gesprek over mee.'),
        ('schild', 'Wat u weet over het bouwjaar',
         'Bij woningen van voor 1994 is asbest een reeel aandachtspunt bij sloopwerk. '
         'Weet u het bouwjaar, dan weten we waar we op moeten letten.'),
        ('mensen', 'Wie er meebeslist',
         'Bij een VvE of bij gedeelde muren met de buren is het handig om vroeg te '
         'weten wie er akkoord moet geven.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('document', 'Een tekening van de nieuwe situatie',
         'Zodat duidelijk is wat er komt te staan, en zodat een berekening en een '
         'vergunningaanvraag daarop kunnen aansluiten.'),
        ('trap', 'Een planning met vaste partijen',
         'Wie wanneer komt. De stukadoors, metselaars en elektriciens zijn dezelfde '
         'mensen als vorige keer.'),
        ('vinkje', 'Een verbouwing die af is',
         'Van sloopwerk tot afwerking, in een woning waarin dagelijks wordt '
         'opgeruimd.'),
        ('mensen', 'Een aanspreekpunt',
         'Martin en Mario zijn de mensen die het gesprek voerden en ook de mensen die '
         'op de bouw staan.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Mag ik zomaar een muur doorbreken?',
         'Een niet-dragende scheidingswand kan meestal zonder meer weg. Draagt de muur, '
         'dan moet de belasting worden overgenomen en hoort daar een constructieve '
         'berekening bij. Ook de vraag of er een vergunning nodig is hangt daarvan af: '
         'constructieve wijzigingen zijn niet zonder meer vergunningvrij.'),
        ('Hoe weet ik of een muur draagt?',
         'Niet aan de dikte alleen. Het gaat om wat erop rust: de balklaag van de '
         'verdieping, de kap, of een muur die daarboven doorloopt. Dat stellen we bij '
         'de opname vast, en bij twijfel laten we het narekenen in plaats van het te '
         'schatten.'),
        ('Kan ik tijdens de verbouwing thuis blijven?',
         'Vaak wel, maar het hangt af van wat er gebeurt. Bij werk aan de keuken of de '
         'badkamer is een deel van de woning tijdelijk niet te gebruiken. Wat er wel en '
         'niet kan tijdens het werk, bespreken we vooraf zodat u het kunt inplannen.'),
        ('Regelen jullie ook de stukadoor en de elektricien?',
         'Ja. We werken al jaren met dezelfde stukadoors, metselaars en elektriciens, '
         'en met vaste partners voor loodgieterswerk, elektrotechniek en stuc- en '
         'spuitwerk. Dat coordineren wij; u heeft er een aanspreekpunt voor.'),
        ('Kunnen er tijdens de verbouwing nog dingen bij?',
         'Dat gebeurt bijna altijd &mdash; tijdens het werk zie je pas wat er kan. Als '
         'het inpasbaar is, bespreken we wat het betekent voor het werk en de planning '
         'voordat we het doen.'),
    ],
}


# ---------------------------------------------------------------------------
#  Nieuwbouw
# ---------------------------------------------------------------------------
VERHAAL['nieuwbouw.html'] = {
    'wanneer_kop': 'Wanneer u met een nieuwbouwplan bij een aannemer aanklopt',
    'wanneer_intro': (
        'Nieuwbouw op maat begint bijna nooit bij een compleet plan. Het begint bij een '
        'kavel, een idee of een bijgebouw dat er moet komen.'),
    'situaties': [
        ('U heeft een kavel en een idee',
         'Er is grond en er is een beeld van hoe het moet worden, maar nog geen '
         'tekening. Wij maken de bouwtekening op basis van uw wensen en coordineren het '
         'project daarna van de eerste tekening tot de finishing touch.'),
        ('Er moet een bijgebouw komen',
         'Een garage, een berging, een schuur of een tuinhuis dat meer moet zijn dan een '
         'bouwpakket. Constructief is dat nieuwbouw: eigen fundering, eigen '
         'draagconstructie, eigen dak.'),
        ('Het huis moet plat en opnieuw',
         'Bij vervangende nieuwbouw is het bestaande pand het uitgangspunt niet meer, '
         'maar de kavel, de aansluitingen en het omgevingsplan wel.'),
    ],
    'uitleg_kop': 'Wat er bij nieuwbouw op maat komt kijken',
    'uitleg_extra': [
        'Bij nieuwbouw ligt niets vast behalve de kavel en de regels. Dat is de vrijheid '
        'ervan en meteen het lastige: elke keuze &mdash; de plattegrond, de goothoogte, '
        'de gevel, de indeling &mdash; heeft gevolgen voor de rest.',
        'Het traject valt uiteen in drie sporen die naast elkaar lopen. Het ontwerp: wat '
        'wordt het en hoe ziet het eruit. Het constructieve spoor: hoe staat het '
        'overeind, wat draagt wat, en wat betekent de bodem voor de fundering &mdash; op '
        'slappe grond, zoals in grote delen van Noord-Holland, wordt er geheid. En het '
        'vergunningenspoor: past het plan binnen het omgevingsplan van de gemeente en '
        'binnen de eisen uit het Besluit bouwwerken leefomgeving.',
        'Voor nieuwbouw gelden die eisen onverkort: isolatie, luchtdichtheid, '
        'ventilatie, daglicht, brandveiligheid en energieprestatie. Anders dan bij een '
        'verbouwing kunt u er niet omheen met een verwijzing naar de bestaande situatie, '
        'want die is er niet. Dat is geen bezwaar maar een gegeven, en het is de reden '
        'dat de tekening en de berekening voor de eerste paal al kloppen moeten.',
    ],
    'stappen_kop': 'Van kavel naar sleutel',
    'stappen_intro': (
        'Bij nieuwbouw is de coordinatie het werk. Wij zijn het aanspreekpunt en houden '
        'de partijen op elkaar afgestemd, indien gewenst van de eerste tekening tot de '
        'finishing touch.'),
    'stappen': [
        ('Gesprek over het plan',
         'Wat wilt u bouwen, waar, en wat ligt er al vast? De kavel, het omgevingsplan '
         'en uw programma van eisen bepalen samen de ruimte waarin we werken.',
         None),
        ('Bouwtekening',
         'Wij maken de bouwtekening op basis van uw wensen. Dat is de tekening waarmee '
         'de rest van het traject werkt: de constructeur, de vergunningaanvraag en de '
         'uitvoering.',
         None),
        ('Constructie en fundering',
         'De draagconstructie en het funderingsplan komen van EWP, ons vaste bureau voor '
         'ontwerp, constructie en bouwadvies. Moet er geheid worden, dan doet Smit '
         'Heiwerken dat.',
         'Wat de bodem aankan bepaalt de fundering. Dat is een berekening, geen '
         'aanname.'),
        ('Vergunning',
         'Met tekening en berekening kan de omgevingsvergunning worden aangevraagd. De '
         'gemeente toetst aan het omgevingsplan en aan de bouwtechnische eisen.',
         'De gemeente bepaalt de doorlooptijd van de aanvraag; die staat in de '
         'ontvangstbevestiging.'),
        ('Bouwen',
         'Grondwerk, fundering, ruwbouw, dak, kozijnen en dichtzetten. Wij coordineren '
         'het geheel en de vaste partners doen hun deel.',
         None),
        ('Afbouw en oplevering',
         'Installaties, stucwerk, timmerwerk en afwerking, tot en met de finishing '
         'touch als u dat wilt. We lopen het werk met u na voordat we het overdragen.',
         None),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Bij nieuwbouw is de start bepalend. Hoe completer het beeld aan het begin, hoe '
        'minder er onderweg opnieuw getekend hoeft te worden.'),
    'input': [
        ('huis', 'De kavelgegevens',
         'Waar de grond ligt, hoe groot hij is en wat het omgevingsplan er toestaat. '
         'Kadastrale gegevens en een situatietekening als u die heeft.'),
        ('lijst', 'Een programma van eisen',
         'Hoeveel ruimtes, welke functies, hoeveel verdiepingen, en waar u beslist niet '
         'van af wilt wijken.'),
        ('document', 'Wat er al getekend is',
         'Een schetsontwerp van een architect, een eerdere aanvraag of vooroverleg met '
         'de gemeente.'),
        ('blad', 'Uw uitgangspunten',
         'Wat u belangrijk vindt aan materiaal, isolatie en onderhoud. Dat bepaalt meer '
         'keuzes dan mensen vooraf denken.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('document', 'Een bouwtekening op maat',
         'Gemaakt op basis van uw wensen, en bruikbaar voor de vergunningaanvraag.'),
        ('grafiek', 'Constructie en fundering doorgerekend',
         'Via EWP, met heiwerk door Smit Heiwerken waar de bodem daarom vraagt.'),
        ('mensen', 'Een gecoordineerd project',
         'Wij zijn het aanspreekpunt en stemmen de partijen op elkaar af, indien gewenst '
         'van de eerste tekening tot de finishing touch.'),
        ('vinkje', 'Een woning die af is',
         'Ruwbouw, dak, kozijnen, installaties en afwerking, opgeleverd na een ronde '
         'langs het werk met u erbij.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Maken jullie ook de bouwtekening, of moet ik een architect hebben?',
         'Wij maken de bouwtekening op basis van uw wensen. Heeft u al een architect, '
         'dan werken we met zijn ontwerp verder. Voor de constructie werken we samen met '
         'EWP, ons vaste bureau voor ontwerp, constructie en bouwadvies.'),
        ('Coordineren jullie het hele project?',
         'Ja, indien gewenst van de eerste tekening tot de finishing touch. Dat is ook '
         'waarom we met een vaste kring van bedrijven werken: bij een nieuwbouwproject '
         'is de afstemming tussen partijen het grootste deel van het werk.'),
        ('Moet er geheid worden?',
         'Dat hangt van de bodem af. In grote delen van Noord-Holland is de grond slap en '
         'wordt er geheid; wat er nodig is volgt uit het funderingsadvies en niet uit een '
         'vuistregel. Heiwerk doen we met Smit Heiwerken.'),
        ('Is er altijd een vergunning nodig voor nieuwbouw?',
         'Voor een nieuw hoofdgebouw vrijwel altijd. Voor een bijgebouw op eigen erf kan '
         'het anders liggen: onder de Omgevingswet is een bijbehorend bouwwerk in het '
         'achtererfgebied onder voorwaarden vergunningvrij. De vergunningcheck van het '
         'Omgevingsloket geeft uitsluitsel voor uw situatie.'),
        ('Bouwen jullie ook alleen de ruwbouw?',
         'Dat kan. In de offerte staat waar ons werk begint en waar het ophoudt; wilt u '
         'zelf afbouwen, dan stemmen we daarop af.'),
    ],
}


# ---------------------------------------------------------------------------
#  Dakopbouw en dakkapel
# ---------------------------------------------------------------------------
VERHAAL['dakopbouw-en-dakkapel.html'] = {
    'wanneer_kop': 'Wanneer de zolder een kamer moet worden',
    'wanneer_intro': (
        'Een dakkapel en een dakopbouw lossen hetzelfde probleem op &mdash; te weinig '
        'staande hoogte en te weinig licht &mdash; maar op een andere schaal.'),
    'situaties': [
        ('De zolder heeft schuine wanden en te weinig hoogte',
         'U kunt er alleen middenin staan. Een dakkapel geeft over de breedte ervan '
         'volledige stahoogte en maakt de ruimte bruikbaar in plaats van bergruimte.'),
        ('Er is een slaapkamer of werkkamer bij nodig',
         'Wordt de zolder een verblijfsruimte, dan gelden er eisen aan daglicht en '
         'ventilatie. Een dakkapel levert allebei tegelijk.'),
        ('De hele verdieping moet erbij',
         'Bij een dakopbouw gaat het dak eraf of omhoog en komt er een volwaardige '
         'verdieping. Dat is een grotere ingreep, met gevolgen voor de constructie en '
         'meestal voor de vergunning.'),
    ],
    'uitleg_kop': 'Dakkapel of dakopbouw: wat is het verschil',
    'uitleg_extra': [
        'Een dakkapel is een uitbouw in het bestaande dakvlak. Het dak blijft liggen; er '
        'wordt een gat in gemaakt en de dakkapel wordt op de bestaande dakconstructie '
        'gezet. Daar hoort een raveling bij: de doorgezaagde sporen worden opgevangen '
        'door balken die de belasting naar weerskanten verdelen.',
        'Een dakopbouw is ingrijpender. Daar wordt het dakvlak opgetrokken of vervangen, '
        'zodat er een hele verdieping bij komt. Dat raakt de draagconstructie van de hele '
        'woning: het extra gewicht moet uiteindelijk in de fundering terechtkomen, en dat '
        'is een constructieve vraag en geen timmervraag.',
        'Voor de vergunning is het onderscheid groot. Een dakkapel op het achterdakvlak '
        'is onder de Omgevingswet in veel gevallen vergunningvrij, mits hij aan '
        'maatvoorwaarden voldoet: onder andere een plat dak, voldoende afstand tot de '
        'dakrand en de nok, en een dakkapel die niet boven het dak uitkomt. Aan de '
        'voorkant of aan de straatzijde ligt dat anders, en veel gemeenten hebben '
        'daarvoor sneltoetscriteria in hun omgevingsplan. Een dakopbouw is vrijwel altijd '
        'vergunningplichtig. De vergunningcheck van het Omgevingsloket is het startpunt.',
    ],
    'stappen_kop': 'Hoe een dakkapel of dakopbouw tot stand komt',
    'stappen_intro': (
        'Een dakkapel is werk waarbij het huis een dag of wat open is. Daarom staat of '
        'valt het met voorbereiding: als alles klaarligt, is het snel dicht.'),
    'stappen': [
        ('Opname op zolder en op het dak',
         'De sporenafstand, de staat van het dakbeschot, de isolatie en de plek waar de '
         'dakkapel kan komen. Bij een dakopbouw kijken we bovendien naar wat de '
         'draagconstructie eronder aankan.',
         None),
        ('Tekening en vergunningcheck',
         'We tekenen de dakkapel of de opbouw in en kijken wat er in uw gemeente geldt. '
         'Bij een dakopbouw hoort er een constructieve berekening bij; die maakt EWP.',
         'Aan de achterkant is een dakkapel vaak vergunningvrij; aan de voorkant '
         'meestal niet. Dat verschilt per gemeente.'),
        ('Offerte en maatvoering',
         'In de offerte staat de uitvoering: de maten, het materiaal van het kozijnwerk, '
         'de afwerking van de zijwangen en de beglazing.',
         None),
        ('Voorbereiding en prefab',
         'Het kozijnwerk en de elementen worden op maat gemaakt voordat het dak opengaat. '
         'Dat is precies waarom een dakkapel in korte tijd kan staan.',
         None),
        ('Plaatsen',
         'Het dakvlak gaat open, de raveling wordt aangebracht en de dakkapel wordt '
         'geplaatst, gestort of gemonteerd en waterdicht gemaakt.',
         'Van buiten dicht voordat de dag om is: dat is de opzet, en daar is de '
         'voorbereiding op ingericht.'),
        ('Afwerken van binnen',
         'Isolatie, betimmering, stucwerk en de aansluiting op de bestaande wanden en '
         'het plafond. Elektra loopt via De Heer Elektrotechniek.',
         None),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Bij een dakkapel zit het werk in de maatvoering. Wat u hierover kunt aanleveren, '
        'scheelt in de voorbereiding.'),
    'input': [
        ('liniaal', 'De maten van het dakvlak',
         'Breedte, hellingshoek en de hoogte van goot tot nok. Zo niet, dan meten wij in '
         'bij de opname.'),
        ('huis', 'Wat er bij de buren staat',
         'Bij rijtjeswoningen bepaalt het beeld van de straat vaak wat de gemeente '
         'toestaat. Een foto van de rij helpt.'),
        ('lijst', 'Waar de zolder voor wordt gebruikt',
         'Slaapkamer, werkkamer of bergruimte. Dat bepaalt de eisen aan daglicht, '
         'ventilatie en isolatie.'),
        ('document', 'Wat uw gemeente vraagt',
         'Sneltoetscriteria of eerdere correspondentie over een dakkapel in uw straat, '
         'als u die heeft.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('document', 'Een tekening en duidelijkheid over de vergunning',
         'Wat er komt, in welke maten, en of er een aanvraag nodig is.'),
        ('zon', 'Stahoogte en daglicht',
         'Over de volle breedte van de dakkapel bruikbare ruimte, met licht en '
         'ventilatie erbij.'),
        ('schild', 'Een dak dat dicht is',
         'Raveling, isolatie, waterdichte aansluitingen en een nette afwerking van de '
         'zijwangen.'),
        ('vinkje', 'Binnen afgewerkt',
         'Betimmering, stucwerk en elektra, aangesloten op wat er al was.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Heb ik een vergunning nodig voor een dakkapel?',
         'Op het achterdakvlak vaak niet, mits de dakkapel aan de maatvoorwaarden uit het '
         'Besluit bouwwerken leefomgeving voldoet: onder meer een plat dak, voldoende '
         'afstand tot de dakranden en de nok, en niet boven het dak uitkomen. Aan de '
         'voorkant of aan een zijkant die naar openbaar gebied is gekeerd, geldt dat '
         'niet en toetst de gemeente aan haar omgevingsplan. De vergunningcheck van het '
         'Omgevingsloket geeft uitsluitsel.'),
        ('Hoe lang staat mijn dak open?',
         'Zo kort mogelijk. Het kozijnwerk en de elementen worden vooraf op maat '
         'gemaakt, zodat het plaatsen zelf snel gaat en het dak van buiten weer dicht is '
         'zodra de dakkapel staat. Hoeveel dagen het hele werk kost hangt af van de maat '
         'en de afwerking; dat staat in de offerte.'),
        ('Wat is het verschil in impact tussen een dakkapel en een dakopbouw?',
         'Een dakkapel zit in het bestaande dakvlak en laat de draagconstructie verder '
         'met rust. Bij een dakopbouw komt er een verdieping bij en moet het extra '
         'gewicht via de bestaande constructie in de fundering terechtkomen. Dat vraagt '
         'een berekening en vrijwel altijd een vergunning.'),
        ('Kan er een dakkapel op elk dak?',
         'Niet op elk dak even eenvoudig. De hellingshoek, de hoogte van goot tot nok en '
         'de staat van de kap bepalen wat er kan. Bij een te flauwe helling of te weinig '
         'hoogte levert een dakkapel weinig stahoogte op en is een opbouw de betere '
         'oplossing. Dat stellen we bij de opname vast.'),
        ('Moet de zolder aan eisen voldoen als er een slaapkamer komt?',
         'Ja. Het Besluit bouwwerken leefomgeving stelt eisen aan een ruimte waarin '
         'geslapen of gewerkt wordt, onder meer aan de vluchtmogelijkheid en aan de '
         'plafondhoogte. Wat er in uw situatie nodig is, stellen we bij de opname vast; '
         'soms is het een extra voorziening, soms is het al in orde.'),
    ],
}


# ---------------------------------------------------------------------------
#  Renovatie
# ---------------------------------------------------------------------------
VERHAAL['renovatie.html'] = {
    'wanneer_kop': 'Wanneer een woning aan een opknapbeurt toe is',
    'wanneer_intro': (
        'Renovatie gaat niet over anders wonen maar over beter wonen in hetzelfde huis. '
        'Meestal begint het bij een onderdeel dat op is.'),
    'situaties': [
        ('Het dak is aan vervanging toe',
         'Losse of gebroken pannen, een versleten dakbedekking op een plat dak, of een '
         'dakbeschot dat aan het eind van zijn leven is. Een dak dat lekt beschadigt '
         'alles eronder.'),
        ('De afwerking is versleten',
         'Stucwerk dat loslaat, plafonds die scheuren, kozijnen die niet meer sluiten. '
         'Op zichzelf klein werk, maar het bepaalt hoe de hele woning aanvoelt.'),
        ('U heeft een woning gekocht die eerst aangepakt moet worden',
         'Bij een oudere woning is de volgorde belangrijk: eerst wat waterdicht en '
         'constructief in orde moet zijn, dan pas de afwerking.'),
    ],
    'uitleg_kop': 'Wat renovatie is, en waarom de volgorde ertoe doet',
    'uitleg_extra': [
        'Bij renovatie vervangt of herstelt u wat er is, zonder de indeling wezenlijk te '
        'veranderen. Dat maakt het minder ingrijpend dan een verbouwing, maar niet '
        'eenvoudiger: u werkt aan onderdelen die al jaren met elkaar samenwerken, en wat '
        'u vervangt moet op de rest aansluiten.',
        'De volgorde is bijna altijd dezelfde. Eerst wat het huis droog en heel houdt: '
        'dak, goten, gevel en kozijnen. Dan wat eronder zit: isolatie, leidingen, '
        'elektra. Pas daarna de afwerking, want stucwerk dat na een lekkage is '
        'aangebracht mag u overdoen.',
        'Renovatie is ook het natuurlijke moment om te isoleren. Als het dak er toch af '
        'gaat, is isoleren aan de buitenkant een kleine stap extra; als het achteraf moet '
        'gebeuren, is het een apart project. Voor verbouw geldt daarbij dat u niet onder '
        'het bestaande niveau mag uitkomen, en dat het Besluit bouwwerken leefomgeving '
        'minimumeisen stelt zodra u een constructieonderdeel vervangt.',
    ],
    'stappen_kop': 'Hoe een renovatie loopt',
    'stappen_intro': (
        'Renovatie is bij uitstek werk waarbij het loont om eerst te kijken en dan pas '
        'te beginnen: wat u openhaalt, bepaalt de rest van het werk.'),
    'stappen': [
        ('Opname en beoordeling',
         'Wat is er aan de hand, hoe ver reikt het, en wat kan blijven zitten. Bij een '
         'dak: de staat van pannen, panlatten, dakbeschot en isolatie.',
         None),
        ('Voorstel met een volgorde erin',
         'Wat er nu moet, wat er tegelijk verstandig is en wat kan wachten. Dat scheelt '
         'later dubbel werk.',
         'Werk dat elkaar raakt, doen we in een keer: een dak dat er toch af gaat, is het '
         'moment om te isoleren.'),
        ('Offerte',
         'Per onderdeel, zodat u kunt kiezen wat u nu laat doen en wat later.',
         None),
        ('Uitvoering',
         'Wat het huis droog en heel houdt eerst, de afwerking daarna. Stukadoorswerk en '
         'spuitwerk lopen via Peter Helmich, loodgieterswerk via Sanders.',
         None),
        ('Nalopen',
         'We lopen het werk met u na, buiten en binnen. Wat u ziet, nemen we mee.',
         None),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Bij renovatie is de geschiedenis van de woning het halve verhaal.'),
    'input': [
        ('lijst', 'Wat u opvalt',
         'Vochtplekken, scheuren, tocht, deuren die klemmen. Ook wanneer het begon, als '
         'u dat weet.'),
        ('klok', 'Het bouwjaar en wat er eerder is gedaan',
         'Een eerdere verbouwing, een vervangen dak of nieuwe kozijnen bepalen wat we '
         'aantreffen.'),
        ('schild', 'Wat u weet over asbest',
         'Bij woningen van voor 1994 hoort er voor sloopwerk een asbestinventarisatie te '
         'liggen. Is die er al, dan helpt dat.'),
        ('document', 'Rapporten die er al zijn',
         'Een bouwkundige keuring bij aankoop, of een rapport van een eerdere inspectie.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('lijst', 'Een beoordeling van wat er is',
         'Wat er aan de hand is, hoe ver het reikt en wat er kan blijven zitten.'),
        ('trap', 'Een volgorde die klopt',
         'Eerst droog en heel, dan isolatie en installaties, dan afwerking.'),
        ('vinkje', 'Werk dat af is opgeleverd',
         'Met de vaste stukadoors, metselaars en elektriciens waarmee we werken.'),
        ('blad', 'Een moment om te isoleren',
         'Waar het werk het toch al openlegt, wijzen we u erop. Dat scheelt een tweede '
         'project.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Wat is het verschil tussen renovatie en verbouwing?',
         'Bij renovatie vervangt of herstelt u wat er is en blijft de indeling in grote '
         'lijnen zoals hij was. Bij een verbouwing verandert de indeling of de '
         'constructie. In de praktijk lopen ze in elkaar over: een dak dat vervangen '
         'wordt is renovatie, maar een dakkapel erbij is verbouwing.'),
        ('Heb ik voor renovatie een vergunning nodig?',
         'Gewoon onderhoud en het vervangen van onderdelen door gelijkwaardige is meestal '
         'vergunningvrij. Verandert het uiterlijk van de woning, of raakt het de '
         'constructie, dan kan het anders liggen &mdash; en bij een monument of in een '
         'beschermd stadsgezicht gelden aparte regels. De vergunningcheck van het '
         'Omgevingsloket is het startpunt.'),
        ('Kan ik onderdelen los laten doen?',
         'Ja. We zetten de offerte per onderdeel op, zodat u kunt kiezen wat nu gebeurt '
         'en wat later. We geven daarbij aan welk werk beter in een keer kan, omdat het '
         'anders dubbel wordt gedaan.'),
        ('Is renovatie het moment om te isoleren?',
         'Vaak wel. Als een dak of een gevel toch open moet, kost isoleren relatief '
         'weinig extra ten opzichte van een apart isolatieproject later. Vervangt u een '
         'constructieonderdeel, dan stelt het Besluit bouwwerken leefomgeving daar '
         'bovendien minimumeisen aan.'),
    ],
}


# ---------------------------------------------------------------------------
#  Deuren en puien
# ---------------------------------------------------------------------------
VERHAAL['deuren-en-puien.html'] = {
    'wanneer_kop': 'Wanneer een deur of pui aan vervanging toe is',
    'wanneer_intro': (
        'Een deur of pui is het onderdeel van de gevel dat u elke dag aanraakt. Dat is '
        'ook waar u het eerst merkt dat het niet meer klopt.'),
    'situaties': [
        ('De voordeur sluit niet meer goed',
         'Klemmen, tocht, een slot dat gedwongen moet worden. Bij een oudere houten deur '
         'is dat vaak werk dat niet meer terug te draaien is.'),
        ('U wilt de tuin dichter bij de woonkamer',
         'Openslaande deuren of een schuifpui maken van een achtergevel een opening. Dat '
         'is een constructieve ingreep zodra de opening groter wordt dan hij was.'),
        ('Er komt een aanbouw of nieuwbouw',
         'Bij een nieuwe uitbouw kiest u de pui erbij. Dat is het moment om te bepalen '
         'wat er open moet kunnen en hoeveel licht er binnenkomt.'),
    ],
    'uitleg_kop': 'Wat er te kiezen valt, en wat de keuze bepaalt',
    'uitleg_extra': [
        'Ons aanbod in deuren en puien is heel divers: van een voordeur tot openslaande '
        'deuren, een schuifpui of een pui op maat. Wat het wordt, hangt af van drie '
        'dingen: hoeveel opening u wilt, hoeveel ruimte er is om te draaien of te '
        'schuiven, en wat de gevel constructief aankan.',
        'Openslaande deuren hebben binnen of buiten draairuimte nodig, maar geven een '
        'volledig vrije doorgang. Een schuifpui neemt geen draairuimte in, maar schuift '
        'langs een vast deel, dus de helft van de opening blijft dicht. Bij een '
        'hefschuifpui is dat comfortabeler en zwaarder uitgevoerd. Welke variant het '
        'wordt, is vooral een woonvraag &mdash; en pas daarna een technische.',
        'Wordt de opening in de gevel groter dan hij was, dan is het ook een '
        'constructieve vraag. De belasting boven de opening moet worden opgevangen door '
        'een latei of een stalen ligger, en die moet zijn krachten kwijt aan de zijkanten. '
        'Dat is precies het punt waarop een pui een bouwkundige klus wordt in plaats van '
        'een montageklus.',
    ],
    'stappen_kop': 'Van keuze naar geplaatste pui',
    'stappen_intro': (
        'Bij deuren en puien is de maatvoering het werk. Het inmeten gebeurt daarom pas '
        'als vaststaat wat er komt, en niet andersom.'),
    'stappen': [
        ('Kiezen wat het wordt',
         'Voordeur, achterdeur, openslaande deuren, schuifpui of een pui op maat. We '
         'kijken naar de draairuimte, de lichtinval en het aanzicht van de gevel.',
         'Ons aanbod is divers; het is nuttig om te weten wat u wilt kunnen openen en hoe '
         'vaak.'),
        ('Inmeten',
         'De bestaande opening wordt exact opgemeten, inclusief de aansluiting op '
         'metselwerk, dorpel en vloer.',
         None),
        ('Constructief nakijken als de opening verandert',
         'Wordt de opening groter, dan komt er een latei of ligger boven. Dat wordt '
         'berekend voordat er iets uitgehakt wordt.',
         None),
        ('Bestellen en voorbereiden',
         'De pui of deur wordt op maat gemaakt. De levertijd is die van de leverancier; '
         'die hoort u zodra de bestelling staat.',
         None),
        ('Plaatsen en afwerken',
         'Uitnemen, stellen, monteren, aansluiten op het metselwerk en afwerken aan de '
         'binnen- en buitenzijde. De woning gaat op de dag van plaatsing weer dicht.',
         None),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Voor een goede offerte hebben we vooral een beeld nodig van de bestaande '
        'situatie.'),
    'input': [
        ('liniaal', 'De maten van de bestaande opening',
         'Bij benadering is genoeg voor de offerte; wij meten exact in voordat er '
         'besteld wordt.'),
        ('lijst', 'Wat u wilt kunnen openen',
         'Volledig open, deels open, of alleen licht en zicht. Dat bepaalt de keuze '
         'tussen draaien en schuiven.'),
        ('huis', 'Een foto van de gevel',
         'Zo zien we het aanzicht, de bestaande kozijnindeling en waar de pui in past.'),
        ('document', 'Bij een VvE: de afspraken',
         'Kozijnen en gevels zijn bij een VvE vaak gemeenschappelijk. Dan is toestemming '
         'van de vergadering nodig.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('lijst', 'Een onderbouwd advies',
         'Welke variant past bij uw gevel, uw ruimte en wat u wilt kunnen openen.'),
        ('liniaal', 'Exact inmeten',
         'Op maat besteld, zodat er niet ter plekke gepast hoeft te worden.'),
        ('vinkje', 'Geplaatst en afgewerkt',
         'Aan de binnen- en buitenzijde aangesloten op het metselwerk en de vloer.'),
        ('schild', 'Een gevel die dicht is',
         'Kierdicht en waterdicht aangesloten, zodat u er geen tocht voor terugkrijgt.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Openslaande deuren of een schuifpui: wat is beter?',
         'Dat hangt af van hoeveel ruimte er langs de gevel is en van hoe vaak u de '
         'pui echt open wilt zetten. Staat er een terras of een tuinset vlak voor de '
         'gevel, dan is schuiven bijna altijd de praktischere keus. Zet u hem in de '
         'zomer wekenlang open, dan weegt de vrije doorgang van draaideuren zwaarder. '
         'We nemen het bij de opname met u door.'),
        ('Kan de opening in de gevel groter?',
         'Vaak wel. Boven de opening moet de belasting worden opgevangen door een latei '
         'of een stalen ligger, en die moet zijn krachten aan de zijkanten kwijt. Dat '
         'laten we berekenen voordat er gehakt wordt; het is geen kwestie van proberen.'),
        ('Leveren jullie de deuren en puien zelf?',
         'We plaatsen ze en we adviseren over de keuze; ons aanbod is divers. Voor '
         'kunststof kozijnen werken we met Select Windows, onze vaste leverancier.'),
        ('Hoe lang staat mijn gevel open?',
         'De pui wordt op maat gemaakt en pas geplaatst als hij er is. Uitnemen en '
         'plaatsen gebeurt op dezelfde dag, zodat de woning dezelfde dag weer dicht is. '
         'De levertijd vooraf is die van de leverancier.'),
    ],
}


# ---------------------------------------------------------------------------
#  Kunststof kozijnen en voorgevels
# ---------------------------------------------------------------------------
VERHAAL['kunststof-kozijnen.html'] = {
    'wanneer_kop': 'Wanneer kunststof de logische keuze is',
    'wanneer_intro': (
        'Kunststof kozijnen zijn geen compromis meer. Ze lijken tegenwoordig sterk op '
        'hout en hebben functioneel een aantal voordelen die zich elk jaar herhalen.'),
    'situaties': [
        ('U bent klaar met schilderen',
         'Houten kozijnen vragen periodiek onderhoud, en dat onderhoud is niet vrijblijvend: '
         'gebeurt het niet, dan volgt houtrot. Kunststof is onderhoudsarm en blijft lang '
         'mooi.'),
        ('De stookkosten lopen op',
         'Oude kozijnen met enkel glas of verouderd dubbelglas zijn een groot deel van '
         'het warmteverlies van een woning. Nieuwe kozijnen met goed isolerend glas '
         'schelen op de energierekening.'),
        ('De voorgevel is toe aan vernieuwing',
         'Bij een kunststof voorgevel wordt het hele geveldeel vervangen in plaats van '
         'losse kozijnen. Dat geeft een strak beeld en één doorlopende aansluiting.'),
    ],
    'uitleg_kop': 'Wat kunststof kozijnen doen, en waar u op let',
    # De eerste alinea van dit blok is de brontekst zelf; die wordt er door de
    # bouwer voor gezet en staat daarom niet nog een keer in deze lijst.
    'uitleg_extra': [
        'Technisch zit het verschil in twee dingen. Het profiel is opgebouwd uit kamers '
        'die lucht insluiten en daarmee isoleren, en het is voorzien van rubberen '
        'aanslagen die het kozijn kierdicht maken. Het glas is een aparte keuze: HR++ of '
        'triple glas bepaalt samen met het profiel wat een raam werkelijk isoleert. Een '
        'goed profiel met matig glas levert weinig op, en andersom net zo goed.',
        'Waar het in de praktijk op vastloopt, is de aansluiting op het metselwerk. Een '
        'kozijn dat perfect is maar slecht is aangezet, geeft alsnog tocht en op termijn '
        'vocht. Dat deel is bouwkundig werk en niet montagewerk, en het is de reden dat '
        'wij de kozijnen zelf plaatsen in plaats van ze te laten afleveren.',
    ],
    'stappen_kop': 'Van keuze naar geplaatst kozijn',
    'stappen_intro': (
        'Kozijnen vervangen is werk waarbij uw gevel per dagdeel opengaat en weer dicht '
        'moet. Alles wat vooraf klaar kan liggen, ligt daarom vooraf klaar.'),
    'stappen': [
        ('Opname en advies',
         'Welke kozijnen worden vervangen, welke indeling, welke kleur binnen en buiten, '
         'en welk glas. Kleur binnen en buiten kan verschillen.',
         'Dat wat de kleuren binnen en buiten doen, is waar klanten achteraf het meest '
         'over te spreken zijn.'),
        ('Inmeten',
         'Elk kozijn wordt exact opgemeten. Bij een voorgevel wordt het geveldeel als '
         'geheel ingemeten in plaats van kozijn voor kozijn.',
         None),
        ('Bestellen bij Select Windows',
         'Onze vaste leverancier voor kunststof kozijnen maakt ze op maat. De levertijd '
         'is die van de leverancier en hoort u zodra de order staat.',
         None),
        ('Plaatsen',
         'De oude kozijnen eruit, de nieuwe erin, stellen, aanzetten op het metselwerk en '
         'afkitten. Per dag wordt er niet meer opengemaakt dan diezelfde dag weer dicht '
         'kan.',
         None),
        ('Afwerken',
         'De aansluiting binnen en buiten afwerken, en waar nodig stuc- en spuitwerk door '
         'Peter Helmich.',
         None),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Voor een offerte hebben we een beeld nodig van welke kozijnen het betreft en hoe '
        'ze er nu uitzien.'),
    'input': [
        ('huis', 'Foto&rsquo;s van de gevel',
         'Van buiten en van binnen, zodat we de indeling en het aanzicht zien.'),
        ('lijst', 'Welke kozijnen het betreft',
         'Alleen de voorgevel, de hele woning, of specifieke ramen. En of de voordeur '
         'meegaat.'),
        ('liniaal', 'De maten bij benadering',
         'Genoeg voor de offerte. Voor de bestelling meten wij exact in.'),
        ('document', 'Bij een VvE: de toestemming',
         'Gevels en kozijnen zijn bij een VvE vaak gemeenschappelijk; dan beslist de '
         'vergadering mee.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('lijst', 'Advies over profiel, glas en kleur',
         'Wat samen bepaalt hoeveel een raam werkelijk isoleert, en hoe de gevel eruit '
         'komt te zien.'),
        ('liniaal', 'Op maat gemaakt',
         'Via Select Windows, onze vaste leverancier voor kunststof kozijnen.'),
        ('schild', 'Bouwkundig aangezet',
         'De aansluiting op het metselwerk is waar het meestal misgaat; die maken wij '
         'zelf.'),
        ('blad', 'Onderhoudsarm en isolerend',
         'Geen schilderbeurten meer, en minder warmteverlies via de gevel.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Zie je dat het kunststof is?',
         'Nauwelijks. Kunststof kozijnen zijn qua uiterlijk tegenwoordig bijna niet meer '
         'van houten te onderscheiden. De profielen zijn slanker geworden en er zijn '
         'houtnerfafwerkingen waarbij het verschil op een meter afstand niet meer opvalt.'),
        ('Wat scheelt het op de energierekening?',
         'Dat hangt af van wat er nu zit en welk glas erin komt. De winst zit in twee '
         'dingen tegelijk: het profiel dat isoleert en kierdicht sluit, en het glas. '
         'Wat het in uw situatie oplevert, hangt zo sterk af van de bestaande kozijnen dat '
         'een percentage noemen niets waard is; wel weten we welke combinatie het meeste '
         'effect heeft.'),
        ('Moet ik kunststof kozijnen onderhouden?',
         'Onderhoudsarm is niet onderhoudsvrij. Schoonmaken en af en toe de scharnieren en '
         'rubbers nalopen houdt ze goed. Wat wegvalt is het schilderwerk, en daarmee het '
         'risico op houtrot.'),
        ('Kan ik alleen de voorgevel doen?',
         'Ja. Een kunststof voorgevel is een geveldeel dat als geheel wordt vervangen; dat '
         'kan los van de rest van de woning. Bij een VvE is daar meestal wel toestemming '
         'van de vergadering voor nodig, omdat de gevel gemeenschappelijk is.'),
        ('Wie levert de kozijnen?',
         'Select Windows is onze vaste leverancier voor kunststof kozijnen. Wij doen het '
         'inmeten, het plaatsen en het bouwkundig aanzetten.'),
    ],
}


# ---------------------------------------------------------------------------
#  Gevelbekleding
# ---------------------------------------------------------------------------
VERHAAL['gevelbekleding.html'] = {
    'wanneer_kop': 'Wanneer gevelbekleding het antwoord is',
    'wanneer_intro': (
        'Met gevelbekleding geeft u uw huis in een handomdraai een nieuwe uitstraling. '
        'Er zijn drie redenen waarom mensen ermee beginnen.'),
    'situaties': [
        ('De gevel is verweerd',
         'Verkleurd metselwerk, oud houtwerk of een gevelvlak dat niet meer bij de rest '
         'past. Bekleding geeft er een nieuw front voor terug.'),
        ('Een dakopbouw of aanbouw moet aansluiten',
         'Bij een nieuwe verdieping of uitbouw is bekleding een manier om het nieuwe deel '
         'een eigen, rustig vlak te geven in plaats van het metselwerk te imiteren.'),
        ('Er moet isolatie bij',
         'Bekleding wordt meestal op een regelwerk gemonteerd. In die ruimte kan isolatie, '
         'en dan doet de gevel twee dingen tegelijk.'),
    ],
    'uitleg_kop': 'Hoe gevelbekleding is opgebouwd',
    'uitleg_extra': [
        'Gevelbekleding is een afwerking die vóór de bestaande gevel of vóór een nieuwe '
        'constructie komt. U kiest uit verschillende kleuren en materialen: hout, '
        'kunststof, plaatmateriaal of composiet, in delen die horizontaal of verticaal '
        'lopen.',
        'De opbouw is bij vrijwel elk materiaal hetzelfde. Op de gevel komt een regelwerk, '
        'daarachter blijft een geventileerde spouw, en de bekleding wordt op dat regelwerk '
        'bevestigd. Die spouw is het belangrijkste onderdeel: hij voert vocht af dat achter '
        'de bekleding komt. Zonder die luchtlaag blijft vocht staan en gaat de constructie '
        'eronder achteruit &mdash; ook bij materiaal dat zelf niet rot.',
        'Het materiaal bepaalt vooral het onderhoud en de uitstraling. Hout vraagt periodiek '
        'onderhoud en vergrijst als u dat niet doet; kunststof en composiet zijn '
        'onderhoudsarm maar hebben een ander karakter. Wat er in uw straat mag, kan '
        'bovendien vastliggen: verandert het aanzicht van de woning, dan kan het '
        'omgevingsplan van uw gemeente eisen stellen.',
    ],
    'stappen_kop': 'Hoe een gevel wordt bekleed',
    'stappen_intro': (
        'Het zichtbare deel is de bekleding, maar het werk zit in wat eronder komt.'),
    'stappen': [
        ('Beoordelen van de bestaande gevel',
         'Wat zit erachter, is het vlak, en is de ondergrond gezond genoeg om een '
         'regelwerk op te bevestigen?',
         None),
        ('Kiezen van materiaal en kleur',
         'Hout, kunststof, plaat of composiet, en de richting van de delen. Dat bepaalt '
         'het beeld en het onderhoud.',
         'Kijk niet alleen naar hoe het er nu uitziet maar naar hoe het over tien jaar '
         'staat; dat verschilt sterk per materiaal.'),
        ('Nakijken wat er mag',
         'Verandert het aanzicht van de woning, dan kan de gemeente eisen stellen via het '
         'omgevingsplan. Bij een VvE beslist de vergadering mee.',
         None),
        ('Regelwerk en isolatie',
         'Het regelwerk gaat op de gevel, met een geventileerde spouw erachter. Waar het '
         'kan, gaat er isolatie in.',
         None),
        ('Monteren en afwerken',
         'De bekleding wordt gemonteerd en de aansluitingen bij kozijnen, hoeken, dakrand '
         'en maaiveld worden afgewerkt. Daar zit het vakwerk.',
         None),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': 'Voor een goed voorstel hebben we het gevelvlak zelf nodig, en uw smaak.',
    'input': [
        ('huis', 'Foto&rsquo;s van de gevel',
         'Het hele vlak, en de aansluitingen bij kozijnen, hoeken en dakrand.'),
        ('liniaal', 'De maten van het vlak',
         'Bij benadering; wij meten in bij de opname.'),
        ('lijst', 'Waar uw voorkeur ligt',
         'Materiaal, kleur en richting van de delen. Voorbeelden van gevels die u mooi '
         'vindt, helpen meer dan woorden.'),
        ('document', 'Wat er al vastligt',
         'Eisen van de gemeente of van de VvE over het aanzicht van de gevel.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('lijst', 'Een materiaalkeuze die past',
         'Bij het beeld dat u wilt en bij het onderhoud dat u erin wilt steken.'),
        ('schild', 'Een geventileerde opbouw',
         'Regelwerk met een spouw erachter, zodat vocht weg kan in plaats van te blijven '
         'staan.'),
        ('blad', 'Isolatie waar het kan',
         'De ruimte achter de bekleding is de logische plek om te isoleren.'),
        ('vinkje', 'Nette aansluitingen',
         'Bij kozijnen, hoeken, dakrand en maaiveld. Daar zie je of het werk klopt.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Welk materiaal kan ik het beste kiezen?',
         'Dat hangt af van hoeveel onderhoud u wilt doen en welk beeld u zoekt. Hout heeft '
         'karakter maar vraagt periodiek onderhoud en vergrijst zonder. Kunststof, plaat en '
         'composiet zijn onderhoudsarm en houden hun kleur langer, maar ogen strakker. We '
         'nemen het bij de opname met u door.'),
        ('Kan ik meteen isoleren?',
         'Meestal wel, en het is het logische moment. De bekleding komt op een regelwerk met '
         'een geventileerde spouw erachter; in die opbouw kan isolatie mee. Achteraf isoleren '
         'betekent dat de bekleding er weer af moet.'),
        ('Heb ik er een vergunning voor nodig?',
         'Gevelbekleding verandert het aanzicht van de woning, en dat is precies waar het '
         'omgevingsplan van uw gemeente iets over kan zeggen. In een beschermd stadsgezicht of '
         'bij een monument ligt het strenger. De vergunningcheck van het Omgevingsloket geeft '
         'uitsluitsel; bij een VvE beslist de vergadering bovendien mee.'),
        ('Waarom moet er een luchtlaag achter?',
         'Achter elke gevelbekleding komt vocht &mdash; door slagregen, door kieren of vanuit '
         'de woning. Een geventileerde spouw voert dat af. Zonder blijft het vocht staan tegen '
         'de constructie eronder, en dan levert een nieuwe gevel op termijn schade op in plaats '
         'van bescherming.'),
    ],
}


# ---------------------------------------------------------------------------
#  Bouwadvies en bouwtekening
# ---------------------------------------------------------------------------
VERHAAL['bouwadvies.html'] = {
    'wanneer_kop': 'Wanneer u eerst wilt weten of het kan',
    'wanneer_intro': (
        'Niet elk plan begint met een offerte. Soms is de eerste vraag simpelweg: kan dit, '
        'mag dit, en wat komt erbij kijken?'),
    'situaties': [
        ('Er is een idee, maar nog geen tekening',
         'U weet wat u wilt bereiken maar niet hoe het eruit moet zien. Wij vertalen uw '
         'plannen naar een bouwtekening.'),
        ('U wilt weten of er een vergunning nodig is',
         'Of een plan vergunningvrij kan, hangt af van maten, plek en het omgevingsplan. Een '
         'tekening is meestal nodig om die vraag te kunnen beantwoorden.'),
        ('Er moet iets aangevraagd worden',
         'Voor een omgevingsvergunning heeft de gemeente tekeningen nodig die de bestaande en '
         'de nieuwe situatie laten zien. Die verzorgen wij.'),
    ],
    'uitleg_kop': 'Wat bouwadvies en een bouwtekening inhouden',
    'uitleg_extra': [
        'Uiteraard voorzien we u, indien gewenst, ook van bouwadvies en verzorgen we de '
        'technische tekeningen. Dat is geen los product maar het begin van vrijwel elk '
        'project: zonder tekening is er niets om over te beslissen en niets om aan te vragen.',
        'Een bouwtekening laat twee situaties zien: hoe het nu is en hoe het wordt. Daar horen '
        'plattegronden, doorsneden en gevelaanzichten bij, met maten erin. Voor een aanvraag '
        'komt daar een situatietekening bij die laat zien waar het bouwwerk op het perceel '
        'staat. Dat is wat de gemeente nodig heeft om te toetsen, en wat op de bouw nodig is om '
        'te maken wat er bedoeld werd.',
        'Bouwadvies gaat over de stap daarvoor: wat is er mogelijk, wat kost het aan ingrepen '
        'en waar loopt het plan vast. Soms is het antwoord dat een andere oplossing beter werkt '
        'dan de bedachte &mdash; een dakopbouw in plaats van een dakkapel, of een uitbouw over '
        'de volle breedte in plaats van een serre. Voor de constructieve kant werken we samen '
        'met EWP, ons vaste bureau voor ontwerp, constructie en bouwadvies.',
    ],
    'stappen_kop': 'Hoe een plan een tekening wordt',
    'stappen_intro': (
        'U kunt vrijblijvend een orientatiegesprek aanvragen of een offerte laten opstellen. '
        'Beide beginnen hetzelfde.'),
    'stappen': [
        ('Orientatiegesprek',
         'Wat wilt u bereiken, wat staat er nu, en wat ligt er al vast? Vrijblijvend aan te '
         'vragen.',
         None),
        ('Opname van de bestaande situatie',
         'Maten, constructie en aansluitingen. Zonder een kloppende bestaande situatie is een '
         'tekening van de nieuwe situatie een schets.',
         None),
        ('Bouwtekening',
         'Plattegronden, doorsneden en gevelaanzichten van de bestaande en de nieuwe '
         'situatie, met maatvoering.',
         None),
        ('Constructief advies waar nodig',
         'Raakt het plan de draagconstructie, dan komt de berekening van EWP erbij.',
         None),
        ('Naar vergunning of naar offerte',
         'Met de tekening kunt u de vergunningaanvraag doen, of we zetten er een offerte voor '
         'de uitvoering onder. Of allebei.',
         'De tekening is van u; u zit er niet mee vast aan de uitvoering.'),
    ],
    'input_kop': 'Wat wij van u nodig hebben',
    'input_intro': (
        'Hoe meer er al ligt, hoe sneller de tekening klopt. Ontbreekt alles, dan beginnen we '
        'bij het inmeten.'),
    'input': [
        ('document', 'Bestaande tekeningen',
         'Een bouwtekening, de plattegrond uit de verkoopbrochure, of het bouwdossier van uw '
         'gemeente.'),
        ('lijst', 'Wat u wilt bereiken',
         'Liever in functies dan in oplossingen: &lsquo;een werkkamer erbij&rsquo; laat meer '
         'ruimte dan &lsquo;een dakkapel van drie meter&rsquo;.'),
        ('huis', 'Kadastrale gegevens',
         'Voor de situatietekening bij een vergunningaanvraag, en bij bouwen tegen de '
         'erfgrens.'),
        ('klok', 'Wanneer het moet liggen',
         'Als er een aanvraagmoment of een verhuisdatum aan hangt, is het handig dat vroeg te '
         'weten.'),
    ],
    'oplevering_kop': 'Wat u van ons krijgt',
    'oplevering': [
        ('document', 'Een bouwtekening',
         'Bestaande en nieuwe situatie, met plattegronden, doorsneden en gevelaanzichten.'),
        ('lijst', 'Advies over wat er kan',
         'Inclusief het alternatief dat u zelf niet had bedacht, als dat er is.'),
        ('grafiek', 'Constructief advies waar nodig',
         'Via EWP, ons vaste bureau voor ontwerp, constructie en bouwadvies.'),
        ('vinkje', 'Een basis voor de aanvraag',
         'Tekeningen die bruikbaar zijn voor een omgevingsvergunning.'),
    ],
    'voordelen_kop': 'Waarom mensen hiervoor bij J. Boom uitkomen',
    'faq': [
        ('Kan ik alleen een tekening laten maken?',
         'Ja. We verzorgen de technische tekeningen ook als u de uitvoering nog niet bij ons '
         'onderbrengt. U kunt vrijblijvend een orientatiegesprek aanvragen of een offerte laten '
         'opstellen.'),
        ('Vragen jullie de vergunning voor mij aan?',
         'Wij verzorgen de tekeningen die u bij de aanvraag nodig heeft. De aanvraag zelf loopt '
         'via het Omgevingsloket en de gemeente beslist erover; die termijn ligt niet bij ons.'),
        ('Wat kost een bouwtekening?',
         'Dat hangt af van de omvang van het plan en van wat er al ligt. Vraag een offerte aan; '
         'dan weet u het voordat u iets vastlegt.'),
        ('Werken jullie samen met een constructeur?',
         'Ja. Voor ontwerp, constructie en bouwadvies werken we samen met EWP. Raakt uw plan de '
         'draagconstructie, dan komt de berekening daarvandaan.'),
    ],
}


# ---------------------------------------------------------------------------
#  De voordelen: hetzelfde bij elke dienst, want het gaat over het bedrijf
# ---------------------------------------------------------------------------
# Alle vier zijn terug te lezen op www.jboom.nl. Ze zeggen iets over hoe J. Boom
# werkt en niet over de dienst, dus ze verschillen niet per pagina.
VOORDELEN = [
    ('mensen', 'U heeft met de bazen zelf te maken',
     'Martin en Mario voeren het gesprek, maken de planning en staan op de bouw. Er zit '
     'geen laag tussen.'),
    ('klok', 'Een strakke planning',
     'U weet van tevoren wat u kunt verwachten en wanneer uw woning klaar is voor gebruik. '
     'Onze werktijden zijn flexibel.'),
    ('schild', 'Vaste partners, geen wisselende ploegen',
     'Dezelfde stukadoors, metselaars en elektriciens bij elk project. Het werk ligt daardoor '
     'niet stil en niemand loopt elkaar in de weg.'),
    ('huis', 'Bekend in Purmerend en omstreken',
     'Een familiebedrijf sinds 1935, inmiddels in de vierde generatie, met het werk vlak bij '
     'huis.'),
]


def verhaal(bestand):
    """De verhaallaag bij een dienstpagina, met de vaste voordelen erbij."""
    v = dict(VERHAAL[bestand])
    v['voordelen'] = VOORDELEN
    return v
