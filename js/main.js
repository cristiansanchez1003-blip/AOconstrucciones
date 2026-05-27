/* ============================================
   AO CONSTRUCCIONES — Main JavaScript
   Scroll Animations · Navbar · Mobile Menu · Multi-Step Form
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
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
  const counters = document.querySelectorAll('[data-counter]');

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
    const target = parseInt(element.getAttribute('data-counter'), 10);
    const suffix = element.getAttribute('data-suffix') || '';
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
      if (currentStep < formSteps.length - 1) {
        updateFormStep(currentStep + 1);
      }
    });
  });

  // Back buttons
  btnBack.forEach(btn => {
    btn.addEventListener('click', () => {
      if (currentStep > 0) {
        updateFormStep(currentStep - 1);
      }
    });
  });

  function getSelectedLabel(name) {
    const selected = formContainer?.querySelector(`input[name="${name}"]:checked`);
    const label = selected ? formContainer.querySelector(`label[for="${selected.id}"]`) : null;
    return label ? label.textContent.trim().replace(/\s+/g, ' ') : '';
  }

  function getSelectLabel(id) {
    const select = document.getElementById(id);
    return select?.selectedOptions?.[0]?.textContent.trim() || '';
  }

  function normalizePhone(phone) {
    return phone.trim().replace(/[^\d+]/g, '');
  }

  function markInvalidField(field) {
    if (!field) return;
    field.focus({ preventScroll: true });
    field.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function validateLeadForm() {
    const firstServiceOption = document.querySelector('input[name="service"]');
    const requiredChecks = [
      { field: document.getElementById('input-name'), isValid: field => Boolean(field?.value.trim()) },
      { field: document.getElementById('input-email'), isValid: field => Boolean(field?.value.trim()) },
      { field: document.getElementById('input-phone'), isValid: field => Boolean(field?.value.trim()) },
      { field: firstServiceOption, isValid: () => Boolean(document.querySelector('input[name="service"]:checked')) },
      { field: document.getElementById('input-location'), isValid: field => Boolean(field?.value.trim()) },
      { field: document.getElementById('input-budget'), isValid: field => Boolean(field?.value.trim()) },
      { field: document.getElementById('input-message'), isValid: field => Boolean(field?.value.trim()) }
    ];

    const invalidCheck = requiredChecks.find(check => !check.isValid(check.field));

    if (invalidCheck) {
      markInvalidField(invalidCheck.field);
      return false;
    }

    return true;
  }

  function sendToWhatsApp(event) {
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

    const whatsappText = [
      '🏗️ *Nueva Cotización - Construcciones AO* 🏗️',
      '--------------------------------------------',
      `👤 *Cliente:* ${name}`,
      `📧 *Email:* ${email}`,
      `📞 *Teléfono:* ${phone}`,
      '',
      '📍 *Detalles del Proyecto:*',
      `• Tipo de proyecto: ${projectType}`,
      `• Ubicación: ${location}`,
      `• Presupuesto estimado: ${budget}`,
      `• Descripción: ${message}`
    ].join('\n');

    const encodedMessage = encodeURIComponent(whatsappText);
    window.location.href = `https://api.whatsapp.com/send?phone=56949745384&text=${encodedMessage}`;
  }

  if (formContainer) {
    formContainer.addEventListener('submit', sendToWhatsApp);
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
