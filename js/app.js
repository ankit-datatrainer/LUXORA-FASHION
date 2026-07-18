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

    initCart();
    initShopFilters();
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
   2. SHOPPING CART LOGIC
   ============================== */
let cart = JSON.parse(localStorage.getItem('luxora_cart')) || [];

function initCart() {
    updateCartUI();

    // Attach event listeners to all cart icons to open drawer
    const cartIcons = document.querySelectorAll('.cart-icon-toggle');
    cartIcons.forEach(icon => {
        icon.addEventListener('click', (e) => {
            e.preventDefault();
            toggleCartDrawer(true);
        });
    });

    // Close drawer logic
    const closeCartBtn = document.getElementById('close-cart');
    const cartOverlay = document.getElementById('cart-overlay');
    if (closeCartBtn) closeCartBtn.addEventListener('click', () => toggleCartDrawer(false));
    if (cartOverlay) cartOverlay.addEventListener('click', () => toggleCartDrawer(false));

    // Global Add to Cart listener
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('.add-to-cart-btn');
        if (!btn) return;
        
        e.preventDefault();
        const id = btn.dataset.id;
        const title = btn.dataset.title;
        const price = parseFloat(btn.dataset.price);
        const image = btn.dataset.image;

        addToCart({ id, title, price, image });
    });
}

function toggleCartDrawer(open) {
    const drawer = document.getElementById('cart-drawer-container');
    const panel = document.getElementById('cart-drawer-panel');
    const overlay = document.getElementById('cart-overlay');
    
    if (!drawer || !panel || !overlay) return;

    if (open) {
        drawer.classList.remove('invisible', 'pointer-events-none');
        overlay.classList.remove('opacity-0');
        panel.classList.remove('translate-x-full');
    } else {
        overlay.classList.add('opacity-0');
        panel.classList.add('translate-x-full');
        setTimeout(() => {
            drawer.classList.add('invisible', 'pointer-events-none');
        }, 300); // Wait for transition
    }
}

function addToCart(product) {
    const existing = cart.find(item => item.id === product.id);
    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({ ...product, quantity: 1 });
    }
    saveCart();
    updateCartUI();
    toggleCartDrawer(true);
}

function removeFromCart(id) {
    cart = cart.filter(item => item.id !== id);
    saveCart();
    updateCartUI();
}

function updateQuantity(id, delta) {
    const item = cart.find(item => item.id === id);
    if (item) {
        item.quantity += delta;
        if (item.quantity <= 0) {
            removeFromCart(id);
        } else {
            saveCart();
            updateCartUI();
        }
    }
}

function saveCart() {
    localStorage.setItem('luxora_cart', JSON.stringify(cart));
}

function updateCartUI() {
    // 1. Update badges
    const badges = document.querySelectorAll('.cart-badge');
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    badges.forEach(badge => {
        badge.innerText = totalItems;
        badge.style.display = totalItems > 0 ? 'flex' : 'none';
    });

    // 2. Update Drawer Items
    const itemsContainer = document.getElementById('cart-items-container');
    const subtotalEl = document.getElementById('cart-subtotal');
    
    if (!itemsContainer) return;

    itemsContainer.innerHTML = '';
    let subtotal = 0;

    if (cart.length === 0) {
        itemsContainer.innerHTML = '<div class="text-center py-10 text-on-surface-variant font-body-md">Your cart is empty</div>';
    } else {
        cart.forEach(item => {
            subtotal += item.price * item.quantity;
            
            const html = `
                <div class="flex gap-4 border-b border-outline-variant py-4">
                    <div class="w-20 h-24 bg-surface-container flex-shrink-0">
                        <img src="${item.image}" alt="${item.title}" class="w-full h-full object-cover">
                    </div>
                    <div class="flex-1 flex flex-col justify-between">
                        <div>
                            <h4 class="font-label-md text-xs uppercase tracking-widest text-on-surface mb-1">${item.title}</h4>
                            <p class="font-body-md text-on-surface-variant">₹${item.price.toFixed(2)}</p>
                        </div>
                        <div class="flex items-center justify-between mt-2">
                            <div class="flex items-center border border-outline w-fit">
                                <button onclick="updateQuantity('${item.id}', -1)" class="px-2 py-1 hover:bg-surface-container active:scale-95">-</button>
                                <span class="px-3 font-body-md text-sm">${item.quantity}</span>
                                <button onclick="updateQuantity('${item.id}', 1)" class="px-2 py-1 hover:bg-surface-container active:scale-95">+</button>
                            </div>
                            <button onclick="removeFromCart('${item.id}')" class="text-xs font-label-md uppercase tracking-widest text-on-surface-variant hover:text-error underline">Remove</button>
                        </div>
                    </div>
                </div>
            `;
            itemsContainer.insertAdjacentHTML('beforeend', html);
        });
    }

    if (subtotalEl) {
        subtotalEl.innerText = `₹${subtotal.toFixed(2)}`;
    }
}

// Make functions available globally so onclick attributes work
window.updateQuantity = updateQuantity;
window.removeFromCart = removeFromCart;


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
