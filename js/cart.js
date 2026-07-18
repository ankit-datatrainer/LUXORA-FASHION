const PRODUCTS = {
    'sugarbaby': { id: 'sugarbaby', name: 'Sugarbaby 🍓 🎀', price: 899.00, image: 'images/cat_babydolls.png' },
    'roleplay': { id: 'roleplay', name: 'Latex Bunny Roleplay Set 🐰', price: 1199.00, image: 'images/cat_roleplay.png' },
    'bridal': { id: 'bridal', name: 'Bridal theme Lace Set 🤍', price: 999.00, image: 'images/cat_bridal.png' },
    'dominatrix': { id: 'dominatrix', name: 'Dominatrix Harness Dress', price: 999.00, image: 'images/cat_latex.png' },
    'desert': { id: 'desert', name: 'Desert Fantasy Set', price: 999.00, image: 'images/cat_lingerie_sets.png' },
    'pikachu': { id: 'pikachu', name: 'Pikachu Cosplay Bodysuit', price: 749.00, image: 'images/cat_bodysuits.png' }
};

let cart = JSON.parse(localStorage.getItem('luxora_cart')) || [];

function saveCart() {
    localStorage.setItem('luxora_cart', JSON.stringify(cart));
    updateCartUI();
}

function addToCart(productId, size, quantity = 1) {
    const product = PRODUCTS[productId];
    if (!product) return;

    const existingItem = cart.find(item => item.id === productId && item.size === size);
    if (existingItem) {
        existingItem.quantity += parseInt(quantity);
    } else {
        cart.push({
            id: productId,
            name: product.name,
            price: product.price,
            image: product.image,
            size: size,
            quantity: parseInt(quantity)
        });
    }
    
    saveCart();
    openCart();
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
}

function updateQuantity(index, delta) {
    if (cart[index]) {
        cart[index].quantity += delta;
        if (cart[index].quantity <= 0) {
            removeFromCart(index);
        } else {
            saveCart();
        }
    }
}

function toggleCart() {
    const cartDrawer = document.getElementById('cart-drawer');
    const overlay = document.getElementById('cart-overlay');
    if (cartDrawer.classList.contains('translate-x-full')) {
        openCart();
    } else {
        closeCart();
    }
}

function openCart() {
    document.getElementById('cart-drawer').classList.remove('translate-x-full');
    document.getElementById('cart-overlay').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeCart() {
    document.getElementById('cart-drawer').classList.add('translate-x-full');
    document.getElementById('cart-overlay').classList.add('hidden');
    document.body.style.overflow = '';
}

function updateCartUI() {
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    const cartCountElements = document.querySelectorAll('.cart-count');
    
    if (!cartItemsContainer) return;

    let total = 0;
    let itemCount = 0;
    cartItemsContainer.innerHTML = '';

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p class="text-gray-500 mt-10 text-center">Your cart is empty.</p>';
    } else {
        cart.forEach((item, index) => {
            const itemTotal = item.price * item.quantity;
            total += itemTotal;
            itemCount += item.quantity;

            cartItemsContainer.innerHTML += `
                <div class="flex gap-4 mb-6 border-b border-gray-100 pb-6">
                    <img src="${item.image}" alt="${item.name}" class="w-24 h-32 object-cover">
                    <div class="flex-1">
                        <h4 class="font-bold text-sm mb-1">${item.name}</h4>
                        <p class="text-xs text-gray-500 mb-2">Size: ${item.size}</p>
                        <p class="text-sm mb-3">Rs. ${item.price.toFixed(2)}</p>
                        <div class="flex items-center gap-3">
                            <button onclick="updateQuantity(${index}, -1)" class="w-6 h-6 flex items-center justify-center border border-gray-300">-</button>
                            <span class="text-sm">${item.quantity}</span>
                            <button onclick="updateQuantity(${index}, 1)" class="w-6 h-6 flex items-center justify-center border border-gray-300">+</button>
                        </div>
                    </div>
                    <button onclick="removeFromCart(${index})" class="material-symbols-outlined text-gray-400 hover:text-black">close</button>
                </div>
            `;
        });
    }

    cartTotalElement.innerText = `Rs. ${total.toFixed(2)}`;
    cartCountElements.forEach(el => {
        el.innerText = itemCount;
        if (itemCount > 0) el.classList.remove('hidden');
        else el.classList.add('hidden');
    });
}

function injectCartHTML() {
    const cartHTML = `
        <!-- Cart Overlay -->
        <div id="cart-overlay" class="fixed inset-0 bg-black/50 z-[90] hidden transition-opacity" onclick="closeCart()"></div>
        
        <!-- Cart Drawer -->
        <div id="cart-drawer" class="fixed top-0 right-0 h-full w-full max-w-[400px] bg-white z-[100] translate-x-full transition-transform duration-300 ease-in-out flex flex-col shadow-2xl">
            <div class="p-6 border-b border-gray-200 flex justify-between items-center">
                <h3 class="font-headline-sm text-xl uppercase tracking-widest">Your Cart</h3>
                <button onclick="closeCart()" class="material-symbols-outlined text-2xl hover:rotate-90 transition-transform">close</button>
            </div>
            
            <div id="cart-items" class="p-6 flex-1 overflow-y-auto">
                <!-- Items will be injected here -->
            </div>
            
            <div class="p-6 border-t border-gray-200 bg-gray-50">
                <div class="flex justify-between items-center mb-6">
                    <span class="font-bold uppercase tracking-widest">Subtotal</span>
                    <span id="cart-total" class="font-bold text-lg">Rs. 0.00</span>
                </div>
                <p class="text-xs text-gray-500 mb-6 text-center">Shipping & taxes calculated at checkout</p>
                <button class="w-full bg-black text-white py-4 uppercase tracking-widest hover:bg-gray-800 transition-colors">Checkout</button>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', cartHTML);
    updateCartUI();
}

document.addEventListener('DOMContentLoaded', () => {
    injectCartHTML();
    
    // Add click listeners to any bag icons
    const bagIcons = document.querySelectorAll('.shopping-bag-icon');
    bagIcons.forEach(icon => {
        icon.addEventListener('click', (e) => {
            e.preventDefault();
            toggleCart();
        });
    });
});
