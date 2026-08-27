# Estado del proyecto — AO Construcciones

Documento vivo. Recoge decisiones, IDs y pendientes que **no** se pueden deducir
leyendo el código ni el historial de git. Si retomas este proyecto en una sesión
nueva, empieza por acá.

**Última actualización:** 27 de agosto de 2026

---

## 1. Qué es esto

Sitio de AO Construcciones, constructora familiar chilena. Andrés es el dueño y
hace todos los presupuestos personalmente, en terreno. Cristian (espíritu
digital) lleva el sitio y la publicidad.

El encargo: el sitio existía pero no estaba en condiciones de recibir tráfico
pagado. Se auditó completo y se está preparando para Google Ads.

**Sitio:** https://aoconstrucciones.cl · estático, Vercel, deploy automático
desde la rama `main` de GitHub.

---

## 2. Datos del negocio

| | |
|---|---|
| Dueño | Andrés Oces |
| Razón social | INGENIERÍA EN PROYECTOS DE OBRAS CIVILES SUSTENTABLES Y EDIFICACIÓN AO |
| RUT | 78.154.344-6 |
| Teléfono | +56 9 7992 5812 |
| Correo | construyeao@gmail.com |
| Horario | todos los días, 8:00 – 21:00 |
| Trayectoria | 15 años · 200+ obras ejecutadas |
| Zona de servicio | San José de Maipo / Cajón del Maipo, Pirque, Puente Alto, La Florida |

**Servicios** — lista completa enviada por Andrés el 15 de agosto de 2026:

1. Proyectos desde cota cero (obra nueva)
2. Ampliaciones
3. Remodelaciones interiores y exteriores
4. Fabricación de quinchos
5. Montaje de cobertizos
6. Fabricación de portones
7. Fabricación y reparación de techumbre
8. Instalación de quebravistas
9. Fabricación de deck
10. Instalación de piso vinílico
11. Proyectos de pintura y fachadas

Además: cierres perimetrales, terrazas, y **instalación** de casas prefabricadas
(no las fabrica).

> **Cinco de estos no existen en el sitio:** cobertizos, portones, quebravistas,
> piso vinílico y pintura/fachadas. No están en el home, ni en las landings, ni
> en el portafolio, ni en los grupos de la campaña. Es contenido nuevo por crear.

---

## 3. IDs y cuentas

```
Google Tag Manager     GTM-TWJVTWLD      versión 2 publicada
Google Analytics 4     G-S4RFL0C3L1      propiedad "AO construcciones" (549900997)
Google Ads             365-657-1293      dentro del MCC Espíritu Digital (534-787-9097)
Search Console         verificado por archivo HTML, sitemap enviado
Cuenta Google          espiritudigital.chile@gmail.com  (authuser=3)
Perfil de Empresa      https://share.google/K1ZzYydFXDxCS9WZD
Link de reseñas        https://g.page/r/CbLqUGAYENtCEAI/review
Campaña de Búsqueda    24141314300  "AO - Busqueda - Zona Sur"
Microsoft Clarity      y7xa9avwgc   clarity.microsoft.com
Web3Forms              1ff1d598-f68d-4de3-970f-cc09a3144591
```

El link de reseñas es el que hay que pasarle a Andrés para que lo mande a sus
clientes. Es el pendiente 5 y el mayor factor de conversión que falta.

**Archivo `google7b6f7779de1d8a12.html` en la raíz: no borrar.** Es la
verificación de Search Console.

---

## 4. Reglas de contenido — leer antes de escribir nada

> **Excepción decidida por Cristian el 25 de agosto de 2026.** El sitio promete
> *"te contactaremos en menos de 24 horas"* en el formulario y en el mensaje de
> éxito. **Es deliberado y se deja.** El compromiso de responder rápido es de
> Andrés, no del sitio. Se quitó una vez por error creyendo que violaba la
> regla 1; **no volver a quitarlo.**

1. **Nunca inventar precios, plazos, garantías ni certificaciones.** El
   presupuesto lo hace Andrés en terreno; no se dan cifras por teléfono ni por
   metro cuadrado. Ya ocurrió una vez: se publicaron "una cocina parte en 5
   millones" y "6 a 10 semanas", ambos inventados, y estuvieron en producción.
2. **Nunca publicar conteo de obras por comuna.** El portafolio solo refleja las
   obras con registro fotográfico (15 en San José de Maipo, 4 en Puente Alto, 2
   en La Florida), no el total ejecutado. Mostrar "15 en San José de Maipo" junto
   a "200+ obras" hace parecer que hay poca experiencia local.
   Los **sectores** sí se pueden nombrar.
