const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');

document.documentElement.classList.add('js');

function closeMenu() {
    navigation.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
}

menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(isOpen));
    navigation.classList.toggle('is-open', isOpen);
});

navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) closeMenu();
});

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
        closeMenu();
        menuButton.focus();
    }
});

document.addEventListener('click', (event) => {
    if (!event.target.closest('nav')) closeMenu();
});

window.matchMedia('(min-width: 601px)').addEventListener('change', closeMenu);

const links = [...navigation.querySelectorAll('a')];
const sections = links.map((link) => document.querySelector(link.getAttribute('href'))).filter(Boolean);

if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
        for (const entry of entries) {
            if (!entry.isIntersecting) continue;
            for (const link of links) {
                if (link.getAttribute('href') === `#${entry.target.id}`) {
                    link.setAttribute('aria-current', 'location');
                } else {
                    link.removeAttribute('aria-current');
                }
            }
        }
    }, { rootMargin: '-15% 0px -60% 0px', threshold: 0 });
    sections.forEach((section) => observer.observe(section));
}
