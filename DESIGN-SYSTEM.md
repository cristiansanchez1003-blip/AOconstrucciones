# Sistema de diseño — AO Construcciones

Documento de referencia extraído del código real de `css/styles.css` e `index.html`.
Sirve para que cualquier página nueva se vea parte del mismo sitio.

> **Importante:** `css/styles.css` define los tokens dos veces. El bloque de la
> línea 6 es una paleta oscura que quedó **completamente anulada** por el bloque
> de tema claro del final del archivo. **Los valores válidos son los del tema
> claro**, listados abajo. No usar los oscuros.

---

## 1. Color

### Tokens vigentes

| Token | Valor | Uso |
|---|---|---|
| `--bg-primary` | `#fafaf9` | Fondo general de la página |
| `--bg-surface` | `#ffffff` | Tarjetas, inputs, superficies elevadas |
| `--bg-elevated` | `#f4f4f3` | Superficie intermedia |
| `--bg-deep` | `#eceff1` | Superficie de mayor profundidad |
| `--accent-color` | `#e53935` | **Único acento.** CTAs, íconos activos, énfasis |
| `--text-primary` | `#1e293b` | Títulos y texto principal |
| `--text-secondary` | `#64748b` | Texto de apoyo, descripciones |
| `--border-subtle` | `rgba(30, 41, 59, 0.12)` | Bordes de tarjetas e inputs |
| `--border-accent` | `rgba(229, 57, 53, 0.38)` | Bordes en estado activo |
| `--white` | `#ffffff` | |
| `--shadow-soft` | `0 18px 52px rgba(15, 23, 42, 0.1)` | Sombra de tarjetas |
| `--shadow-red` | `0 18px 42px rgba(229, 57, 53, 0.12)` | Sombra bajo elementos con acento |

### Reglas de uso

- **Un solo acento: el rojo `#e53935`.** No introducir un segundo color de marca.
  Todo el peso visual del rojo se gasta en los CTAs; si se usa para decorar,
  el botón deja de destacar.
- Fondos alternados entre secciones: `var(--bg-primary)` y
  `rgba(30, 41, 59, 0.025)`. Nada más fuerte.
- El **footer es la única zona oscura** del sitio: `#111111`.
- Sobre fotos siempre va un degradado oscuro antes del texto blanco:
  `linear-gradient(180deg, rgba(18,18,18,0.02), rgba(18,18,18,0.78))`.
- El verde `#25d366` está reservado **exclusivamente** al botón de WhatsApp,
  por reconocimiento de marca. No usarlo en ningún otro elemento.

> El portafolio (`portafolio.html`) tiene su propia paleta embebida —verde bosque
> `#2D4739` y café madera `#8B5A2B`— que **no** corresponde al resto del sitio.
> Es deuda pendiente de unificar. **No tomarla como referencia.**

---

## 2. Tipografía

```
--font-heading: "Montserrat", sans-serif;   /* pesos 400, 500, 600, 700 */
--font-body:    "Poppins", sans-serif;      /* pesos 300, 400, 500, 600 */
```

Ambas se cargan desde Google Fonts con `display=swap`.

| Elemento | Familia | Tamaño | Peso | Notas |
|---|---|---|---|---|
| H1 (hero) | Montserrat | `clamp(2rem, 6vw, 3.2rem)` | 800 | `line-height: 1.08`, `letter-spacing: -0.02em`, `text-wrap: balance` |
| H2 (sección) | Montserrat | `clamp(1.5rem, 4vw, 2.1rem)` | 800 | `max-width: 22ch` |
| H3 (tarjeta) | Montserrat | `1rem – 1.05rem` | 700 | |
| Cuerpo | Poppins | `16px` | 400 | `line-height: 1.7` |
| Texto de apoyo | Poppins | `0.9rem` | 400 | color `--text-secondary` |
| Etiqueta / eyebrow | Montserrat | `0.76rem` | 700 | mayúsculas, `letter-spacing: 0.06em`, color acento |
| Botón | Montserrat | `1rem` | 700 | |

**Ancho de lectura:** los párrafos se limitan entre `52ch` y `62ch`. Los títulos
usan `max-width` en `ch` y `text-wrap: balance` para que no queden líneas huérfanas.

