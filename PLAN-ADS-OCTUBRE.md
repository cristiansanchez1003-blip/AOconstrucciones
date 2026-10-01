# Optimización de Google Ads — octubre 2026

Análisis del 1 de octubre de 2026 con los informes de todo el período
(12 ago – 1 oct): términos de búsqueda (955 términos), palabras clave, anuncios
y recursos. Complementa a [`PLAN-CAMPANA.md`](PLAN-CAMPANA.md).

## Dónde estamos

| | |
|---|---|
| Clics | 423 |
| Impresiones | 4.123 |
| CTR | 10,26% |
| CPC promedio | $408 |
| Gasto | $172.752 |
| Conversiones registradas | 15 (2 `generate_lead` + 13 `whatsapp_click`) |
| Contactos reales confirmados | 6 (uno llegó con la campaña pausada) |

| Grupo | Clics | Costo | Conv. | Costo/conv. | CTR |
|---|---|---|---|---|---|
| E — Exteriores | 105 | $42.945 | 3 | $14.315 | 11,6% |
| B — Remodelaciones | 100 | $41.061 | 4 | $10.265 | 9,6% |
| F — Genérico local | 81 | $33.372 | 4 | $8.343 | 7,6% |
| D — Obra nueva | 58 | $24.442 | 1 | $24.442 | 13,6% |
| C — Techumbres | 44 | $17.624 | 3 | $5.875 | 13,5% |
| A — Ampliaciones | 35 | $13.308 | 0 | — | 9,5% |

**E y B pasaron los 100 clics**: ya se les pueden tocar anuncios y URLs.

## Hallazgo principal: 38% del gasto visible fue a búsquedas sin intención

Google muestra términos que suman $88.974 (el resto lo oculta por privacidad).
De eso, **$33.745 (38%) fue a búsquedas que las negativas de abajo habrían
bloqueado**, con una sola "conversión": *"constructora necesita pintores"*,
alguien buscando trabajo que tocó WhatsApp.

| Tipo | Términos | Clics | Costo |
|---|---|---|---|
| Informativas ("cómo", "ideas", "colores", "modelos") | 99 | 32 | $12.781 |
| Marcas de otras constructoras | 42 | 21 | $9.359 |
| Precio ("valor", "precio") | 60 | 16 | $6.570 |
| Prefabricadas y modulares | 11 | 5 | $2.684 |
| Empleo | 2 | 3 | $1.501 |
| Fuera de zona | 5 | 3 | $1.095 |
| Portones eléctricos (otro oficio) | 6 | 2 | $730 |

Como **la campaña gasta todo su presupuesto diario**, cada peso que se va en
estas búsquedas le quita un clic a alguien que sí quiere contratar.

> **Las negativas no incluyen plurales ni variantes.** Se había cargado
> `prefabricada`, y aun así entraron *"casa prefabricadas"* y *"quinchos
> modulares prefabricados"*. Por eso la lista trae singular y plural.

## 1. Negativas nuevas (nivel campaña, concordancia amplia)

Pegar en *Palabras clave → Palabras clave negativas → + → Agregar a la campaña*.
Las que van entre comillas son de frase.

```
como
cómo
ideas
color
colores
modelos
requisitos
listado
"mas grandes"
"paginas de construccion"
valor
precio
precios
prefabricado
prefabricados
prefabricadas
modular
modulares
necesita
necesitan
trabajadores
electrico
electricos
eléctrico
eléctricos
valdivia
buin
"san joaquin"
"pie andino"
pocuro
"mena y ovalle"
bricsa
"amaro rivera"
belfi
ohla
contec
euroconstructora
lister
rengalil
democorp
terracon
picton
aitue
inarco
carran
traza
i7
"fv spa"
"el sauce"
"bio bio"
"cordillera ingenieria"
volcan
instalbaños
"portones master"
oval
hd
```

**Revisadas contra las palabras clave activas: ninguna las bloquea.** Ojo con
no agregar `cordillera` sola: es parte del mensaje propio de AO.

**No se negativizan** `barato` ni `económico`: *"cierres perimetrales
económicos en chile"* trajo 2 conversiones.

## 2. Páginas de destino por palabra clave (grupo E)

Hoy los 6 anuncios llevan al home. Las búsquedas de quinchos y portones tienen
ahora su propia página, con antes y después, obras y formulario con el servicio
ya marcado.

