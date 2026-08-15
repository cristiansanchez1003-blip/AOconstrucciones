# -*- coding: utf-8 -*-
"""
Valida los textos de anuncio y los recursos contra los limites de Google Ads.

Google rechaza el recurso sin decir cual se paso del limite, asi que conviene
correr esto antes de pegar nada en la interfaz.

    python tools-validar-anuncios.py

Lee los bloques de titulos y descripciones de estrategia-google-ads.md y de
PLAN-CAMPANA.md, y valida los recursos definidos abajo.
"""

import io
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

LIMITE_TITULO = 30
LIMITE_DESCRIPCION = 90
LIMITE_SITELINK_TEXTO = 25
LIMITE_SITELINK_DESC = 35
LIMITE_DESTACADO = 25
LIMITE_SNIPPET_VALOR = 25

MAX_TITULOS = 15
MAX_DESCRIPCIONES = 4

# Recursos finales, ya corregidos en PLAN-CAMPANA.md seccion 1.
SITELINKS = [
    ("Ver obras ejecutadas", "Fotos reales del proceso", "Y del resultado final"),
    ("Cotiza tu proyecto", "Cuentanos que necesitas", "Solo nombre y telefono"),
    ("Obras en Puente Alto", "Obras en Hacienda El Penon", "Y Condominio La Vizcachas"),
    ("Obras en La Florida", "Remodelaciones y techumbres", "Atencion directa del dueno"),
    ("Cajon del Maipo", "Las Vertientes y El Manzano", "El Canelo y San Gabriel"),
]

DESTACADOS = [
    "Cotizacion sin costo",
    "El dueno va a terreno",
    "15 anos de experiencia",
    "200+ obras ejecutadas",
    "Atencion todos los dias",
    "Sin intermediarios",
    "Constructora local",
]

SNIPPET_ENCABEZADO = "Servicios"
SNIPPET_VALORES = ["Ampliaciones", "Remodelaciones", "Techumbres",
                   "Construccion", "Terrazas", "Quinchos"]

# Terminos prohibidos en cualquier texto que salga a publicidad.
PROHIBIDOS = ["cota cero", "garantiz", "garantía", "garantia"]


def leer(nombre):
    ruta = os.path.join(BASE, nombre)
    if not os.path.exists(ruta):
        return None
    return io.open(ruta, encoding="utf-8").read()


def extraer_bloques(texto, desde, hasta):
    """Devuelve [(grupo, tipo, linea)] de los bloques ``` bajo **Titulos**/**Descripciones**."""
    if texto is None:
        return []
    try:
        ini = texto.index(desde)
    except ValueError:
        return []
    fin = texto.index(hasta) if hasta and hasta in texto else len(texto)
    sec = texto[ini:fin]

    filas = []
    grupo = None
    tipo = None
    lineas = sec.split("\n")
    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if linea.startswith("### Grupo") or linea.startswith("**Grupo"):
            grupo = re.sub(r"^[#* ]+|\*+$", "", linea).strip()
            grupo = re.sub(r"\s*\(.*\)$", "", grupo)
        elif linea.startswith("**Títulos**") or linea.startswith("**Titulos**"):
            tipo = "titulo"
        elif linea.startswith("**Descripciones**"):
            tipo = "descripcion"
        elif linea.startswith("```"):
            if tipo is None:
                # bloque suelto: en PLAN-CAMPANA los titulos extra van sin encabezado
                tipo_bloque = "titulo"
            else:
                tipo_bloque = tipo
            i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                t = lineas[i].strip()
                if t and not t.startswith("Texto:") and not t.startswith("Descripci") \
                        and not t.startswith("URL:"):
                    filas.append((grupo or "(sin grupo)", tipo_bloque, t))
                i += 1
            tipo = None
        i += 1
    return filas


def revisar(filas, errores):
    for grupo, tipo, texto in filas:
        limite = LIMITE_TITULO if tipo == "titulo" else LIMITE_DESCRIPCION
        if len(texto) > limite:
            errores.append('%s / %s (%d de %d): "%s"'
                           % (grupo, tipo, len(texto), limite, texto))
        bajo = texto.lower()
        for mal in PROHIBIDOS:
            if mal in bajo:
                errores.append('%s / %s contiene "%s": "%s"' % (grupo, tipo, mal, texto))


def main():
    errores = []

    plan = leer("PLAN-CAMPANA.md")

    if plan is None:
        print("No se encontro PLAN-CAMPANA.md")
        return 1

    # PLAN-CAMPANA.md seccion 3 es la fuente unica de los textos finales.
    # La estrategia se deja fuera a proposito: su seccion 8 es la version
    # incompleta (sin grupos E y F, sin llegar a 15 titulos).
    filas = extraer_bloques(plan, "## 3. Textos de anuncio", "## 4. Keywords")

    if not filas:
        print("No se encontraron textos en PLAN-CAMPANA.md seccion 3")
        return 1

    revisar(filas, errores)

    # Conteo por grupo
    por_grupo = {}
    for grupo, tipo, _ in filas:
        g = re.sub(r"\s*—.*$", "", grupo).strip()
        por_grupo.setdefault(g, {"titulo": 0, "descripcion": 0})
        por_grupo[g][tipo] += 1

    print("TEXTOS DE ANUNCIO")
    for g in sorted(por_grupo):
        c = por_grupo[g]
        marca = ""
        if c["titulo"] > MAX_TITULOS:
            marca = "  <- sobran %d titulos" % (c["titulo"] - MAX_TITULOS)
            errores.append("%s tiene %d titulos, el maximo es %d" % (g, c["titulo"], MAX_TITULOS))
        elif c["titulo"] and c["titulo"] < MAX_TITULOS:
            marca = "  <- faltan %d para llenar el RSA" % (MAX_TITULOS - c["titulo"])
        if c["descripcion"] > MAX_DESCRIPCIONES:
            errores.append("%s tiene %d descripciones, el maximo es %d"
                           % (g, c["descripcion"], MAX_DESCRIPCIONES))
        print("  %-32s %2d titulos, %d descripciones%s"
              % (g, c["titulo"], c["descripcion"], marca))

    print("\nRECURSOS")
    for texto, d1, d2 in SITELINKS:
        for valor, limite, que in ((texto, LIMITE_SITELINK_TEXTO, "texto"),
                                   (d1, LIMITE_SITELINK_DESC, "desc 1"),
                                   (d2, LIMITE_SITELINK_DESC, "desc 2")):
            if len(valor) > limite:
                errores.append('Enlace de sitio / %s (%d de %d): "%s"'
                               % (que, len(valor), limite, valor))
    print("  %d enlaces de sitio" % len(SITELINKS))

    for valor in DESTACADOS:
        if len(valor) > LIMITE_DESTACADO:
            errores.append('Texto destacado (%d de %d): "%s"'
                           % (len(valor), LIMITE_DESTACADO, valor))
    print("  %d textos destacados" % len(DESTACADOS))

    for valor in SNIPPET_VALORES:
        if len(valor) > LIMITE_SNIPPET_VALOR:
            errores.append('Valor de fragmento (%d de %d): "%s"'
                           % (len(valor), LIMITE_SNIPPET_VALOR, valor))
    print("  fragmento '%s' con %d valores" % (SNIPPET_ENCABEZADO, len(SNIPPET_VALORES)))

    print("")
    if errores:
        print("FUERA DE LIMITE (%d):" % len(errores))
        for e in errores:
            print("  - " + e)
        return 1

    print("Todo dentro de limite. Listo para pegar en Google Ads.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
