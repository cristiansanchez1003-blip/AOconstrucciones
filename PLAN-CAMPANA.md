# Plan de carga — Campaña de Búsqueda

Complemento operativo de [`estrategia-google-ads.md`](estrategia-google-ads.md).
Ese documento define la estrategia y el porqué. **Este es del que se copia y se
pega**: trae los textos finales de los 6 grupos, las pujas, las URLs y el orden
de carga.

**Creado:** 15 de agosto de 2026 · **Actualizado:** 15 de agosto de 2026 con las
respuestas de Andrés

---

## 1. Puja: qué se puede y qué no

> **Corregido el 15 de agosto de 2026, verificado en la interfaz.** Una versión
> anterior de este documento recomendaba **CPC manual con puja por grupo**. Eso
> **no es posible**: Google eliminó el CPC manual del flujo de creación. Las
> únicas opciones que ofrece son Maximizar conversiones, CPA objetivo, Maximizar
> valor de conversión, ROAS objetivo, Clics e Impresiones.

La estrategia §7 pide **Maximizar clics con límite de CPC $700**, y aparte un
**tope de $500 solo para el Grupo F**. Esas dos cosas no se pueden tener a la vez.

Con Maximizar clics, el límite de CPC se define **a nivel de campaña**. Las pujas
por grupo quedan guardadas pero **no se usan**: Google fija la puja de cada
subasta por su cuenta. No hay forma de darle a un grupo un techo distinto, y sin
CPC manual tampoco hay forma de esquivarlo.

**Lo que queda configurado:** Clics, con límite de CPC de **CLP 700** para toda
la campaña. Es la Fase 1 de la estrategia §7, tal cual.

### Qué se pierde y por qué importa poco por ahora

El orden de margen que mandó Andrés no se puede expresar en las pujas. Un lead de
obra nueva y uno de piso vinílico se pagan igual.

En la práctica el costo es bajo: Google estima **CPC de CLP 128 a 302** para esta
campaña, muy por debajo del techo de 700. Un tope que casi nunca se toca no
diferencia nada aunque se pudiera fijar por grupo.

**Dónde sí se va a expresar el margen:** en la Fase 2, al migrar a Maximizar
conversiones con **valores de conversión relativos** derivados del orden de
Andrés. Ver §2. Ese es el mecanismo correcto y no depende del CPC manual.

---

## 2. El orden de margen y dónde se usa

Orden que mandó Andrés el 15 de agosto de 2026, de mayor a menor margen:

| # | Servicio | Grupo |
|---|---|---|
| 1 | Proyectos desde cota cero | D — Obra nueva |
| 2 | Ampliaciones | A — Ampliaciones |
| 3 | Remodelaciones interiores y exteriores | B — Remodelaciones |
| 4 | Fabricación de quinchos | E — Exteriores |
| 5 | Montaje de cobertizos | E — Exteriores |
| 6 | Fabricación de portones | E — Exteriores |
| 7 | Fabricación y reparación de techumbre | C — Techumbres |
| 8 | Instalación de quebravistas | E — Exteriores |
| 9 | Fabricación de deck | E — Exteriores |
| 10 | Instalación de piso vinílico | B — Remodelaciones |
| 11 | Proyectos de pintura y fachadas | B — Remodelaciones |

**No se puede usar en las pujas** — ver §1. Se usa en dos lugares:

**Ahora, en la lectura de resultados.** Al revisar el informe de términos de
búsqueda y decidir qué pausar, un lead de obra nueva vale más que uno de pintura
aunque hayan costado lo mismo. El orden es el criterio para decidir.

**En la Fase 2, en los valores de conversión.** Al migrar a Maximizar
conversiones, se asignan valores relativos en GA4 siguiendo este orden. A Smart
Bidding le sirve la **proporción** entre conversiones, no el monto absoluto — por
eso funciona aunque Andrés no haya querido dar el ticket promedio.

**Sobre el Grupo C.** La estrategia lo marca como prioritario y sigue siéndolo
aunque el margen lo deje séptimo: tiene el volumen creciente (+350% interanual) y
las pujas más baratas de la investigación ($24–$311). Es el motor de volumen y de
aprendizaje de la cuenta. Que deje menos por obra no lo hace menos importante
para juntar los primeros datos.

