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
             'Construcción de casas desde cero, ampliaciones, remodelaciones interiores y '
             'exteriores, techumbres, terrazas, decks, quinchos, cobertizos, portones, '
             'quebravistas, piso vinílico y pintura de fachadas. En el portafolio están las '
             'obras con fotos del proceso.'),
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
             'Remodelaciones interiores, cocinas, techumbres, quinchos, cobertizos, portones, '
             'quebravistas, piso vinílico, pintura de fachadas y escaleras, entre otras. '
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
             'Remodelaciones interiores y exteriores, techumbres, piso vinílico, pintura de '
             'fachadas, portones y quebravistas, entre otros. Puedes ver las obras de la '
             'comuna en el portafolio.'),
        ],
    },
]

SERVICIOS = [  # (nombre, icono, descripción, link)
    ('Obra nueva', 'i-building',
     'Casas construidas desde cero: fundaciones, estructura y terminaciones.', 'portafolio.html'),
    ('Ampliaciones', 'i-expand',
     'Más metros cuadrados sin romper el diseño original de tu casa.', 'portafolio.html'),
    ('Remodelaciones', 'i-paint-roller',
     'Cocinas, baños, interiores, pisos, pintura y fachadas.', 'portafolio.html'),
    ('Techumbres', 'i-roof',
     'Reparación y cambio de techumbre, con revisión en terreno.', 'portafolio.html'),
    ('Quinchos', 'i-fire',
     'Quinchos nuevos, cocinas de quincho a medida y remodelaciones.', 'construccion-de-quinchos.html'),
    ('Portones y cierres', 'i-gate',
     'Portones a medida, reparación de portones y cierres perimetrales.', 'fabricacion-de-portones.html'),
]

# Obra destacada de cada página: se muestra en antes y después, con fotos del
# proceso. Solo obras cuyo archivo sin número es de verdad la foto del "antes"
# (las subidas desde el 23 de septiembre de 2026); en las más antiguas ese
# archivo puede ser una foto de proceso.
DESTACADA_FACHADA = {
    'id': 'remodelacion-de-fachada-y-balcon',
    'titulo': 'Fachada y balcón en Las Vertientes',
    'texto': 'Un muro de estuco gastado pasó a ser una fachada nueva, con revestimiento de '
             'paneles verticales, un balcón con estructura metálica e iluminación exterior.',
    'proceso': [3, 4, 5, 6],
}
DESTACADA_QUINCHO = {
    'id': 'construccion-de-quincho',
    'titulo': 'Cocina de quincho en Hacienda El Peñón',
    'texto': 'Bajo un techo que ya existía armamos una cocina de quincho a medida: muebles, '
             'parrilla integrada, lavaplatos y campana.',
    'proceso': [2, 3, 5, 6],
}
DESTACADA_PORTON = {
    'id': 'construccion-de-porton',
    'titulo': 'Portón nuevo en El Manzano',
    'texto': 'Fabricamos e instalamos un portón de estructura metálica con revestimiento de madera.',
    'proceso': [],
}

RESENAS = [  # Reseñas reales del Perfil de Empresa, las mismas del home.
    ('Marco Zamorano',
     'AO me hizo mi cocina, la que quedó increíble. Elegante, buenas terminaciones, y muy rápido. '
     'Agradecido!'),
    ('Marcela Escárate',
     'De acuerdo a nuestra experiencia podemos destacar, cumplen con los tiempos, excelente calidad '
     'en materiales, también destacó calidad de trabajadores y limpieza.'),
    ('Israel Zamora',
     'Recomiendo plenamente a AO por la calidad de su trabajo y su compromiso con el cliente. '
     'Realizaron la remodelación y pintura de nuestra casa con un alto nivel de detalle, '
     'profesionalismo y cumplimiento de los tiempos comprometidos. Fueron súper limpios y '
     'prolijos, y es algo que es difícil de encontrar.'),
]
PERFIL_GOOGLE = 'https://share.google/K1ZzYydFXDxCS9WZD'

