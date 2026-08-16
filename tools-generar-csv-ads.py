# -*- coding: utf-8 -*-
"""
Genera los CSV de carga masiva de Google Ads desde los documentos del repo.

    python tools-generar-csv-ads.py

Lee:
  estrategia-google-ads.md   seccion 4 (keywords) y seccion 5 (negativas)
  PLAN-CAMPANA.md            seccion 3 (anuncios), seccion 4 (keywords nuevas)

Escribe en ads-csv/:
  1-grupos.csv       grupos de anuncios con su puja maxima
  2-keywords.csv     keywords con concordancia y URL final donde corresponde
  3-negativas.csv    negativas a nivel de campana, en amplia
  4-anuncios.csv     los 6 RSA

Nada se transcribe a mano: si cambia un documento, se vuelve a correr esto.
"""

import csv
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(BASE, "ads-csv")

CAMPANA = "AO - Busqueda - Zona Sur"

# La carga masiva exige "Customer ID" en cada fila cuando el alcance del upload
# queda en "Multiple accounts", que es el valor por defecto. Incluirlo siempre
# hace que los archivos funcionen con cualquiera de los dos alcances.
CUSTOMER_ID = "365-657-1293"

# La carga masiva no identifica la campana por nombre: exige el ID numerico.
# Es el de "AO - Busqueda - Zona Sur", publicada el 15 de agosto de 2026.
CAMPAIGN_ID = "24141314300"

# Nombre de grupo y puja maxima, de PLAN-CAMPANA.md seccion 2.
GRUPOS = {
    "A": ("A - Ampliaciones", "800"),
    "B": ("B - Remodelaciones", "700"),
    "C": ("C - Techumbres", "450"),
    "D": ("D - Obra Nueva", "900"),
    "E": ("E - Exteriores", "600"),
    "F": ("F - Generico Local", "500"),
}

SITIO = "https://aoconstrucciones.cl"

# URLs a nivel de keyword, de PLAN-CAMPANA.md seccion 7.
URL_POR_KEYWORD = {
    "ampliacion casa puente alto": "/constructora-puente-alto.html",
    "ampliacion casa la florida": "/constructora-la-florida.html",
    "techumbre puente alto": "/constructora-puente-alto.html",
    "constructora puente alto": "/constructora-puente-alto.html",
    "constructora la florida": "/constructora-la-florida.html",
    "constructora cajon del maipo": "/constructora-san-jose-de-maipo.html",
    "constructora san jose de maipo": "/constructora-san-jose-de-maipo.html",
}

# Negativas que NO se cargan, de PLAN-CAMPANA.md seccion 5.
NEGATIVAS_EXCLUIDAS = {"pintor", "movimiento de tierra", "faena"}

CONCORDANCIA = {"frase": "Phrase", "exacta": "Exact"}


def leer(nombre):
    ruta = os.path.join(BASE, nombre)
    if not os.path.exists(ruta):
        sys.exit("No se encontro %s" % nombre)
    return io.open(ruta, encoding="utf-8").read()


def seccion(texto, desde, hasta):
    ini = texto.index(desde)
    fin = texto.index(hasta) if hasta in texto else len(texto)
    return texto[ini:fin]


def letra_de_grupo(encabezado):
    m = re.search(r"Grupo\s+([A-F])\b", encabezado)
    return m.group(1) if m else None


def keywords_de_estrategia(texto):
    """Lee las tablas | keyword | concordancia | ... | de la seccion 4."""
    sec = seccion(texto, "## 4. PALABRAS CLAVE POR SERVICIO", "## 5. PALABRAS CLAVE NEGATIVAS")
    filas = []
    grupo = None
    for linea in sec.split("\n"):
        s = linea.strip()
        if s.startswith("### "):
            grupo = letra_de_grupo(s)
            continue
        if not s.startswith("|") or grupo is None:
            continue
        celdas = [c.strip() for c in s.strip("|").split("|")]
        if len(celdas) < 2:
            continue
        kw, conc = celdas[0], celdas[1].lower()
        if kw.lower() in ("keyword", "palabra clave") or set(kw) <= set("-: "):
            continue
        if conc not in CONCORDANCIA:
            continue
        filas.append((grupo, kw, CONCORDANCIA[conc]))
    return filas


def keywords_de_plan(texto):
    """Lee los bloques ``` de la seccion 4 de PLAN-CAMPANA. Todas en frase."""
    sec = seccion(texto, "## 4. Keywords de los servicios nuevos", "## 5. Negativas")
    filas = []
    grupo = None
    lineas = sec.split("\n")
    i = 0
    while i < len(lineas):
        s = lineas[i].strip()
        if s.startswith("### "):
            grupo = letra_de_grupo(s)
        elif s.startswith("```") and grupo:
            i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                kw = lineas[i].strip()
                if kw:
                    filas.append((grupo, kw, "Phrase"))
                i += 1
        i += 1
    return filas


