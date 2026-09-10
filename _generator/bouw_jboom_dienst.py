# -*- coding: utf-8 -*-
"""Het dienstenoverzicht en de negen dienstpagina's.

Eén skelet voor alle negen, met de secties die het template daarvoor heeft. De
volgorde volgt wat een bezoeker nodig heeft:

  01 hero               waar ben ik
  02 statement          waar gaat dit over, met de eerste CTA
  03 wanneer            herken ik mijn situatie hierin
  04 uitleg             hoe zit het in elkaar    <- de tekst van www.jboom.nl
  05 aanpak             hoe verloopt het traject
  06 input              wat moet ik zelf aanleveren
  07 oplevering         wat heb ik aan het eind in handen
  08 voordelen          waarom bij J. Boom
  09 werkzaamheden      (alleen op een hoofddienst) wat valt hieronder
  10 projectbewijs      foto's van dit soort werk, met een link naar de serie
  11 vragen             wat mensen meestal nog willen weten
  12 partners           met wie we samenwerken
  13 slot               CTA

De brontekst van www.jboom.nl staat in `inhoud_jboom.BRONTEKST` en komt
onveranderd in het uitlegblok terecht. De rest van de tekst staat in
`inhoud_dienst_verhaal.py`; bovenin dat bestand staat waar die vakinhoud op
gebaseerd is en wat er bewust niet in staat.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *          # noqa: F401,F403
from schil import _plat
import inhoud_jboom as D
import inhoud_dienst_verhaal as V
import inhoud_copy as C

UIT = pathlib.Path(__file__).resolve().parent.parent

ICONEN = {
    "vinkje": '<path d="M9.6 16.2 5.4 12l-1.4 1.4 5.6 5.6L20.4 8.2 19 6.8 9.6 16.2Z"/>',
    "schild": '<path d="M12 2 4 5v6.5c0 4.6 3.2 8.4 8 10.5 4.8-2.1 8-5.9 8-10.5V5l-8-3Zm0 2.2 6 2.2v5.1c0 3.5-2.3 6.5-6 8.3-3.7-1.8-6-4.8-6-8.3V6.4l6-2.2Z"/>',
    "lijst": '<path d="M3 5h4v4H3V5Zm6 1h12v2H9V6ZM3 10h4v4H3v-4Zm6 1h12v2H9v-2ZM3 15h4v4H3v-4Zm6 1h12v2H9v-2Z"/>',
    "trap": '<path d="M3 21v-4h5v-4h5V9h5V5h3v18H3Zm2-2h14V7h-1v4h-5v4H8v4H5v0Z"/>',
    "klok": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm0 2a8 8 0 1 1 0 16 8 8 0 0 1 0-16Zm-1 3v6l5 3 1-1.7-4-2.3V7h-2Z"/>',
    "mensen": '<path d="M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm0-6a2 2 0 1 1 0 4 2 2 0 0 1 0-4Zm7 6a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM2 21v-2c0-2.8 3.1-4 7-4s7 1.2 7 4v2H2Zm2-2h10c0-1.2-1.9-2-5-2s-5 .8-5 2Zm14 2v-2c0-1.2-.4-2.2-1.1-3 3 .3 5.1 1.5 5.1 3v2h-4Z"/>',
    "grafiek": '<path d="M3 21V3h2v16h16v2H3Zm4-4V9h3v8H7Zm5 0V5h3v12h-3Zm5 0v-6h3v6h-3Z"/>',
    "document": '<path d="M6 2h8l6 6v14H6V2Zm2 2v16h10V9h-5V4H8Zm7 .4V7h2.6L15 4.4ZM9 12h8v2H9v-2Zm0 4h8v2H9v-2Z"/>',
    # Vier iconen erbij voor deze site: een woning, een maatvoering, daglicht en
    # isolatie. Zelfde tekenstijl als hierboven: één pad, 24 bij 24, gevuld.
    "huis": '<path d="M12 3 2 11h3v10h6v-6h2v6h6V11h3L12 3Zm0 2.6 6 4.8V19h-2v-6H8v6H6v-8.6l6-4.8Z"/>',
    "liniaal": '<path d="M2 8h20v8H2V8Zm2 2v4h16v-4h-2v2h-2v-2h-2v3h-2v-3h-2v2H8v-2H6v2H4v-2Z"/>',
    "zon": '<path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 2a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm-1-8h2v3h-2V1Zm0 19h2v3h-2v-3ZM1 11h3v2H1v-2Zm19 0h3v2h-3v-2ZM4.2 2.8l2.1 2.1-1.4 1.4-2.1-2.1 1.4-1.4Zm13.5 13.5 2.1 2.1-1.4 1.4-2.1-2.1 1.4-1.4Zm2.1-13.5 1.4 1.4-2.1 2.1-1.4-1.4 2.1-2.1ZM6.3 17.7l1.4 1.4-2.1 2.1-1.4-1.4 2.1-2.1Z"/>',
    "blad": '<path d="M20 3c0 9-5.2 14-11 14a6 6 0 0 1-2.5-.5C5 19 4.4 20.6 4 22H2c.5-2.3 1.4-4.6 3.3-7.2C4.5 13.6 4 12 4 10c0-4 3-7 8-7h8Zm-2.2 2H12c-3.9 0-6 2.1-6 5 0 1.1.2 2 .6 2.8C9 9.6 12.3 7.6 16 6.6c-3.4 1.7-6.2 4.2-8.3 8.2.5.1 1 .2 1.3.2 4.4 0 8.4-3.6 8.8-10Z"/>',
}


def icoon(naam):
    return (f'<svg class="voordeel__icoon" width="24" height="24" viewBox="0 0 24 24" '
            f'aria-hidden="true">{ICONEN[naam]}</svg>')


def _t(x):
    return D._tekens(x)


# ------------------------------------------------------------------ onderdelen
def _situatiekaarten(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">Situatie {i + 1:02d}</span>
            <h3 class="panel__title">{_t(titel)}</h3>
            <p class="panel__body">{_t(tekst)}</p>
          </div>
        </div>''' for i, (titel, tekst) in enumerate(items))


def _trap(items):
    return "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{i + 1:02d}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{_t(titel)}</h3>
            <p class="trede__tekst">{_t(tekst)}</p>
            {f'<p class="trede__gedrag"><span>Goed om te weten</span> {_t(detail)}</p>' if detail else ''}
          </div>
        </li>''' for i, (titel, tekst, detail) in enumerate(items))


def _icoonpanelen(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            {icoon(ico)}
            <h3 class="voordeel__titel">{_t(titel)}</h3>
            <p class="panel__body">{_t(tekst)}</p>
          </div>
        </div>''' for i, (ico, titel, tekst) in enumerate(items))


def _paneelblok(nr, ident, label, kop, items, lead=None, kolommen=4):
    """Kop met daaronder een rij panelen met een icoon erin."""
    leadregel = (f'            <p class="article-body" style="margin-top:var(--space-500); '
                 f'max-width:var(--content-max-half)">{_t(lead)}</p>\n' if lead else '')
    return f'''  <section class="content-block" id="s{nr}-{ident}">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{label}</span>
            <h2 class="section-heading">{_t(kop)}</h2>
{leadregel}          </div>
        </div>
      </div>
      <div class="panel-row panel-row--{kolommen}">
{_icoonpanelen(items)}
      </div>
    </div>
  </section>'''


def _uitleg(nr, alineas, kop, label='Hoe het werkt'):
    """Het uitlegblok: de tekst van www.jboom.nl plus de vakinhoudelijke uitleg."""
    tekst = "\n".join(f'              <p>{_t(a)}</p>' for a in D.splits_lang(alineas))
    return f'''  <section class="content-block" id="s{nr}-uitleg">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{label}</span>
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(kop)}</h2>
            <div class="article-body">
{tekst}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>'''


def _fotoserie(nr, dienstbestand):
    """Vier foto's van dit soort werk, met een link naar de hele serie.

       Welke serie erbij hoort staat in inhoud_jboom.PROJECTSERIES; een dienst
       die in geen enkele serie voorkomt krijgt dit blok niet."""
    reeks = next((s for s in D.PROJECTSERIES if dienstbestand in s['diensten']), None)
    if not reeks:
        return ''
    sleutels = galerij(reeks['prefix'])
    # Vier foto's die verder nergens op deze pagina staan: niet de hero, en niet
    # de eerste van de serie, want die staat op de projectpagina bovenaan.
    hero = D.dienst_beeld(dienstbestand)
    keuze = [k for k in sleutels if k != hero][:8][::2][:4]
    kaarten = "\n".join(f'''        <figure class="galerij__item">
          {foto(k, maten="(max-width: 767px) 50vw, 25vw")}
        </figure>''' for k in keuze)
    return f'''  <section class="content-block" id="s{nr}-projectbewijs">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-600)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Uit de praktijk</span>
            <h2 class="section-heading">{_t(reeks['titel'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              Vier beelden uit de serie van {len(sleutels)} foto&rsquo;s die J. Boom van dit
              soort werk publiceerde.
            </p>
            <div style="margin-top:var(--space-600)">
              {knop("Bekijk de hele serie", reeks['bestand'], "secundair")}
            </div>
          </div>
        </div>
      </div>
      <div class="galerij galerij--4">
{kaarten}
      </div>
    </div>
  </section>'''


# ------------------------------------------------------------------- de pagina
def dienstpagina(bestand):
    titel = D.dienst_titel(bestand)
    v = V.verhaal(bestand)
    k = C.dienst(bestand)
    nr = [1]

    def volgend():
        nr[0] += 1
        return f'{nr[0]:02d}'

    label = D.ouder(bestand) or 'Diensten'
    delen = [paginahero('01', 'introductie', label, D.afbreek(_t(titel)),
                        D.dienst_beeld(bestand))]

    # 02 statement met de eerste CTA
    delen.append(f'''  <section class="content-text-side-cta" id="s{volgend()}-statement">
    <div class="container">
      <div class="content-text-side-cta--container">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body article-body">
{chr(10).join(f"              <p>{_t(a)}</p>" for a in k['lead'])}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop(*k['cta'])}
          </div>
        </div>
      </div>
    </div>
  </section>''')

    # 03 wanneer is dit iets voor u
    delen.append(f'''  <section class="content-block" id="s{volgend()}-wanneer">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Herkenbaar?</span>
            <h2 class="section-heading">{_t(v['wanneer_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{_t(v['wanneer_intro'])}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{_situatiekaarten(v['situaties'])}
      </div>
    </div>
  </section>''')

    # 04 uitleg: de tekst van www.jboom.nl eerst, dan de vakinhoudelijke uitleg
    delen.append(_uitleg(volgend(), D.BRONTEKST[bestand] + v['uitleg_extra'],
                         C.UITLEG_KOP[bestand]))

    # 05 aanpak
    delen.append(f'''  <section class="band background--grey" id="s{volgend()}-aanpak">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Aanpak</span>
          <h2 class="section-heading">{_t(v['stappen_kop'])}</h2>
          <p class="article-body" style="margin-top:var(--space-500)">{_t(v['stappen_intro'])}</p>
          <div style="margin-top:var(--space-600)">
            {knop("Onze werkwijze", "werkwijze.html", "secundair")}
          </div>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{_trap(v['stappen'])}
          </ol>
        </div>
      </div>
    </div>
  </section>''')

    # 06 wat de klant aanlevert
    delen.append(_paneelblok(volgend(), 'input', 'Wat u aanlevert',
                             v['input_kop'], v['input'], v['input_intro']))

    # 07 wat de klant krijgt
    delen.append(_paneelblok(volgend(), 'oplevering', 'Oplevering',
                             v['oplevering_kop'], v['oplevering']))

    # 08 voordelen
    delen.append(_paneelblok(volgend(), 'voordelen', 'Waarom J. Boom',
                             v['voordelen_kop'], v['voordelen']))

    # 09 de werkzaamheden onder een hoofddienst
    if D.is_hoofddienst(bestand) and WERKZAAMHEDEN.get(titel):
        kaarten = "\n".join(dienstkaart(i, d, '')
                            for i, d in enumerate(WERKZAAMHEDEN[titel]))
        delen.append(f'''  <section class="content-block" id="s{volgend()}-werkzaamheden">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Werkzaamheden</span>
            <h2 class="section-heading">Wat er bij {D.afbreek(_t(titel.lower()))} komt kijken</h2>
          </div>
        </div>
      </div>
      <div class="row g-0">
{kaarten}
      </div>
    </div>
  </section>''')

    # 10 projectbewijs
    bewijs = _fotoserie(volgend(), bestand)
    if bewijs:
        delen.append(bewijs)
    else:
        nr[0] -= 1

    # 11 vragen
    faq_items = [(vr, [_t(a) for a in D.splits_lang([aw])]) for vr, aw in v['faq']]
    delen.append(faq_blok(volgend(), faq_items, 'Wat mensen meestal nog vragen'))
    faq_ld_blok = faq_ld(faq_items)

    # 12 partners en 13 slot
    delen.append(logoslider(volgend()))
    delen.append(ctablok(volgend(), k['slot_kop']))

    extra = json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": titel,
        "name": titel,
        "description": _plat(k['lead'][0]),
        "areaServed": {"@type": "City", "name": D.PLAATS},
        "provider": {"@type": "GeneralContractor", "name": D.NAAM_VOLUIT},
    }, ensure_ascii=False, indent=2)
    extra += "\n</script>\n<script type=\"application/ld+json\">\n" + faq_ld_blok

    (UIT / bestand).write_text(pagina(
        bestand=bestand,
        titel=f'{titel} in Purmerend | {D.NAAM_KORT}',
        omschrijving=_plat(k['lead'][0])[:158],
        namespace='dienst', pagina_css='service.css', css_naam='service',
        inhoud="\n\n".join(delen), extra_ld=extra,
    ), encoding='utf-8')
    return bestand


# ---------------------------------------------------------------- overzicht
def _keuzekaarten(items):
    """De drie vragen waarmee mensen bellen, elk met een link naar de dienst.

       Elk paneel zit in een eigen <div>, net als bij de andere panelenrijen in
       dit template. Dat is geen opsmuk: .panel-row--3 > * geeft de kolom zijn
       breedte en .panel zet daarbinnen width:100%. Beide selectors wegen even
       zwaar, dus zonder die div wint .panel en staan de drie kaarten onder
       elkaar op volle breedte."""
    return "\n".join(f'''        <div>
          <a class="panel panel--{'grey' if i % 2 == 0 else 'wit'} panel--link hover--icon" href="{bestand}">
            <span class="panel__meta">Vraag {i + 1:02d}</span>
            <h3 class="panel__title">{vraag}</h3>
            <p class="panel__body">{antwoord}</p>
            <span class="panel__voet">{D.dienst_titel(bestand)} {icoonknop("", "button--secundair")}</span>
          </a>
        </div>''' for i, (vraag, antwoord, bestand) in enumerate(items))


def _partnerlijst():
    regels = []
    for naam, rol, url in D.PARTNERS:
        merk = (f'<a href="{url}" rel="noopener">{naam}</a>' if url else naam)
        regels.append(f'                <li><strong>{merk}</strong><br>{rol}</li>')
    return "\n".join(regels)


def overzicht():
    k = C.DIENSTEN_OVERZICHT
    hoofd = "\n".join(dienstkaart(i, d, '') for i, d in enumerate(SERVICES))
    werk = []
    for _, t, _ in D.HOOFDDIENSTEN:
        werk += WERKZAAMHEDEN[t]
    werkkaarten = "\n".join(dienstkaart(i, d, '', kolom="col-lg-4")
                            for i, d in enumerate(werk))
    los = "\n".join(dienstkaart(i, d, '', kolom="col-lg-6")
                    for i, d in enumerate(LOSSE_DIENSTEN))

    inhoud = f'''{paginahero('01', 'diensten', 'Diensten', D.afbreek(_t(k['h1'])), 'jboom-dakopbouw-woning')}

  <section class="content-text-side-cta" id="s02-statement">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(k['lead_kop'])}</h2>
            <div class="content-text-side-cta--body article-body">
{chr(10).join(f"              <p>{_t(a)}</p>" for a in k['lead'])}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop(*k['lead_cta'])}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s03-kiezen">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Waar begint u?</span>
            <h2 class="section-heading">{_t(k['kies_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{_t(k['kies_lead'])}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{_keuzekaarten(k['kies'])}
      </div>
    </div>
  </section>

  <section class="content-block" id="s04-diensten">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Diensten</span>
            <h2 class="section-heading">{_t(k['hoofd_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{_t(k['hoofd_lead'])}</p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{hoofd}
      </div>
      <div class="content-block--container background--white"
           style="padding-top:var(--space-700); padding-bottom:var(--space-600)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <h3 class="font-size--md">Werkzaamheden die daaronder vallen</h3>
          </div>
        </div>
      </div>
      <div class="row g-0">
{werkkaarten}
      </div>
      <div class="content-block--container background--white"
           style="padding-top:var(--space-700); padding-bottom:var(--space-600)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <h3 class="font-size--md">{_t(k['losse_kop'])}</h3>
            <p class="article-body" style="margin-top:var(--space-400); max-width:var(--content-max-half)">{_t(k['losse_lead'])}</p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{los}
      </div>
    </div>
  </section>

{citaten("05", kop="Wat klanten over J. Boom zeggen")}

  <section class="content-block" id="s06-samenwerking">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Samenwerking</span>
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(k['samen_kop'])}</h2>
            <div class="article-body">
{chr(10).join(f"              <p>{_t(a)}</p>" for a in k['samen'])}
              <h3 class="font-size--md" style="margin-top:var(--space-600)">{_t(k['samen_lijst_kop'])}</h3>
              <ul class="case-lijst" role="list">
{_partnerlijst()}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{logoslider("07")}

{ctablok("08", k['slot_kop'], k['slot'])}
'''
    (UIT / 'diensten.html').write_text(pagina(
        bestand='diensten.html',
        titel=f'Diensten van {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Aannemersbedrijf J. Boom is gespecialiseerd in aanbouw, verbouw, '
                      'dakkapellen, dakopbouw en kunststof kozijnen, en is in te huren '
                      'voor nieuwbouw, renovatie, gevelbekleding en bouwadvies.'),
        namespace='diensten', pagina_css='service.css', css_naam='service',
        inhoud=inhoud,
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Diensten van Aannemersbedrijf J. Boom",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": t,
                 "url": f"{BASIS}/{b}"}
                for i, (b, t, _, _) in enumerate(ALLE_DIENSTEN)],
        }, ensure_ascii=False, indent=2),
    ), encoding='utf-8')
    return 'diensten.html'


def main():
    gemaakt = [overzicht()] + [dienstpagina(b) for b, _, _, _ in ALLE_DIENSTEN]
    print(f"diensten: overzicht + {len(gemaakt) - 1} dienstpagina's")
    return gemaakt


if __name__ == '__main__':
    main()