3. **"Cota cero" no se usa en publicidad.** Es jerga del rubro; la gente no busca
   así. Internamente sí es el nombre del servicio.
   El 15 de agosto de 2026 se sacó de todo lo que Google lee como descripción:
   las 4 meta descriptions, los `description` de JSON-LD y la respuesta del
   FAQPage. Se reemplazó por **"construcción de casas desde cero"**. Sigue en
   los títulos de tarjeta, en las categorías del portafolio y en los `id`/`value`
   del formulario, que son nombres internos y no se tocan.
4. La marca de agua de las fotos dice "CONSTRUCCIONES AO" con el logotipo
   apilado. **Es el logo actual, no un error.** Se deja tal cual.

---

## 5. Lo que está hecho

### Medición — completa y verificada
- `js/tracking.js` en las 6 páginas, carga GTM y expone `window.aoTrack()`
- Eventos: `generate_lead`, `whatsapp_click`, `tel_click`, `email_click`
- La redirección a WhatsApp **espera el `eventCallback` de GTM** antes de salir
  del sitio, con red de seguridad de 1.300 ms. Sin eso el beacon se cortaba.
- No se envían datos personales al dataLayer, solo tipo de proyecto, comuna y
  presupuesto.
- GA4 vinculado a Ads, conversiones importadas: `generate_lead` (Submit lead
  form) y `whatsapp_click` (Contact), ambas **Primary**, conteo **una por
  sesión**. `tel_click` marcado como evento clave en GA4 pero no importado.
- La conversión heredada "Vista de una página" se bajó a **Secondary** y se sacó
  de los objetivos: contaba *cada* vista de página.
- **Microsoft Clarity** desde el 25 de agosto: mapas de calor y grabaciones de
  sesión. Carga desde `tracking.js`, aparte de GTM a propósito, para que un
  cambio de contenedor no se lo lleve por delante.
- **4 dimensiones personalizadas en GA4** (26 de agosto), ámbito Event:
  `project_type`, `project_location`, `project_budget` y `lead_backup`.
  **No son retroactivas**: solo leen datos desde esa fecha.
- `whatsapp_click` y `tel_click` ahora mandan `link_location`, que distingue
  `barra_movil`, `boton_flotante`, `hero` y `footer`.

### Rendimiento
- Carga inicial del home: **1.466 KB → 285 KB**
- 133 imágenes convertidas a WebP, 19 huérfanas borradas
- Font Awesome eliminado, reemplazado por sprite SVG inline de 19 símbolos
- `vercel.json` con caché por tipo de recurso

### SEO
- Meta tags, canonical, JSON-LD `GeneralContractor` con `address` y `geo`,
  **sin `streetAddress`** por ser negocio de área de servicio
- `robots.txt` y `sitemap.xml`
- 3 landings por comuna en HTML estático, generadas por
  `tools-generar-landings.py`

### Formulario
- De 7 campos obligatorios a 3: servicio, nombre y teléfono
- De 3 pasos a 2, con el selector de servicio primero
- Validación por paso con mensajes visibles
- **Web3Forms activo desde el 26 de agosto de 2026.** Los leads llegan por
  correo a `espiritudigital.chile@gmail.com` **antes** de ofrecer WhatsApp.
  Probado de punta a punta.

---

## 6. Pendientes, por prioridad

### Bloqueante para lanzar campañas
1. ~~Key de Web3Forms~~ **Puesta el 26 de agosto de 2026**, a nombre de
   `espiritudigital.chile@gmail.com`. Los leads llegan a Cristian, que se los
   pasa a Andrés. Cuando Andrés entregue su propia key, se reemplaza la línea 17
   de `js/main.js` y listo.

   > **Lo que costó lanzarla sin ella.** Entre el 12 y el 26 de agosto,
   > **3 personas completaron el formulario** (`generate_lead` en GA4) y sus
   > datos se perdieron: con la key en `'PENDIENTE'`, `saveLead()` retorna
   > `false` sin hacer la petición, así que el nombre y el teléfono nunca
   > salieron del navegador. Ninguna llegó a Andrés por WhatsApp — confirmado
   > con él. **Las 3 no completaron el envío en WhatsApp.**
   >
   > La hipótesis: la persona aprieta "Enviar" en el formulario, da el trámite
   > por terminado, y no entiende por qué se le abre WhatsApp con un mensaje
   > escrito sobre ella misma. El flujo le pedía hacer el trabajo dos veces.
   >
   > Con la key puesta esto se corrige solo: `saveLead()` guarda el lead y
   > `showSuccess()` muestra confirmación con WhatsApp como paso **opcional**.
