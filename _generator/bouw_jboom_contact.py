# -*- coding: utf-8 -*-
"""Contact, offerte, privacybeleid en cookies.

De bronsite heeft een contactformulier met vier velden (naam, e-mail,
telefoonnummer, bericht) en een akkoordvinkje dat naar de privacyverklaring
verwijst. Dat formulier wordt hier door het formuliercomponent van het template
gerenderd, met de dienstenlijst van J. Boom als onderwerpkeuze.

Let op: het formulier verstuurt nog niets. ENDPOINT in contactformulier.js is
leeg. Dat gold al voor het template en is met deze migratie niet veranderd; het
staat als openstaand punt in CONTENT-TODO.md.

De offertepagina heeft de bronsite niet als aparte pagina, maar er wordt op vier
plekken naar verwezen ("Direct een offerte aanvragen", "laat een offerte
opstellen"). Die pagina staat er dus wel, met hetzelfde formulier en een
onderwerp dat al op offerte staat.

Voor het privacybeleid heeft J. Boom wel een echte verklaring: een PDF op het
eigen domein. Daar wordt naartoe verwezen in plaats van dat er beleid wordt
verzonnen.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
import inhoud_jboom as D
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent

# De privacyzin die op de bronsite onder het contactformulier staat, letterlijk.
AVG = ('We gebruiken de informatie in dit formulier om contact met u op te nemen over '
       'uw vraag. Door dit formulier te verzenden, gaat u ermee akkoord dat wij uw '
       'gegevens kunnen verzamelen en gebruiken voor de redenen die hierboven genoemd '
       'staan.')


def _t(x):
    return D._tekens(x)


def _p(alineas, inspring='              '):
    return "\n".join(f'{inspring}<p>{_t(a)}</p>' for a in alineas)


def _icoonpanelen(items):
    from bouw_jboom_dienst import icoon
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            {icoon(ico)}
            <h3 class="voordeel__titel">{_t(titel)}</h3>
            <p class="panel__body">{_t(tekst)}</p>
          </div>
        </div>''' for i, (ico, titel, tekst) in enumerate(items))


# ---------------------------------------------------------------------- contact
def contact():
    # De gegevens staan in de vlakkenrij van het template: vier vlakken tot de
    # schermrand. De kleuren lopen vast in dezelfde volgorde, dus adres,
    # telefoon, e-mail en KvK krijgen op elke pagina hetzelfde vlak.
    #
    # Openingstijden staan er niet bij; de bron noemt ze niet. Wat de bron wel
    # zegt over bereikbaarheid ("onze werktijden zijn flexibel") staat in de
    # tekst en niet als een tijd die niet klopt.
    gegevens = [
        ('Adres', f'{D.STRAAT}<br>{D.POSTCODE_PLAATS}<br>'
                  f'<a href="{D.ROUTE}" rel="noopener">Routebeschrijving</a>'),
        ('Telefoon', f'<a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>'),
        ('E-mail', f'<a href="mailto:{D.EMAIL}">{D.EMAIL}</a>'),
        ('KvK', D.KVK),
    ]

    inhoud = f'''{paginahero("01", "contact", "Contact", D.afbreek(_t(C.CONTACT['h1'])), "jboom-bedrijfsbus")}

  <section class="content-text-side-cta" id="s02-introductie">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(C.CONTACT['kop'])}</h2>
            <div class="content-text-side-cta--body article-body">
{_p(C.CONTACT['lead'])}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop("Bel " + TELEFOON_WEERGAVE, "tel:" + TELEFOON_LINK)}
          </div>
        </div>
      </div>
    </div>
  </section>

{contactblok({"nr": "03", "waarde": "overig"}, kop=C.CONTACT['formulier_kop'],
             intro=C.CONTACT['formulier_lead'])}

{vlakkenrij("04", "gegevens", D.NAAM_KORT, gegevens, subtitel="Gegevens")}

  <section class="content-block" id="s05-privacy">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Uw gegevens</span>
            <div class="article-body" style="margin-top:var(--space-500)">
{_p([AVG])}
              <p><a href="privacybeleid.html">Meer over hoe wij met uw gegevens omgaan</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{citaten("06", kop="Wat klanten over J. Boom zeggen")}

{ctablok("07", C.CONTACT['slot_kop'],
         f'Bel {D.TELEFOON_WEERGAVE}. Is er nood aan de man? Dan staan wij zo op de stoep.')}
'''
    (UIT / 'contact.html').write_text(pagina(
        bestand='contact.html',
        titel=f'Neem contact op met {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Bouw- of verbouwplannen? Neem contact op met Aannemersbedrijf J. Boom '
                      'uit Purmerend. Bel 0299 - 43 34 98, mail info@jboom.nl of vul het '
                      'formulier in.'),
        namespace='contact', pagina_css='contact.css', css_naam='contact',
        inhoud=inhoud,
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "ContactPage",
            "name": "Contact",
            "url": BASIS + "/contact.html",
        }, ensure_ascii=False, indent=2),
    ), encoding='utf-8')
    return 'contact.html'


# ---------------------------------------------------------------------- offerte
def offerte():
    k = C.OFFERTE
    stappen = "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{i + 1:02d}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{_t(titel)}</h3>
            <p class="trede__tekst">{_t(tekst)}</p>
            {f'<p class="trede__gedrag"><span>Goed om te weten</span> {_t(detail)}</p>' if detail else ''}
          </div>
        </li>''' for i, (titel, tekst, detail) in enumerate(k['daarna']))

    inhoud = f'''{paginahero("01", "offerte", "Offerte", D.afbreek(_t(k['h1'])), "jboom-aanbouw-15")}

  <section class="content-text-side-cta" id="s02-introductie">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(k['kop'])}</h2>
            <div class="content-text-side-cta--body article-body">
{_p(k['lead'])}
              <p>Liever bellen? Dat kan ook:
                 <a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>.</p>
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop("Onze werkwijze", "werkwijze.html", "secundair")}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s03-helpt">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Voorbereiding</span>
            <h2 class="section-heading">{_t(k['helpt_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{_t(k['helpt_lead'])}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{_icoonpanelen(k['helpt'])}
      </div>
    </div>
  </section>

  <section class="band background--grey" id="s04-formulier">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Offerte</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">Vraag uw offerte aan</h2>
          <p class="article-body">Vul het formulier in en vertel kort wat u wilt bouwen of
             verbouwen. Wij nemen zo snel mogelijk contact met u op.</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Heeft u tekeningen of foto&rsquo;s? Stuur die gerust mee per mail naar
            <a href="mailto:{D.EMAIL}">{D.EMAIL}</a>.
          </p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Liever bellen? <a href="tel:{D.TELEFOON_LINK}">{D.TELEFOON_WEERGAVE}</a>
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <!-- data-projectadres zet het extra adresveld aan: bij een offerte is
               het adres van de woning het eerste dat we willen weten. -->
          <div data-contactformulier data-onderwerp="offerte" data-projectadres></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail uw aanvraag gerust naar
              <a href="mailto:{D.EMAIL}">{D.EMAIL}</a> of bel {D.TELEFOON_WEERGAVE}.</p>
          </noscript>
        </div>
      </div>
    </div>
  </section>

  <section class="band background--white" id="s05-daarna">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Daarna</span>
          <h2 class="section-heading">{_t(k['daarna_kop'])}</h2>
          <p class="article-body" style="margin-top:var(--space-500)">
            Vier stappen, en u zit nergens aan vast tot u de offerte tekent.
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{stappen}
          </ol>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s06-privacy">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Uw gegevens</span>
            <div class="article-body" style="margin-top:var(--space-500)">
{_p([AVG])}
              <p><a href="privacybeleid.html">Meer over hoe wij met uw gegevens omgaan</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{citaten("07", kop="Zo ging het bij anderen")}

{ctablok("08", k['slot_kop'],
         f'Bel {D.TELEFOON_WEERGAVE} en vertel kort wat u van plan bent.')}
'''
    (UIT / 'offerte.html').write_text(pagina(
        bestand='offerte.html',
        titel=f'Offerte aanvragen | {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Vraag vrijblijvend een offerte aan bij Aannemersbedrijf J. Boom uit '
                      'Purmerend voor een aanbouw, verbouwing, dakkapel, nieuwbouw of '
                      'kunststof kozijnen.'),
        namespace='offerte', pagina_css='contact.css', css_naam='contact',
        inhoud=inhoud,
    ), encoding='utf-8')
    return 'offerte.html'


# ------------------------------------------------------------- tekstpagina's
def _tekstpagina(bestand, titel, omschrijving, kop, blokken):
    secties = []
    for i, (subkop, alineas) in enumerate(blokken, start=2):
        kopregel = (f'            <h2 class="font-size--md" style="margin-bottom:var(--space-400)">{subkop}</h2>\n'
                    if subkop else '')
        secties.append(f'''  <section class="content-block" id="s{i:02d}-blok">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
{kopregel}            <div class="article-body">
{_p(alineas)}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>''')
    inhoud = patroonhero('01', 'kop', titel, kop) + "\n\n" + "\n\n".join(secties)
    (UIT / bestand).write_text(pagina(
        bestand=bestand, titel=f'{titel} | {D.NAAM_KORT}', omschrijving=omschrijving,
        namespace='tekst', pagina_css='tekstpagina.css', css_naam='tekstpagina',
        inhoud=inhoud,
    ), encoding='utf-8')
    return bestand


def privacybeleid():
    """Verwijst naar de verklaring die J. Boom zelf heeft gepubliceerd.

       De bronsite linkt in de voet naar een PDF: het privacy- en
       cookiestatement van Aannemersbedrijf J. Boom v.o.f. Dat is de geldende
       verklaring, en die wordt hier niet overgeschreven of samengevat &mdash;
       een samenvatting van een juridisch document dat naast het origineel staat
       levert twee versies op die uit elkaar gaan lopen."""
    return _tekstpagina(
        'privacybeleid.html', 'Privacybeleid',
        'De privacyverklaring van Aannemersbedrijf J. Boom v.o.f. en hoe wij met de '
        'gegevens uit het contactformulier omgaan.',
        'Privacybeleid',
        [(None, ['Aannemersbedrijf J. Boom v.o.f. heeft een privacy- en cookiestatement '
                 'volgens de richtlijnen van het ministerie van Economische Zaken. Dat is '
                 'de geldende verklaring.',
                 f'<a href="{D.PRIVACY_PDF}" rel="noopener">Lees het privacy- en '
                 'cookiestatement (PDF)</a>']),
         ('Het contactformulier op deze site',
          [AVG,
           'Het formulier vraagt om uw naam, e-mailadres en waar het over gaat; een '
           'telefoonnummer, bedrijfsnaam en adres zijn optioneel. Die gegevens gebruiken '
           'wij om uw vraag te beantwoorden of een offerte op te stellen, en voor niets '
           'anders.',
           'Er zit geen tracking van derden in het formulier: de spamcontrole loopt via '
           'een onzichtbaar veld en niet via een dienst van een andere partij.']),
         ('Uw gegevens inzien of laten verwijderen',
          [f'Wilt u weten welke gegevens wij van u hebben, of wilt u ze laten '
           f'verwijderen? Bel {D.TELEFOON_WEERGAVE} of mail naar '
           f'<a href="mailto:{D.EMAIL}">{D.EMAIL}</a>.'])])


def cookies():
    return _tekstpagina(
        'cookies.html', 'Cookies',
        'Welke cookies deze website plaatst en hoe u uw keuze wijzigt.',
        'Cookies',
        [(None, ['Deze website plaatst alleen wat nodig is om hem te laten werken. '
                 'Analytische cookies staan uit tot u ze zelf aanzet via de '
                 'cookiemelding; daarin kunt u uw keuze ook weer wijzigen.']),
         ('Wat er nu staat',
          ['<strong>Functioneel</strong> &mdash; nodig om de site te laten werken. Hieronder '
           'valt de keuze die u in de cookiemelding maakt; die wordt in uw browser '
           'bewaard zodat de melding niet elke keer terugkomt.',
           '<strong>Analytisch</strong> &mdash; om te zien welke pagina&rsquo;s bezocht '
           'worden. Deze staan uit tot u ze aanzet.',
           '<strong>Marketing</strong> &mdash; voor advertenties en het meten daarvan. '
           'Deze zijn op dit moment niet in gebruik.']),
         ('Cookies van anderen',
          ['De lettertypen en de afbeeldingen op deze site staan op onze eigen server, '
           'dus daar gaat geen verzoek voor naar een andere partij. Er staat geen '
           'ingesloten video, kaart of socialemediawidget op deze site.']),
         ('Uw keuze wijzigen',
          ['U kunt uw keuze op elk moment aanpassen via de cookiemelding, en cookies '
           'daarnaast in uw browser verwijderen.',
           f'Vragen hierover? Bel {D.TELEFOON_WEERGAVE} of mail naar '
           f'<a href="mailto:{D.EMAIL}">{D.EMAIL}</a>. In het '
           f'<a href="{D.PRIVACY_PDF}" rel="noopener">privacy- en cookiestatement (PDF)</a> '
           'staat de volledige verklaring.'])])


def main():
    gemaakt = [contact(), offerte(), privacybeleid(), cookies()]
    print(f'{len(gemaakt)} contact- en tekstpagina\'s geschreven')
    return gemaakt


if __name__ == '__main__':
    main()