| Palabra clave | URL final |
|---|---|
| `construccion de quincho` | `https://aoconstrucciones.cl/construccion-de-quinchos.html` |
| `hacer un quincho` | `https://aoconstrucciones.cl/construccion-de-quinchos.html` |
| `fabricacion de portones` | `https://aoconstrucciones.cl/fabricacion-de-portones.html` |
| `porton metalico` | `https://aoconstrucciones.cl/fabricacion-de-portones.html` |
| `porton corredero` | `https://aoconstrucciones.cl/fabricacion-de-portones.html` |
| `reparacion de porton` | `https://aoconstrucciones.cl/fabricacion-de-portones.html` |
| `cierre perimetral` | `https://aoconstrucciones.cl/fabricacion-de-portones.html` |

Se cambian en *Palabras clave → columna "URL final" → lápiz*.

**Palabras clave nuevas** (frase, grupo E), con la URL de su página:
`"porton de fierro"`, `"portones corredizos"` → portones;
`"quincho de ladrillo"` → quinchos. Salieron en el informe con impresiones y
sin palabra clave propia.

## 3. Ruta visible de los anuncios

Los 6 anuncios tienen la ruta vacía (`aoconstrucciones.cl` a secas). Agregarla
hace que el anuncio se vea más específico. Máximo 15 caracteres por campo.

| Grupo | Ruta 1 | Ruta 2 |
|---|---|---|
| A | ampliaciones | zona-sur |
| B | remodelaciones | zona-sur |
| C | techumbres | zona-sur |
| D | casas-nuevas | zona-sur |
| E | quinchos | portones |
| F | constructora | zona-sur |

## 4. Recursos nuevos

**Vínculos a sitio** (nivel campaña):

| Texto | Descripción 1 | Descripción 2 | URL |
|---|---|---|---|
| Construcción de Quinchos | Quinchos nuevos y remodelación | Mira la obra en El Peñón | `/construccion-de-quinchos.html` |
| Portones y Cierres | Portones a medida | Y cierres perimetrales | `/fabricacion-de-portones.html` |
| Reseñas de Clientes | 5,0 estrellas en Google | Opiniones verificadas | `/#resenas` |

**Texto destacado:** `5,0 en Google`.

**Imágenes** (Google sugiere +4,1% de CTR). Listas en
`_entregables-andres/google-ads-imagenes/`, en cuadrado 1200×1200 y horizontal
1200×628, **sin marca de agua**: Google rechaza imágenes con logos o texto
encima. Fachada y balcón de Las Vertientes, cocina del quincho de El Peñón, casa
nueva de El Manzano y portón de El Manzano. Más el **logo** cuadrado para el
recurso de logotipo de la empresa: `logo-ao-icono-cuadrado-600.jpg` (solo el
ícono de la casa; el logo horizontal no se lee al tamaño del anuncio).

**Estado (1 de octubre):** todo lo de esta sección quedó creado, más el nombre
de la empresa "AO Construcciones" a nivel cuenta, que acompaña al logo.

## 5. Lo que no se cambia todavía, y por qué

- **Estrategia de puja: sigue en Maximizar clics.** Hay 15 conversiones, en el
  rango de las 15-20 que pedía el plan, pero 13 son clics al botón de WhatsApp
  y una fue de alguien buscando trabajo. Si se pasa a Maximizar conversiones,
  Google optimizaría hacia gente que toca el botón, no hacia gente que cotiza.
  Se revisa a fin de octubre.
- **Grupo A (Ampliaciones):** 35 clics y 0 conversiones, bajo el umbral de 100.
  Se espera.
- **Grupo D (Obra nueva):** el costo por conversión más alto, pero es el
  servicio de mayor margen y gran parte de su basura (prefabricadas, modelos,
  marcas) la limpian las negativas. Se revisa a fin de mes.
- **Techumbres** convierte mejor que todos, pero viene la primavera. Si cae,
  es estacional; quinchos y terrazas deberían subir.

## 6. Pendiente de verificar

- **Llamadas desde los anuncios:** el recurso de llamada tuvo 23 clics, pero
  las llamadas no cuentan como conversión. Si Chile tiene números de desvío,
  crear la conversión *Llamadas desde anuncios* con duración mínima de 60 s.
- **Horarios:** pedir el informe por hora y día para la revisión de fin de mes.
