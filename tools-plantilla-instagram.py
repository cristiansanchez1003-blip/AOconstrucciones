"""Plantilla de Instagram de AO Construcciones.

Arma las portadas y las láminas de carrusel de cada publicación con la misma
estructura, colores y tipografía, para que el feed se vea ordenado. Usa las
fotos reales tal cual (solo las recorta): no inventa nada de la obra.

Entrada: _entregables-andres/instagram/<carpeta>/ con las fotos de la obra.
Salida:  _entregables-andres/instagram/<carpeta>/publicar/ (01-portada.jpg,
         02-....jpg, en el orden del carrusel).

Para una publicación nueva: crea la carpeta con las fotos, agrega su entrada
en POSTS y corre:  python tools-plantilla-instagram.py [carpeta]
Portadas de las historias destacadas:  python tools-plantilla-instagram.py destacadas
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

RAIZ = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(RAIZ, "_entregables-andres", "instagram")
LOGO = os.path.join(RAIZ, "assets", "img", "ao-construcciones-logo-portfolio-transparent.webp")
FUENTE = "C:/Windows/Fonts/bahnschrift.ttf"

# Paleta sacada del logo.
AZUL = (24, 60, 77)        # #183C4D
TERRACOTA = (166, 84, 66)  # #A65442
OLIVA = (152, 149, 56)     # #98953A
OLIVA_CLARO = (200, 195, 107)  # #C8C36B, el oliva legible sobre el azul
CREMA = (244, 241, 233)    # #F4F1E9
BLANCO = (255, 255, 255)

W, H = 1080, 1350          # 4:5, el formato vertical del feed
MARGEN = 40
SEP = 12
ALTO_CABECERA = 176
FRANJA = 8
CUERPO_Y0 = ALTO_CABECERA + FRANJA + 26
PIE_Y0 = 1250
CUERPO_Y1 = PIE_Y0 - 20
RADIO = 22


def fuente(tam, estilo="Bold Condensed"):
    f = ImageFont.truetype(FUENTE, tam)
    f.set_variation_by_name(estilo)
    return f


def abrir(carpeta, nombre):
    im = Image.open(os.path.join(CARPETA, carpeta, nombre + ".jpg"))
    return ImageOps.exif_transpose(im).convert("RGB")


def recortar(im, ancho, alto, fx=0.5, fy=0.5):
    """Recorte tipo 'cover' hacia el punto (fx, fy), en fracciones de la foto."""
    escala = max(ancho / im.width, alto / im.height)
    im = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
    x = round((im.width - ancho) * fx)
    y = round((im.height - alto) * fy)
    return im.crop((x, y, x + ancho, y + alto))


def pegar_foto(lienzo, im, caja, fx=0.5, fy=0.5, radio=RADIO):
    x0, y0, x1, y1 = caja
    foto = recortar(im, x1 - x0, y1 - y0, fx, fy)
    mascara = Image.new("L", foto.size, 0)
    ImageDraw.Draw(mascara).rounded_rectangle((0, 0, foto.width, foto.height), radio, fill=255)
    lienzo.paste(foto, (x0, y0), mascara)


def pastilla(dib, x, y, texto, fondo, tam=30):
    f = fuente(tam)
    l, t, r, b = dib.textbbox((0, 0), texto, font=f)
    px, py = 18, 10
    ancho, alto = (r - l) + 2 * px, (b - t) + 2 * py
    dib.rounded_rectangle((x, y, x + ancho, y + alto), alto // 2, fill=fondo)
    dib.text((x + px - l, y + py - t), texto, font=f, fill=BLANCO)


def texto_que_cabe(dib, texto, ancho_max, tam, estilo):
    while tam > 30:
        f = fuente(tam, estilo)
        if dib.textlength(texto, font=f) <= ancho_max:
            return f
        tam -= 2
    return fuente(tam, estilo)


def logo_en(lienzo, x, y, alto):
    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.resize((round(logo.width * alto / logo.height), alto), Image.LANCZOS)
    lienzo.paste(logo, (x, y), logo)
    return logo.width


def pie(lienzo, dib):
    dib.rectangle((0, PIE_Y0, W, H), fill=CREMA)
    logo_en(lienzo, MARGEN, PIE_Y0 + 14, 72)
    f1, f2 = fuente(30), fuente(28, "SemiBold SemiCondensed")
    t1, t2 = "COTIZA SIN COSTO", "aoconstrucciones.cl"
    dib.text((W - MARGEN - dib.textlength(t1, font=f1), PIE_Y0 + 18), t1, font=f1, fill=TERRACOTA)
    dib.text((W - MARGEN - dib.textlength(t2, font=f2), PIE_Y0 + 54), t2, font=f2, fill=AZUL)


def base(titulo, lugar):
    lienzo = Image.new("RGB", (W, H), CREMA)
    dib = ImageDraw.Draw(lienzo)
    dib.rectangle((0, 0, W, ALTO_CABECERA), fill=AZUL)
    dib.rectangle((0, ALTO_CABECERA, W, ALTO_CABECERA + FRANJA), fill=TERRACOTA)
    ft = texto_que_cabe(dib, titulo, W - 2 * MARGEN - 20, 72, "Bold Condensed")
    dib.text((MARGEN + 20, 34), titulo, font=ft, fill=BLANCO)
    fl = fuente(32, "SemiBold SemiCondensed")
    dib.rectangle((MARGEN, 40, MARGEN + 7, 136), fill=TERRACOTA)
    dib.text((MARGEN + 20, 118), lugar, font=fl, fill=OLIVA_CLARO)
    pie(lienzo, dib)
    return lienzo, dib


def portada_apilada(p):
    lienzo, dib = base(p["titulo"], p["lugar"])
    medio = (CUERPO_Y0 + CUERPO_Y1) // 2
    cajas = [(MARGEN, CUERPO_Y0, W - MARGEN, medio - SEP // 2),
             (MARGEN, medio + SEP // 2, W - MARGEN, CUERPO_Y1)]
    for (nombre, fx, fy), caja, (texto, color) in zip(p["fotos"], cajas, [("ANTES", AZUL), ("DESPUÉS", TERRACOTA)]):
        pegar_foto(lienzo, abrir(p["carpeta"], nombre), caja, fx, fy)
        pastilla(dib, caja[0] + 20, caja[1] + 20, texto, color)
    return lienzo


def portada_lado_a_lado(p):
    lienzo, dib = base(p["titulo"], p["lugar"])
    medio = W // 2
    cajas = [(MARGEN, CUERPO_Y0, medio - SEP // 2, CUERPO_Y1),
             (medio + SEP // 2, CUERPO_Y0, W - MARGEN, CUERPO_Y1)]
    for (nombre, fx, fy), caja, (texto, color) in zip(p["fotos"], cajas, [("ANTES", AZUL), ("DESPUÉS", TERRACOTA)]):
        pegar_foto(lienzo, abrir(p["carpeta"], nombre), caja, fx, fy)
        pastilla(dib, caja[0] + 20, caja[1] + 20, texto, color)
    return lienzo


def portada_evolucion(p):
    lienzo, dib = base(p["titulo"], p["lugar"])
    mx, my = W // 2, (CUERPO_Y0 + CUERPO_Y1) // 2
    cajas = [(MARGEN, CUERPO_Y0, mx - SEP // 2, my - SEP // 2),
             (mx + SEP // 2, CUERPO_Y0, W - MARGEN, my - SEP // 2),
             (MARGEN, my + SEP // 2, mx - SEP // 2, CUERPO_Y1),
             (mx + SEP // 2, my + SEP // 2, W - MARGEN, CUERPO_Y1)]
    for i, ((nombre, fx, fy), caja, texto) in enumerate(zip(p["fotos"], cajas, p["etiquetas"])):
        pegar_foto(lienzo, abrir(p["carpeta"], nombre), caja, fx, fy)
        pastilla(dib, caja[0] + 16, caja[1] + 16, texto, TERRACOTA if i == 3 else AZUL, 26)
    return lienzo


def portada_collage(p):
    lienzo, dib = base(p["titulo"], p["lugar"])
    corte = CUERPO_Y0 + 600
    pegar_foto(lienzo, abrir(p["carpeta"], p["fotos"][0][0]), (MARGEN, CUERPO_Y0, W - MARGEN, corte), *p["fotos"][0][1:])
    ancho = (W - 2 * MARGEN - 2 * SEP) // 3
    for i, (nombre, fx, fy) in enumerate(p["fotos"][1:4]):
        x0 = MARGEN + i * (ancho + SEP)
        pegar_foto(lienzo, abrir(p["carpeta"], nombre), (x0, corte + SEP, x0 + ancho, CUERPO_Y1), fx, fy)
    for (texto, caja_x, caja_y) in p.get("etiquetas_collage", []):
        pastilla(dib, caja_x, caja_y, texto, AZUL, 26)
    return lienzo


def lamina(p, nombre, etiqueta, color, fx=0.5, fy=0.5):
    """Lámina interior del carrusel: la foto completa con el mismo pie."""
    lienzo = Image.new("RGB", (W, H), CREMA)
    dib = ImageDraw.Draw(lienzo)
    pegar_foto(lienzo, abrir(p["carpeta"], nombre), (0, 0, W, PIE_Y0), fx, fy, radio=0)
    dib.rectangle((0, PIE_Y0 - FRANJA, W, PIE_Y0), fill=TERRACOTA)
    pastilla(dib, MARGEN, MARGEN, etiqueta, color)
    pie(lienzo, dib)
    return lienzo


TIPOS = {"apilada": portada_apilada, "lado": portada_lado_a_lado,
         "evolucion": portada_evolucion, "collage": portada_collage}

# Cada foto va como (nombre, fx, fy): fx y fy dicen hacia dónde recortar
# (0 = izquierda/arriba, 1 = derecha/abajo). Las fotos con la marca de agua
# vieja se recortan hacia arriba (fy=0) para dejar la marca fuera.
POSTS = [
    {"carpeta": "01-techumbre-la-granja", "tipo": "apilada",
     "titulo": "TECHUMBRE NUEVA", "lugar": "La Granja",
     "fotos": [("antes", 0.5, 0.45), ("despues-con-clientes", 0.3, 0.0)],
     "carrusel": [("despues", "RESULTADO", 0.5, 0.5), ("proceso-1", "EL PROCESO · 1/3", 0.5, 0.5),
                  ("proceso-2", "EL PROCESO · 2/3", 0.5, 0.5), ("proceso-3", "EL PROCESO · 3/3", 0.5, 0.5)]},
    {"carpeta": "02-casa-desde-cero-el-manzano", "tipo": "evolucion",
     "titulo": "DE TERRENO A CASA", "lugar": "El Manzano, San José de Maipo",
     "fotos": [("antes", 0.5, 0.6), ("proceso-2", 0.5, 0.5), ("proceso-3", 0.5, 0.5), ("despues", 0.5, 0.6)],
     "etiquetas": ["1 · FUNDACIONES", "2 · ESTRUCTURA", "3 · REVESTIMIENTO", "4 · TERMINADA"],
     "carrusel": [("despues", "RESULTADO", 0.5, 0.5), ("proceso-1", "EL PROCESO · 1/4", 0.5, 0.5),
                  ("proceso-2", "EL PROCESO · 2/4", 0.5, 0.5), ("proceso-3", "EL PROCESO · 3/4", 0.5, 0.5),
                  ("proceso-4", "EL PROCESO · 4/4", 0.5, 0.5)]},
    {"carpeta": "03-quincho-hacienda-el-penon", "tipo": "apilada",
     "titulo": "COCINA DE QUINCHO", "lugar": "Hacienda El Peñón, Puente Alto",
     "fotos": [("antes", 0.5, 0.55), ("despues", 0.5, 0.45)],
     "carrusel": [("despues", "RESULTADO", 0.6, 0.5), ("proceso-1", "EL PROCESO · 1/3", 0.5, 0.5),
                  ("proceso-2", "EL PROCESO · 2/3", 0.5, 0.5), ("proceso-3", "EL PROCESO · 3/3", 0.5, 0.5)]},
    {"carpeta": "04-acceso-quincho-las-vertientes", "tipo": "lado",
     "titulo": "NUEVO ACCESO AL QUINCHO", "lugar": "Las Vertientes, San José de Maipo",
     "fotos": [("antes", 0.5, 0.5), ("despues", 0.5, 0.5)],
     "carrusel": [("proceso-1", "EL PROCESO · 1/2", 0.5, 0.5), ("proceso-2", "EL PROCESO · 2/2", 0.5, 0.5)]},
    {"carpeta": "05-porton-el-manzano", "tipo": "apilada",
     "titulo": "PORTÓN A MEDIDA", "lugar": "El Manzano, San José de Maipo",
     "fotos": [("antes", 0.5, 0.55), ("despues", 0.5, 0.5)],
     "carrusel": [("proceso-1", "EL PROCESO", 0.5, 0.5)]},
    {"carpeta": "06-techumbre-las-vertientes", "tipo": "apilada",
     "titulo": "CAMBIO DE TECHUMBRE", "lugar": "Las Vertientes, San José de Maipo",
     "fotos": [("antes", 0.5, 0.4), ("despues", 0.5, 0.1)],
     "carrusel": [("proceso-1", "EL PROCESO · 1/2", 0.5, 0.5), ("proceso-2", "EL PROCESO · 2/2", 0.5, 0.5)]},
    {"carpeta": "07-cocina-el-manzano", "tipo": "apilada",
     "titulo": "COCINA NUEVA", "lugar": "El Manzano, San José de Maipo",
     "fotos": [("antes", 0.5, 0.5), ("despues", 0.5, 0.4)],
     "carrusel": [("proceso-1", "EL PROCESO · 1/3", 0.5, 0.5), ("proceso-2", "EL PROCESO · 2/3", 0.5, 0.5),
                  ("proceso-3", "EL PROCESO · 3/3", 0.5, 0.5)]},
    {"carpeta": "08-interior-pirque", "tipo": "collage",
     "titulo": "REMODELACIÓN INTERIOR", "lugar": "Pirque",
     "fotos": [("foto-1-living", 0.5, 0.7), ("foto-2-comedor", 0.5, 0.5),
               ("foto-3-pasillo", 0.5, 0.5), ("foto-4-pasillo", 0.5, 0.5)],
     "carrusel": [("foto-1-living", "LIVING", 0.5, 0.5), ("foto-2-comedor", "COMEDOR", 0.5, 0.5),
                  ("foto-3-pasillo", "PASILLO", 0.5, 0.5), ("foto-4-pasillo", "PASILLO", 0.5, 0.5)]},
    {"carpeta": "extra-09-deck-melocoton", "tipo": "apilada",
     "titulo": "DECK NUEVO", "lugar": "Melocotón, San José de Maipo",
     "fotos": [("antes", 0.5, 0.5), ("despues", 0.5, 0.45)],
     "carrusel": [("proceso-1", "EL PROCESO", 0.5, 0.5)]},
    {"carpeta": "extra-10-casa-en-el-arbol", "tipo": "lado",
     "titulo": "CASA EN EL ÁRBOL", "lugar": "El Manzano, San José de Maipo",
     "fotos": [("antes", 0.45, 0.5), ("despues", 0.5, 0.4)],
     "carrusel": [("proceso-1", "EL PROCESO", 0.5, 0.5)]},
    {"carpeta": "extra-11-fachada-las-vertientes", "tipo": "lado",
     "titulo": "FACHADA Y BALCÓN NUEVOS", "lugar": "Las Vertientes, San José de Maipo",
     "fotos": [("antes", 0.5, 0.5), ("despues", 0.5, 0.5)],
     "carrusel": [("proceso-1", "EL PROCESO", 0.5, 0.5)]},
]


DESTACADAS = ["TECHUMBRES", "QUINCHOS", "PORTONES", "OBRA NUEVA", "REMODELACIONES", "CLIENTES"]


def destacada(nombre):
    """Portada de historia destacada (1080 × 1920): Instagram muestra el centro en un círculo."""
    lienzo = Image.new("RGB", (1080, 1920), AZUL)
    dib = ImageDraw.Draw(lienzo)
    cx, cy, r = 540, 960, 400
    dib.ellipse((cx - r, cy - r, cx + r, cy + r), outline=TERRACOTA, width=14)
    f = texto_que_cabe(dib, nombre, 600, 120, "Bold Condensed")
    l, t, rr, b = dib.textbbox((0, 0), nombre, font=f)
    dib.text((cx - (rr - l) / 2 - l, cy - (b - t) / 2 - t - 30), nombre, font=f, fill=BLANCO)
    dib.rectangle((cx - 60, cy + 70, cx + 60, cy + 80), fill=OLIVA_CLARO)
    return lienzo


def armar_destacadas():
    salida = os.path.join(CARPETA, "destacadas")
    os.makedirs(salida, exist_ok=True)
    for nombre in DESTACADAS:
        destacada(nombre).save(os.path.join(salida, nombre.lower().replace(" ", "-") + ".jpg"), quality=92)
    print("destacadas ->", len(DESTACADAS))


def armar(p):
    salida = os.path.join(CARPETA, p["carpeta"], "publicar")
    os.makedirs(salida, exist_ok=True)
    TIPOS[p["tipo"]](p).save(os.path.join(salida, "01-portada.jpg"), quality=92)
    for i, (nombre, etiqueta, fx, fy) in enumerate(p.get("carrusel", []), start=2):
        color = TERRACOTA if etiqueta == "RESULTADO" else AZUL
        lamina(p, nombre, etiqueta, color, fx, fy).save(
            os.path.join(salida, f"{i:02d}-{nombre}.jpg"), quality=92)
    print(p["carpeta"], "->", 1 + len(p.get("carrusel", [])), "láminas")


if __name__ == "__main__":
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    if filtro in ("", "destacadas"):
        armar_destacadas()
    for p in POSTS:
        if filtro and filtro in p["carpeta"] or not filtro:
            armar(p)