2. ~~Confirmar facturación en Google Ads.~~ **Confirmada** (15 de agosto de 2026).

### Alto impacto
3. ~~Open Graph en home, portafolio y privacidad.~~ **Hecho**, commit `e7a2779`.
   Las 6 páginas tienen `og:title`.
4. **Recursos del anuncio**: enlaces de sitio, textos destacados, fragmentos
   estructurados, recurso de llamada, recurso de ubicación vinculado al Perfil
   de Empresa.
5. **Reseñas en el Perfil de Empresa.** Es el mayor factor de conversión que
   falta. Cuando lleguen, incorporarlas a las landings.
6. **Pre-renderizar el portafolio.** Sigue generándose 100% con JavaScript, así
   que las 23 obras y sus comunas no existen en el HTML que Google recibe.

### Deuda técnica
7. **443 líneas de JS muerto** en `portafolio.html`, líneas 1240-1683. El bloque
   arranca con `return;` en la línea 1242. Hay dos copias divergentes de
   `escapeHTML`, `parseCSV` y `openProjectModal`.
8. **Dependencia de Google Sheets** en cada carga del portafolio (7 referencias).
   Aporta un solo proyecto, "Cierres Perimetrales", y **su foto está rota**: los
   links vienen separados por espacios y son URLs de página de ImgBB, no
   directas.
9. Dos paletas distintas: el home usa rojo `#e53935`, el portafolio verde
   `#2D4739` con su propio CSS embebido.
10. La política de privacidad menciona analítica pero **no remarketing**, y la
    publicidad personalizada quedó activada al vincular GA4 con Ads.

---

## 7. Decisiones tomadas y por qué

**Geografía de la campaña.** Cristian decidió **no ampliar** más allá de la zona
donde Andrés efectivamente trabaja, aunque el volumen de búsqueda local sea bajo.
Ver `estrategia-google-ads.md`, que documenta el costo de esa restricción: abrir
a toda la Región Metropolitana multiplicaría el volumen por ~17.

**El mecanismo de la cola larga cambió.** La idea original era concordancia
exacta con cola larga fina. La investigación la descartó: con 10 búsquedas
mensuales por término, la exacta deja la campaña en cero impresiones. La
especificidad viene de **concordancia de frase + negativas agresivas +
segmentación geográfica estricta**. La exacta queda solo para términos con
volumen probado.

**Se espera no gastar todo el presupuesto.** Con este volumen es esperable gastar
$60.000–$100.000 de los $150.000. **Eso no se arregla ampliando comunas.** Si
sobra de forma sostenida, se baja la inversión a $100.000 y la diferencia se
convierte en más servicio. Hay que avisarle esto a Andrés **antes** de lanzar,
no cuando pregunte.

**Presupuesto.** $150.000 CLP mensuales ≈ $4.930 diarios. Una sola campaña de
Búsqueda, sin Display ni Performance Max.

**Lanzar antes de perfeccionar las landings.** Sin datos no se sabe qué mejorar,
y el material que falta —fotos del Drive, reseñas— todavía no existe.

**Versionado de assets por hash.** `tools-versionar-assets.py` estampa un hash
del contenido en cada referencia a CSS y JS. Antes había una versión fija
(`?v=industrial-premium`) que nunca cambiaba, y con el caché de 24 h de
`vercel.json` los navegadores servían CSS viejo indefinidamente. **Correr ese
script después de tocar CSS o JS y antes de commitear.**

**GTM se inyecta desde `tracking.js`**, no con el snippet pegado en cada página.
Ventaja: el ID vive en un solo lugar y no hay riesgo de cargarlo dos veces.
Costo: Search Console no puede verificar por Analytics ni por Tag Manager,
porque lee el HTML crudo. Por eso se verificó con archivo HTML.

---

## 8. Herramientas del repo

```
tools-generar-landings.py    regenera las 3 landings desde los datos del portafolio
tools-versionar-assets.py    sella CSS y JS con hash de contenido en todos los HTML
tools-validar-anuncios.py    revisa límites de Google Ads en los textos y recursos
DESIGN-SYSTEM.md             tokens, componentes, IDs que espera main.js, reglas
estrategia-google-ads.md     documento maestro de campaña: keywords, negativas, pujas
PLAN-CAMPANA.md              lo que le falta a la estrategia para poder cargarla
```

Flujo al tocar el diseño:

```bash
python tools-generar-landings.py
python tools-versionar-assets.py
git add -A && git commit && git push
```

---

## 9. Recursos del anuncio — listos para pegar

