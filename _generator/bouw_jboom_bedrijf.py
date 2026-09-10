# -*- coding: utf-8 -*-
"""Over ons, historie, werkwijze en de referenties.

Vier pagina's over het bedrijf. De feiten komen uit de homepage en de
dienstenpagina van www.jboom.nl (de bron heeft geen aparte over-onspagina);
de referenties komen van /klanten-over-j-boom.

Het oorspronkelijke template had hier zes pagina's, waaronder een teampagina en
een vacaturepagina. Die zijn er niet meer, en dat is een inhoudelijke keuze:

  - een teampagina van twee mensen zonder foto's is dunner dan hetzelfde blok
    op over-ons.html, dus staat het daar;
  - vacatures zijn er niet. De bron vertelt juist het omgekeerde: het bedrijf
    is rond 2000 bewust teruggebracht naar twee man en wordt niet uitgebreid.
    Een vacaturepagina zou daar tegenin gaan.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
from schil import _plat
import inhoud_jboom as D
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent


def _t(x):
    return D._tekens(x)


def _p(alineas):
    return "\n".join(f'              <p>{_t(a)}</p>' for a in D.splits_lang(alineas))


def _partnermerk(naam, url):
    """De naam van een partner, als link waar de bron er een had."""
    return f'<a href="{url}" rel="noopener">{naam}</a>' if url else naam


def _tekstsectie(nr, ident, kop, alineas, subtitel=None, achtergrond='white'):
    label = (f'            <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>\n'
             if subtitel else '')
    kopregel = f'            <h2 class="section-heading">{_t(kop)}</h2>\n' if kop else ''
    return f'''  <section class="content-block" id="s{nr}-{ident}">
    <div class="container">
      <div class="content-block--container background--{achtergrond}">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
{label}{kopregel}            <div class="article-body" style="margin-top:var(--space-500)">
{_p(alineas)}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>'''


# --------------------------------------------------------------------- over ons
def over_ons():
    k = C.BEDRIJF['over-ons.html']
    # De bron zegt over deze twee alleen wie ze zijn en hoe ze zich tot elkaar
    # verhouden. Er staat dus geen functieomschrijving bij die verzonnen zou
    # zijn; wat er staat is wat de bron zegt, per persoon anders.
    zegt = {
        'Mario Boom': 'Besloot vijfenzestig jaar na de oprichting het bedrijf qua '
                      'personeel niet meer uit te breiden, maar terug te brengen naar '
                      'twee man.',
        'Martin Babel': 'Werkt samen met zijn zwager hard en met veel plezier aan de '
                        'projecten, voornamelijk in Purmerend en omstreken.',
    }
    mensen = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">{rol}</span>
            <h3 class="panel__title">{naam}</h3>
            <p class="panel__body">{_t(zegt[naam])}</p>
          </div>
        </div>''' for i, (naam, rol) in enumerate(D.VAKMENSEN))
    groepen = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <h3 class="panel__title">{g}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (g, tekst) in enumerate([
        ('Particulieren', 'Van een nieuwe voordeur tot een complete uitbouw of een '
                          'nieuwbouwwoning bij mensen thuis. Dit is het grootste deel '
                          'van ons werk.'),
        ('Verenigingen van Eigenaren', 'Werk aan gevels, kozijnen en gemeenschappelijke '
                                       'onderdelen, met de besluitvorming die daarbij hoort.'),
    ]))

    # De archieffoto in de hero, op verzoek. Let op de maat: het bronbestand is
    # 436x284 en meer heeft de bron niet. Nagemeten op 1440px is dit vak
    # 720x492, dus de foto wordt 1,65x opgeschaald in CSS-pixels -- en op een
    # scherm met dubbele pixeldichtheid komt hij 3,3x tekort. Daar wordt hij
    # zichtbaar zachter van; op een grote retina-monitor het meest.
    #
    # Bewust geaccepteerd, en bewust geen opgeschaalde varianten aangemaakt:
    # pixels bijverzinnen maakt het beeld niet scherper, alleen het bestand
    # groter. De ladder van dit beeld blijft dus [436].
    #
    # De uitsnede valt mee: het vak is 1,462 en de foto 1,535, dus er gaat maar
    # een paar procent van de zijkanten af.
    #
    # Komt er een scan van het origineel, dan wordt dit een van de sterkste
    # beelden van de site; zie punt 3 in CONTENT-TODO.md.
    # Komt er ooit een scan van het origineel, dan is dit één regel in
    # beeldplan.json plus maak_assets.py draaien; zie punt 3 in CONTENT-TODO.md.
    inhoud = f'''{paginahero('01', 'over-ons', 'Over ons', D.afbreek(_t(k['h1'])), 'jboom-historie')}

{_tekstsectie('02', 'lead', None, k['lead'])}

  <section class="content-block" id="s03-wie">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Het team</span>
            <h2 class="section-heading">{_t(k['wie_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{_t(k['wie_lead'])}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--2">
{mensen}
      </div>
    </div>
  </section>

  <section class="content-block" id="s04-voor-wie">
    <div class="container">
      <div class="content-block--container background--grey">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Opdrachtgevers</span>
            <h2 class="section-heading">{_t(k['werk_kop'])}</h2>
            <div class="article-body" style="margin-top:var(--space-500)">
{_p(k['werk'])}
            </div>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--2">
{groepen}
      </div>
    </div>
  </section>

{_tekstsectie('05', 'samenwerking', k['samen_kop'], k['samen'], subtitel='Samenwerking')}

{citaten("06", kop="Wat klanten over J. Boom zeggen")}

  <section class="content-block" id="s07-verder">
    <div class="container">
      <div class="row g-0">
{beeldkaart("Historie", "Van 1935 tot nu, in vier generaties.",
            'jboom-veranda-voorgevel', alt="", kleur="grey", href="historie.html")}
{beeldkaart("Werkwijze", "Hoe een opdracht bij ons verloopt, van gesprek tot oplevering.",
            'jboom-aanbouw-16', alt="", kleur="white", href="werkwijze.html")}
{beeldkaart("Diensten", "Aanbouw, verbouw, nieuwbouw, dakkapellen, kozijnen en gevels.",
            'jboom-dakopbouw-woning', alt="", kleur="white", href="diensten.html")}
{beeldkaart("Projecten", "Werk dat in en rondom Purmerend is opgeleverd.",
            'jboom-aanbouw-schuifpui', alt="", kleur="grey", href="projecten.html")}
      </div>
    </div>
  </section>

{logoslider("08")}

{ctablok("09", k['slot_kop'])}
'''
    (UIT / 'over-ons.html').write_text(pagina(
        bestand='over-ons.html',
        titel=f'Over {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Aannemersbedrijf J. Boom is een familiebedrijf uit Purmerend, actief '
                      'sinds 1935 en inmiddels in de vierde generatie. Martin Babel en Mario '
                      'Boom werken voor particulieren en VvE&rsquo;s in Purmerend en omstreken.'),
        namespace='over-ons', pagina_css='over-ons.css', css_naam='over-ons',
        inhoud=inhoud,
    ), encoding='utf-8')
    return 'over-ons.html'


# --------------------------------------------------------------------- historie
def historie():
    k = C.BEDRIJF['historie.html']
    # De vier momenten die de bron noemt. Er staat geen jaartal bij het moment
    # waarop het bedrijf naar twee man ging; de bron zegt "vijfenzestig jaar na
    # oprichting", en dat staat er dus ook zo.
    tijdlijn = [
        ('1935', 'De grootvader van J. Boom sr. begint in Purmerend',
         'Hij begint voor zichzelf als aannemer. Zijn werkzaamheden bestaan onder andere '
         'uit verbouwingen en renovaties.', None),
        ('In die jaren', 'Meegebouwd aan De Rusthoeve',
         'In die periode werkt hij mee aan de bouw van verzorgingshuis De Rusthoeve in '
         'Purmerend.', None),
        ('De jaren daarna', 'In de familie gebleven en gegroeid',
         'Aannemersbedrijf J. Boom is altijd in de familie gebleven en door de jaren heen '
         'enorm gegroeid.', None),
        ('Vijfenzestig jaar na de oprichting', 'Bewust terug naar twee man',
         'Mario Boom, zoon van J. Boom sr., besluit het bedrijf qua personeel niet meer uit '
         'te breiden maar terug te brengen naar twee man. Samen met zijn zwager Martin Babel '
         'werkt hij sindsdien aan de projecten.',
         'Dat is nog steeds zo. Het is de reden dat u bij J. Boom met de mensen praat die '
         'het werk ook uitvoeren.'),
        ('Nu', 'De vierde generatie',
         'Inmiddels staat de vierde generatie aan het roer. Door de jaren heen is J. Boom '
         'een bekende naam in Purmerend en omgeving geworden.', None),
    ]
    treden = "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{jaar}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{_t(titel)}</h3>
            <p class="trede__tekst">{_t(tekst)}</p>
            {f'<p class="trede__gedrag"><span>Goed om te weten</span> {_t(detail)}</p>' if detail else ''}
          </div>
        </li>''' for i, (jaar, titel, tekst, detail) in enumerate(tijdlijn))

    inhoud = f'''{paginahero('01', 'historie', 'Historie', D.afbreek(_t(k['h1'])), 'jboom-veranda-voorgevel')}

{_tekstsectie('02', 'lead', None, k['lead'])}

  <section class="band background--grey" id="s03-tijdlijn">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Tijdlijn</span>
          <h2 class="section-heading">Vier generaties aannemers</h2>
          <p class="article-body" style="margin-top:var(--space-500)">
            Wat de bron erover vertelt, op volgorde. Waar de bron geen jaartal noemt,
            staat hier geen jaartal.
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{treden}
          </ol>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s04-beeld">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Uit het archief</span>
            <h2 class="section-heading">Hetzelfde werk, andere tijd</h2>
            <div class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              <p>Metselwerk, stellingen, handwerk. Het gereedschap is veranderd en de
                 regels ook, maar het vak is hetzelfde gebleven: iets bouwen dat er over
                 vijftig jaar nog staat.</p>
            </div>
          </div>
        </div>
      </div>
      <figure class="archieffoto">
        {foto('jboom-historie', maten="(max-width: 467px) calc(100vw - 32px), 436px")}
        <figcaption>De enige foto uit het familiearchief die J. Boom heeft gepubliceerd.
          Groter dan dit is het origineel niet, dus staat hij hier op zijn eigen maat.</figcaption>
      </figure>
    </div>
  </section>

  <section class="content-block" id="s05-verder">
    <div class="container">
      <div class="row g-0">
{beeldkaart("Over ons", "Wie Martin en Mario zijn, en voor wie zij werken.",
            'jboom-veranda-zonwering', alt="", kleur="grey", href="over-ons.html")}
{beeldkaart("Klanten over J. Boom", f"{len(D.REFERENTIES)} referenties, ondertekend en met datum.",
            'jboom-voordeur-gevel', alt="", kleur="white", href="referenties.html")}
      </div>
    </div>
  </section>

{logoslider("06")}

{ctablok("07", k['slot_kop'])}
'''
    (UIT / 'historie.html').write_text(pagina(
        bestand='historie.html',
        titel=f'Historie van {D.NAAM_KORT} | sinds 1935 in Purmerend',
        omschrijving=('In 1935 begon de grootvader van J. Boom sr. in Purmerend met zijn '
                      'aannemersbedrijf. Vier generaties later werken Mario Boom en Martin '
                      'Babel er nog steeds met veel plezier.'),
        namespace='historie', pagina_css='service.css', css_naam='service',
        inhoud=inhoud,
    ), encoding='utf-8')
    return 'historie.html'


# -------------------------------------------------------------------- werkwijze
def werkwijze():
    k = C.BEDRIJF['werkwijze.html']
    # Elke stap is terug te lezen op www.jboom.nl: het orientatiegesprek en de
    # offerte staan op de homepage, de bouwtekening en de coordinatie bij
    # Nieuwbouw, de vaste partners onder "De krachten gebundeld", en de strakke
    # planning en het dagelijks opruimen in de referenties.
    stappen = [
        ('Vrijblijvend orientatiegesprek',
         'U belt, mailt of vult het formulier in. We komen langs, kijken naar de bestaande '
         'situatie en horen wat u wilt bereiken. Daar zit u nergens aan vast.',
         'Zijn uw plannen nog niet concreet? Dan is dit precies het moment om te bellen.'),
        ('Bouwtekening en advies',
         'Uiteraard voorzien we u, indien gewenst, van bouwadvies en verzorgen we de '
         'technische tekeningen. Zo wordt uit een plan iets waarover te beslissen valt.',
         None),
        ('Constructie waar dat nodig is',
         'Raakt het plan de draagconstructie, dan komt de berekening van EWP, ons vaste '
         'bureau voor ontwerp, constructie en bouwadvies.',
         None),
        ('Offerte',
         'U krijgt een offerte waarin staat wat er gebeurt en wat erin zit, in dezelfde '
         'taal als het gesprek dat we voerden.',
         None),
        ('Planning',
         'Wij houden van een strakke planning. Daardoor weet u van tevoren wat u kunt '
         'verwachten en wanneer uw woning klaar is voor gebruik.',
         'Onze werktijden zijn flexibel. Is er nood aan de man? Dan staan wij zo op de '
         'stoep.'),
        ('Uitvoering met vaste partners',
         'Altijd dezelfde stukadoors, metselaars en elektriciens. Doordat we op elkaar '
         'ingespeeld zijn ligt het werk nooit stil en loopt niemand elkaar in de weg.',
         None),
        ('Oplevering',
         'We lopen het werk met u na en nemen mee wat u nog ziet. Ook daarna zijn we '
         'bereikbaar voor vragen over wat we gedaan hebben.',
         None),
    ]
    treden = "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{i + 1:02d}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{_t(titel)}</h3>
            <p class="trede__tekst">{_t(tekst)}</p>
            {f'<p class="trede__gedrag"><span>Goed om te weten</span> {_t(detail)}</p>' if detail else ''}
          </div>
        </li>''' for i, (titel, tekst, detail) in enumerate(stappen))

    partners = "\n".join(f'                <li><strong>{_partnermerk(naam, url)}</strong>'
                          f'<br>{rol}</li>' for naam, rol, url in D.PARTNERS)

    inhoud = f'''{patroonhero('01', 'werkwijze', 'Werkwijze', D.afbreek(_t(k['h1'])))}

{_tekstsectie('02', 'lead', None, k['lead'])}

  <section class="band background--grey" id="s03-stappen">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Stap voor stap</span>
          <h2 class="section-heading">Van eerste telefoontje tot oplevering</h2>
          <p class="article-body" style="margin-top:var(--space-500)">
            Niet elk project doorloopt alle stappen. Een voordeur vervangen vraagt geen
            bouwtekening; een uitbouw wel.
          </p>
          <div style="margin-top:var(--space-600)">
            {knop("Vraag een offerte aan", "offerte.html", "secundair")}
          </div>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{treden}
          </ol>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s04-partners">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Samenwerking</span>
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">De krachten gebundeld</h2>
            <div class="article-body">
{_p(C.DIENSTEN_OVERZICHT['samen'])}
              <h3 class="font-size--md" style="margin-top:var(--space-600)">De bedrijven die aan uw project bijdragen</h3>
              <ul class="case-lijst" role="list">
{partners}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{citaten("05", kop="Zo ervaren klanten het")}

{logoslider("06")}

{ctablok("07", k['slot_kop'])}
'''
    (UIT / 'werkwijze.html').write_text(pagina(
        bestand='werkwijze.html',
        titel=f'Werkwijze van {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Van vrijblijvend orientatiegesprek en bouwtekening tot offerte, '
                      'planning en oplevering. Zo verloopt een opdracht bij '
                      'Aannemersbedrijf J. Boom uit Purmerend.'),
        namespace='werkwijze', pagina_css='service.css', css_naam='service',
        inhoud=inhoud,
    ), encoding='utf-8')
    return 'werkwijze.html'


# ------------------------------------------------------------------ referenties
def referenties():
    k = C.BEDRIJF['referenties.html']
    blokken = []
    for i, (kop, citaat, naam, datum, onderwerp, beeld) in enumerate(D.REFERENTIES):
        ondertekening = f'{naam}, {datum}' if datum else naam
        kant = 'grey' if i % 2 == 0 else 'white'
        blokken.append(f'''  <section class="band background--{kant}" id="s{i + 3:02d}-referentie">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <figure class="referentie__beeld">
            {foto(beeld, maten="(max-width: 991px) 100vw, 33vw")}
          </figure>
        </div>
        <div class="col-lg-8 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">{onderwerp}</span>
          <h2 class="section-heading">{_t(kop)}</h2>
          <blockquote class="referentie__citaat">
            <p>{_t(citaat)}</p>
          </blockquote>
          <hr class="quote__streep">
          <p class="referentie__naam">{ondertekening}</p>
        </div>
      </div>
    </div>
  </section>''')

    inhoud = f'''{paginahero('01', 'referenties', 'Referenties', D.afbreek(_t(k['h1'])), 'jboom-voordeur-gevel')}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row g-0">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{_t(k['kop'])}</h2>
          <div class="article-body">
{chr(10).join(f"            <p>{_t(a)}</p>" for a in k['lead'])}
          </div>
          <p class="article-body" style="margin-top:var(--space-500)">
            <a href="{D.OUDERE_REFERENTIES_PDF}" rel="noopener">Bekijk de oudere referenties (PDF)</a>
          </p>
        </div>
      </div>
    </div>
  </section>

{chr(10).join(blokken)}

  <section class="content-block" id="s{len(D.REFERENTIES) + 3:02d}-verder">
    <div class="container">
      <div class="row g-0">
{beeldkaart("Projecten", "Werk dat in en rondom Purmerend is opgeleverd.",
            'jboom-aanbouw-schuifpui', alt="", kleur="grey", href="projecten.html")}
{beeldkaart("Onze werkwijze", "Hoe een opdracht bij ons verloopt, van gesprek tot oplevering.",
            'jboom-aanbouw-16', alt="", kleur="white", href="werkwijze.html")}
      </div>
    </div>
  </section>

{logoslider(f'{len(D.REFERENTIES) + 4:02d}')}

{ctablok(f'{len(D.REFERENTIES) + 5:02d}', k['slot_kop'])}
'''
    (UIT / 'referenties.html').write_text(pagina(
        bestand='referenties.html',
        titel=f'Klanten over {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Lees wat klanten schreven over hun dakopbouw, uitbouw, verbouwing of '
                      'kunststof kozijnen van Aannemersbedrijf J. Boom uit Purmerend.'),
        namespace='referenties', pagina_css='cases.css', css_naam='cases',
        inhoud=inhoud,
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Referenties van Aannemersbedrijf J. Boom",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": kop}
                for i, (kop, *_rest) in enumerate(D.REFERENTIES)],
        }, ensure_ascii=False, indent=2),
    ), encoding='utf-8')
    return 'referenties.html'


def main():
    gemaakt = [over_ons(), historie(), werkwijze(), referenties()]
    print(f'{len(gemaakt)} bedrijfspagina\'s geschreven')
    return gemaakt


if __name__ == '__main__':
    main()
