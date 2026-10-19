/* ============================================
   PORTFOLIO FLASK - JAVASCRIPT
   Tugas Individu 3 - Pengenalan Flask
   ============================================ */

(function () {
    'use strict';

    /* ===== 1. Navbar scroll effect ===== */
    const navbar = document.getElementById('mainNavbar');
    if (navbar) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        };
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
    }

    /* ===== 2. Smooth scroll untuk anchor link ===== */
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    /* ===== 3. Back to top button ===== */
    const backToTopBtn = document.getElementById('backToTop');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        }, { passive: true });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ===== 4. Active navbar link otomatis ===== */
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const currentPath = window.location.pathname;
    navLinks.forEach((link) => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });

    /* ===== 5. Inisialisasi AOS (Animate On Scroll) ===== */
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100,
            disable: window.innerWidth < 576,
        });
    }

    /* ===== 6. Animasi progress bar saat terlihat ===== */
    const progressBars = document.querySelectorAll('.progress-bar-custom');
    if (progressBars.length > 0) {
    // Inisialisasi: ambil width dari data-width (Hindari CSS validator komplain)
    progressBars.forEach((bar) => {
        const w = bar.getAttribute('data-width') || '0';
        bar.style.width = '0%';
        bar.setAttribute('data-target-width', w + '%');
    });

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const bar = entry.target;
                    const targetWidth = bar.getAttribute('data-target-width') || '0%';
                    setTimeout(() => {
                        bar.style.width = targetWidth;
                    }, 100);
                    observer.unobserve(bar);
                }
            });
        },
        { threshold: 0.3 }
    );
    progressBars.forEach((bar) => observer.observe(bar));
    }

    /* ===== 7. Counter animation (jika ada) ===== */
    const counters = document.querySelectorAll('[data-counter]');
    counters.forEach((counter) => {
        const target = parseInt(counter.dataset.counter, 10);
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;
        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        updateCounter();
    });

    /* ===== 8. Form validation sederhana ===== */
    const forms = document.querySelectorAll('form');
    forms.forEach((form) => {
        form.addEventListener('submit', function (e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            requiredFields.forEach((field) => {
                if (!field.value.trim()) {
                    field.style.borderColor = '#ef4444';
                    isValid = false;
                } else {
                    field.style.borderColor = '';
                }
            });
            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    /* ===== 9. Year auto-update di footer ===== */
    const yearEls = document.querySelectorAll('[data-year]');
    if (yearEls.length > 0) {
        const year = new Date().getFullYear();
        yearEls.forEach((el) => (el.textContent = year));
    }

    /* ===== 10. Console banner (developer easter egg) ===== */
    console.log(
        '%c🚀 Portfolio Flask - Tugas Individu 3',
        'color: #2563eb; font-size: 16px; font-weight: bold;'
    );
    console.log(
        '%cDibuat dengan Flask 3.x + Python 3.12 + Bootstrap 5',
        'color: #64748b; font-size: 12px;'
    );
    console.log(
        '%cPengenalan Flask - Pertemuan 7',
        'color: #0ea5e9; font-size: 12px; font-style: italic;'
    );
})();