**Sobre el Grupo F.** La estrategia §10.2 pide un tope de $500 que **no se puede
aplicar** por grupo. Queda bajo el techo único de $700, así que hay que vigilarlo
con el informe de términos de búsqueda en vez de con la puja. Es el de mayor
volumen y mayor riesgo de la cuenta.

### Valor por conversión: no va a haber monto

La estrategia §7 pide asignar valor a las conversiones usando **ticket promedio ×
tasa de cierre**. Andrés mandó el orden de margen pero **no quiso dar el monto**,
y no se va a insistir.

No bloquea nada. Cuando llegue el momento de migrar a puja por valor —fase 2 o 3,
recién con 15–20 conversiones acumuladas— se usan **valores relativos** derivados
del orden de margen en vez de pesos reales. A Smart Bidding le sirve la
proporción entre conversiones, no la cifra absoluta: si obra nueva vale 100 y
pintura 20, optimiza igual de bien que con montos verdaderos.

Lo que sí se pierde es poder responder "¿el costo por lead es rentable?" con un
número. Esa pregunta queda para cuando Andrés quiera darlo, si alguna vez quiere.

---

## 3. Textos de anuncio — versión final

Los 6 grupos, 15 títulos y 4 descripciones cada uno. **Copiar de acá**, no de la
estrategia §8: esa versión no tiene los Grupos E y F, no llega a 15 títulos y no
incluye los servicios nuevos.

Validado con `tools-validar-anuncios.py`: títulos ≤30, descripciones ≤90, sin
precios, sin plazos, sin garantías, sin "cota cero", sin conteo de obras por comuna.

### Grupo A — Ampliaciones

**Títulos**
```
Ampliaciones de Casa
Ampliamos Tu Casa
Constructora Zona Sur
El Dueño Te Visita
Cotización Sin Costo
Ampliación Segundo Piso
Cerramos Tu Terraza
Puente Alto y La Florida
Cajón del Maipo y Pirque
Constructora con Trayectoria
Visita Técnica a Terreno
Hablas Directo con el Dueño
Ampliaciones Residenciales
Obras Ejecutadas en Tu Zona
Ampliaciones en Tu Comuna
```

**Descripciones**
```
Ampliaciones de vivienda en Puente Alto, La Florida, Pirque y Cajón del Maipo.
El dueño visita tu casa, revisa el proyecto contigo y prepara la cotización sin costo.
Constructora local. Trabajamos en tu zona y conocemos el terreno donde construyes.
Cuéntanos qué necesitas por WhatsApp y coordinamos una visita a tu domicilio.
```

### Grupo B — Remodelaciones

Incluye los servicios nuevos de **piso vinílico** y **pintura y fachadas**.

**Títulos**
```
Remodelación de Casas
Remodelamos Tu Cocina
Remodelación de Baños
Constructora Zona Sur
El Dueño Te Visita
Cotización Sin Costo
Remodelación Integral
Puente Alto y La Florida
Cajón del Maipo y Pirque
Renovamos Tu Hogar
Coordina por WhatsApp
Cambio de Cerámica
Remodelación de Escaleras
Instalación Piso Vinílico
Pintura y Fachadas
```

**Descripciones**
```
Remodelación de cocinas, baños, pisos y pintura en Puente Alto, La Florida y Pirque.
El dueño va a tu casa, conversan el proyecto y recibes la cotización sin costo.
Constructora local. Ejecutamos remodelaciones residenciales en tu misma comuna.
Escríbenos por WhatsApp con lo que tienes en mente y coordinamos la visita.
```

### Grupo C — Techumbres

**Títulos**
```
Cambio de Techumbre
Reparación de Techos
¿Techo con Goteras?
Solución a Filtraciones
Constructora Zona Sur
Revisión Sin Costo
Cambio de Planchas de Zinc
Puente Alto y La Florida
Atendemos el Cajón del Maipo
Techumbre Residencial
Te Visitamos y Evaluamos
Escríbenos por WhatsApp
Techumbre en Tu Comuna
Reparamos Tu Techo
Cotización Sin Costo
```

