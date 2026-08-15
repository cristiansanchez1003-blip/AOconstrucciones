# -*- coding: utf-8 -*-
"""
Genera las landings por comuna como HTML estatico.

Lee las obras reales y su ubicacion desde portafolio.html, para que las fotos y
los sectores que aparecen en cada landing sean los que de verdad se ejecutaron
ahi. Nada se arma con JavaScript: Google recibe el contenido completo en el HTML.

Uso:  python generar-landings.py
"""
import re, os, collections, unicodedata, urllib.parse, html, json

ROOT = 'C:/Users/cristian1/Desktop/AOconstrucciones'
PORT_DIR = 'Portafolio AOconstrucciones'
SITE = 'https://aoconstrucciones.cl'

# ---------- 1. Leer las obras reales del portafolio ----------
src = open(os.path.join(ROOT, 'portafolio.html'), encoding='utf-8').read()
locs = dict(re.findall(r'"([^"]+)":\s*"([^"]+)"',
                       re.search(r'const projectLocations = \{(.*?)\};', src, re.S).group(1)))
files = [f for f in re.findall(r'"([^"]+\.webp)"', src) if '/' not in f]


def strip_accents(s):
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', strip_accents(s).lower()).strip('-')


def base_name(f):
    b = re.sub(r'\.[^.]+$', '', f)
    b = re.sub(r'\s+', ' ', b).strip()
    b = re.sub(r'\s+resultado\s+final$', '', b, flags=re.I)
    return re.sub(r'\s+\d+$', '', b).strip()


def humanize(b):
    t = b[0].upper() + b[1:]
    for pat, rep in [(r'\bremodelacion\b', 'Remodelación'), (r'\bRemodelacion\b', 'Remodelación'),
                     (r'\bconstruccion\b', 'Construcción'), (r'\bConstruccion\b', 'Construcción'),
                     (r'\breparacion\b', 'Reparación'), (r'\bReparacion\b', 'Reparación'),
                     (r'\bporton\b', 'Portón'), (r'\barbol\b', 'árbol'),
                     (r'^2da\b', 'Segunda'), (r'^3ra\b', 'Tercera'), (r'^4ta\b', 'Cuarta')]:
        t = re.sub(pat, rep, t)
    return t.strip()


groups = collections.defaultdict(list)
for f in files:
    groups[slug(base_name(f))].append(f)

obras = []
for pid, fs in groups.items():
    loc = locs.get(pid)
    if not loc:
        continue
    portada = next((x for x in fs if re.search(r'\sresultado\s+final\.', x, re.I)), fs[0])
    sector, _, com = loc.partition(',')
    obras.append({
        'id': pid,
        'titulo': humanize(base_name(fs[0])),
        'sector': sector.strip(),
        'comuna': (com.strip() or sector.strip()),
        'portada': f'{PORT_DIR}/{portada}',
        'fotos': len(fs),
    })

por_comuna = collections.defaultdict(list)
for o in obras:
    por_comuna[o['comuna']].append(o)

