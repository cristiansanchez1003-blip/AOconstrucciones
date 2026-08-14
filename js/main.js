/* ============================================
   AO CONSTRUCCIONES — Main JavaScript
   Scroll Animations · Navbar · Mobile Menu · Multi-Step Form
   ============================================ */

/* ---------------------------------------------------------------
   RESPALDO DEL FORMULARIO — Web3Forms

   PARA ACTIVAR: consigue tu access key gratis en https://web3forms.com
   (pones construyeao@gmail.com, te llega la key por correo, sin crear
   cuenta) y reemplázala abajo.

   Mientras siga en "PENDIENTE", el formulario funciona exactamente como
   antes: manda al usuario a WhatsApp. Con la key puesta, el lead queda
   guardado por correo ANTES de ofrecer WhatsApp, así no se pierde ninguno.
   --------------------------------------------------------------- */
const WEB3FORMS_ACCESS_KEY = 'PENDIENTE';
const WEB3FORMS_KEY_OK =
  WEB3FORMS_ACCESS_KEY !== 'PENDIENTE' && WEB3FORMS_ACCESS_KEY.length > 20;

document.addEventListener('DOMContentLoaded', () => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- NAVBAR SCROLL BEHAVIOR ----
  const navbar = document.getElementById('navbar');
  const SCROLL_THRESHOLD = 60;

  const handleNavbarScroll = () => {
    if (window.scrollY > SCROLL_THRESHOLD) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll();

  // ---- SMOOTH SCROLL FOR NAV LINKS ----
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        const navHeight = navbar.offsetHeight;
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight - 20;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });

        // Close mobile menu if open
        closeMobileMenu();
      }
    });
  });

  // ---- MOBILE MENU ----
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.getElementById('nav-links');
  const mobileOverlay = document.getElementById('mobile-overlay');

  function openMobileMenu() {
    menuToggle.classList.add('active');
    navLinks.classList.add('open');
    mobileOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileMenu() {
    menuToggle.classList.remove('active');
    navLinks.classList.remove('open');
    mobileOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      if (navLinks.classList.contains('open')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
  }

  if (mobileOverlay) {
    mobileOverlay.addEventListener('click', closeMobileMenu);
  }

  // ---- INTERSECTION OBSERVER — SCROLL REVEAL ----
  const revealElements = document.querySelectorAll(
    '.reveal, .reveal-left, .reveal-right, .reveal-scale, .clip-reveal'
  );

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    }
  );

  revealElements.forEach(el => revealObserver.observe(el));

  // ---- COUNTER ANIMATION ----
  // The final value is written in the HTML so it is visible without JS.
  // We only animate from 0 up to that value once the stat scrolls into view.
  const counters = document.querySelectorAll('[data-target]');

  const counterObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  counters.forEach(counter => counterObserver.observe(counter));

  function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'), 10);
    const suffix = element.getAttribute('data-suffix') || '';

    // Nothing sensible to animate towards — leave the HTML value untouched.
    if (!Number.isFinite(target)) return;

    if (prefersReducedMotion) {
      element.textContent = target + suffix;
      return;
    }

    const duration = 2000;
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);

      element.textContent = current + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        element.textContent = target + suffix;
      }
    }

    requestAnimationFrame(update);
  }

  // ---- PROCESS STEPS — SEQUENTIAL ANIMATION ----
  const processSteps = document.querySelectorAll('.process__step');

  const processObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Animate steps sequentially
          const steps = entry.target.closest('.process__timeline').querySelectorAll('.process__step');
          steps.forEach((step, index) => {
            setTimeout(() => {
              step.classList.add('is-visible');
            }, index * 200);
          });
          processObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  // Observe only first step to trigger all
  if (processSteps.length > 0) {
    processObserver.observe(processSteps[0]);
  }

  // Add reveal styles to process steps
  processSteps.forEach(step => {
    step.style.opacity = '0';
    step.style.transform = 'translateY(30px)';
    step.style.transition = 'opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)';
  });

  // CSS for visible process step
  const style = document.createElement('style');
  style.textContent = `
    .process__step.is-visible {
      opacity: 1 !important;
      transform: translateY(0) !important;
    }
  `;
  document.head.appendChild(style);

  // ---- MULTI-STEP FORM ----
  const formSteps = document.querySelectorAll('.form-step');
  const stepperSteps = document.querySelectorAll('.form-stepper__step');
  const stepperLines = document.querySelectorAll('.form-stepper__line');
  const btnNext = document.querySelectorAll('.form-nav__btn--next');
  const btnBack = document.querySelectorAll('.form-nav__btn--back');
  const btnSubmit = document.querySelector('.form-nav__btn--submit');
  const formSuccess = document.querySelector('.form-success');
  const formContainer = document.getElementById('lead-form');

  let currentStep = 0;

  function updateFormStep(step) {
    // Update form steps
    formSteps.forEach((s, i) => {
      s.classList.toggle('active', i === step);
    });

    // Update stepper dots
    stepperSteps.forEach((s, i) => {
      s.classList.remove('active', 'completed');
      if (i === step) {
        s.classList.add('active');
      } else if (i < step) {
        s.classList.add('completed');
      }
    });

    currentStep = step;
  }

  // Next buttons
  btnNext.forEach(btn => {
    btn.addEventListener('click', () => {
      // Validamos el paso actual antes de avanzar. Antes se podía llegar al
      // final con todo vacío y recién ahí te devolvían al principio.
      if (!validateStep(currentStep)) return;

      if (currentStep < formSteps.length - 1) {
        updateFormStep(currentStep + 1);
      }
    });
  });

  // Back buttons
  btnBack.forEach(btn => {
    btn.addEventListener('click', () => {
      if (currentStep > 0) {
        clearFeedback();
        updateFormStep(currentStep - 1);
      }
    });
  });

  // Al corregir un campo, borramos el mensaje de error de inmediato.
  ['input-name', 'input-phone'].forEach(id => {
    document.getElementById(id)?.addEventListener('input', () => showFeedback(1, ''));
  });
  document.querySelectorAll('input[name="service"]').forEach(radio => {
    radio.addEventListener('change', () => showFeedback(0, ''));
  });

  function getSelectedLabel(name) {
    const selected = formContainer?.querySelector(`input[name="${name}"]:checked`);
    const label = selected ? formContainer.querySelector(`label[for="${selected.id}"]`) : null;
    return label ? label.textContent.trim().replace(/\s+/g, ' ') : '';
  }

  function getSelectLabel(id) {
    const select = document.getElementById(id);
    // La opción por defecto está deshabilitada y sin value: si no eligieron
    // nada devolvemos vacío, no el texto del placeholder. Si no, GA4 recibiría
    // "Selecciona una comuna" como si fuera una comuna real.
    if (!select || !select.value) return '';
    return select.selectedOptions?.[0]?.textContent.trim() || '';
  }

  function normalizePhone(phone) {
    return phone.trim().replace(/[^\d+]/g, '');
  }

  function markInvalidField(field) {
    if (!field) return;
    field.focus({ preventScroll: true });
    field.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function showFeedback(step, message) {
    const box = document.getElementById(`feedback-${step + 1}`);
    if (box) box.textContent = message || '';
  }

  function clearFeedback() {
    document.querySelectorAll('.form-feedback').forEach(el => { el.textContent = ''; });
  }

  // Solo tres campos obligatorios: servicio, nombre y teléfono. El resto es
  // opcional a propósito — cada campo extra obligatorio cuesta conversiones.
  const stepChecks = [
    [
      {
        field: () => document.querySelector('input[name="service"]'),
        isValid: () => Boolean(document.querySelector('input[name="service"]:checked')),
        message: 'Elige qué tipo de proyecto necesitas.'
      }
    ],
    [
      {
        field: () => document.getElementById('input-name'),
        isValid: () => Boolean(document.getElementById('input-name')?.value.trim()),
        message: 'Escribe tu nombre para saber cómo llamarte.'
      },
      {
        field: () => document.getElementById('input-phone'),
        // Chile: 8 dígitos mínimo; evita "123" pero no bloquea formatos con +56, espacios o guiones.
        isValid: () => normalizePhone(document.getElementById('input-phone')?.value || '').replace(/\D/g, '').length >= 8,
        message: 'Necesitamos un teléfono válido para contactarte.'
      }
    ]
  ];

  function validateStep(step) {
    const checks = stepChecks[step] || [];
    const failed = checks.find(check => !check.isValid());

    if (failed) {
      showFeedback(step, failed.message);
      markInvalidField(failed.field());
      return false;
    }

    showFeedback(step, '');
    return true;
  }

  function validateLeadForm() {
    // Si falta algo de un paso anterior, volvemos a ese paso en vez de dejar
    // al usuario con un error que no puede ver.
    for (let step = 0; step < stepChecks.length; step += 1) {
      const failed = stepChecks[step].find(check => !check.isValid());
      if (failed) {
        if (step !== currentStep) updateFormStep(step);
        showFeedback(step, failed.message);
        markInvalidField(failed.field());
        return false;
      }
    }

    clearFeedback();
    return true;
  }

  // El lead se guarda ANTES de ofrecer WhatsApp. Antes el único destino era la
  // redirección: si el usuario no tenía WhatsApp o cancelaba el salto de app, el
  // contacto se perdía sin dejar rastro.
  async function saveLead(payload) {
    if (!WEB3FORMS_KEY_OK) {
      if (window.console) {
        console.warn(
          '[AO] Respaldo del formulario inactivo: falta la access key de Web3Forms en js/main.js. ' +
          'El lead se envía solo por WhatsApp, como antes.'
        );
      }
      return false;
    }

    try {
      const response = await fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload)
      });

      const result = await response.json();
      return response.ok && result.success === true;
    } catch (error) {
      console.error('[AO] No se pudo guardar el lead de respaldo:', error);
      return false;
    }
  }

  function showSuccess(whatsappUrl) {
    const successWhatsApp = document.getElementById('success-whatsapp');
    if (successWhatsApp) successWhatsApp.href = whatsappUrl;

    formContainer.style.display = 'none';
    const stepper = document.querySelector('.form-stepper');
    if (stepper) stepper.style.display = 'none';
    if (formSuccess) formSuccess.classList.add('active');
  }

  async function handleLeadSubmit(event) {
    event.preventDefault();

    if (!formContainer || !validateLeadForm()) {
      return;
    }

    const name = document.getElementById('input-name').value.trim();
    const email = document.getElementById('input-email').value.trim();
    const phone = normalizePhone(document.getElementById('input-phone').value);
    const projectType = getSelectedLabel('service');
    const location = getSelectLabel('input-location');
    const budget = getSelectLabel('input-budget');
    const message = document.getElementById('input-message').value.trim();

    // Solo servicio, nombre y teléfono son obligatorios: omitimos del mensaje
    // las líneas que el usuario dejó en blanco en vez de mandarlas vacías.
    const whatsappText = [
      '🏗️ *Nueva Cotización - AO Construcciones* 🏗️',
      '--------------------------------------------',
      `👤 *Cliente:* ${name}`,
      `📞 *Teléfono:* ${phone}`,
      email && `📧 *Email:* ${email}`,
      '',
      '📍 *Detalles del Proyecto:*',
      `• Tipo de proyecto: ${projectType}`,
      location && `• Comuna: ${location}`,
      budget && `• Presupuesto estimado: ${budget}`,
      message && `• Descripción: ${message}`
    ].filter(Boolean).join('\n');

    const whatsappUrl =
      `https://api.whatsapp.com/send?phone=56979925812&text=${encodeURIComponent(whatsappText)}`;

    // Evita envíos duplicados por doble clic.
    const originalLabel = btnSubmit ? btnSubmit.innerHTML : '';
    if (btnSubmit) {
      btnSubmit.disabled = true;
      btnSubmit.innerHTML = 'Enviando…';
    }

    const payload = {
      access_key: WEB3FORMS_ACCESS_KEY,
      subject: `Nueva cotización de ${name} — ${projectType}`,
      from_name: 'Sitio web AO Construcciones',
      Nombre: name,
      Teléfono: phone,
      'Tipo de proyecto': projectType
    };

    // Los campos opcionales solo viajan si el usuario los completó, para que el
    // correo no llegue lleno de líneas vacías.
    if (email) {
      payload.replyto = email;
      payload.Email = email;
    }
    if (location) payload.Comuna = location;
    if (budget) payload['Presupuesto estimado'] = budget;
    if (message) payload['Descripción'] = message;

    const saved = await saveLead(payload);

    if (btnSubmit) {
      btnSubmit.disabled = false;
      btnSubmit.innerHTML = originalLabel;
    }

    // La conversión se registra igual, se haya guardado o no: el usuario
    // completó el formulario. Solo enviamos datos del proyecto, nunca nombre,
    // email ni teléfono.
    const finish = () => {
      if (saved) {
        // El lead ya está a salvo: mostramos confirmación y dejamos WhatsApp a un toque.
        showSuccess(whatsappUrl);
      } else {
        // Sin respaldo, volvemos al comportamiento anterior para no perder el contacto.
        window.location.href = whatsappUrl;
      }
    };

    if (typeof window.aoTrack === 'function') {
      window.aoTrack('generate_lead', {
        form_name: 'cotizacion_home',
        project_type: projectType,
        project_location: location,
        project_budget: budget,
        lead_backup: saved ? 'ok' : 'fallback_whatsapp'
      }, finish);
    } else {
      finish();
    }
  }

  if (formContainer) {
    formContainer.addEventListener('submit', handleLeadSubmit);
  }

  // ---- ACTIVE NAV LINK ON SCROLL ----
  const sections = document.querySelectorAll('section[id]');
  const navLinksAll = document.querySelectorAll('.navbar__link');

  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinksAll.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
          });
        }
      });
    },
    {
      threshold: 0.3,
      rootMargin: '-80px 0px -50% 0px'
    }
  );

  sections.forEach(section => sectionObserver.observe(section));

  // ---- PARALLAX-LIKE SUBTLE HERO FLOAT ----
  const heroVisual = document.querySelector('.hero__visual');
  if (heroVisual && window.innerWidth > 768) {
    window.addEventListener('mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 12;
      const y = (e.clientY / window.innerHeight - 0.5) * 8;
      heroVisual.style.transform = `translate(${x}px, ${y}px)`;
    }, { passive: true });
  }
});