**Descripciones**
```
Reparación y cambio de techumbre en Puente Alto, La Florida, Pirque y Cajón del Maipo.
¿Filtraciones o goteras? Vamos a terreno, revisamos el techo y cotizamos sin costo.
Constructora local con trayectoria. Trabajamos techumbres residenciales en tu comuna.
Escríbenos por WhatsApp y coordinamos la visita técnica cuando te acomode.
```

### Grupo D — Obra nueva

**Títulos**
```
Construcción de Casas
Construimos en Tu Terreno
¿Tienes un Terreno?
Constructora Zona Sur
El Dueño Te Visita
Cotización Sin Costo
Construcción en Parcela
Cajón del Maipo y Pirque
Puente Alto y La Florida
Constructora con Trayectoria
Visitamos Tu Terreno
Conversa con el Dueño
Construimos Desde Cero
Obra Nueva Residencial
200+ Obras Ejecutadas
```

**Descripciones**
```
Construcción de casas en Cajón del Maipo, Pirque, Puente Alto y La Florida.
Vamos a tu terreno, evaluamos las condiciones y preparamos la cotización sin costo.
Constructora local. Conocemos el terreno y la normativa de la zona donde construyes.
Cuéntanos de tu proyecto por WhatsApp y coordinamos una visita a tu terreno.
```

### Grupo E — Exteriores

Incluye los servicios nuevos de **cobertizos**, **portones** y **quebravistas**.

**Títulos**
```
Construcción de Quinchos
Montaje de Cobertizos
Fabricación de Portones
Instalación de Quebravistas
Construcción de Terrazas
Terraza Techada
Decks para Tu Patio
Cierres Perimetrales
Constructora Zona Sur
El Dueño Te Visita
Cotización Sin Costo
Puente Alto y La Florida
Cajón del Maipo y Pirque
Coordina por WhatsApp
Obras Ejecutadas en Tu Zona
```

**Descripciones**
```
Quinchos, cobertizos, terrazas, decks y portones en Puente Alto, La Florida y Pirque.
El dueño visita tu casa, conversan el proyecto y recibes la cotización sin costo.
Constructora local. Trabajamos exteriores residenciales en tu misma comuna.
Cuéntanos qué tienes en mente por WhatsApp y coordinamos la visita a terreno.
```

### Grupo F — Genérico local

**Títulos**
```
Constructora en Puente Alto
Constructora en La Florida
Constructora Cajón del Maipo
Constructora Zona Sur
Constructora Local
15 Años de Trayectoria
200+ Obras Ejecutadas
El Dueño Te Visita
Cotización Sin Costo
Ampliaciones y Remodelaciones
Techumbres y Obra Nueva
Visita Técnica a Domicilio
Hablas Directo con el Dueño
Atendemos Todos los Días
Coordina por WhatsApp
```

**Descripciones**
```
Constructora en Puente Alto, La Florida, Pirque y Cajón del Maipo. Cotización sin costo.
Ampliaciones, remodelaciones, techumbres y obra nueva. Más de 200 obras ejecutadas.
El dueño visita tu casa, revisa el proyecto contigo y prepara la cotización sin costo.
Escríbenos por WhatsApp y coordinamos una visita a tu domicilio cuando te acomode.
```

---

## 4. Keywords de los servicios nuevos

Se suman a las de la estrategia §4. Todas en **concordancia de frase**, siguiendo
el criterio del §3 de la estrategia.

### Al Grupo E — Exteriores

```
montaje de cobertizo
construccion de cobertizo
cobertizo para auto
cobertizo de madera
fabricacion de portones
porton metalico
porton corredero
reparacion de porton
instalacion de quebravistas
quebravistas para terraza
panel quebravistas
```

> `reparacion de porton` tiene respaldo real: hay una obra con ese nombre en el
> portafolio, en Las Vertientes.

### Al Grupo B — Remodelaciones

```
instalacion de piso vinilico
instalador piso vinilico
piso vinilico para casa
pintura de casas
pintar fachada
pintor de casas
pintura exterior casa
```

> ⚠️ **Vigilar `piso vinilico`.** Es un producto que se compra en retail, así que
> buena parte del volumen es gente buscando dónde comprarlo, no quién se lo
> instale. Las negativas de la §5.4 de la estrategia (`comprar`, `venta de`,
> `precio metro cuadrado material`, `sodimac`, `easy`) cubren lo grueso, pero es
> el término a revisar primero en el informe de términos de búsqueda.