# ---------- 2. Definicion de cada landing ----------
COMUNAS = [
    {
        'slug': 'san-jose-de-maipo',
        'nombre': 'San José de Maipo',
        'titulo': 'Constructora en San José de Maipo y Cajón del Maipo',
        'hero': 'construccion-deck',
        'intro': '15 años construyendo en el Cajón del Maipo.',
        'contexto': 'Construir en cordillera no es lo mismo que construir en Santiago. '
                    'Es la zona donde más hemos trabajado.',
        'faq': [
            ('¿Trabajan en todo el Cajón del Maipo?',
             'Sí. Tenemos obras ejecutadas en Las Vertientes, El Manzano, El Canelo, Melocotón y '
             'San Gabriel. Puedes verlas todas en nuestro portafolio.'),
            ('¿Cómo se hace el presupuesto?',
             'Andrés, dueño de la empresa, va en persona a ver el proyecto. No damos precios por '
             'teléfono ni por metro cuadrado: cada obra depende del terreno, del acceso y de lo '
             'que quieras lograr. La visita no tiene costo.'),
            ('¿Qué tipo de obras hacen en la zona?',
             'Construcción desde cota cero, ampliaciones, remodelaciones interiores, techumbres, '
             'terrazas, decks y quinchos. En el portafolio están todas con fotos del proceso.'),
        ],
    },
    {
        'slug': 'puente-alto',
        'nombre': 'Puente Alto',
        'titulo': 'Constructora en Puente Alto',
        'hero': 'construccion-deck',
        'intro': 'Ampliaciones, remodelaciones y obra nueva en Puente Alto.',
        'contexto': 'Trabajamos en condominios y sectores con reglamento, coordinando la faena '
                    'con la administración.',
        'faq': [
            ('¿Trabajan en condominios?',
             'Sí. Tenemos obras ejecutadas en Hacienda El Peñón y en el Condominio La Vizcachas. '
             'Estamos acostumbrados a coordinar la faena con la administración.'),
            ('¿Cómo se hace el presupuesto?',
             'Andrés, dueño de la empresa, va en persona a ver el proyecto. No damos precios por '
             'teléfono: cada obra depende de lo que haya en terreno. La visita no tiene costo.'),
            ('¿Qué tipo de obras hacen en Puente Alto?',
             'Remodelaciones interiores, cocinas, techumbres, quinchos y escaleras, entre otras. '
             'Las obras de la comuna están en el portafolio con fotos del resultado.'),
        ],
    },
    {
        'slug': 'la-florida',
        'nombre': 'La Florida',
        'titulo': 'Constructora en La Florida',
        'hero': 'construccion-deck',
        'intro': 'Remodelaciones, techumbres y ampliaciones en La Florida.',
        'contexto': 'Viviendas con años que piden renovarse: techumbres cumplidas e interiores '
                    'que ya no acomodan.',
        'faq': [
            ('¿Reparan o cambian techumbres?',
             'Sí. Vamos a ver el estado en terreno y te decimos si conviene intervenir solo el '
             'sector afectado o renovar la techumbre completa.'),
            ('¿Cómo se hace el presupuesto?',
             'Andrés, dueño de la empresa, va en persona a ver el proyecto. No damos precios por '
             'teléfono: cada obra depende de lo que haya en terreno. La visita no tiene costo.'),
            ('¿Qué tipo de obras hacen en La Florida?',
             'Remodelaciones interiores y trabajos de techumbre, entre otros. Puedes ver las '
             'obras de la comuna en el portafolio.'),
        ],
    },
]

SERVICIOS = [
    ('Cota Cero', 'i-building',
     'Obra nueva completa: fundaciones, estructura y terminaciones hasta la entrega llave en mano.'),
    ('Ampliaciones', 'i-expand',
     'Más metros cuadrados sin romper el diseño original de tu casa, cuidando luz y aislación.'),
    ('Remodelaciones', 'i-paint-roller',
     'Cocinas, baños, terrazas e interiores renovados con materiales nobles y buena terminación.'),
]

SPRITE_IDS = ['i-arrow-right', 'i-arrow-left', 'i-phone', 'i-location-dot', 'i-clock',
              'i-circle-check', 'i-shield-halved', 'i-building', 'i-expand', 'i-paint-roller',
              'i-ellipsis', 'i-paper-plane', 'i-whatsapp', 'i-envelope']

# Reutilizamos el sprite ya definido en index.html para no duplicar los trazos.
idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
sprite_full = re.search(r'(<svg class="icon-sprite".*?</svg>)', idx, re.S).group(1)
symbols = dict(re.findall(r'(<symbol id="(i-[a-z-]+)".*?</symbol>)', sprite_full, re.S))
sprite = ('  <svg class="icon-sprite" aria-hidden="true" focusable="false"><defs>\n'
          + '\n'.join('    ' + s for s, n in
                      sorted(((s, n) for s, n in symbols.items() if n in SPRITE_IDS), key=lambda x: x[1]))
          + '\n  </defs></svg>')

WA = ('https://wa.me/56979925812?text=Hola%2C%20vi%20su%20sitio%20web%20y%20'
      'quiero%20cotizar%20un%20proyecto')


def icon(name):
    return f'<svg class="icon" aria-hidden="true" focusable="false"><use href="#{name}"></use></svg>'


def img_url(path):
    return urllib.parse.quote(path)


def e(s):
    return html.escape(s, quote=False)