def negativas_de_estrategia(texto):
    sec = seccion(texto, "## 5. PALABRAS CLAVE NEGATIVAS", "## 6. ESTRUCTURA DE CAMPAÑA")
    terminos = []
    dentro = False
    for linea in sec.split("\n"):
        s = linea.strip()
        if s.startswith("```"):
            dentro = not dentro
            continue
        if dentro and s:
            for t in s.split(","):
                t = t.strip()
                if t:
                    terminos.append(t)
    vistos = set()
    limpio = []
    excluidas = []
    for t in terminos:
        k = t.lower()
        if k in NEGATIVAS_EXCLUIDAS:
            excluidas.append(t)
            continue
        if k in vistos:
            continue
        vistos.add(k)
        limpio.append(t)
    return limpio, excluidas


def anuncios_de_plan(texto):
    sec = seccion(texto, "## 3. Textos de anuncio", "## 4. Keywords")
    grupos = {}
    grupo = None
    tipo = None
    lineas = sec.split("\n")
    i = 0
    while i < len(lineas):
        s = lineas[i].strip()
        if s.startswith("### "):
            grupo = letra_de_grupo(s)
            if grupo:
                grupos.setdefault(grupo, {"titulo": [], "descripcion": []})
        elif s.startswith("**Títulos**"):
            tipo = "titulo"
        elif s.startswith("**Descripciones**"):
            tipo = "descripcion"
        elif s.startswith("```") and grupo and tipo:
            i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                t = lineas[i].strip()
                if t:
                    grupos[grupo][tipo].append(t)
                i += 1
            tipo = None
        i += 1
    return grupos


def escribir(nombre, encabezados, filas):
    """Antepone Customer ID y Campaign ID a todas las filas y escribe el CSV."""
    ruta = os.path.join(SALIDA, nombre)
    encabezados = ["Customer ID", "Campaign ID"] + list(encabezados)
    filas = [[CUSTOMER_ID, CAMPAIGN_ID] + list(f) for f in filas]
    # utf-8-sig para que Excel lo abra bien y Google Ads lo acepte igual.
    with io.open(ruta, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(encabezados)
        w.writerows(filas)
    print("  %-18s %d filas" % (nombre, len(filas)))


def main():
    if not os.path.isdir(SALIDA):
        os.makedirs(SALIDA)

    estrategia = leer("estrategia-google-ads.md")
    plan = leer("PLAN-CAMPANA.md")

    # 1 - Grupos
    filas = [[CAMPANA, nombre, puja, "Paused"] for _, (nombre, puja) in sorted(GRUPOS.items())]
    escribir("1-grupos.csv", ["Campaign", "Ad Group", "Max CPC", "Status"], filas)

    # 2 - Keywords
    kws = keywords_de_estrategia(estrategia) + keywords_de_plan(plan)
    filas = []
    con_url = 0
    for letra, kw, conc in kws:
        if letra not in GRUPOS:
            continue
        url = URL_POR_KEYWORD.get(kw.lower(), "")
        if url:
            url = SITIO + url
            con_url += 1
        filas.append([CAMPANA, GRUPOS[letra][0], kw, conc, url])
    escribir("2-keywords.csv",
             ["Campaign", "Ad Group", "Keyword", "Criterion Type", "Final URL"], filas)

    # 3 - Negativas
    negativas, excluidas = negativas_de_estrategia(estrategia)
    filas = [[CAMPANA, t, "Campaign Negative Broad"] for t in negativas]
    escribir("3-negativas.csv", ["Campaign", "Keyword", "Criterion Type"], filas)

    # 4 - Anuncios
    anuncios = anuncios_de_plan(plan)
    encabezados = (["Campaign", "Ad Group", "Ad type"]
                   + ["Headline %d" % n for n in range(1, 16)]
                   + ["Description %d" % n for n in range(1, 5)]
                   + ["Final URL"])
    filas = []
    problemas = []
    for letra in sorted(anuncios):
        if letra not in GRUPOS:
            continue
        t = anuncios[letra]["titulo"]
        d = anuncios[letra]["descripcion"]
        if len(t) != 15 or len(d) != 4:
            problemas.append("Grupo %s tiene %d titulos y %d descripciones"
                             % (letra, len(t), len(d)))
        filas.append([CAMPANA, GRUPOS[letra][0], "Responsive search ad"]
                     + t[:15] + d[:4] + [SITIO + "/"])
    escribir("4-anuncios.csv", encabezados, filas)

    print("")
    print("Campana: %s" % CAMPANA)
    print("  %d keywords en %d grupos, %d con URL propia" % (len(kws), len(GRUPOS), con_url))
    print("  %d negativas de campana" % len(negativas))
    print("  %d anuncios responsivos" % len(filas))
    if excluidas:
        print("  excluidas a proposito: %s" % ", ".join(sorted(set(excluidas))))
    if problemas:
        print("")
        print("REVISAR:")
        for p in problemas:
            print("  - " + p)
        return 1
    print("")
    print("Los grupos salen en Paused. La campana se crea y se enciende a mano.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