---

## 5. Negativas: correcciones a la lista

Andrés respondió el 15 de agosto de 2026 y eso cierra lo que la estrategia §5
dejaba abierto.

### Sacar de negativas

| Término | Sección | Por qué |
|---|---|---|
| `pintor` | 5.11 | **Hace "Proyectos de Pintura y Fachadas"**, es servicio propio. |
| `movimiento de tierra` | 5.12 | El JSON-LD del home describe la obra nueva como "desde fundaciones y **movimiento de tierra** hasta la entrega llave en mano". Servicio propio, no obra pública. |
| `faena` | 5.12 | Palabra de uso corriente en construcción en Chile. **Cargar solo si aparece basura real** en el informe de términos. |

### Resto del bloque 5.11 — se mantiene

`gasfiter`, `gasfiteria`, `electricista`, `cerrajero`, `mudanza`, `fletes`,
`aseo`, `jardineria`, `fumigacion`, `desabolladura`: no están en la lista de
servicios de Andrés.

> ⚠️ **Ojo con `cerrajero`.** En Chile "cerrajería" también nombra al taller que
> **fabrica portones metálicos**, y Andrés fabrica portones. Se deja como negativa
> por ahora —el grueso de esas búsquedas es apertura de cerraduras— pero hay que
> mirar el informe de términos las primeras semanas. Si aparece intención real de
> portón, se retira.

### Bloque 5.8 — prefabricadas: la respuesta fue intermedia

Andrés **no fabrica** casas prefabricadas, pero **sí las instala**. La estrategia
asumía un sí o un no.

**Decisión: cargar 5.8 completo igual, por ahora.** El motivo es aritmético. Una
negativa amplia como `prefabricada` bloquea cualquier consulta que la contenga,
incluida "instalación de casa prefabricada". No hay forma de dejar pasar solo la
intención de instalación con negativas a nivel de campaña: la frase del comprador
está contenida dentro de la frase del instalador.

El tráfico de "casas prefabricadas" es de gente que quiere **comprar una casa**,
tiene volumen alto y no es cliente. Con $4.930 diarios, dejarlo entrar para
capturar la cola de instalación sale más caro de lo que rinde.

**Cuando haya datos**, la salida limpia es un grupo propio de instalación con las
negativas de 5.8 movidas a nivel de grupo en los demás. No antes.

---

## 6. Recursos — versión final

Correcciones sobre lo redactado en `ESTADO-PROYECTO.md` §9 y en la estrategia §9.
El límite de un enlace de sitio es **25 caracteres** en el texto y **35** en cada
línea de descripción. El de un texto destacado es **25**.

### Enlaces de sitio

| Texto | Descripción 1 | Descripción 2 | URL |
|---|---|---|---|
| Ver obras ejecutadas | Fotos reales del proceso | Y del resultado final | `/portafolio.html` |
| Cotiza tu proyecto | Cuéntanos qué necesitas | Solo nombre y teléfono | `/#contacto` |
| Obras en Puente Alto | Obras en Hacienda El Peñón | Y Condominio La Vizcachas | `/constructora-puente-alto.html` |
| Obras en La Florida | Remodelaciones y techumbres | Atención directa del dueño | `/constructora-la-florida.html` |
| Cajón del Maipo | Las Vertientes y El Manzano | El Canelo y San Gabriel | `/constructora-san-jose-de-maipo.html` |

**Qué cambió y por qué:**

- `Constructora en Puente Alto` (27) y `Constructora en La Florida` (26) se
  pasaban del límite de 25. Ahora son `Obras en...`.
- El enlace de Cajón del Maipo decía **"15 obras en la zona"**. Eso es publicar
  conteo de obras por comuna, prohibido por la regla 2 del `ESTADO-PROYECTO.md` y
  por la regla permanente 2 de la estrategia. Reemplazado por sectores, que sí se
  pueden nombrar.

### Textos destacados

```
Cotización sin costo
El dueño va a terreno
15 años de experiencia
200+ obras ejecutadas
Atención todos los días
Sin intermediarios
Constructora local
```