# Cómo trabajamos: lo que de verdad pasa, sin plazos ni garantías (regla 1).
PASOS = [
    ('Nos cuentas tu proyecto',
     'Por el formulario, WhatsApp o teléfono. Atendemos todos los días, de 8:00 a 21:00.',
     '<path d="M5 7h26v17H15l-7 6v-6H5z"/><path d="M11 13h14M11 18h9"/>'),
    ('Visita en terreno, sin costo',
     'Andrés, el dueño, va a ver el lugar y conversa contigo lo que quieres lograr.',
     '<path d="M18 32s-10-9.5-10-17a10 10 0 0 1 20 0c0 7.5-10 17-10 17z"/><circle cx="18" cy="15" r="3.5"/>'),
    ('Recibes tu cotización',
     'Con lo que incluye el trabajo, para que decidas con calma. Sin compromiso.',
     '<path d="M9 4h13l6 6v22H9z"/><path d="M22 4v6h6"/><path d="M13 17h10M13 22h10M13 27h6"/>'),
    ('Construimos contigo',
     'El dueño está a cargo de la obra y hablas directo con él durante todo el proceso.',
     '<path d="M18 4 5 15h4v15h18V15h4z"/><path d="m13 22 4 4 7-8"/>'),
]

# Páginas por servicio. Las obras salen del portafolio por su id (el slug del
# nombre de archivo). Sin fotos no hay página: cobertizos quedó fuera por eso.
PAGINAS_SERVICIO = [
    {
        'file': 'construccion-de-quinchos.html',
        'tag': 'Quinchos · Zona sur de Santiago',
        'titulo': 'Construcción de quinchos',
        'intro': 'Quinchos nuevos y remodelación de quinchos en Cajón del Maipo, Pirque, '
                 'Puente Alto y La Florida.',
        'contexto': 'Construimos quinchos completos y también renovamos los que ya existen: '
                    'cocina, parrilla, revestimientos y accesos.',
        'hero': 'construccion-de-quincho',
        'obras': ['construccion-de-quincho', 'remodelacion-de-quincho',
                  'remodelacion-acceso-a-quincho'],
        'servicio': 'quincho',
        'faq': [
            ('¿Construyen el quincho completo o solo la cocina?',
             'Las dos cosas. Construimos quinchos nuevos y también remodelamos los que ya '
             'existen. En Hacienda El Peñón, por ejemplo, armamos una cocina de quincho a '
             'medida bajo un techo que ya estaba.'),
            ('¿Cómo se hace el presupuesto?',
             'Andrés, dueño de la empresa, va en persona a ver el espacio. No damos precios por '
             'teléfono: cada quincho depende del lugar, de lo que quieras incluir y de lo que '
             'ya exista. La visita no tiene costo.'),
            ('¿En qué comunas trabajan?',
             'En Cajón del Maipo, Pirque, Puente Alto y La Florida.'),
        ],
    },
    {
        'file': 'fabricacion-de-portones.html',
        'tag': 'Portones y cierres · Zona sur de Santiago',
        'titulo': 'Fabricación de portones y cierres',
        'intro': 'Portones, reparación de portones y cierres perimetrales en Cajón del Maipo, '
                 'Pirque, Puente Alto y La Florida.',
        'contexto': 'Fabricamos e instalamos portones a medida, reparamos los que ya existen y '
                    'cerramos el perímetro de tu terreno.',
        'hero': 'construccion-de-porton',
        'obras': ['construccion-de-porton', 'cierre-perimetral', 'reparacion-de-porton'],
        'servicio': 'porton',
        'faq': [
            ('¿Fabrican el portón o solo lo instalan?',
             'Lo fabricamos y lo instalamos. También reparamos portones que ya existen, como '
             'el de Las Vertientes que está en el portafolio.'),
            ('¿Con qué materiales trabajan?',
             'Depende de cada proyecto. En El Manzano hicimos un portón de estructura metálica '
             'con revestimiento de madera, y un cierre perimetral con polines y malla '
             'electrosoldada galvanizada.'),
            ('¿Cómo se hace el presupuesto?',
             'Andrés, dueño de la empresa, va en persona a ver el terreno y el acceso. No damos '
             'precios por teléfono ni por metro lineal. La visita no tiene costo.'),
        ],
    },
]

