# Instagram — plantilla y banco de publicaciones

Cuenta: **@aoconstrucciones.cl** (creada el 19 de octubre de 2026; la antigua
@aoconstrucciones2026 se va a eliminar). Todo el feed usa **una sola plantilla**
con los colores del logo, para que se vea ordenado y reconocible.

## La plantilla AO

**Paleta** (sacada del logo):

| Color | HEX | Dónde va |
|---|---|---|
| Azul petróleo | `#183C4D` | Cabecera, etiqueta "ANTES", etiquetas de proceso |
| Terracota | `#A65442` | Franja bajo la cabecera, etiqueta "DESPUÉS" / "RESULTADO", "COTIZA SIN COSTO" |
| Oliva claro | `#C8C36B` | El lugar, bajo el título (es el oliva del logo `#98953A`, aclarado para que se lea sobre el azul) |
| Crema | `#F4F1E9` | Fondo y pie |
| Blanco | `#FFFFFF` | Texto sobre azul y terracota |

**Tipografía:** títulos y etiquetas en una letra **condensada, negrita y en
mayúsculas**, parecida a la del logo (en el script: Bahnschrift Bold Condensed;
en Canva sirven *Oswald* o *Bebas Neue*). El lugar va en semibold, en
minúsculas.

**Estructura** (1080 × 1350 px, el formato vertical del feed):

1. **Cabecera azul** con el título en blanco (qué se hizo), el lugar en oliva
   claro y una barrita terracota a la izquierda.
2. **Franja terracota** de 8 px.
3. **Fotos** sobre fondo crema, con esquinas redondeadas y 12 px de separación,
   con sus etiquetas en pastilla.
4. **Pie crema:** logo a la izquierda; "COTIZA SIN COSTO" (terracota) y
   "aoconstrucciones.cl" (azul) a la derecha.

**Formatos de portada:**

- **Apilada:** antes arriba, después abajo. Para fotos horizontales.
- **Lado a lado:** antes a la izquierda, después a la derecha. Para fotos
  verticales tomadas desde el mismo ángulo.
- **Evolución:** 4 fotos numeradas ("1 · FUNDACIONES"…). Para obras con proceso
  largo.
- **Collage:** una foto grande y tres chicas. Para obras sin foto del antes.