`El dueño visita en terreno` (26), `Trato directo, sin intermediarios` (33) y
`Atención directa del dueño` (26) se pasaban del límite.

### Fragmento estructurado

Encabezado **`Servicios`**. La estrategia proponía `Catálogo de servicios`, que no
está en la lista cerrada de encabezados que acepta Google; `Servicios` sí.

```
Ampliaciones · Remodelaciones · Techumbres · Construcción · Terrazas · Quinchos
```

### Recurso de llamada

Número **+56 9 7992 5812**, con horario **8:00–21:00 todos los días**.

Es distinto del horario de la campaña, que va 24/7, y las dos cosas conviven: la
campaña corre siempre, pero el número solo se muestra cuando hay alguien que
conteste. Un clic a llamar a las 3 AM se paga y no se contesta.

Activar **informes de llamadas** con duración mínima de **60 segundos**, para
filtrar toques accidentales. Verificar si Google ofrece números de desvío en
Chile; la disponibilidad varía por país.

### Recurso de ubicación

Vincular el **Perfil de Empresa**: `https://share.google/K1ZzYydFXDxCS9WZD`

---

## 7. URLs de destino

La estrategia no las define.

**Regla general:** el anuncio del grupo apunta al **home**, que cubre todos los
servicios. Las keywords que nombran una comuna llevan **URL final a nivel de
keyword** hacia su landing. Así se aprovechan las landings sin dividir la campaña
por comuna, que es lo que la estrategia §6 dice explícitamente que no hay que hacer.

| Grupo | URL del anuncio |
|---|---|
| A, B, C, D, E, F | `https://aoconstrucciones.cl/` |

**URLs a nivel de keyword:**

| Keyword | URL final |
|---|---|
| `ampliacion casa puente alto` | `/constructora-puente-alto.html` |
| `ampliacion casa la florida` | `/constructora-la-florida.html` |
| `techumbre puente alto` | `/constructora-puente-alto.html` |
| `constructora puente alto` | `/constructora-puente-alto.html` |
| `constructora la florida` | `/constructora-la-florida.html` |
| `constructora cajon del maipo` | `/constructora-san-jose-de-maipo.html` |
| `constructora san jose de maipo` | `/constructora-san-jose-de-maipo.html` |

> **Pirque no tiene landing.** Está en las 4 comunas de segmentación y aparece en
> los textos de anuncio, pero no hay página propia ni obras registradas. Su
> tráfico cae al home. No es bloqueante; queda como la primera landing a crear si
> Pirque muestra volumen.

---

## 8. Decisiones reconciliadas

| Tema | Resolución |
|---|---|
| **Horario de la campaña** | **24/7, sin segmentar.** Manda la estrategia §7: el presupuesto va a sobrar, restringir horas solo quita inventario en un mercado ya chico. Se revisa el informe por hora en el mes 2. |
| **Horario del recurso de llamada** | **8:00–21:00.** Ver §6. |
| **Estrategia de puja** | **CPC manual con puja por grupo**, no Maximizar clics. Ver §1 y §2. |
| **Web3Forms** | La estrategia lo marca bloqueante en §13. **Se lanza igual sin él.** El formulario ya deriva a WhatsApp y eso se mide. |
| **Ajuste móvil +15%** | **No cargarlo el día 1.** Se aplica cuando los datos confirmen que el tráfico es móvil. |
| **Riesgo 10.5 — respuesta al WhatsApp** | **Cerrado.** Contesta Andrés, dentro del horario, rápido. Era el riesgo más grande del proyecto. |

---

## 8-bis. Estado de la carga al 15 de agosto de 2026

**La campaña está publicada y pausada.**

```
Nombre        AO - Busqueda - Zona Sur
ID            24141314300
Estado        Paused
Cuenta        CLP 0/día · 0 impresiones · 0 clics · CLP 0 gastado
```

Al publicar, Google la dejó **activa** (`Eligible (Learning)`) y se pausó
enseguida. No alcanzó a gastar nada: las keywords quedan en revisión al crear una
campaña en cuenta nueva, así que no hay entrega inmediata.