**No se pueden crear antes de la campaña.** Google Ads no muestra la sección de
recursos mientras la cuenta no tenga ninguna campaña: el menú `Campañas` solo
ofrece Campañas, Experimentos y Grupos de campañas, y `/aw/assets` y
`/aw/extensions` devuelven 404. Se cargan durante la creación de la campaña o
justo después.

Contenido ya redactado, respetando la regla de no prometer precios ni plazos:

### Enlaces de sitio

| Texto | Descripción 1 | Descripción 2 | URL |
|---|---|---|---|
| Ver obras ejecutadas | Fotos reales del proceso | Y del resultado final | /portafolio.html |
| Cotiza tu proyecto | Cuéntanos qué necesitas | Solo nombre y teléfono | /#contacto |
| Constructora en Puente Alto | Obras en Hacienda El Peñón | Y Condominio La Vizcachas | /constructora-puente-alto.html |
| Constructora en La Florida | Remodelaciones y techumbres | Atención directa del dueño | /constructora-la-florida.html |
| Cajón del Maipo | 15 obras en la zona | Las Vertientes, El Manzano | /constructora-san-jose-de-maipo.html |

### Textos destacados

```
Cotización sin costo
El dueño visita en terreno
15 años de experiencia
200+ obras ejecutadas
Atención todos los días
Trato directo, sin intermediarios
```

### Fragmentos estructurados

Encabezado **Servicios**:
```
Ampliaciones · Remodelaciones · Techumbres · Terrazas · Quinchos · Obra nueva
```

### Recurso de llamada

Número **+56 9 7992 5812**, horario 8:00 a 21:00 todos los días.
Activar **informes de llamadas** para que las llamadas desde el anuncio cuenten
como conversión, con duración mínima de 60 segundos para filtrar toques
accidentales. **Verificar si Google ofrece números de desvío en Chile** — la
disponibilidad varía por país y Ads lo avisa al configurarlo.

### Recurso de ubicación

Vincular el **Perfil de Empresa de Google**. Es de los que más rinde para una
constructora local.

---

## 10. Próximo correo a Andrés

Se envía **cuando las campañas estén corriendo**, no antes. Debe incluir:

1. Que pregunte **"¿cómo nos encontró?"** en llamadas de números nuevos, y lleve
   registro. Cubre el hueco de las llamadas directas, que hoy son invisibles.
2. La **key de Web3Forms**, a nombre de su correo.
3. El **Drive con las mejores fotos**, pidiendo explícitamente **fotos del estado
   inicial** (el "antes"), que hoy no existen: las numeradas del portafolio son
   de proceso o demolición.
4. **Cuántas obras reales tiene por comuna**, para poder publicar esa cifra sin
   inventarla.
5. El **link de reseñas** (`https://g.page/r/CbLqUGAYENtCEAI/review`) para que se
   lo mande a los clientes con los que quedó bien.
6. Avisarle que **el presupuesto probablemente no se gaste completo** — es
   esperable gastar $60.000–$100.000 de los $150.000. Anticiparlo, porque la
   reacción natural va a ser pedir ampliar comunas, y eso está descartado.

**No pedirle el ticket promedio.** Se le pidió el 15 de agosto de 2026 y **no
quiso darlo**; mandó solo los servicios ordenados por margen. No insistir. Ver
`PLAN-CAMPANA.md` §2 para cómo se resuelve el valor por conversión sin el monto.

### Respondido por Andrés el 15 de agosto de 2026

Los tres datos que `estrategia-google-ads.md` §14 marcaba como bloqueantes ya
están:

- **Quién contesta el WhatsApp:** Andrés mismo, dentro del horario de atención,
  rápido y bien. **El riesgo 10.5 de la estrategia queda cerrado** — era el más
  grande del proyecto.
- **Prefabricadas:** no las fabrica, pero **sí las instala**. Ver `PLAN-CAMPANA.md`
  §5 para cómo se resolvió en las negativas.
- **Oficios que no ofrece:** quedan los del bloque 5.11 menos `pintor`, porque sí
  hace pintura y fachadas.

---

## 11. Monitoreo de la campaña — estado al 27 de agosto de 2026

La campaña lleva **16 días corriendo**. Esta sección es el punto de partida para
retomar; lo de arriba es la historia del proyecto.

### Números al 27 de agosto

| Google Ads (12–27 ago) | |
|---|---|
| Impresiones | 1.303 |
| Clics | 131 |
| CTR | 10,05% |
| CPC promedio | **CLP 425** |
| Gasto | CLP 55.642 · ~70% del presupuesto |
| Conversiones | 4, **todas `whatsapp_click`** |