COMUNAS[0]['destacada'] = DESTACADA_FACHADA   # San José de Maipo
COMUNAS[1]['destacada'] = DESTACADA_QUINCHO   # Puente Alto
COMUNAS[2]['destacada'] = DESTACADA_FACHADA   # La Florida: no hay antes local
PAGINAS_SERVICIO[0]['destacada'] = DESTACADA_QUINCHO
PAGINAS_SERVICIO[0]['incluye'] = [
    ('Quinchos nuevos', 'i-fire', 'Construimos el quincho completo, desde la base hasta las terminaciones.'),
    ('Cocina de quincho a medida', 'i-building',
     'Muebles, mesones, espacio para la parrilla, lavaplatos y campana.'),
    ('Revestimientos en piedra', 'i-shield-halved',
     'Muros y mesones revestidos en piedra, resistentes al uso y a la intemperie.'),
    ('Remodelación y accesos', 'i-paint-roller',
     'Renovamos quinchos que ya existen, sus accesos y terminaciones.'),
]
PAGINAS_SERVICIO[1]['destacada'] = DESTACADA_PORTON
PAGINAS_SERVICIO[1]['incluye'] = [
    ('Portones a medida', 'i-gate', 'Fabricamos e instalamos el portón según el ancho y el uso de tu acceso.'),
    ('Reparación de portones', 'i-paint-roller', 'Reparamos portones existentes: estructura, revestimiento y cierre.'),
    ('Cierres perimetrales', 'i-shield-halved', 'Cerramos el perímetro de tu terreno con polines y malla.'),
    ('Visita en terreno', 'i-location-dot', 'Medimos el acceso y vemos el terreno antes de cotizar.'),
]

# Opciones del formulario: las mismas que en index.html.
OPCIONES = [  # (id, value, icono, etiqueta)
    ('opt-cota', 'cota-cero', 'i-building', 'Obra nueva'),
    ('opt-ampliacion', 'ampliacion', 'i-expand', 'Ampliación'),
    ('opt-remodel', 'remodelacion', 'i-paint-roller', 'Remodelación'),
    ('opt-techumbre', 'techumbre', 'i-roof', 'Techumbre'),
    ('opt-quincho', 'quincho', 'i-fire', 'Quincho o terraza'),
    ('opt-porton', 'porton', 'i-gate', 'Portón o cierre'),
    ('opt-otro', 'otro', 'i-ellipsis', 'Otro'),
]
COMUNAS_FORM = [('san-jose-de-maipo', 'San José de Maipo'), ('cajon-del-maipo', 'Cajón del Maipo'),
                ('pirque', 'Pirque'), ('puente-alto', 'Puente Alto'), ('la-florida', 'La Florida'),
                ('otra', 'Otra comuna')]
ZONA = 'Trabajamos en Cajón del Maipo, Pirque, Puente Alto y La Florida.'
INSTAGRAM = 'https://www.instagram.com/aoconstrucciones2026/'

