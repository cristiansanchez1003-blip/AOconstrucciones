# Auditoría de Google Ads: AO Construcciones (17 de noviembre de 2026)

Campaña "AO - Busqueda - Zona Sur" (24141314300), cuenta 365-657-1293.
Datos sacados por la API de Google Ads y GA4 (solo lectura), desde agosto hasta
el 16 de noviembre. Auditoría hecha con la skill `google-ads-operacion`.
Nada se cambió en la cuenta.

Etiquetas de procedencia de la skill: **[Google]**, **[Agencia/terceros]**,
**[Mixta]**. "Plan ED" = el plan propio de Espíritu Digital, pensado para su
campaña. AO tiene su propia configuración (Maximizar clics, $4.930 diarios), y
se respeta.

## 1. Foto general

| Mes | Clics | Gasto | Conv. medidas | Tasa conv. | Costo/conv. | Cuota de impresiones | Perdida por ranking | Perdida por presupuesto |
|---|---|---|---|---|---|---|---|---|
| Agosto | 192 | $79.045 | 12 | 6,3% | $6.587 | 32% | 51% | 17% |
| Septiembre | 231 | $93.707 | 5 | 2,2% | $18.741 | 30% | 61% | 8% |
| Octubre | 466 | $149.814 | 22 | 4,7% | $6.810 | 27% | 54% | 19% |
| Nov 1–16 | 291 | $83.359 | 25 | 8,6% | $3.334 | 27% | 57% | 15% |

- **La campaña está en su mejor momento**: noviembre lleva la mejor tasa de
  conversión (8,6%) y el costo por conversión más bajo ($3.334).
- **Contactos reales del 1 al 15 de noviembre: 11** (Google midió 25). Cada
  contacto real costó ~$7.600. La diferencia es normal: un clic en WhatsApp
  cuenta como conversión aunque la persona no escriba.
- **Solo aparecemos en 1 de cada 4 búsquedas** donde podríamos salir
  (cuota de impresiones 27%). Lo que más se pierde es por **ranking (57%)**,
  no por presupuesto (15%).

## 2. "Limitada por volumen de búsqueda" y el 65% de optimización