**El CPC baja sin parar gracias a las negativas:** 654 → 497 → 449 → 425.
El CTR sobre 10% dice que los anuncios enganchan. **La campaña no es el problema.**

| GA4 (28 días, 227 usuarios) | |
|---|---|
| `form_start` | 9 eventos / 7 personas |
| `generate_lead` | 4 eventos / 3 personas |
| `whatsapp_click` | 9 eventos / 8 personas |
| `tel_click` | 3 eventos / 3 personas |
| `scroll` (90%) | 67 eventos / **23 personas = 10,1%** |

### El diagnóstico, y cómo se llegó

**Contactos reales que le llegaron a Andrés: cero.** Confirmado con él. Consiguió
un cliente nuevo en el período, pero por recomendación, no por el sitio.

Clarity resolvió el misterio en dos días. De **25 sesiones venidas de anuncios**:

- **18 duraron menos de 20 segundos**, casi todas con 1 página y **0 clics**
- 4 entre 20 y 60 segundos
- 3 más de un minuto

Y el resto de los indicadores descartan que el sitio esté roto:

```
Rage clicks         0%     Errores de JavaScript   0%
Dead clicks         0%     CLS                     0 (bueno)
Excessive scrolling 0%     LCP                     4 s  ← el problema
```

**Era velocidad, no diseño.** Con el 75,76% del tráfico en ChromeMobile, un LCP
de 4 segundos significa que la gente se iba antes de que la página se dibujara.
Las sesiones de 1 y 3 segundos no son rechazo: son personas que nunca vieron nada.

**El segundo hallazgo:** solo **7 toques en 24 vistas del home**, y 3 de ellos en
la píldora de calificación del hero — que además los mandaba a Google. No es que
rechacen la oferta; es que no había nada que tocar sin hacer scroll, y el scroll
promedio es 43,74%.

### Lo que se hizo el 27 de agosto

1. **`preload` + `fetchpriority="high"` en la imagen del hero** (`add05a9`). Era
   el elemento LCP y se descubría después de la fuente y el CSS.
2. **La píldora de calificación ahora baja a `#resenas`** en vez de salir a
   Google. Era el elemento más pinchado del sitio.
3. **Barra de contacto fija en móvil** (`d917c18`): *Llamar ahora* y *WhatsApp*,
   siempre visibles, sin scroll. El teléfono va primero a propósito — quien tiene
   goteras quiere llamar, no llenar un formulario. Probada en celular por Cristian.
4. **Tres reseñas de Google en el sitio** más la calificación en el hero.

### Lo primero que hay que mirar mañana

**Clarity, después de 2–3 días de datos nuevos:**

- **LCP** — ¿bajó de los 4 segundos? Es la métrica que dice si el arreglo sirvió.
- **Toques en la barra** — el parámetro `link_location` en GA4 ahora distingue
  `barra_movil` de `boton_flotante`, `hero` y `footer`.
- **Duración de sesión** — ¿siguen yéndose antes de los 20 segundos?

### Pendientes concretos

1. ⚠️ **Verificación de anunciante en Google Ads — vence el 22 de septiembre
   de 2026.** Si se pasa, Google pausa los anuncios. Sigue apareciendo el aviso
   *"Verify your identity"* en la pantalla principal de Ads. **Es lo más urgente.**
2. **Negativas por agregar:** `modulares`, `prefabricados`. Salieron de
   `quinchos modulares prefabricados`.
3. **Vigilar `constructora`:** su CTR cayó de 17,86% a 6,65%. Trae más
   impresiones con peor calce.
4. **Política de privacidad:** no menciona la grabación de sesiones de Clarity.
   Con la Ley 21.719 vigente conviene declararlo. Es un párrafo.
5. **Web3Forms a nombre de Andrés.** Hoy los leads llegan al correo de Cristian.

### Expectativa realista — leer antes de angustiarse

La estrategia proyectaba **5 a 18 cotizaciones al mes** con el presupuesto
completo. Con 131 clics en 16 días y el 70% del presupuesto usado, el orden de
magnitud esperable es de **4 a 8 contactos al mes**, no cuarenta.

La zona es chica y el presupuesto acotado. Eso se sabía desde la investigación
de keywords, y por eso se le anticipó a Andrés que el presupuesto no se gastaría
completo. **Medir el éxito contra una expectativa imposible lleva a tocar cosas
que no había que tocar.**

### La regla que no ha cambiado

**No se tocan pujas, presupuesto ni textos de anuncio bajo 100 clics acumulados
por grupo.** Las negativas sí se ajustan siempre, desde el día uno.
