# -*- coding: utf-8 -*-
"""Het projectenoverzicht en de twee projectseries.

WAT DE BRON HEEFT
  www.jboom.nl heeft een projectenpagina met twee categorieen, en achter elke
  categorie een fotoserie: 46 foto's bij "Aanbouw, opbouw & verbouw" en 33 bij
  "Dakkapellen, gevels, kozijnen & deuren". Verder niets. Geen opdrachtgever,
  geen plaats, geen jaartal, geen opgave, geen aanpak, geen resultaat.

WAAROM HIER GEEN CASE STUDIES STAAN
  Het template heeft een case-studytemplate met een opgave, een uitdaging, een
  aanpak en een resultaat. Dat is een sterke sectie en hij zou hier goed staan
  — maar alleen als die vier dingen ergens vandaan komen. Ze zijn per project
  niet bekend en ze zijn niet af te leiden uit een foto. Ze verzinnen zou
  betekenen dat er over echt uitgevoerd werk bij echte mensen thuis iets wordt
  beweerd wat J. Boom nooit heeft gezegd.

WAT ER DAN WEL STAAT
  Twee volwaardige seriepagina's in plaats van 79 lege projectpagina's: wat er
  in deze serie te zien is, welke werkzaamheden erachter zitten, de volledige
  fotoserie met een beschrijvende alt-tekst per foto, de referenties die over
  dit soort werk gaan, en de doorstap naar de diensten. De bezoeker weet
  daarmee wat het project was, wat J. Boom deed en wat hij daarna kan doen —
  zonder dat er iets is bijverzonnen.
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


def _galerij(sleutels):
    """De hele fotoserie als raster.

       Elke foto krijgt zijn eigen alt-tekst uit beeldplan.json; het is dus geen
       decoratieve strook maar inhoud die ook zonder beeld te volgen is."""
    items = "\n".join(f'''      <figure class="galerij__item">
        {foto(k, maten="(max-width: 599px) 50vw, (max-width: 991px) 33vw, 25vw")}
      </figure>''' for k in sleutels)
    return f'    <div class="galerij galerij--raster">\n{items}\n    </div>'


def _dienstkaarten(bestanden):
    kaarten = []
    for i, b in enumerate(bestanden):
        rij = next(d for d in ALLE_DIENSTEN if d[0] == b)
        kaarten.append(dienstkaart(i, rij, '', kolom="col-lg-3 col-md-6"))
    return "\n".join(kaarten)


# ---------------------------------------------------------------- overzicht
def _reeksrijen():
    rijen = []
    for i, s in enumerate(D.PROJECTSERIES):
        aantal = len(galerij(s['prefix']))
        diensten = " &middot; ".join(D.dienst_titel(b) for b in s['diensten'])
        rijen.append(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="{s['bestand']}" aria-label="{_plat(s['titel'])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta"><span class="cases-grid__meta-item">{aantal} foto&rsquo;s</span></div>
          <h3 class="cases-grid__title">{D.afbreek(_t(s['titel']))}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{diensten}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(s['hero'], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''')
    return "\n".join(rijen)


def overzicht():
    k = C.PROJECTEN_OVERZICHT
    totaal = sum(len(galerij(s['prefix'])) for s in D.PROJECTSERIES)
    inhoud = f'''{paginahero('01', 'projecten', 'Projecten', D.afbreek(_t(k['h1'])), 'jboom-dakkapel-band')}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row g-0">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">{_t(k['kop'])}</h2>
          <p class="case-lead">{_t(k['lead'])}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            {totaal} foto&rsquo;s, verdeeld over twee series.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-grid" id="s03-reeksen">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">{_t(k['reeksen_kop'])}</h2>
        {knop("Vraag een offerte aan", "offerte.html", "secundair")}
      </div>
      <p class="article-body" style="max-width:var(--content-max-half); margin-bottom:var(--space-600)">{_t(k['reeksen_lead'])}</p>
      <div class="cases-grid__list">
{_reeksrijen()}
      </div>
    </div>
  </section>

{citaten("04", kop="Wat klanten over dit werk schreven")}

{logoslider("05")}

{ctablok("06", k['slot_kop'], k['slot'])}
'''
    (UIT / 'projecten.html').write_text(pagina(
        bestand='projecten.html',
        titel=f'Projecten van {D.NAAM_KORT} uit Purmerend',
        omschrijving=('Bekijk de bouwprojecten die Aannemersbedrijf J. Boom uit Purmerend '
                      'heeft gerealiseerd: aanbouw, opbouw en verbouw, en dakkapellen, '
                      'gevels, kozijnen en deuren.'),
        namespace='projecten', pagina_css='cases.css', css_naam='cases',
        inhoud=inhoud,
    ), encoding='utf-8')
    return 'projecten.html'


# ---------------------------------------------------------------- serie
def serie(s):
    k = C.PROJECTSERIE[s['bestand']]
    sleutels = galerij(s['prefix'])
    nr = [1]

    def volgend():
        nr[0] += 1
        return f'{nr[0]:02d}'

    delen = [paginahero('01', 'project', 'Projecten', D.afbreek(_t(k['h1'])), s['hero'])]

    # 02 de lead van de bronsite, groot gezet
    delen.append(f'''  <section class="band background--white" id="s{volgend()}-lead">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">{_t(k['kop'])}</h2>
        <p class="case-lead">{_t(k['lead'])}</p>
      </div>
    </div>
  </section>''')

    # 03 wat er te zien is
    delen.append(f'''  <section class="band background--grey" id="s{volgend()}-toelichting">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="case-blok__kop">{_t(k['wat_kop'])}</h2>
        <div class="case-blok__body">
{chr(10).join(f"          <p>{_t(a)}</p>" for a in k['wat'])}
        </div>
      </div>
    </div>
  </section>''')

    # 04 de fotoserie
    delen.append(f'''  <section class="content-block" id="s{volgend()}-fotos">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-600)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">{len(sleutels)} foto&rsquo;s</span>
            <h2 class="section-heading">{_t(k['galerij_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{_t(k['galerij_lead'])}</p>
          </div>
        </div>
      </div>
{_galerij(sleutels)}
    </div>
  </section>''')

    # 05 de werkzaamheden achter deze serie
    delen.append(f'''  <section class="content-block" id="s{volgend()}-diensten">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Diensten</span>
            <h2 class="section-heading">{_t(k['diensten_kop'])}</h2>
          </div>
        </div>
      </div>
      <div class="row g-0">
{_dienstkaarten(s['diensten'])}
      </div>
    </div>
  </section>''')

    # 06 referenties die over dit werk gaan
    onderwerpen = [D.dienst_titel(b).split(' en ')[0].lower() for b in s['diensten']]
    passend = [r for r in REFERENTIES
               if any(o.split()[0][:6] in r[1].lower() for o in onderwerpen)]
    delen.append(citaten(volgend(), kop='Wat klanten over dit werk schreven',
                         items=passend or None))

    # 07 de andere serie
    ander = next(a for a in D.PROJECTSERIES if a['bestand'] != s['bestand'])
    delen.append(f'''  <section class="cases-grid" id="s{volgend()}-verwant">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">De andere serie</h2>
        {knop("Alle projecten", "projecten.html", "secundair")}
      </div>
      <div class="cases-grid__list">
      <a class="cases-grid__row cases-grid__row--grey hover--icon"
         href="{ander['bestand']}" aria-label="{_plat(ander['titel'])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta"><span class="cases-grid__meta-item">{len(galerij(ander['prefix']))} foto&rsquo;s</span></div>
          <h3 class="cases-grid__title">{D.afbreek(_t(ander['titel']))}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{" &middot; ".join(D.dienst_titel(b) for b in ander['diensten'])}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(ander['hero'], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>
      </div>
    </div>
  </section>''')

    delen.append(logoslider(volgend()))
    delen.append(ctablok(volgend(), k['slot_kop'], k['slot']))

    (UIT / s['bestand']).write_text(pagina(
        bestand=s['bestand'],
        titel=f"{s['titel']} | {D.NAAM_KORT} uit Purmerend",
        omschrijving=_plat(k['lead'])[:158],
        namespace='project', pagina_css='cases.css', css_naam='cases',
        inhoud="\n\n".join(delen),
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "ImageGallery",
            "name": s['titel'],
            "description": _plat(k['lead']),
            "numberOfItems": len(sleutels),
            "author": {"@type": "GeneralContractor", "name": D.NAAM_VOLUIT},
        }, ensure_ascii=False, indent=2),
    ), encoding='utf-8')
    return s['bestand']


def main():
    gemaakt = [overzicht()] + [serie(s) for s in D.PROJECTSERIES]
    print(f"projecten: overzicht + {len(gemaakt) - 1} seriepagina's")
    return gemaakt


if __name__ == '__main__':
    main()
