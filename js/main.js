// Main JavaScript for Luxora Fashion

document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle functionality
    window.toggleMenu = function() {
        const menu = document.getElementById('mobile-menu');
        if (menu) {
            menu.classList.toggle('translate-x-full');
        }
    };

    // Simple carousel interaction
    document.querySelectorAll('button').forEach(btn => {
        btn.addEventListener('click', () => {
            const icon = btn.querySelector('.material-symbols-outlined');
            if (icon && (icon.innerText === 'chevron_left' || icon.innerText === 'chevron_right')) {
                const carousel = btn.closest('section').querySelector('.overflow-x-auto');
                if (carousel) {
                    const scrollAmount = carousel.offsetWidth * 0.8;
                    carousel.scrollBy({
                        left: icon.innerText === 'chevron_left' ? -scrollAmount : scrollAmount,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});
