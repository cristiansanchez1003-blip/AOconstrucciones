# Estado del proyecto — AO Construcciones

Documento vivo. Recoge decisiones, IDs y pendientes que **no** se pueden deducir
leyendo el código ni el historial de git. Si retomas este proyecto en una sesión
nueva, empieza por acá.

**Última actualización:** 14 de agosto de 2026

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
| Razón social | INGENIERÍA EN PROYECTOS DE OBRAS CIVILES SUSTENTABLES Y EDIFICACIÓN AO |
| RUT | 78.154.344-6 |
| Teléfono | +56 9 7992 5812 |
| Correo | construyeao@gmail.com |
| Horario | todos los días, 8:00 – 21:00 |
| Trayectoria | 15 años · 200+ obras ejecutadas |
| Zona de servicio | San José de Maipo / Cajón del Maipo, Pirque, Puente Alto, La Florida |

**Servicios:** obra nueva desde cero, ampliaciones, remodelaciones interiores
(cocinas, baños, escaleras), techumbres, terrazas, decks, quinchos, cierres
perimetrales.

---

## 3. IDs y cuentas

```
Google Tag Manager     GTM-TWJVTWLD      versión 2 publicada
Google Analytics 4     G-S4RFL0C3L1      propiedad "AO construcciones" (549900997)
Google Ads             365-657-1293      dentro del MCC Espíritu Digital (534-787-9097)
Search Console         verificado por archivo HTML, sitemap enviado
Cuenta Google          espiritudigital.chile@gmail.com  (authuser=3)
```

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
   `'PENDIENTE'`, si WhatsApp falla el lead se pierde.
2. **Confirmar facturación en Google Ads.**

### Alto impacto
3. **Open Graph en home, portafolio y privacidad.** Solo lo tienen las landings.
   El home es la página que más se comparte por WhatsApp y no muestra nada.
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
La estrategia es compensar con especificidad: cola larga con intención
inequívoca. Ver `investigacion-keywords.md`.

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
DESIGN-SYSTEM.md             tokens, componentes, IDs que espera main.js, reglas
```

Flujo al tocar el diseño:

```bash
python tools-generar-landings.py
python tools-versionar-assets.py
git add -A && git commit && git push
```

---

## 9. Próximo correo a Andrés

Se envía **cuando las campañas estén corriendo**, no antes. Debe incluir:

1. Que pregunte **"¿cómo nos encontró?"** en llamadas de números nuevos, y lleve
   registro. Cubre el hueco de las llamadas directas, que hoy son invisibles.
2. La **key de Web3Forms**, a nombre de su correo.
3. El **Drive con las mejores fotos**, pidiendo explícitamente **fotos del estado
   inicial** (el "antes"), que hoy no existen: las numeradas del portafolio son
   de proceso o demolición.
4. **Cuántas obras reales tiene por comuna**, para poder publicar esa cifra sin
   inventarla.