> **Al publicar, Google ofrece "Set up with a Google Tag". Rechazar.** El sitio ya
> tiene GTM-TWJVTWLD con GA4 y las conversiones importadas. Instalar otro tag
> duplicaría la medición y ensuciaría los datos que costó dejar limpios.

**Verificado en la interfaz, correcto:**

| Ajuste | Estado |
|---|---|
| Nombre | `AO - Busqueda - Zona Sur` |
| Tipo | Búsqueda |
| Search Partners | Desmarcado |
| Display | Desmarcado |
| Ubicaciones | Las 4 comunas |
| **Opción de ubicación** | **Presence: people in or regularly in** |
| Presupuesto | CLP 4.930/día |
| Puja | Clics, tope CLP 700 |
| Horario | All day (24/7) |
| Rotación | Optimizar |
| Inicio | 15 ago 2026, sin término |

**También verificado, y ya correcto — no hay que tocarlo:**

| Ajuste | Estado |
|---|---|
| **AI Max** | **Apagado**, a nivel de campaña y de grupo |
| **Text customization** | **Apagada** |
| **Final URL expansion** | **Apagada** |

Las dos últimas figuraban encendidas al leer el resumen a medio cargar. Con la
configuración ya recorrida, la pantalla de AI Max las reporta apagadas:
*"Asset optimization: Text customization and Final URL expansion turned off"*.
Conviene confirmarlo una vez más después de publicar.

### Cargado el 17 de agosto de 2026

La campaña quedó **llena y pausada**. Publicado desde Google Ads Editor:

- **6 grupos**, en Habilitado. `Ad group 1` ya no existe.
- **67 keywords**, 170 negativas de campaña, 6 anuncios responsivos.
- **3 de los 5 enlaces de sitio**, a nivel de campaña, en revisión:
  Ver obras ejecutadas · Cotiza tu proyecto · Obras en Puente Alto.
- **El fragmento estructurado**, encabezado `Servicios` en **español**, con sus
  6 valores: Ampliaciones · Remodelaciones · Techumbres · Construcción ·
  Terrazas · Quinchos.
- **Los 7 textos destacados**, a nivel de campaña: Cotización sin costo ·
  El dueño va a terreno · 15 años de experiencia · 200+ obras ejecutadas ·
  Atención todos los días · Sin intermediarios · Constructora local.

> **Al cargar recursos, fijar siempre "Add to: Campaign"** y elegir
> `AO - Busqueda - Zona Sur`. El formulario viene en **Account** por defecto, y
> a nivel de cuenta los recursos se aplicarían también a campañas futuras.
>
> El check de la campaña en el diálogo *Select campaigns* **no responde al clic
> por coordenada**; hay que apuntar al checkbox mismo.

Ruta de los recursos, que tampoco es adivinable por URL:
**Assets → Assets**, o sea `ads.google.com/aw/assetreport/associations`.
El menú de recursos recién aparece cuando la cuenta tiene una campaña.

**Pendiente, en este orden:**

0. **Los 2 enlaces de sitio que faltan** (§6): `Obras en La Florida` y
   `Cajón del Maipo`.
0b. **El recurso de llamada.** **No se guardó.** Lo que ya se sabe del
   formulario, para no redescubrirlo:
   - País **Chile** (no United States, que es el default), número **979925812**
     sin el +56 ni el 9 inicial. El ejemplo que muestra es `600 123 456`.
   - **"Call reporting on"** ya viene activado por defecto.
   - El horario está en *Advanced options* → *Days and hours*, que arranca en
     `All days, 12:00 AM a 12:00 AM`. **Hay que dejarlo 8:00 AM – 9:00 PM.**
     Los desplegables de hora no responden bien a la automatización; se hace
     más rápido a mano.
   - No guardarlo con el horario en 24/7: un clic a llamar de madrugada se
     paga y no se contesta.
0c. **El recurso de ubicación** con el Perfil de Empresa.
1. **Borrar el borrador `Campaign #1`** (CLP 1.000/día), basura de un intento
   previo. No gasta nada, pero ensucia la cuenta.
2. **Borrar el grupo `Ad group 1`**, temporal, con 3 keywords y 3 títulos del
   Grupo A. Se creó solo para poder cerrar el asistente, que no deja avanzar sin
   al menos un grupo y un anuncio. **Borrarlo recién después de subir los CSV**,
   porque una campaña sin ningún grupo puede dar problemas.