**Láminas del carrusel:** la foto completa, con una etiqueta ("EL PROCESO ·
1/3" o "RESULTADO") y el mismo pie, para que todo el carrusel se vea de la
misma marca.

## Las imágenes ya están armadas

`tools-plantilla-instagram.py` arma cada publicación con la plantilla, usando
las fotos reales tal cual: solo las recorta, no cambia nada de la obra.

Cada carpeta de `_entregables-andres/instagram/` tiene una subcarpeta
**`publicar/`** con las láminas en orden: `01-portada.jpg`, `02-…`, `03-…`. Se
suben así, como carrusel.

Las fotos que traían la marca de agua vieja se recortaron hacia arriba para
dejarla fuera, así que no se repite el logo.

**Para una obra nueva:** crea la carpeta con las fotos (`antes.jpg`,
`despues.jpg`, `proceso-1.jpg`…), agrega su entrada en `POSTS` dentro del
script y corre `python tools-plantilla-instagram.py nombre-carpeta`. O pídele a
Claude que la arme.

## Si quieres fotos más vistosas con IA

**Opción recomendada:** mejora con IA **solo las fotos**, nunca el diseño. Así
la plantilla queda perfecta y sin errores de ortografía.

1. Sube una foto de la carpeta a la IA con el **prompt de mejora** de abajo.
2. Guarda el resultado en la misma carpeta y **con el mismo nombre**
   (reemplaza la original; el original queda en `_fotos-originales/` o en git).
3. Vuelve a correr el script para esa carpeta.

```
Mejora esta foto como un fotógrafo de arquitectura: endereza las líneas
verticales, equilibra la luz y el color, dale un cielo más limpio si está
quemado y aumenta la nitidez, sin que se vea artificial. Reglas: es una obra
real de una empresa constructora. No cambies la estructura, la forma, los
materiales, los colores ni las proporciones de la construcción. No agregues ni
quites elementos (muebles, plantas, ventanas, personas, autos, herramientas).
Si la foto trae un logo superpuesto, elimínalo limpiamente. Mantén el tamaño y
la proporción de la foto original.
```

**Opción "todo en la IA":** si prefieres que la IA arme la portada completa,
adjunta tres cosas: la plantilla de referencia
(`01-techumbre-la-granja/publicar/01-portada.jpg`), el logo
(`logo-ao-transparente.png`) y las fotos de la obra. Pega el **prompt maestro**
y completa el bloque de la publicación. Revisa siempre que los textos tengan
tildes y que el logo no venga deformado; si viene mal, la opción recomendada
es más segura.

```
PROMPT MAESTRO — PLANTILLA AO CONSTRUCCIONES

Usa la imagen "plantilla" adjunta como diseño obligatorio: copia exactamente
su estructura, proporciones, márgenes, colores y tipo de letra. Formato
vertical 1080 × 1350 px.
- Cabecera azul petróleo (#183C4D) de 176 px de alto. Título en mayúsculas,
  letra condensada negrita, blanca. Debajo, el lugar en oliva claro (#C8C36B).
  A la izquierda del título, una barrita vertical terracota (#A65442).
- Bajo la cabecera, una franja terracota (#A65442) de 8 px.
- Fondo crema (#F4F1E9). Fotos con esquinas redondeadas, márgenes de 40 px y
  12 px de separación entre ellas.
- Etiquetas en forma de pastilla, letra condensada negrita blanca: "ANTES" en
  azul petróleo y "DESPUÉS" en terracota, en la esquina superior izquierda de
  cada foto.
- Pie crema: a la izquierda el logo adjunto tal cual, sin redibujarlo; a la
  derecha "COTIZA SIN COSTO" en terracota y debajo "aoconstrucciones.cl" en
  azul petróleo.
- No agregues ningún otro texto, ícono ni adorno. Revisa ortografía y tildes.
Reglas de las fotos: es una obra real. No cambies la estructura, la forma, los
materiales, los colores ni las proporciones de la construcción, y no agregues
ni quites elementos. Solo mejora la luz, el color y la nitidez. Si una foto
trae un logo superpuesto, elimínalo.

PUBLICACIÓN:
Título: [TÍTULO]
Lugar: [LUGAR]
Formato: [apilada / lado a lado / evolución / collage]
Fotos: [qué foto va en cada lugar]
```

## Las publicaciones

Orden sugerido, 2 por semana (martes y viernes). Techumbre va primero porque
fue el servicio que más contactos trajo en octubre.

| # | Carpeta | Título · Lugar | Formato | Láminas |
|---|---|---|---|---|
| 01 | `01-techumbre-la-granja` | TECHUMBRE NUEVA · La Granja | Apilada | 5 |
| 02 | `02-casa-desde-cero-el-manzano` | DE TERRENO A CASA · El Manzano, San José de Maipo | Evolución | 6 |
| 03 | `03-quincho-hacienda-el-penon` | COCINA DE QUINCHO · Hacienda El Peñón, Puente Alto | Apilada | 5 |
| 04 | `04-acceso-quincho-las-vertientes` | NUEVO ACCESO AL QUINCHO · Las Vertientes, San José de Maipo | Lado a lado | 3 |
| 05 | `05-porton-el-manzano` | PORTÓN A MEDIDA · El Manzano, San José de Maipo | Apilada | 2 |
| 06 | `06-techumbre-las-vertientes` | CAMBIO DE TECHUMBRE · Las Vertientes, San José de Maipo | Apilada | 3 |
| 07 | `07-cocina-el-manzano` | COCINA NUEVA · El Manzano, San José de Maipo | Apilada | 4 |
| 08 | `08-interior-pirque` | REMODELACIÓN INTERIOR · Pirque | Collage | 5 |
| Extra | `extra-09-deck-melocoton` | DECK NUEVO · Melocotón, San José de Maipo | Apilada | 2 |
| Extra | `extra-10-casa-en-el-arbol` | CASA EN EL ÁRBOL · El Manzano, San José de Maipo | Lado a lado | 2 |
| Extra | `extra-11-fachada-las-vertientes` | FACHADA Y BALCÓN NUEVOS · Las Vertientes, San José de Maipo | Lado a lado | 2 |

La fachada de Las Vertientes quedó como extra porque probablemente es el antes
y después que ya se publicó.

**Fotos para la opción "todo en la IA"** (el bloque PUBLICACIÓN): las mismas
que usa la portada armada. Apilada y lado a lado: `antes.jpg` y `despues.jpg`
(en la 01, `despues-con-clientes.jpg`). Evolución (02): `antes`, `proceso-2`,
`proceso-3` y `despues`, con las etiquetas "1 · FUNDACIONES", "2 ·
ESTRUCTURA", "3 · REVESTIMIENTO" y "4 · TERMINADA". Collage (08): el living
grande y las otras tres abajo.

**Cuidado con las personas que aparecen en las fotos:** no siempre son los
clientes. En la 01, el hombre de polera amarilla del "después" es el mismo que
aparece trabajando en el proceso. Los textos no dicen quién es quién.

## Textos

Usan solo datos reales de cada obra: no prometen precios, plazos ni garantías.

### 01 · Techumbre nueva en La Granja

> Techumbre nueva en La Granja 🏠
>
> Retiramos la cubierta antigua, preparamos la base y dejamos un techo
> completamente nuevo. Desliza para ver el proceso ➡️
>
> ¿Tu techo tiene goteras o ya cumplió su vida útil? Escríbenos: la cotización
> no tiene costo y vamos a terreno a ver tu caso.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #Techumbre #CambioDeTechumbre #ReparacionDeTechos
> #AntesYDespues #Constructora #LaGranja #PuenteAlto #LaFlorida

### 02 · De terreno a casa en El Manzano

> De terreno vacío a casa terminada en El Manzano 🏡
>
> Fundaciones y radier, estructura con paneles OSB, barrera de humedad,
> revestimiento exterior y terminaciones interiores. Todo con nuestro equipo,
> de principio a fin.
>
> Desliza para ver el proceso ➡️
>
> ¿Tienes un terreno y quieres construir? Conversemos. Cotización sin costo.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #ConstruccionDeCasas #ObraNueva #CasaPropia
> #CajonDelMaipo #SanJoseDeMaipo #ElManzano #Constructora

### 03 · Cocina de quincho en Hacienda El Peñón

> Se viene el verano ☀️ ¿Tu quincho está listo?
>
> Cocina de quincho a medida en Hacienda El Peñón, Puente Alto: muebles con
> cubierta blanca, parrilla integrada, lavaplatos, campana y refrigerador bajo
> cubierta. Lista para los asados de la temporada 🔥
>
> Construimos y remodelamos quinchos. Cotización sin costo.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #Quincho #Quinchos #CocinaDeQuincho #Parrilla
> #AntesYDespues #PuenteAlto #Constructora

### 04 · Nuevo acceso al quincho en Las Vertientes

> Donde había una ventana, ahora hay una entrada 🚪
>
> En Las Vertientes abrimos el muro para instalar una puerta doble de vidrio y
> darle al quincho un acceso directo desde la casa. El pulgar arriba lo dice
> todo 👍
>
> ¿Quieres cambiar cómo se usa un espacio de tu casa? Escríbenos.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #Remodelacion #AntesYDespues #Quincho #CajonDelMaipo
> #SanJoseDeMaipo #Constructora

### 05 · Portón a medida en El Manzano

> Portón nuevo en El Manzano 🔨
>
> Estructura metálica con revestimiento de madera, fabricado e instalado por
> nuestro equipo. Seguridad y una entrada que cambia la cara de la casa.
>
> Hacemos portones y cierres perimetrales a medida. Cotización sin costo.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #Porton #Portones #PortonDeMadera #CierrePerimetral
> #CajonDelMaipo #SanJoseDeMaipo #Constructora

### 06 · Cambio de techumbre en Las Vertientes

> Así cambia un techo 👇
>
> En Las Vertientes reemplazamos las planchas antiguas, que ya estaban dañadas,
> por una cubierta nueva con todas sus terminaciones. Un techo en buen estado
> protege toda la casa.
>
> ¿El tuyo ya pide cambio? Te visitamos y cotizamos sin costo.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #Techumbre #CambioDeTechumbre #ReparacionDeTechos
> #AntesYDespues #CajonDelMaipo #SanJoseDeMaipo #Constructora

### 07 · Cocina nueva en El Manzano

> Una cocina completamente nueva en El Manzano ✨
>
> Desliza para ver cómo era el espacio y todo el proceso, hasta llegar a una
> cocina con isla central e iluminación nueva ➡️
>
> Remodelamos cocinas, baños e interiores. Cotización sin costo.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #RemodelacionDeCocina #Cocina #Remodelacion #AntesYDespues
> #CajonDelMaipo #SanJoseDeMaipo #Constructora

### 08 · Remodelación interior en Pirque

> Remodelación interior en Pirque 🏠
>
> Pisos nuevos, pintura e instalación de lámparas en pasillos, comedor y
> living. Cambios que se notan apenas entras a la casa.
>
> Trabajamos en Pirque, Cajón del Maipo, Puente Alto y La Florida. Cotización
> sin costo.
>
> 📲 WhatsApp +56 9 7992 5812 · link en la bio
>
> #AOConstrucciones #Pirque #RemodelacionInterior #Remodelacion #PisosNuevos
> #Constructora #PuenteAlto

### Extras

- **Deck en Melocotón:** un deck nuevo alrededor del carro de arrastre, con
  escalera de acceso. Bueno para la temporada de verano.
- **Casa en el árbol:** la más simpática para generar comentarios.
- **Fachada y balcón en Las Vertientes:** revestimiento de paneles verticales,
  balcón nuevo con estructura metálica y cielo de madera, e iluminación
  exterior.

## Perfil

- **Foto de perfil:** `foto-de-perfil-instagram.jpg`. Una foto de casa no se
  distingue en un círculo tan chico; el ícono sí.
- **Nombre** (se encuentra en el buscador): `AO Construcciones · Constructora`.
- **Bio:**

  ```
  🏡 Obras nuevas, ampliaciones, remodelaciones y techumbres
  📍 Cajón del Maipo · Pirque · Puente Alto · La Florida
  ⭐ 5,0 en Google · 15 años de experiencia
  👇 Cotiza sin costo por WhatsApp
  ```

- **Link de la bio:** `aoconstrucciones.cl/ig`. Es una redirección de
  `vercel.json` hacia
  `/?utm_source=instagram&utm_medium=social&utm_campaign=bio`, así la bio se ve
  corta y Analytics igual cuenta las visitas que llegan desde Instagram.
- **Destacadas por servicio:** Techumbres, Quinchos, Portones, Obra nueva,
  Remodelaciones y Clientes. Las portadas ya están hechas con la misma paleta
  en `_entregables-andres/instagram/destacadas/`: se suben como historia y se
  eligen como portada al crear la destacada.
