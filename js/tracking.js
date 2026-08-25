/* ============================================
   AO CONSTRUCCIONES — Medición
   Google Tag Manager + eventos de conversión

   Se carga en index.html y portafolio.html, antes de main.js.

   ---------------------------------------------------------------
   PARA ACTIVAR: reemplaza GTM_ID por tu contenedor real (GTM-XXXXXXX).
   Mientras siga en "GTM-PENDIENTE" no se carga GTM, pero los eventos
   igual se encolan en dataLayer, así que todo funciona apenas pongas
   el ID. El sitio nunca queda roto por un ID falso.
   ---------------------------------------------------------------

   Eventos que dispara:
     generate_lead    formulario de cotización enviado
     whatsapp_click   clic en cualquier enlace a WhatsApp
     tel_click        clic en el teléfono
     email_click      clic en el correo

   No se envían datos personales (nombre, email, teléfono) al dataLayer:
   solo el tipo de proyecto, la comuna y el rango de presupuesto.
   ============================================ */

(() => {
  'use strict';

  const GTM_ID = 'GTM-TWJVTWLD';

  // Microsoft Clarity: mapas de calor y grabaciones de sesion. Sirve para ver
  // hasta donde baja la gente y donde abandona, que GA4 no muestra.
  // Vacio = no se carga y el sitio funciona igual.
  const CLARITY_ID = 'y7xa9avwgc';
  const IS_CONFIGURED = /^GTM-[A-Z0-9]+$/.test(GTM_ID) && GTM_ID !== 'GTM-PENDIENTE';

  window.dataLayer = window.dataLayer || [];

  // ---- CARGA DE GOOGLE TAG MANAGER ----
  if (IS_CONFIGURED) {
    window.dataLayer.push({
      'gtm.start': new Date().getTime(),
      event: 'gtm.js'
    });

    const gtmScript = document.createElement('script');
    gtmScript.async = true;
    gtmScript.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(GTM_ID);
    document.head.appendChild(gtmScript);
  } else if (window.console) {
    console.warn(
      '[AO] Medición inactiva: falta el ID de Google Tag Manager en js/tracking.js. ' +
      'Los eventos se están encolando en dataLayer y se enviarán apenas se configure.'
    );
  }

  // ---- CARGA DE MICROSOFT CLARITY ----
  // Va aparte de GTM a propósito: si mañana se cambia el contenedor, la
  // grabación de sesiones no se cae con él.
  if (CLARITY_ID) {
    window.clarity = window.clarity || function () {
      (window.clarity.q = window.clarity.q || []).push(arguments);
    };

    const clarityScript = document.createElement('script');
    clarityScript.async = true;
    clarityScript.src = 'https://www.clarity.ms/tag/' + encodeURIComponent(CLARITY_ID);
    document.head.appendChild(clarityScript);
  }

  // ---- DISPARO DE EVENTOS ----
  // GTM envía las etiquetas de forma asíncrona. Si navegamos de inmediato
  // (por ejemplo al redirigir a WhatsApp) el beacon se corta y la conversión
  // se pierde. Por eso esperamos el eventCallback antes de continuar, con un
  // tope de tiempo para no dejar al usuario esperando si GTM no responde.
  const WAIT_MS = 1200;

  function once(fn) {
    let called = false;
    return function () {
      if (called) return;
      called = true;
      if (typeof fn === 'function') fn();
    };
  }

  function track(eventName, params, onDone) {
    const done = once(onDone);

    // Sin GTM configurado no hay nada que esperar: seguimos de inmediato.
    if (!IS_CONFIGURED) {
      window.dataLayer.push(Object.assign({ event: eventName }, params));
      done();
      return;
    }

    window.dataLayer.push(Object.assign({ event: eventName }, params, {
      eventCallback: done,
      eventTimeout: WAIT_MS
    }));

    // Red de seguridad: si GTM nunca llama al callback, continuamos igual.
    window.setTimeout(done, WAIT_MS + 100);
  }

  window.aoTrack = track;

  // ---- AUTO-CABLEADO DE ENLACES ----
  // Los enlaces a WhatsApp, teléfono y correo se trackean solos en ambas
  // páginas. Como abren en pestaña nueva o entregan el control al sistema
  // operativo, no hace falta retrasar la navegación.
  function wireLinks() {
    document.addEventListener('click', (event) => {
      const link = event.target.closest('a[href]');
      if (!link) return;

      const href = link.getAttribute('href') || '';

      if (href.includes('wa.me') || href.includes('api.whatsapp.com')) {
        track('whatsapp_click', {
          link_location: link.id === 'whatsapp-float' ? 'boton_flotante' : 'footer',
          page_path: window.location.pathname
        });
        return;
      }

      if (href.startsWith('tel:')) {
        track('tel_click', { page_path: window.location.pathname });
        return;
      }

      if (href.startsWith('mailto:')) {
        track('email_click', { page_path: window.location.pathname });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wireLinks);
  } else {
    wireLinks();
  }
})();
