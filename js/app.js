// LUXORA FASHION - Main Application Logic

document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();

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

    // initShopFilters(); // Handled by shop.html inline script
});

/* ==============================
   1. MOBILE MENU LOGIC
   ============================== */
function initMobileMenu() {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const overlay = document.getElementById('mobile-menu-overlay');

    window.toggleMenu = function() {
        if (!mobileMenu) return;
        const isClosed = mobileMenu.classList.contains('-translate-x-full');
        if (isClosed) {
            mobileMenu.classList.remove('-translate-x-full');
            if (overlay) {
                overlay.classList.remove('opacity-0', 'pointer-events-none');
                overlay.classList.add('opacity-50', 'pointer-events-auto');
            }
        } else {
            mobileMenu.classList.add('-translate-x-full');
            if (overlay) {
                overlay.classList.remove('opacity-50', 'pointer-events-auto');
                overlay.classList.add('opacity-0', 'pointer-events-none');
            }
        }
    }

    if (menuBtn) menuBtn.addEventListener('click', toggleMenu);
    if (closeMenuBtn) closeMenuBtn.addEventListener('click', toggleMenu);
    if (overlay) overlay.addEventListener('click', toggleMenu);
}


/* ==============================
   3. SHOP FILTER & SORT LOGIC
   ============================== */
function initShopFilters() {
    const filterBtn = document.getElementById('filter-btn');
    const filterDrawer = document.getElementById('filter-drawer');
    const filterOverlay = document.getElementById('filter-overlay');
    const filterContent = document.getElementById('filter-content');
    const closeFilterBtn = document.getElementById('close-filter');
    const applyFilterBtn = document.getElementById('apply-filters-btn');

    if (!filterBtn || !filterDrawer) return; // Not on shop page

    function toggleFilter(open) {
        if (open) {
            filterDrawer.classList.remove('invisible', 'pointer-events-none');
            filterOverlay.classList.remove('opacity-0');
            filterContent.classList.remove('translate-x-full');
        } else {
            filterOverlay.classList.add('opacity-0');
            filterContent.classList.add('translate-x-full');
            setTimeout(() => {
                filterDrawer.classList.add('invisible', 'pointer-events-none');
            }, 300);
        }
    }

    filterBtn.addEventListener('click', () => toggleFilter(true));
    closeFilterBtn.addEventListener('click', () => toggleFilter(false));
    filterOverlay.addEventListener('click', () => toggleFilter(false));

    // Simple Sort Logic
    if (applyFilterBtn) {
        applyFilterBtn.addEventListener('click', () => {
            const sortRadios = document.getElementsByName('sort');
            let sortValue = 'newest';
            sortRadios.forEach(radio => {
                if (radio.checked) sortValue = radio.value;
            });
            
            sortProducts(sortValue);
            toggleFilter(false);
        });
    }
}

function sortProducts(criteria) {
    const grid = document.getElementById('product-grid');
    if (!grid) return;

    let products = Array.from(grid.querySelectorAll('.product-card'));
    
    products.sort((a, b) => {
        const priceA = parseFloat(a.dataset.price);
        const priceB = parseFloat(b.dataset.price);
        
        if (criteria === 'price_asc') {
            return priceA - priceB;
        } else if (criteria === 'price_desc') {
            return priceB - priceA;
        }
        // If 'newest' or default, we just rely on original DOM order or a data-date attribute
        // For simplicity, we just leave it or shuffle slightly if no date provided
        return 0; 
    });

    // Re-append to grid
    products.forEach(p => grid.appendChild(p));
}