---

## 3. Espaciado, radios y movimiento

```css
--radius-sm: 8px;    /* inputs, botones, tarjetas chicas */
--radius-md: 14px;   /* tarjetas estándar */
--radius-lg: 22px;   /* contenedores grandes, imagen del hero */

--section-px: clamp(1rem, 5vw, 5rem);   /* padding lateral de sección */
--section-py: clamp(4rem, 9vw, 7rem);   /* padding vertical de sección */

--ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
--transition: 0.35s var(--ease-out);
```

- Contenedor: `.container { width: min(100%, 1240px); margin-inline: auto; }`
- Grillas con `gap`, nunca márgenes por elemento.
- **Toda animación debe respetar `@media (prefers-reduced-motion: reduce)`.**

### Patrón de animación de entrada

Elementos con clase `.reveal`, `.reveal-left`, `.reveal-right` o `.clip-reveal`
parten en `opacity: 0; transform: translateY(28px)` y reciben `.is-visible` vía
IntersectionObserver. Retardos escalonados con `.delay-1` (0.08s), `.delay-2`
(0.16s), `.delay-3` (0.24s).

---

## 4. Componentes existentes y reutilizables

### Botones

```html
<a class="btn-primary">Texto <svg class="icon"><use href="#i-arrow-right"></use></svg></a>
<a class="btn-secondary">Texto</a>
```

- `.btn-primary` — fondo rojo, texto blanco, `min-height: 48px`,
  sombra `0 14px 30px rgba(229,57,53,0.2)`, en hover sube 2px.
- `.btn-secondary` — contorno sutil sobre superficie clara.
- **Área táctil mínima 48×48 px.**

### Íconos

Sprite SVG inline al inicio del `<body>`, sin librerías externas.
Se usan así:

```html
<svg class="icon" aria-hidden="true" focusable="false"><use href="#i-arrow-right"></use></svg>
```

Los íconos escalan con `width: 1em` según el `font-size` heredado.
Disponibles: `i-arrow-right`, `i-arrow-left`, `i-phone`, `i-envelope`,
`i-location-dot`, `i-clock`, `i-circle-check`, `i-compass`, `i-shield-halved`,
`i-leaf`, `i-seedling`, `i-paper-plane`, `i-paint-roller`, `i-expand`,
`i-ellipsis`, `i-building`, `i-whatsapp`, `i-instagram`, `i-facebook-f`.

Los funcionales son de trazo (`stroke`, 2px, `linecap: round`); los de marca son
rellenos. **Si se necesita un ícono nuevo, dibujarlo en el mismo estilo de trazo.**

### Tarjeta de servicio (`.service-card`)

Foto a sangre con degradado oscuro encima, número de servicio como eyebrow,
título en blanco sobre la imagen, y enlace con flecha. Relación 420×460.

### Formulario (`.contact__form-card`)

Wizard de **2 pasos**, ya optimizado para conversión:

- **Paso 1** — tipo de servicio (4 radios con ícono) + comuna (opcional)
- **Paso 2** — nombre* y teléfono*, con email / presupuesto / descripción
  dentro de un `<details class="form-more">` plegado

**Solo tres campos obligatorios: servicio, nombre y teléfono.** No agregar más.

IDs que el JavaScript espera (`js/main.js`) — deben mantenerse tal cual:

```
#lead-form  #form-step-1  #form-step-2  #stepper-1  #stepper-2
#btn-next-1  #btn-back-2  #btn-submit
#opt-cota  #opt-remodel  #opt-ampliacion  #opt-otro   (name="service")
#input-name  #input-phone  #input-email  #input-location  #input-budget  #input-message
#feedback-1  #feedback-2
.form-success  #success-whatsapp
```

### Botón flotante de WhatsApp

```html
<a id="whatsapp-float" class="whatsapp-btn" href="...">…</a>
```

Fijo abajo a la derecha, 60×60 px (56×56 en móvil), verde `#25d366`.
`id` y `class` son necesarios para el rastreo en GTM: **no cambiarlos.**

---

## 5. Medición — no romper

Toda página del sitio carga `js/tracking.js` en el `<head>`, antes que cualquier
otro script. Expone `window.aoTrack(evento, params, callback)`.