3. **Subir los 4 CSV** de `ads-csv/`, generados con `tools-generar-csv-ads.py`.
   Ver §8-ter: la carga masiva está a medio resolver.
4. **Cargar los recursos** de la §6.
5. **Verificar** con la §10.
6. **Encender la campaña.** Ese botón lo aprieta Cristian, no antes de que la
   §10 esté completa.

### Cómo llegar al botón de publicar, si hay que repetirlo

La pantalla de Review se queda pegada en *"Checking for errors…"* y no dibuja
`Publish campaign` si se llega por URL directa. Lo que sí funciona:

1. Campañas → pestaña `Drafts` → `Finish` en el borrador.
2. Navegar por el rail lateral hasta **Budget**.
3. Apretar **Next** desde Budget. Ahí el resumen carga completo y aparece el botón.

> **Ojo con las "Recommendations" del resumen.** Traen un botón `Apply all` que
> agrega keywords elegidas por Google, saltándose la lista curada y las
> concordancias decididas. **No aplicarlas.**

---

## 8-ter. Carga masiva: dónde está trabada

**Dónde vive la herramienta.** No es adivinable por URL: se llega por
**Tools → Bulk actions → Uploads**, y la ruta real es
`ads.google.com/aw/bulk/uploads`. Intentar `/aw/bulkactions/uploads`,
`/aw/bulkupload` o `/aw/uploads` da 404.

**El flujo.** `+ New Upload` → `Select source` → `Upload a file` → elegir el
archivo → **`Preview`** → revisar → `Apply`.

> **Usar siempre `Preview` antes de `Apply`.** Muestra cuántos cambios, cuántos
> exitosos y cuántos errores, sin tocar la cuenta. Los dos intentos hechos hasta
> ahora fallaron completos, y gracias al preview no se aplicó nada.

### Errores encontrados, en orden

**1. `Missing value in "Customer ID"` — resuelto.** El alcance del upload viene
en "Multiple accounts", que exige identificar la cuenta en cada fila.
`tools-generar-csv-ads.py` ahora antepone `Customer ID = 365-657-1293` a los
cuatro archivos.

**2. `Missing value in "Campaign ID"` — sin resolver.** Se agregó
`Campaign ID = 24141314300` a todas las filas y el error persiste igual. El
preview sí resuelve bien la cuenta, el nombre de campaña y los nombres de grupo,
así que el archivo se entiende: lo que falla es el esquema de columnas.

### Cómo cerrarlo

Dejar de adivinar encabezados. La página tiene un **`Download template
(optional)`** justo arriba del selector de origen. Bajar esa plantilla, mirar sus
encabezados exactos y ajustar `tools-generar-csv-ads.py` para que los replique.

**Alternativa, probablemente más rápida:** hacer la carga con **Google Ads
Editor**, la aplicación de escritorio gratuita de Google. Es la herramienta
estándar para construir campañas en volumen, acepta pegar keywords y anuncios
directo desde una planilla, valida offline y publica todo de una vez.

---

## 9. Paso a paso de lo que falta

La campaña ya existe, publicada y pausada, con toda su configuración correcta
(§8-bis). Lo que falta es llenarla y encenderla.

Antes de empezar, regenerar los archivos:

```bash
python tools-generar-csv-ads.py
```

Deja dos carpetas con los mismos datos en formatos distintos:
`ads-csv/` para la carga web y `ads-csv-editor/` para Google Ads Editor.

---

### Paso 1 — Cargar los 6 grupos, keywords, anuncios y negativas

**Recomendado: Google Ads Editor.** Es gratis, es de Google y está hecho para
esto. Evita el problema de esquema de columnas que dejó trabada la carga web
(§8-ter).

1. Bajar e instalar desde `ads.google.com/intl/es/home/tools/ads-editor/`.
2. Abrir, iniciar sesión con **espiritudigital.chile@gmail.com**, y descargar la
   cuenta **AO Construcciones (365-657-1293)**.