# ---------- 3. Plantilla ----------
def build(c):
    obras_c = sorted(por_comuna.get(c['nombre'], []), key=lambda o: -o['fotos'])
    sectores = sorted({o['sector'] for o in obras_c if o['sector'] != c['nombre']})
    url = f"{SITE}/constructora-{c['slug']}.html"

    # La obra del hero se elige a mano y puede ser de otra comuna: es la foto
    # que mejor representa el trabajo, no necesariamente la local.
    hero_obra = next((o for o in obras if o['id'] == c.get('hero')), obras_c[0])
    resto = [o for o in obras_c if o['id'] != hero_obra['id']]

    # Si el hero es de otra comuna hay que decirlo, o parecería obra de esta.
    hero_es_local = hero_obra['comuna'] == c['nombre']
    hero_lugar = hero_obra['sector'] if hero_es_local else \
        f"{hero_obra['sector']}, {hero_obra['comuna']}"

    tarjetas = '\n'.join(f'''          <article class="local-work" role="listitem">
            <img src="{img_url(o['portada'])}" alt="{e(o['titulo'])} ejecutada por AO Construcciones en {e(o['sector'])}, {e(c['nombre'])}" loading="lazy" width="1080" height="810">
            <figcaption class="local-work__caption">
              <span class="local-work__place">{icon('i-location-dot')} {e(o['sector'])}</span>
              <h3>{e(o['titulo'])}</h3>
            </figcaption>
          </article>''' for o in resto)

    servicios = '\n'.join(f'''          <article class="local-service">
            <span class="local-service__icon">{icon(ic)}</span>
            <h3>{e(nom)}</h3>
            <p>{e(desc)}</p>
          </article>''' for nom, ic, desc in SERVICIOS)

    faqs = '\n'.join(f'''          <details class="faq-item">
            <summary>{e(q)}</summary>
            <p>{e(a)}</p>
          </details>''' for q, a in c['faq'])

    sectores_txt = ''
    if sectores:
        chips = ''.join(f'<li>{e(s)}</li>' for s in sectores)
        sectores_txt = (f'<div class="container"><ul class="local-sectors" '
                        f'aria-label="Sectores donde hemos trabajado">{chips}</ul></div>')

    ld = {
        "@context": "https://schema.org",
        "@type": "GeneralContractor",
        "name": "AO Construcciones",
        "description": f"Constructora en {c['nombre']}: ampliaciones, remodelaciones y "
                       f"construcción desde cota cero.",
        "telephone": "+56979925812",
        "email": "construyeao@gmail.com",
        "url": url,
        "image": f"{SITE}/assets/img/ao-construcciones-logo-portfolio-transparent.webp",
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "San José de Maipo",
                    "addressRegion": "Región Metropolitana", "postalCode": "9460000",
                    "addressCountry": "CL"},
        "areaServed": {"@type": "City", "name": c['nombre'],
                       "addressRegion": "Región Metropolitana", "addressCountry": "CL"},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                          "Saturday", "Sunday"],
            "opens": "08:00", "closes": "21:00"}],
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}}
                             for q, a in c['faq']]}

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{e(c['titulo'])}. Ampliaciones, remodelaciones y construcción desde cota cero. 15 años de experiencia y más de 200 obras ejecutadas. Cotización sin costo.">
  <title>{e(c['titulo'])} | AO Construcciones</title>
  <link rel="canonical" href="{url}">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="assets/img/favicon.png">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(c['titulo'])} | AO Construcciones">
  <meta property="og:description" content="{e(c['intro'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og-aoconstrucciones.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="AO Construcciones">
  <meta property="og:locale" content="es_CL">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">

  <script src="js/tracking.js"></script>

  <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(faq_ld, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
{sprite}

  <header class="navbar" id="navbar" role="banner">
    <div class="navbar__inner">
      <a href="index.html" class="navbar__logo" aria-label="Ir al inicio de AO Construcciones">
        <img src="assets/img/ao-construcciones-logo-portfolio-transparent.webp" alt="AO Construcciones" width="512" height="186">
      </a>
      <a href="tel:+56979925812" class="navbar__cta" id="landing-phone">
        {icon('i-phone')}
        +56 9 7992 5812
      </a>
    </div>
  </header>

  <main>
    <section class="local-hero">
      <div class="container local-hero__grid">
        <div class="local-hero__text">
          <p class="section-tag">{e(c['nombre'])} · Región Metropolitana</p>
          <h1>{e(c['titulo'])}</h1>
          <p class="local-hero__intro">{e(c['intro'])}</p>
          <div class="local-hero__actions">
            <a href="#cotizar" class="btn-primary">Cotiza tu proyecto {icon('i-arrow-right')}</a>
            <a href="{WA}" target="_blank" rel="noopener noreferrer" class="btn-secondary">{icon('i-whatsapp')} WhatsApp</a>
          </div>
          <ul class="local-hero__trust">
            <li><strong>15</strong><span>años de experiencia</span></li>
            <li><strong>200+</strong><span>obras ejecutadas</span></li>
            <li><strong>8–21</strong><span>todos los días</span></li>
          </ul>
        </div>

        <figure class="local-hero__media">
          <img src="{img_url(hero_obra['portada'])}" alt="{e(hero_obra['titulo'])} ejecutada por AO Construcciones en {e(hero_obra['sector'])}, {e(hero_obra['comuna'])}" width="1080" height="810" loading="eager" fetchpriority="high">
          <figcaption>{icon('i-location-dot')} {e(hero_lugar)}</figcaption>
        </figure>
      </div>
      {sectores_txt}
    </section>

    <section class="local-section">
      <div class="container local-section__head">
        <h2>Obras en {e(c['nombre'])}</h2>
        <p class="local-section__lead">{e(c['contexto'])}</p>
        <p class="local-section__note">Algunas de las obras que tenemos registradas en fotos.</p>
      </div>
      <div class="local-works-wrap">
        <div class="local-works" role="list" aria-label="Obras ejecutadas en {e(c['nombre'])}">
{tarjetas}
        </div>
      </div>
      <div class="container local-section__more">
        <a href="portafolio.html" class="btn-secondary">Ver portafolio completo {icon('i-arrow-right')}</a>
      </div>
    </section>

    <section class="local-section local-section--alt">
      <div class="container">
        <h2>Qué hacemos en {e(c['nombre'])}</h2>
        <div class="local-services">
{servicios}
        </div>
      </div>
    </section>

    <section class="local-section" id="cotizar">
      <div class="container local-form">
        <div class="local-form__intro">
          <h2>Cotiza tu proyecto en {e(c['nombre'])}</h2>
          <p>Cuéntanos qué necesitas y te contactamos para coordinar la visita. Solo te
             pedimos tu nombre y un teléfono.</p>
          <ul class="local-form__points">
            <li>{icon('i-circle-check')} Cotización sin costo</li>
            <li>{icon('i-circle-check')} El presupuesto lo hace el dueño, en terreno</li>
            <li>{icon('i-clock')} Atendemos todos los días, 8:00 – 21:00</li>
          </ul>
          <p class="local-form__contact">
            <a href="tel:+56979925812">{icon('i-phone')} +56 9 7992 5812</a>
            <a href="mailto:construyeao@gmail.com">{icon('i-envelope')} construyeao@gmail.com</a>
          </p>
        </div>

        <div class="contact__form-card">
          <div class="form-stepper">
            <div class="form-stepper__step active" id="stepper-1">
              <div class="form-stepper__dot">1</div>
              <span class="form-stepper__label">Proyecto</span>
            </div>
            <div class="form-stepper__line"></div>
            <div class="form-stepper__step" id="stepper-2">
              <div class="form-stepper__dot">2</div>
              <span class="form-stepper__label">Contacto</span>
            </div>
          </div>

          <form id="lead-form" novalidate>
            <div class="form-step active" id="form-step-1">
              <h3 class="form-step__title">¿Qué necesitas?</h3>
              <p class="form-step__subtitle">Elige una opción. Si no calza ninguna, marca "Otro".</p>

              <div class="form-options">
                <div class="form-option">
                  <input type="radio" id="opt-cota" name="service" value="cota-cero">
                  <label for="opt-cota">{icon('i-building')} Desde Cota Cero</label>
                </div>
                <div class="form-option">
                  <input type="radio" id="opt-remodel" name="service" value="remodelacion">
                  <label for="opt-remodel">{icon('i-paint-roller')} Remodelación</label>
                </div>
                <div class="form-option">
                  <input type="radio" id="opt-ampliacion" name="service" value="ampliacion">
                  <label for="opt-ampliacion">{icon('i-expand')} Ampliación</label>
                </div>
                <div class="form-option">
                  <input type="radio" id="opt-otro" name="service" value="otro">
                  <label for="opt-otro">{icon('i-ellipsis')} Otro</label>
                </div>
              </div>

              <div class="form-group">
                <label for="input-location">Comuna <span class="form-optional">(opcional)</span></label>
                <select id="input-location" name="location">
                  <option value="" disabled>Selecciona una comuna</option>
                  <option value="san-jose-de-maipo"{' selected' if c['slug'] == 'san-jose-de-maipo' else ''}>San José de Maipo</option>
                  <option value="cajon-del-maipo">Cajón del Maipo</option>
                  <option value="pirque">Pirque</option>
                  <option value="puente-alto"{' selected' if c['slug'] == 'puente-alto' else ''}>Puente Alto</option>
                  <option value="la-florida"{' selected' if c['slug'] == 'la-florida' else ''}>La Florida</option>
                  <option value="otra">Otra comuna</option>
                </select>
              </div>

              <p class="form-feedback" id="feedback-1" role="alert" aria-live="polite"></p>

              <div class="form-nav">
                <div></div>
                <button type="button" class="form-nav__btn form-nav__btn--next" id="btn-next-1">
                  Siguiente {icon('i-arrow-right')}
                </button>
              </div>
            </div>

            <div class="form-step" id="form-step-2">
              <h3 class="form-step__title">¿Cómo te contactamos?</h3>
              <p class="form-step__subtitle">Con tu nombre y teléfono basta.</p>

              <div class="form-group">
                <label for="input-name">Nombre</label>
                <input type="text" id="input-name" name="name" placeholder="Ej: María González" autocomplete="name" required>
              </div>

              <div class="form-group">
                <label for="input-phone">Teléfono</label>
                <input type="tel" id="input-phone" name="phone" placeholder="+56 9 1234 5678" autocomplete="tel" inputmode="tel" required>
              </div>

              <details class="form-more">
                <summary>Agregar más detalles <span class="form-optional">(opcional)</span></summary>
                <div class="form-group">
                  <label for="input-email">Correo electrónico</label>
                  <input type="email" id="input-email" name="email" placeholder="tu@email.com" autocomplete="email">
                </div>
                <div class="form-group">
                  <label for="input-budget">Presupuesto estimado</label>
                  <select id="input-budget" name="budget">
                    <option value="" disabled selected>Rango de presupuesto</option>
                    <option value="5-15">5 - 15 millones CLP</option>
                    <option value="15-30">15 - 30 millones CLP</option>
                    <option value="30-60">30 - 60 millones CLP</option>
                    <option value="60-plus">Más de 60 millones CLP</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="input-message">Descripción del proyecto</label>
                  <textarea id="input-message" name="message" rows="3" placeholder="Cuéntanos qué quieres construir, remodelar o ampliar..."></textarea>
                </div>
              </details>

              <p class="form-feedback" id="feedback-2" role="alert" aria-live="polite"></p>

              <div class="form-nav">
                <button type="button" class="form-nav__btn form-nav__btn--back" id="btn-back-2">
                  {icon('i-arrow-left')} Atrás
                </button>
                <button type="submit" class="form-nav__btn form-nav__btn--submit" id="btn-submit">
                  Enviar Solicitud {icon('i-paper-plane')}
                </button>
              </div>

              <p class="form-privacy">
                Al enviar aceptas nuestra <a href="privacidad.html">política de privacidad</a>.
              </p>
            </div>
          </form>

          <div class="form-success">
            <div class="form-success__icon">{icon('i-circle-check')}</div>
            <h3 class="form-success__title">¡Solicitud enviada!</h3>
            <p class="form-success__text">Gracias por confiar en AO Construcciones.<br>Te contactaremos a la brevedad.</p>
            <a href="{WA}" id="success-whatsapp" class="form-success__whatsapp" target="_blank" rel="noopener noreferrer">
              {icon('i-whatsapp')} Continuar por WhatsApp
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="local-section local-section--alt">
      <div class="container local-faq">
        <h2>Preguntas frecuentes sobre construir en {e(c['nombre'])}</h2>
{faqs}
      </div>
    </section>
  </main>

  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer__bottom">
        <div>
          <p>&copy; 2026 AO Construcciones. Todos los derechos reservados.</p>
          <p class="footer__credit">
            <a href="index.html">Inicio</a> ·
            <a href="portafolio.html">Portafolio</a> ·
            <a href="privacidad.html">Privacidad</a>
          </p>
        </div>
      </div>
    </div>
  </footer>

  <a id="whatsapp-float" class="whatsapp-btn" href="{WA}" target="_blank" rel="noopener noreferrer"
     aria-label="Escríbenos por WhatsApp para cotizar tu proyecto">
    {icon('i-whatsapp')}
  </a>

  <script src="js/main.js"></script>
</body>
</html>
'''


# ---------- 4. Escribir ----------
generadas = []
for c in COMUNAS:
    out = os.path.join(ROOT, f"constructora-{c['slug']}.html")
    open(out, 'w', encoding='utf-8').write(build(c))
    n = len(por_comuna.get(c['nombre'], []))
    generadas.append((f"constructora-{c['slug']}.html", c['nombre'], n))

print('LANDINGS GENERADAS')
for f, nom, n in generadas:
    print(f'  {f:42} {nom:20} {n} obras reales')

print()
print('Comunas objetivo sin obras registradas:')
for objetivo in ['Pirque']:
    print(f'  - {objetivo}: {len(por_comuna.get(objetivo, []))} obras  -> sin evidencia local')