SPRITE_IDS = ['i-roof', 'i-fire', 'i-gate', 'i-instagram', 'i-arrow-right', 'i-arrow-left', 'i-phone', 'i-location-dot', 'i-clock',
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


# Las fotos del portafolio se sirven como immutable: subir este número cuando
# se reprocesen, para que los navegadores no muestren la versión vieja.
FOTOS_VERSION = '3'


def img_url(path):
    url = urllib.parse.quote(path)
    return f'{url}?v={FOTOS_VERSION}' if path.startswith('Portafolio') else url


def e(s):
    return html.escape(s, quote=False)


def opciones_html(marcado=None):
    return '\n'.join(
        f'                <div class="form-option">\n'
        f'                  <input type="radio" id="{oid}" name="service" value="{val}"'
        f'{" checked" if val == marcado else ""}>\n'
        f'                  <label for="{oid}">{icon(ic)} {lab}</label>\n'
        f'                </div>' for oid, val, ic, lab in OPCIONES)


def comuna_html(marcada=None):
    opts = '\n'.join(f'                    <option value="{v}"{" selected" if v == marcada else ""}>{n}</option>'
                      for v, n in COMUNAS_FORM)
    vacia = '' if marcada else ' selected'
    return ('                <div class="form-group">\n'
            '                  <label for="input-location">Comuna</label>\n'
            '                  <select id="input-location" name="location">\n'
            f'                    <option value="" disabled{vacia}>Selecciona una comuna</option>\n'
            f'{opts}\n'
            '                  </select>\n'
            '                </div>')


# ---------- 3. Plantilla ----------
def build(c):
    servicio = 'obras' in c
    if servicio:
        por_id = {o['id']: o for o in obras}
        obras_c = [por_id[i] for i in c['obras'] if i in por_id]
        sectores = []
        c = {**c, 'nombre': None,
             'h_obras': 'Obras que hemos hecho',
             'h_que': 'Qué podemos hacer por ti',
             'lead_que': 'Cada proyecto se cotiza en terreno, según lo que necesites.',
             'h_cotizar': 'Cotiza tu proyecto',
             'h_faq': 'Preguntas frecuentes',
             'meta': f"{c['titulo']} en Cajón del Maipo, Pirque, Puente Alto y La Florida. "
                     f"El dueño visita en terreno y la cotización no tiene costo.",
             'comuna_sel': None, 'servicio_sel': c['servicio']}
    else:
        obras_c = sorted(por_comuna.get(c['nombre'], []), key=lambda o: -o['fotos'])
        sectores = sorted({o['sector'] for o in obras_c if o['sector'] != c['nombre']})
        c = {**c, 'file': f"constructora-{c['slug']}.html",
             'tag': f"{c['nombre']} · Región Metropolitana",
             'h_obras': f"Obras en {c['nombre']}",
             'h_que': f"Qué hacemos en {c['nombre']}",
             'lead_que': 'También hacemos cobertizos, quebravistas, decks, terrazas, instalación '
                         'de piso vinílico y proyectos de pintura y fachadas.',
             'h_cotizar': f"Cotiza tu proyecto en {c['nombre']}",
             'h_faq': f"Preguntas frecuentes sobre construir en {c['nombre']}",
             'meta': f"{c['titulo']}. Ampliaciones, remodelaciones y construcción de casas desde "
                     f"cero. 15 años de experiencia y más de 200 obras ejecutadas. Cotización sin costo.",
             'comuna_sel': c['slug'], 'servicio_sel': None}
    url = f"{SITE}/{c['file']}"

    # La obra del hero se elige a mano y puede ser de otra comuna: es la foto
    # que mejor representa el trabajo, no necesariamente la local.
    hero_obra = next((o for o in obras if o['id'] == c.get('hero')), obras_c[0])
    resto = [o for o in obras_c if o['id'] != hero_obra['id']]

    # Si el hero es de otra comuna hay que decirlo, o parecería obra de esta.
    hero_es_local = hero_obra['comuna'] == c['nombre'] or hero_obra['sector'] == hero_obra['comuna']
    hero_lugar = hero_obra['sector'] if hero_es_local else \
        f"{hero_obra['sector']}, {hero_obra['comuna']}"

    def lugar(o):
        # En las páginas de servicio hay obras de varias comunas: se nombra la comuna.
        if not servicio or o['sector'] == o['comuna']:
            return o['sector']
        return f"{o['sector']}, {o['comuna']}"

    tarjetas = '\n'.join(f'''          <article class="local-work" role="listitem">
            <img src="{img_url(o['portada'])}" alt="{e(o['titulo'])}, obra de AO Construcciones en {e(o['sector'])}, {e(o['comuna'])}" loading="lazy" width="1080" height="810">
            <figcaption class="local-work__caption">
              <span class="local-work__place">{icon('i-location-dot')} {e(lugar(o))}</span>
              <h3>{e(o['titulo'])}</h3>
            </figcaption>
          </article>''' for o in resto)

    def tarjeta_servicio(nom, ic, desc, href=None):
        mas = (f'\n            <a class="local-service__link" href="{href}">Ver obras {icon("i-arrow-right")}</a>'
               if href else '')
        return f'''          <article class="local-service">
            <span class="local-service__icon">{icon(ic)}</span>
            <h3>{e(nom)}</h3>
            <p>{e(desc)}</p>{mas}
          </article>'''

    if servicio:
        servicios = '\n'.join(tarjeta_servicio(*x) for x in c['incluye'])
        otros = ' '.join(f'<a href="{href}">{e(nom)}</a>' for nom, _, _, href in SERVICIOS
                         if href != c['file'])
        otros_txt = f'\n        <p class="local-services__more">También hacemos: {otros}</p>'
    else:
        servicios = '\n'.join(tarjeta_servicio(*x) for x in SERVICIOS)
        otros_txt = ''

    # Antes y después de la obra destacada, con fotos del proceso.
    d = c['destacada']
    fs = groups[d['id']]
    d_obra = next(o for o in obras if o['id'] == d['id'])
    def foto(pred):
        return next((f for f in fs if pred(re.sub(r'\s+', ' ', re.sub(r'\.[^.]+$', '', f)).strip())), None)
    antes = foto(lambda n: n == base_name(fs[0]))
    despues = foto(lambda n: re.search(r'\sresultado\s+final$', n, re.I))
    proceso = [p for p in (foto(lambda n, k=k: n.endswith(f' {k}')) for k in d['proceso']) if p]
    d_lugar = f"{d_obra['sector']}, {d_obra['comuna']}" if d_obra['sector'] != d_obra['comuna'] else d_obra['sector']
    tira = ''
    if len(proceso) >= 2:
        tira = '\n'.join(f'''          <figure class="local-steps__item" role="listitem">
            <img src="{img_url(PORT_DIR + '/' + p)}" alt="Proceso de la obra en {e(d_lugar)}, foto {i}" loading="lazy" width="600" height="600">
            <figcaption>{i}</figcaption>
          </figure>''' for i, p in enumerate(proceso, 1))
        tira = f'''
        <p class="local-steps__title">Así avanzó la obra</p>
        <div class="local-steps" role="list" aria-label="Fotos del proceso">
{tira}
        </div>'''
    ba_html = f'''    <section class="local-section local-ba-section">
      <div class="container">
        <div class="local-section__head">
          <p class="section-tag">Antes y después</p>
          <h2>{e(d['titulo'])}</h2>
          <p class="local-section__lead">{e(d['texto'])}</p>
        </div>
        <div class="local-ba">
          <figure class="local-ba__item">
            <img src="{img_url(PORT_DIR + '/' + antes)}" alt="Antes de la obra en {e(d_lugar)}" loading="lazy" width="900" height="1200">
            <figcaption class="local-ba__label">Antes</figcaption>
          </figure>
          <figure class="local-ba__item">
            <img src="{img_url(PORT_DIR + '/' + despues)}" alt="Después: {e(d_obra['titulo'])} terminada por AO Construcciones en {e(d_lugar)}" loading="lazy" width="900" height="1200">
            <figcaption class="local-ba__label local-ba__label--after">Después</figcaption>
          </figure>
        </div>
        <p class="local-ba__place">{icon('i-location-dot')} {e(d_lugar)}</p>{tira}
        <div class="local-ba__cta">
          <a href="#cotizar" class="btn-primary">Quiero un cambio así {icon('i-arrow-right')}</a>
          <span>La visita y la cotización no tienen costo.</span>
        </div>
      </div>
    </section>'''

    resenas = '\n'.join(f'''        <article class="review-card">
          <div class="review-card__stars" role="img" aria-label="5 de 5 estrellas">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <blockquote class="review-card__text">{e(t)}</blockquote>
          <div class="review-card__author">
            <span class="review-card__name">{e(n)}</span>
            <span class="review-card__source">Reseña en Google</span>
          </div>
        </article>''' for n, t in RESENAS)
    resenas_html = f'''    <section class="reviews" id="resenas">
      <div class="container">
        <div class="local-section__head">
          <p class="section-tag">Lo que dicen</p>
          <h2>Clientes que ya construyeron con nosotros</h2>
          <p class="local-section__lead">Reseñas verificadas en Google, escritas por personas que contrataron a AO Construcciones.</p>
        </div>
        <div class="reviews__grid">
{resenas}
        </div>
        <div class="reviews__footer">
          <span class="reviews__score"><strong>5,0</strong> en Google</span>
          <a class="reviews__link" href="{PERFIL_GOOGLE}" target="_blank" rel="noopener noreferrer">Ver el perfil de la empresa</a>
        </div>
      </div>
    </section>'''

    pasos = '\n'.join(f'''          <div class="process__step">
            <div class="process__step-number">
              <svg class="process__step-icon" viewBox="0 0 36 36" aria-hidden="true">{svg}</svg>
              <span class="process__step-num">Paso 0{i}</span>
            </div>
            <div>
              <h3 class="process__step-title">{e(t)}</h3>
              <p class="process__step-desc">{e(desc)}</p>
            </div>
          </div>''' for i, (t, desc, svg) in enumerate(PASOS, 1))
    pasos_html = f'''    <section class="local-section local-section--alt">
      <div class="container">
        <div class="local-section__head">
          <p class="section-tag">Cómo trabajamos</p>
          <h2>De tu idea a la obra terminada</h2>
          <p class="local-section__lead">Una empresa familiar: el dueño va a tu casa, cotiza y está a cargo de la obra.</p>
        </div>
        <div class="process__timeline local-process">
{pasos}
        </div>
      </div>
    </section>'''

    cta_html = f'''    <section class="local-cta">
      <div class="container local-cta__inner">
        <div>
          <h2>¿Tienes un proyecto en mente?</h2>
          <p>El dueño visita tu terreno y te entrega la cotización sin costo. Atendemos todos los días, de 8:00 a 21:00.</p>
        </div>
        <div class="local-cta__actions">
          <a href="#cotizar" class="btn-primary">Cotiza tu proyecto {icon('i-arrow-right')}</a>
          <a href="{WA}" target="_blank" rel="noopener noreferrer" class="local-cta__btn">{icon('i-whatsapp')} WhatsApp</a>
          <a href="tel:+56979925812" class="local-cta__btn">{icon('i-phone')} Llamar</a>
        </div>
      </div>
    </section>'''

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
        "description": c['intro'] if servicio else
                       f"Constructora en {c['nombre']}: ampliaciones, remodelaciones y "
                       f"construcción de casas desde cero.",
        "telephone": "+56979925812",
        "email": "construyeao@gmail.com",
        "url": url,
        "image": f"{SITE}/assets/img/ao-construcciones-logo-portfolio-transparent.webp",
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "San José de Maipo",
                    "addressRegion": "Región Metropolitana", "postalCode": "9460000",
                    "addressCountry": "CL"},
        "areaServed": [{"@type": "City", "name": n, "addressRegion": "Región Metropolitana",
                        "addressCountry": "CL"}
                       for n in (["San José de Maipo", "Pirque", "Puente Alto", "La Florida"]
                                 if servicio else [c['nombre']])],
        "sameAs": [INSTAGRAM],
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
  <meta name="description" content="{e(c['meta'])}">
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
        <span class="navbar__cta-long">+56 9 7992 5812</span><span class="navbar__cta-short">Llamar</span>
      </a>
    </div>
  </header>

  <main>
    <section class="local-hero">
      <div class="container local-hero__grid">
        <div class="local-hero__text">
          <p class="section-tag">{e(c['tag'])}</p>
          <h1>{e(c['titulo'])}</h1>
          <p class="local-hero__intro">{e(c['intro'])}</p>
          <a class="local-hero__rating" href="#resenas">
            <span class="local-hero__stars" role="img" aria-label="Calificación 5 de 5 estrellas">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            <span><strong>5,0</strong> en Google</span>
          </a>
          <div class="local-hero__actions">
            <a href="#cotizar" class="btn-primary">Cotiza tu proyecto {icon('i-arrow-right')}</a>
            <a href="{WA}" target="_blank" rel="noopener noreferrer" class="btn-secondary">{icon('i-whatsapp')} WhatsApp</a>
          </div>
          <p class="local-hero__assure"><span>{icon('i-circle-check')} Cotización sin costo</span><span>{icon('i-circle-check')} El dueño visita en terreno</span></p>
          <ul class="local-hero__trust">
            <li><strong>15</strong><span>años de experiencia</span></li>
            <li><strong>200+</strong><span>obras ejecutadas</span></li>
            <li><strong>8–21</strong><span>todos los días</span></li>
          </ul>
        </div>

        <figure class="local-hero__media">
          <img src="{img_url(hero_obra['portada'])}" alt="{e(hero_obra['titulo'])}, obra de AO Construcciones en {e(hero_obra['sector'])}, {e(hero_obra['comuna'])}" width="1080" height="810" loading="eager" fetchpriority="high">
          <figcaption>{icon('i-location-dot')} {e(hero_lugar)}</figcaption>
        </figure>
      </div>
      {sectores_txt}
    </section>