3. Seleccionar la campaña `AO - Busqueda - Zona Sur`.
4. **Grupos de anuncios:** ir a *Grupos de anuncios* → *Hacer varios cambios* →
   pegar el contenido de `ads-csv-editor/1-grupos.csv`.
5. **Keywords:** *Palabras clave* → *Hacer varios cambios* → pegar
   `ads-csv-editor/2-keywords.csv`.
6. **Negativas:** *Palabras clave negativas de campaña* → *Hacer varios cambios*
   → pegar `ads-csv-editor/3-negativas.csv`.
7. **Anuncios:** *Anuncios* → *Anuncios de búsqueda responsivos* → *Hacer varios
   cambios* → pegar `ads-csv-editor/4-anuncios.csv`.
8. Revisar los errores que marque Editor y corregir.
9. **Publicar** con el botón *Publicar*.

**Alternativa: carga web.** Tools → Bulk actions → Uploads, con los archivos de
`ads-csv/`. Está trabada en `Missing value in "Campaign ID"`; para destrabarla
hay que bajar el `Download template` de esa misma pantalla y copiar sus
encabezados exactos. Siempre usar `Preview` antes de `Apply`.

---

### Paso 2 — Limpiar

1. **Borrar el grupo `Ad group 1`** — el temporal con 3 keywords. Recién después
   de que los 6 grupos reales existan.
2. **Borrar el borrador `Campaign #1`** (CLP 1.000/día), de un intento previo.
   Campañas → pestaña *Drafts* → seleccionarlo → *Editar* → *Quitar*.

---

### Paso 3 — Cargar los recursos

Todos a nivel de campaña. Los textos exactos están en la §6.

1. **5 enlaces de sitio** con sus dos descripciones y su URL.
2. **7 textos destacados.**
3. **Fragmento estructurado**, encabezado `Servicios`, con los 6 valores.
4. **Recurso de llamada:** +56 9 7992 5812, **con horario 8:00–21:00**. Distinto
   del horario de la campaña, que va 24/7.
5. **Activar informes de llamadas**, duración mínima **60 segundos**. Verificar
   si Google ofrece números de desvío en Chile.
6. **Recurso de ubicación:** vincular el Perfil de Empresa
   `https://share.google/K1ZzYydFXDxCS9WZD`.

---

### Paso 4 — Verificar antes de encender

La lista completa está en la §10. Lo que no se puede saltar:

- `python tools-validar-anuncios.py` en verde.
- Las 4 URLs de destino cargan, el formulario avanza sus 2 pasos y WhatsApp responde.
- GA4 con DebugView: `generate_lead` y `whatsapp_click` disparan desde un móvil real.
- En Ads: ambas conversiones **Primary**, conteo "una por sesión".
- Que **"Presence"** siga puesto en la segmentación de ubicación.
- Que `Text customization` y `Final URL expansion` sigan **apagadas**.

---

### Paso 5 — Encender

Campañas → el punto de estado de `AO - Busqueda - Zona Sur` → **Enable**.

**A las 48 horas:** informe de términos de búsqueda y primera ronda de negativas.
Es donde se fuga el presupuesto más rápido. Vigilar primero el Grupo F
(`constructora`) y la keyword `piso vinilico`, que es la de mayor riesgo de traer
gente que quiere comprar el material en vez de contratar la instalación.

---

## 10. Verificación antes de encender

1. `python tools-validar-anuncios.py` — cero recursos fuera de límite.
2. Abrir las 4 URLs de destino: cargan, el formulario avanza los 2 pasos, el
   botón de WhatsApp responde.
3. GA4 con DebugView abierto: enviar el formulario y hacer clic en WhatsApp desde
   un móvil real. Confirmar `generate_lead` y `whatsapp_click`.
4. En Ads: ambas conversiones **Primary**, conteo "una por sesión", y "Vista de
   una página" en Secondary y fuera de los objetivos.
5. Vista previa de anuncios de Ads — no búsquedas reales, que inflan impresiones.
6. Horario 8:00–21:00 idéntico en web, JSON-LD, Perfil de Empresa y recurso de
   llamada.
7. Que los servicios nombrados en los anuncios aparezcan en la página de destino.

A las 48 horas: informe de términos de búsqueda y primera ronda de negativas. Es
donde se fuga el presupuesto más rápido.
