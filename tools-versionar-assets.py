# -*- coding: utf-8 -*-
"""
Sella el CSS y el JS con un hash de su contenido en todos los HTML.

Por que existe: el HTML pedia css/styles.css?v=industrial-premium, una version
fija. Como vercel.json cachea /css/ y /js/ por 24 h, los navegadores seguian
sirviendo la copia vieja aunque el archivo hubiera cambiado, y los estilos
nuevos simplemente no llegaban.

Con un hash del contenido, la URL cambia sola cada vez que el archivo cambia,
y no cambia cuando no. Asi el cache largo es seguro.

Ejecutar despues de tocar CSS o JS, y antes de commitear:
    python tools-versionar-assets.py
"""
import hashlib
import os
import re
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = ['css/styles.css', 'js/main.js', 'js/tracking.js']


def hash_file(rel):
    with open(os.path.join(ROOT, rel), 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:10]


def main():
    versiones = {rel: hash_file(rel) for rel in ASSETS}

    paginas = sorted(glob.glob(os.path.join(ROOT, '*.html')))
    total = 0

    for path in paginas:
        html = open(path, encoding='utf-8').read()
        original = html

        for rel, h in versiones.items():
            # Reemplaza el archivo con o sin ?v= previo, dejando ?v=<hash>.
            patron = re.escape(rel) + r'(\?v=[^"\']*)?'
            html, n = re.subn(patron, f'{rel}?v={h}', html)
            total += n

        if html != original:
            open(path, 'w', encoding='utf-8').write(html)

    print('Hashes de contenido:')
    for rel, h in versiones.items():
        print(f'  {rel:20} -> ?v={h}')
    print()
    print(f'{len(paginas)} paginas revisadas, {total} referencias selladas')

    # Verificacion: ninguna pagina debe quedar con una version fija antigua
    sobrantes = []
    for path in paginas:
        html = open(path, encoding='utf-8').read()
        for m in re.findall(r'(?:css|js)/[a-z.]+\?v=([^"\']*)', html):
            if m not in versiones.values():
                sobrantes.append((os.path.basename(path), m))
    if sobrantes:
        print('\nATENCION, versiones sin sellar:')
        for p, v in sobrantes:
            print(f'  {p} -> ?v={v}')
        raise SystemExit(1)
    print('Todas las referencias quedaron con hash de contenido.')


if __name__ == '__main__':
    main()
