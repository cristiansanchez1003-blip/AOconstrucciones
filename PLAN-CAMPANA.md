# Plan de carga — Campaña de Búsqueda

Complemento operativo de [`estrategia-google-ads.md`](estrategia-google-ads.md).
Ese documento define la estrategia y el porqué. **Este es del que se copia y se
pega**: trae los textos finales de los 6 grupos, las pujas, las URLs y el orden
de carga.

**Creado:** 15 de agosto de 2026 · **Actualizado:** 15 de agosto de 2026 con las
respuestas de Andrés

---

## 1. Problema en la estrategia de puja

La estrategia §7 pide **Maximizar clics con límite de CPC $700**, y aparte un
**tope de $500 solo para el Grupo F**. Esas dos cosas no se pueden tener a la vez.

Con Maximizar clics, el límite de CPC se define **a nivel de campaña** o de la
estrategia de portafolio. Las pujas por grupo de anuncios quedan guardadas pero
**no se usan**: Google fija la puja de cada subasta por su cuenta. No hay forma
de darle a un grupo un techo distinto.

Esto importaba poco cuando todos los grupos valían lo mismo. Ahora que Andrés
mandó los servicios **ordenados por margen**, importa mucho: un lead de obra
nueva no vale lo mismo que uno de piso vinílico, y con un techo único se paga lo
mismo por los dos.

### Solución: CPC manual con puja por grupo

Para arrancar, **CPC manual sin optimizador de CPC**, con puja máxima por grupo.
Es lo que corresponde a una cuenta sin historial de conversiones: el algoritmo no
tiene con qué aprender, así que se le dice explícitamente cuánto vale cada cosa.

Se migra a Maximizar conversiones al acumular 15–20 conversiones, tal como dice
la estrategia §7 fase 2. Ahí el margen se expresa con valores de conversión, no
con pujas.

---

## 2. Pujas por grupo

El orden de margen que mandó Andrés (a–k, de mayor a menor) cruzado con el
volumen y las pujas observadas en el Planificador.

**El criterio:** el margen define **cuánto se está dispuesto a pagar**; el volumen
define **de dónde van a llegar los clics**. No son lo mismo y no se contradicen.

| Grupo | Servicios (puesto en la lista de margen) | Puja máx. |
|---|---|---|
| **D — Obra nueva** | Cota cero (1º) | **$900** |
| **A — Ampliaciones** | Ampliaciones (2º) | **$800** |
| **B — Remodelaciones** | Remodelaciones int/ext (3º), piso vinílico (10º), pintura y fachadas (11º) | **$700** |
| **E — Exteriores** | Quinchos (4º), cobertizos (5º), portones (6º), quebravistas (8º), deck (9º) | **$600** |
| **C — Techumbres** | Techumbre (7º) | **$450** |
| **F — Genérico local** | Todos | **$500** |

**Sobre el Grupo C.** La estrategia lo marca como prioritario y sigue siéndolo,
aunque el margen lo deje séptimo. Las pujas observadas ahí son de $24 a $311, así
que un techo de $450 ya está muy por encima del mercado: va a ganar impresiones
barato igual. Sigue siendo el motor de volumen y de aprendizaje de la cuenta, solo
que ahora no se le paga como si fuera obra nueva.

**Sobre el Grupo F.** Se mantiene en $500 como pide la estrategia §10.2. Es el de
mayor volumen y el de mayor riesgo de la cuenta.

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

## 9. Orden de carga

1. Crear la campaña — Búsqueda, sin socios de búsqueda ni Display.
2. **Ubicación en "Presencia: personas EN tus ubicaciones".** Es el cambio manual
   más importante de toda la cuenta; el default de Google es "presencia o interés".
3. Las 4 comunas. Presupuesto diario **$4.930**. **CPC manual.**
4. Los 6 grupos con sus keywords y concordancias (estrategia §4 + §4 de acá).
5. **Puja máxima por grupo según §2.**
6. Todas las negativas de la estrategia §5, en amplia, a nivel de campaña, con las
   correcciones de la §5 de acá.
7. Los RSA de la §3.
8. URLs a nivel de keyword de la §7.
9. Recursos de la §6.
10. Activar informes de llamadas, duración mínima 60 s.

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
