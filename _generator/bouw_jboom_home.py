# -*- coding: utf-8 -*-
"""De homepage.

De bronsite heeft op de homepage vijf tekstblokken onder elkaar: de
introductie, "Huur ons in voor", "Bouwadvies", "Strakke planning, snel klaar"
en "Bijna 80 jaar bouwplezier in en rondom Purmerend". Die vijf komen hier
allemaal terug, verdeeld over de secties van dit template, en daaronder staan
de diensten, de projecten en de referenties zodat een bezoeker vanaf de
homepage verder kan.

De hero van het template heeft een film. J. Boom heeft er geen, en er wordt er
ook geen bij gemaakt: de hero staat op het beeld van de twee bedrijfsbussen.
site.js hangt alleen een film in als er een data-herovideo staat, dus zonder
dat attribuut valt die code stil zonder fout.
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
    return "\n".join(f'          <p>{_t(a)}</p>' for a in alineas)


def _projectrijen():
    """De twee fotoseries als brede rij."""
    rijen = []
    for i, s in enumerate(D.PROJECTSERIES):
        aantal = len(galerij(s['prefix']))
        rijen.append(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="{s['bestand']}" aria-label="{_plat(s['titel'])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta"><span class="cases-grid__meta-item">{aantal} foto&rsquo;s</span></div>
          <h3 class="cases-grid__title">{D.afbreek(_t(s['titel']))}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{" &middot; ".join(D.dienst_titel(b) for b in s['diensten'])}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(s['hero'], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''')
    return "\n".join(rijen)


hoofddiensten = "\n".join(dienstkaart(i, d, '') for i, d in enumerate(SERVICES))
werk = []
for _b, _t2, _beeld in D.HOOFDDIENSTEN:
    werk += WERKZAAMHEDEN[_t2]
# Zes kaarten in twee rijen van drie en niet in één rij van vier. Op 1440 is
# een kwartkolom 180px inhoud breed, en dan breekt "Dakopbouw en dakkapel" af
# tot "Dakop-bouw en dak-kapel". Op een derde is dat 264px en past het.
werkkaarten = "\n".join(dienstkaart(i, d, '', kolom="col-lg-4 col-md-6")
                        for i, d in enumerate(werk + LOSSE_DIENSTEN))

inhoud = f'''  <!-- ================= 01 INTRODUCTIE =================
       Twee lagen beeld. Onderop de foto van de twee bedrijfsbussen op het
       terrein aan de Pascalstraat: dat is J. Boom zelf, en dat is wat je ziet
       zolang de film niet speelt. Daarover vervaagt de aangeleverde film.

       De film is stockmateriaal en geen opname van J. Boom: een grijze bus, een
       monteur die een kozijn stelt, een woning met een dakkapel. Het werk in
       beeld is wat J. Boom doet, de bus en de monteur zijn niet van hen. Daarom
       is het beeld decoratief (aria-hidden, alt="") en draagt de film geen
       enkele bewering; wat de hero beweert staat in de kop en de lead.

       site.js hangt de film pas in als dat mag: niet bij prefers-reduced-motion,
       niet bij databesparing en niet op een 2g-lijn, en zonder JavaScript
       gebeurt er niets. Vandaar geen src en geen poster hier -- de foto eronder
       is de terugval. Zie ook _generator/maak_herovideo.py. -->
  <section class="hero" id="s01-introductie" data-header-theme="light">
    <div class="hero--beeld" aria-hidden="true">
      {foto("jboom-bedrijfsbussen", laden="eager", maten="100vw", alt="")}
      <video class="hero--video" data-herovideo="assets/video/jboom-hero-1280.mp4"
             muted loop playsinline preload="none" tabindex="-1"></video>
    </div>
    <div class="container hero--container">
      <div class="hero--content">
        <span class="subtitle" style="color:var(--color-white)">{_t(C.HOME['eyebrow'])}</span>
        <h1 class="hero--title">{D.afbreek(_t(C.HOME['h1']))}</h1>
        <div class="hero--intro article-body">
{_p(C.HOME['lead'])}
        </div>
        <div class="hero--actions">
          {knop(*C.HOME['cta_primair'])}
          {knop(*C.HOME['cta_secundair'], "secondary")}
        </div>
      </div>
    </div>
  </section>

{logoslider("02")}

  <!-- ================= 03 WAT J. BOOM DOET ================= -->
  <section class="content-text-side-cta" id="s03-wat-we-doen">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(C.HOME['statement_kop'])}</h2>
            <div class="content-text-side-cta--body article-body">
{_p(C.HOME['statement'])}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop(*C.HOME['statement_cta'])}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 04 DIENSTEN ================= -->
  <section class="content-block" id="s04-diensten">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Diensten</span>
            <h2 class="section-heading">{_t(C.HOME['werkzaamheden_kop'])}</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              {_t(C.HOME['werkzaamheden_lead'])}
            </p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{hoofddiensten}
      </div>
      <div class="content-block--container background--white"
           style="padding-top:var(--space-700); padding-bottom:var(--space-600)">
        <div class="row g-0">
          <div class="col-md-8 col-12">
            <h3 class="font-size--md">{_t(C.HOME['losse_kop'])}</h3>
            <p class="article-body" style="margin-top:var(--space-400); max-width:var(--content-max-half)">
              {_t(C.HOME['losse_lead'])}
            </p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{werkkaarten}
      </div>
    </div>
  </section>

  <!-- ================= 05 REFERENTIES ================= -->
{citaten("05")}

  <!-- ================= 06 PROJECTEN ================= -->
  <section class="cases-grid" id="s06-projecten">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">{_t(C.HOME['projecten_kop'])}</h2>
        {knop(*C.HOME['projecten_cta'], "secundair")}
      </div>
      <div class="cases-grid__list">
{_projectrijen()}
      </div>
    </div>
  </section>

  <!-- ================= 07 PLANNING =================
       Het blok "Strakke planning, snel klaar" van de bronsite, met het beeld
       van de aanbouw in uitvoering ernaast. -->
  <section class="content-text-side-visual" id="s07-planning">
    <div class="container">
      <div class="content-text-side-visual--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-6 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Planning</span>
            <h2 class="section-heading" style="margin-bottom:var(--space-500)">{_t(C.HOME['planning_kop'])}</h2>
            <div class="content-text-side-visual--body article-body">
{_p(C.HOME['planning'])}
            </div>
            <div style="margin-top:var(--space-600)">
              {knop("Zo werken wij", "werkwijze.html", "secundair")}
            </div>
          </div>
          <div class="col-lg-6 col-12">
            <figure class="content-text-side-visual--beeld">
              {foto("jboom-aanbouw-in-uitvoering", maten="(max-width: 991px) 100vw, 50vw")}
            </figure>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 08 OVER ONS ================= -->
  <section class="content-block" id="s08-over-ons">
    <div class="container">
      <div class="content-block--container background--white">
        <div class="row g-0">
          <div class="col-lg-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Over ons</span>
            <h2 class="section-heading">{_t(C.HOME['over_kop'])}</h2>
            <div class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
{_p(C.HOME['over'])}
            </div>
            <div style="margin-top:var(--space-600)">
              {knop(*C.HOME['over_cta'], "secundair")}
            </div>
          </div>
        </div>
      </div>
      <figure class="archieffoto">
        {foto("jboom-historie", maten="(max-width: 467px) calc(100vw - 32px), 436px")}
        <figcaption>Uit het familiearchief. Het bedrijf begon in 1935 en is sindsdien
          in de familie gebleven.</figcaption>
      </figure>
    </div>
  </section>

  <!-- ================= 09 DOORSTAP ================= -->
  <section class="content-block" id="s09-verder">
    <div class="container">
      <div class="row g-0">
{beeldkaart("Onze werkwijze", "Hoe een opdracht bij ons verloopt, van orientatiegesprek tot oplevering.",
            'jboom-aanbouw-16', alt="", kleur="grey", href="werkwijze.html")}
{beeldkaart("Klanten over J. Boom", f"{len(D.REFERENTIES)} referenties, ondertekend en met datum.",
            'jboom-dakkapel-05', alt="", kleur="white", href="referenties.html")}
      </div>
    </div>
  </section>

{ctablok("10", C.HOME['slot_kop'], C.HOME['slot'])}
'''

(UIT / 'index.html').write_text(pagina(
    bestand='index.html',
    titel='Bouwen of verbouwen? Aannemersbedrijf J. Boom uit Purmerend',
    omschrijving=('Bouw en verbouwing door aannemer J. Boom uit Purmerend: van dakkapel '
                  'tot aanbouw of kunststof kozijn, inclusief bouwadvies en technische '
                  'tekeningen. Bel 0299 - 43 34 98 of mail info@jboom.nl.'),
    namespace='home',
    pagina_css='index.css',
    css_naam='index',
    inhoud=inhoud,
    scripts=('index.js',),
    extra_ld=json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": D.NAAM_KORT,
        "url": BASIS + "/",
        "inLanguage": "nl-NL",
    }, ensure_ascii=False, indent=2),
), encoding='utf-8')
print('index.html geschreven')
