/**
 * Global JavaScript utilities for HealthPredict
 * Handles common UI interactions and shared functionality
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize navigation active link highlighting
  initializeNavigation();
  
  // Add smooth scrolling for anchor links
  initializeSmoothScroll();

  // Initialize Language
  initializeLanguage();

  // Check authentication state
  checkAuthState();
});

function checkAuthState() {
    const userJson = localStorage.getItem('user');
    const loginBtn = document.querySelector('.login-btn');
    
    if (userJson && loginBtn) {
        const user = JSON.parse(userJson);
        // Replace "Login" button with User Name and Logout option
        loginBtn.innerHTML = `👤 ${user.fullname}`;
        loginBtn.href = '#';
        loginBtn.classList.add('user-profile-btn');
        
        // Add logout on click with confirmation
        loginBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (confirm('Do you want to logout?')) {
                localStorage.removeItem('user');
                alert('Logged out successfully');
                window.location.reload();
            }
        });
    }
}

function initializeLanguage() {
    const langSelect = document.getElementById('lang-select');
    if (!langSelect) return;

    // Check URL param first, then localStorage
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    const savedLang = localStorage.getItem('healthpredict_lang') || 'en';
    const currentLang = urlLang || savedLang;

    // Set select value
    langSelect.value = currentLang;
    
    // Update local storage if current language is different
    if (currentLang !== savedLang) {
        localStorage.setItem('healthpredict_lang', currentLang);
    }

    // Apply translations
    updateLanguage(currentLang);

    // Handle change with reload
    langSelect.addEventListener('change', (e) => {
        const newLang = e.target.value;
        localStorage.setItem('healthpredict_lang', newLang);
        
        // Force reload with new lang param
        const url = new URL(window.location);
        url.searchParams.set('lang', newLang);
        window.location.href = url.toString();
    });
}

function updateLanguage(lang) {
    if (!window.translations || !window.translations[lang]) return;

    const t = window.translations[lang];

    // 1. Update text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const text = getNestedProperty(t, key);
        if (text) {
            el.textContent = text;
        }
    });

    // 1b. Update placeholders
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
        const key = el.getAttribute('data-i18n-ph');
        const text = getNestedProperty(t, key);
        if (text) {
            el.placeholder = text;
        }
    });

    // 2. Update Streamlit Links (Specific to Product Page)
    // We want to force the 'lang' query param on localhost URLs
    document.querySelectorAll('a[href^="http://localhost"]').forEach(link => {
        const url = new URL(link.href);
        url.searchParams.set('lang', lang);
        link.href = url.toString();
    });
}

function getNestedProperty(obj, path) {
    return path.split('.').reduce((prev, curr) => {
        return prev ? prev[curr] : null;
    }, obj);
}

/**
 * Highlight the active navigation link based on current page
 */
function initializeNavigation() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/**
 * Enable smooth scrolling for all anchor links
 */
function initializeSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
}