- **El aviso no es el problema de fondo.** Lo causan 14 palabras clave que
  casi nadie busca ("rarely served"): las exactas por comuna ("ampliacion casa
  la florida", "constructora san jose de maipo", "techumbre puente alto") y
  frases largas ("quien hace ampliaciones de casas", "maestro de ampliaciones",
  "panel quebravistas"). No gastan ni hacen daño. **El límite real es el
  ranking**: 57% de las impresiones se pierden porque el anuncio no alcanza
  posición. [Google]
- **El 65% de optimización** sale de 13 recomendaciones de Google. La mayoría
  van contra la estrategia: ampliar a Display, socios de búsqueda, Performance
  Max, imágenes dinámicas y formulario de Google. También hay 7 palabras clave
  sugeridas (algunas en concordancia amplia) y "Maximizar conversiones". **El
  puntaje no mide resultados.** Descartar las que no sirven sube el puntaje sin
  cambiar nada. [Google]

## 3. Hallazgos, de más a menos importante

### 3.1 Experiencia en la página de destino "bajo el promedio" (no cumple) [Google]

Es el hallazgo más importante. Casi todas las palabras clave con nivel de
calidad tienen la **experiencia en la página de destino "Bajo el promedio"**.
Siete tienen nivel de calidad 1 ("baja calidad"): pintura exterior casa,
quincho de ladrillos, porton de fierro, porton metalico, cobertizo de madera,
hacer un quincho y cobertizo para auto.

- **Ampliaciones, Remodelaciones, Techumbres y Obra nueva llevan a la portada**
  (aoconstrucciones.cl/). Solo portones, quinchos y las comunas tienen página
  propia. La skill lo marca como no cumple: "una landing por intención o
  servicio. Nada de mandar todo a la portada" [Agencia/terceros].
- Un nivel de calidad bajo encarece cada clic y baja el ranking. Por eso se
  pierde el 57% de las impresiones.
- **Esto es lo que más frena a Obra nueva y Ampliaciones**, la prioridad de
  Andrés. Las palabras clave de A y D tienen buen CTR esperado y buen anuncio
  ("Sobre el promedio"), pero la página de destino las baja.
- Hoy no se pudo medir la velocidad móvil: la API de PageSpeed agotó su cuota
  diaria. Conviene revisarla a mano en pagespeed.web.dev.

**Recomendación:** páginas propias para Obra nueva y Ampliaciones. Andrés no
quiso pagarlas ($35.000 cada una). Opciones: (a) volver a ofrecérselas con este
dato, (b) que Espíritu Digital haga una como inversión en la campaña, o (c) como
mínimo, mandar A y D a una sección de la portada o del portafolio con obras de
ese tipo (cabe en "ajustes menores").

### 3.2 Obra nueva y Ampliaciones no ganan espacio en el presupuesto [Plan de Andrés]

| Periodo | Gasto A + D | % del gasto | Gasto E (exteriores) | % |
|---|---|---|---|---|
| 4 al 16 nov | $13.376 | 20% | $32.233 | 48% |
| Semana 9–15 nov | $4.744 | 14% | $16.977 | 49% |

Aun así, la semana del 9 al 15 llegaron **3 contactos de A y D** (obra nueva
en San José de Maipo; ampliación y casa desde cero en Las Vertientes). Google
midió **solo 1** en A y **0** en D. Lo más probable es que esos clientes
llamaran o escribieran directo, o que llegaran por el perfil de Google, sin
pasar por el botón medido.

**Recomendación:** se cumple la condición que acordamos ("si no sube su parte
del gasto, separarlos"). Propuesta: **una campaña aparte para Obra nueva y
Ampliaciones con presupuesto propio** (por ejemplo, $1.500 de los $4.930
diarios), sin subir el total del mes. Así Google no puede quitarles
presupuesto para dárselo a portones.

### 3.3 La estrategia de puja, en el momento justo para decidir [Mixta]

- Hoy: Maximizar clics con tope de CPC de $700 (el CPC promedio es de ~$290).
- La campaña ya está cerca de las ~30 conversiones al mes que pedimos para
  pasar a "Maximizar conversiones" (octubre: 22; noviembre va camino a ~45).
  *Verificar antes de usar: el umbral de 30 a 50 conversiones mezcla fuentes
  de Google y de agencias.*
- **Pero hay dos riesgos para AO:**
  1. Las conversiones medidas son sobre todo de E y F (portones y
     constructora). Una puja automática se iría todavía más a portones, justo
     lo contrario de lo que pide Andrés.
  2. Google mide más del doble de los contactos reales (25 contra 11), porque
     cuenta clics en WhatsApp.
- **Recomendación:** seguir con Maximizar clics en la campaña actual. Probar
  Maximizar conversiones recién cuando A y D tengan campaña propia, y solo en
  la campaña de exteriores, que es la que tiene volumen. Decidirlo en el cierre
  del 30 de noviembre.

### 3.4 Concordancia amplia en Exteriores (no cumple con el criterio de la skill) [Plan ED]

Hay 3 palabras clave en concordancia amplia, todas en E:

| Palabra clave | Clics | Conv. | Nivel de calidad |
|---|---|---|---|
| portones corredizos | 117 | 13 | — |
| quincho de ladrillos | 71 | 4 | 1 |
| porton de fierro | 31 | 2 | 1 |

**Recomendación:** "portones corredizos" es la mejor palabra clave de la
cuenta: se deja como está. Pasar "quincho de ladrillos" y "porton de fierro" a
frase. Eso le quita algo de gasto a E y lo deja para el resto.

### 3.5 Anuncio de verano de Exteriores: rinde menos que el original [Agencia/terceros]

Últimos 30 días: el anuncio original (quinchos/portones) tuvo 161 clics y 19
conversiones (11,8%). El de verano (quinchos/verano) tuvo 67 clics y
2 conversiones (3,0%). Los dos tienen fuerza "Promedio". **Recomendación:**
pausar el de verano y mejorar los títulos del original hasta llegar a fuerza
"Buena".

### 3.6 Palabras clave de pintura: poco valor para Andrés [decisión de negocio]

Desde agosto, pintor de casas, pintura de casas, pintar fachada y pintura
exterior casa suman 56 clics, $19.882 y 2 conversiones. "pintor de casas" fue
el término que más gastó en los últimos 30 días ($3.532 y 0 conversiones).
Igual que con el piso vinílico, son trabajos de bajo valor. **Recomendación:**
preguntarle a Andrés si quiere clientes de pintura. Si no, pausarlas libera
unos $6.000 al mes para A y D.

### 3.7 Negativas nuevas (revisión de términos de los últimos 30 días) [Agencia/terceros]

Candidatas (no cargadas):

- **Otras constructoras o marcas:** `prosip`, `neredo`, `panguipulli`,
  `"tu casa facil"`, `"gama beta"`, `"los cedros"`, `concreta`, `aconcagua`,
  `sacyr`, `nps`, `quincheria`, `"casas chile spa"`, `independencia` (comuna
  fuera de la zona).
- **Productos y repuestos:** `ruedas`, `kit`, `fotos`, `"tipos de"`,
  `diseños`, `bodegas`, `"en venta"`, `piscinas`, `vinilicos` (la negativa
  `vinilico` no bloquea el plural).
- **Precio bajo** (en el plan ED van desde el día uno, y calza con lo que
  quiere Andrés): `barato`, `baratos`, `barata`, `baratas`, `economico`,
  `economicos`, `economica`, `economicas` y sus versiones con tilde. Se
  colaron, por ejemplo, "remodelación de cocinas pequeñas económicas",
  "cierres perimetrales economicos" y "cobertizos de madera baratos".
- **Dudosas, para preguntarle a Andrés:** `wpc` y `pvc` (cierres de ese
  material), `malla` (malla para cierre) y `panderetas`.

### 3.8 Horario: madrugada con menos rendimiento [Agencia/terceros]

En 60 días, de 0:00 a 6:59 hubo 99 clics, $33.069 (12% del gasto) y
4 conversiones: 4,0% de conversión, contra 5,8% en promedio. Es una muestra
chica. **Opcional:** programar los anuncios de 7:00 a 23:59. Andrés atiende de
8:00 a 21:00, pero un WhatsApp que llega de noche igual sirve, así que no hay
que cortar la noche.

### 3.9 Lo que está bien (cumple)

- Solo Búsqueda: sin Display ni socios de búsqueda. **Cumple.** [Plan ED]
- Ubicación por "Presencia". **Cumple.** [Plan ED]
- Zona: La Florida, Puente Alto, Pirque y San José de Maipo. Los clics vienen
  de ahí.
- Conversiones primarias: formulario y WhatsApp. **Cumple.** [Plan ED]
  El teléfono (`tel_click`) está "oculto" y no cuenta. El plan lo pide como
  **secundaria**: conviene activarlo como secundaria para verlo en Ads sin que
  optimice.
- 283 negativas, por categorías (académicas, laborales, precio, marcas).
  **Cumple.**
- Recursos: 8 sitelinks, 8 textos destacados con cifras confirmadas por
  Andrés, fragmento estructurado, llamada, logo y 8 imágenes. **Cumple.**
  **Falta un sitelink de Obra nueva y otro de Ampliaciones**, los servicios
  prioritarios.
- Anuncios: todos aprobados. Fuerza "Excelente" en D y F, "Buena" en A, B y C,
  "Promedio" en E.
- Dispositivos: el 90% de los clics viene del celular, con la misma tasa de
  conversión que el computador. Sin ajustes.
- Techumbres bajó por temporada (terminaron las lluvias). Su mejor palabra
  clave, "reparacion de techumbre", lleva 7 conversiones. Se deja activa para
  el próximo otoño.

## 4. Plan propuesto, por orden

**Actualización del 17 de noviembre:** Cristian aprobó los puntos 1 al 5 y
quedaron aplicados ese mismo día (detalle en `ESTADO-PROYECTO.md`, "Cambios
aplicados en Google Ads"). Del punto 2 solo se pausó el anuncio de verano; los
títulos del original no se tocaron.

| # | Acción | Quién decide | Impacto esperado |
|---|---|---|---|
| 1 | Cargar las negativas de 3.7 (sin las dudosas) | Cristian | Menos gasto en curiosos y marcas |
| 2 | Pausar el anuncio de verano y mejorar los títulos del original de E | Cristian | Mejor tasa de conversión en E |
| 3 | Pasar "quincho de ladrillos" y "porton de fierro" de amplia a frase | Cristian | Menos gasto disperso en E |
| 4 | Sitelinks "Casas desde cero" y "Ampliaciones y 2° piso" | Cristian | Más visibilidad para A y D |
| 5 | Activar `tel_click` como conversión secundaria | Cristian | Ver las llamadas desde la web |
| 6 | Preguntarle a Andrés por la pintura (y por wpc, pvc, malla y panderetas) | Andrés | Más presupuesto para A y D |
| 7 | Campaña aparte para Obra nueva y Ampliaciones con presupuesto propio | Cristian y Andrés | El presupuesto de A y D queda asegurado |
| 8 | Página propia para Obra nueva (y después Ampliaciones) | Cristian y Andrés | Mejor nivel de calidad y menos impresiones perdidas por ranking |
| 9 | Decidir la estrategia de puja en el cierre del 30 de noviembre | Cristian | — |
| 10 | Descartar las recomendaciones de Google que no aplican | Cristian | El puntaje sube; los resultados no cambian |
| 11 | Preguntarle a Andrés cómo lo contactaron los clientes de A y D | Andrés | Saber si la medición se está perdiendo contactos |
