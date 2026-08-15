# Estado del proyecto — AO Construcciones

Documento vivo. Recoge decisiones, IDs y pendientes que **no** se pueden deducir
leyendo el código ni el historial de git. Si retomas este proyecto en una sesión
nueva, empieza por acá.

**Última actualización:** 15 de agosto de 2026

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
```

El link de reseñas es el que hay que pasarle a Andrés para que lo mande a sus
clientes. Es el pendiente 5 y el mayor factor de conversión que falta.

**Archivo `google7b6f7779de1d8a12.html` en la raíz: no borrar.** Es la
verificación de Search Console.

---

## 4. Reglas de contenido — leer antes de escribir nada

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
- Respaldo por Web3Forms **pendiente de activar** (falta la key)

---

## 6. Pendientes, por prioridad

### Bloqueante para lanzar campañas
1. **Key de Web3Forms** — va en `js/main.js` línea 17. Mientras diga
   `'PENDIENTE'`, si WhatsApp falla el lead se pierde. **Decisión del 15 de
   agosto de 2026: se lanza sin ella.** El formulario ya deriva a WhatsApp y eso
   se mide; el riesgo se limita al caso de que WhatsApp falle. Se le pide a
   Andrés en el correo grande, cuando las campañas ya estén corriendo.
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