Se rastrean automáticamente por delegación de clics:

| Evento | Se dispara con |
|---|---|
| `generate_lead` | envío del formulario (lo dispara `main.js`) |
| `whatsapp_click` | cualquier enlace a `wa.me` o `api.whatsapp.com` |
| `tel_click` | cualquier `href="tel:"` |
| `email_click` | cualquier `href="mailto:"` |

**Consecuencia de diseño:** los teléfonos y correos deben ser enlaces `tel:` /
`mailto:` reales para que la conversión se registre. Nunca texto plano.

---

## 6. Rendimiento — no romper

El sitio pasó de 1.466 KB a 285 KB de carga inicial. Reglas para no perderlo:

- **Imágenes en WebP**, dimensionadas al tamaño real de despliegue.
  Nada por sobre 1.200 px de ancho.
- `loading="lazy"` en todo lo que esté bajo el pliegue; `loading="eager"` solo
  en la imagen principal del hero.
- **Siempre `width` y `height`** en los `<img>`, con las dimensiones reales del
  archivo, para evitar saltos de layout.
- **Sin librerías externas.** Nada de Font Awesome, jQuery, Bootstrap, Swiper ni
  frameworks de carrusel: si se necesita un carrusel, se escribe a mano con
  scroll-snap de CSS.
- Solo dos familias tipográficas, las que ya están cargadas.

---

## 7. Accesibilidad

- Un solo `<h1>` por página, y que contenga la palabra clave local.
- Jerarquía de encabezados sin saltos.
- Foco visible: `outline: 2px solid var(--accent-color); outline-offset: 3px`.
- Contraste mínimo AA (4.5:1) para texto normal.
- `alt` descriptivo en las fotos de obra, mencionando obra y sector.
- Íconos decorativos con `aria-hidden="true"` y `focusable="false"`.
- Respetar `prefers-reduced-motion` en toda animación.

---

## 8. Estructura de una landing por comuna

Orden actual de `constructora-{comuna}.html`:

1. **Cabecera mínima** — logo + teléfono. Sin menú, para no dar salidas.
2. **Hero** — eyebrow con la comuna, H1 `Constructora en {comuna}`, intro,
   píldora con los sectores reales, dos CTAs y tres señales de confianza.
3. **Obras de la comuna** — grilla de tarjetas con foto, sector y título.
4. **Servicios** — tres tarjetas.
5. **Formulario** — con la comuna preseleccionada.
6. **Preguntas frecuentes** — `<details>` con schema `FAQPage`.
7. **Footer reducido** + botón flotante de WhatsApp.

### Datos estructurados

Cada landing lleva dos bloques JSON-LD: `GeneralContractor` acotado a la comuna
(con `address` en San José de Maipo, código postal `9460000`, y `geo`
`-33.6404 / -70.3528`, **sin `streetAddress`** por ser negocio de área de
servicio) y un `FAQPage`.

---

## 9. Reglas de contenido

- **Nunca inventar precios, plazos, garantías ni certificaciones.**
  El presupuesto lo hace Andrés en terreno; no se dan cifras en la web.
- Los sectores y las obras que se mencionan deben salir del mapa
  `projectLocations` de `portafolio.html`. Si no está ahí, no se nombra.
- Datos de negocio verificados: **15 años de experiencia**, **200+ obras
  ejecutadas** (confirmado por Andrés), atención **todos los días de 8:00 a
  21:00**, **+56 9 7992 5812**, **construyeao@gmail.com**.
- **Nunca publicar el número de obras por comuna.** El portafolio tiene 15 obras
  con fotos de San José de Maipo, 4 de Puente Alto y 2 de La Florida, pero esos
  son los proyectos que alcanzaron a quedar fotografiados y publicados, **no el
  total ejecutado en cada comuna**. Mostrar "15 en San José de Maipo" junto a
  "200+ obras" hace parecer que hay poca experiencia local, que es exactamente
  lo contrario de lo que la página debe transmitir. Esas cifras sirven solo para
  decidir internamente qué fotos mostrar.
- Los **sectores** sí se pueden nombrar (El Manzano, Las Vertientes, Hacienda El
  Peñón…), porque afirman dónde se ha trabajado sin afirmar cuánto.