{ba_html}

    <section class="local-section">
      <div class="container local-section__head">
        <h2>{e(c['h_obras'])}</h2>
        <p class="local-section__lead">{e(c['contexto'])}</p>
        <p class="local-section__note">Algunas de las obras que tenemos registradas en fotos.</p>
      </div>
      <div class="local-works-wrap">
        <div class="local-works" role="list" aria-label="{e(c['h_obras'])}">
{tarjetas}
        </div>
      </div>
      <div class="container local-section__more">
        <a href="portafolio.html" class="btn-secondary">Ver portafolio completo {icon('i-arrow-right')}</a>
      </div>
    </section>

{cta_html}

{resenas_html}

    <section class="local-section">
      <div class="container">
        <h2>{e(c['h_que'])}</h2>
        <p class="local-section__lead">{e(c['lead_que'])}</p>
        <div class="local-services">
{servicios}
        </div>{otros_txt}
      </div>
    </section>

{pasos_html}

    <section class="local-section" id="cotizar">
      <div class="container local-form">
        <div class="local-form__intro">
          <h2>{e(c['h_cotizar'])}</h2>
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
{opciones_html(c['servicio_sel'])}
              </div>

              <p class="form-zone">{icon('i-location-dot')} {ZONA}</p>

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
{comuna_html(c['comuna_sel'])}
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
        <h2>{e(c['h_faq'])}</h2>
{faqs}
      </div>
    </section>
  </main>

  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer__inner">
        <div class="footer__brand">
          <div class="footer__brand-name">
            <img src="assets/img/ao-construcciones-logo.webp" alt="AO Construcciones" class="footer__logo-img" width="640" height="240" loading="lazy">
          </div>
          <p class="footer__brand-text">
            Empresa familiar de construcción. 15 años y más de 200 obras en San José de Maipo, Pirque, Puente Alto y La Florida.
          </p>
        </div>

        <div class="footer__col">
          <h4 class="footer__col-title">Contacto</h4>
          <a href="tel:+56979925812" class="footer__link">+56 9 7992 5812</a>
          <a href="mailto:construyeao@gmail.com" class="footer__link">construyeao@gmail.com</a>
          <a href="{WA}" target="_blank" rel="noopener noreferrer" class="footer__link">WhatsApp</a>
          <span class="footer__link">Todos los días, 8:00 – 21:00</span>
        </div>

        <div class="footer__col">
          <h4 class="footer__col-title">Servicios</h4>
          <a href="construccion-de-quinchos.html" class="footer__link">Construcción de quinchos</a>
          <a href="fabricacion-de-portones.html" class="footer__link">Portones y cierres</a>
          <a href="portafolio.html" class="footer__link">Portafolio de obras</a>
          <a href="#cotizar" class="footer__link">Cotizar proyecto</a>
        </div>

        <div class="footer__col">
          <h4 class="footer__col-title">Dónde trabajamos</h4>
          <a href="constructora-san-jose-de-maipo.html" class="footer__link">Constructora en San José de Maipo</a>
          <a href="constructora-puente-alto.html" class="footer__link">Constructora en Puente Alto</a>
          <a href="constructora-la-florida.html" class="footer__link">Constructora en La Florida</a>
        </div>
      </div>

      <div class="footer__bottom">
        <div>
          <p>&copy; 2026 AO Construcciones. Todos los derechos reservados.</p>
          <p class="footer__legal">Ingeniería en Proyectos de Obras Civiles Sustentables y Edificación AO &middot; RUT 78.154.344-6</p>
          <p class="footer__credit"><a href="index.html">Inicio</a> · <a href="privacidad.html">Política de privacidad</a></p>
        </div>
        <div class="footer__social">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer" aria-label="Instagram de AO Construcciones">{icon('i-instagram')}</a>
          <a href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">{icon('i-whatsapp')}</a>
        </div>
      </div>
    </div>
  </footer>

  <div class="contact-bar" role="region" aria-label="Contacto rápido">
    <a class="contact-bar__btn contact-bar__btn--call" href="tel:+56979925812">
      {icon('i-phone')}
      Llamar ahora
    </a>
    <a class="contact-bar__btn contact-bar__btn--wa" href="{WA}" target="_blank" rel="noopener noreferrer">
      {icon('i-whatsapp')}
      WhatsApp
    </a>
  </div>

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

for c in PAGINAS_SERVICIO:
    open(os.path.join(ROOT, c['file']), 'w', encoding='utf-8').write(build(c))
    generadas.append((c['file'], c['titulo'][:20], len(c['obras'])))

print('LANDINGS GENERADAS')
for f, nom, n in generadas:
    print(f'  {f:42} {nom:20} {n} obras reales')

print()
print('Comunas objetivo sin landing propia:')
for objetivo in ['Pirque']:
    print(f'  - {objetivo}: {len(por_comuna.get(objetivo, []))} obras registradas')
