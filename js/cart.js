const PRODUCTS = {
    'prod_0': { id: 'prod_0', name: 'Sugarbaby', price: 899.0, image: 'images/products/prod_0.png' },
    'prod_1': { id: 'prod_1', name: 'Latex Bunny Roleplay Set', price: 1199.0, image: 'images/products/prod_1.jpg' },
    'prod_2': { id: 'prod_2', name: 'Bridal theme Lace Set', price: 999.0, image: 'images/products/prod_2.jpg' },
    'prod_3': { id: 'prod_3', name: 'Dominatrix Harness Dress (Stocking incl)', price: 999.0, image: 'images/products/prod_3.jpg' },
    'prod_4': { id: 'prod_4', name: 'Desert Fantasy Set', price: 999.0, image: 'images/products/prod_4.jpg' },
    'prod_5': { id: 'prod_5', name: 'Pikachu Cosplay Bodysuit', price: 749.0, image: 'images/products/prod_5.jpg' },
    'prod_6': { id: 'prod_6', name: 'cat roleplay fantasy Full set with Headgear', price: 999.0, image: 'images/products/prod_6.jpg' },
    'prod_7': { id: 'prod_7', name: 'Dark Web Cosplay Bodysuit (stockings included)', price: 999.0, image: 'images/products/prod_7.jpg' },
    'prod_8': { id: 'prod_8', name: 'Hot Muse Lace Fantasy Set', price: 899.0, image: 'images/products/prod_8.jpg' },
    'prod_9': { id: 'prod_9', name: 'Afterparty Pearl Shirt', price: 999.0, image: 'images/products/prod_9.jpg' },
    'prod_10': { id: 'prod_10', name: 'Leopard Baddie Bodysuit+Belt', price: 949.0, image: 'images/products/prod_10.jpg' },
    'prod_11': { id: 'prod_11', name: 'Babygirl Lingerie set with gloves', price: 899.0, image: 'images/products/prod_11.jpg' },
    'prod_12': { id: 'prod_12', name: 'Date Night Sparkling Bodystocking full', price: 849.0, image: 'images/products/prod_12.png' },
    'prod_13': { id: 'prod_13', name: 'Bunny Velvet Roleplay', price: 1199.0, image: 'images/products/prod_13.jpg' },
    'prod_14': { id: 'prod_14', name: 'Rainbow Babie', price: 849.0, image: 'images/products/prod_14.png' },
    'prod_15': { id: 'prod_15', name: 'Bubblegum Baddie', price: 949.0, image: 'images/products/prod_15.png' },
    'prod_16': { id: 'prod_16', name: 'Bridal Roleplay Dress', price: 999.0, image: 'images/products/prod_16.jpg' },
    'prod_17': { id: 'prod_17', name: 'Latex Main Character Jacket', price: 1199.0, image: 'images/products/prod_17.jpg' },
    'prod_18': { id: 'prod_18', name: 'Shadow Queen Set', price: 799.0, image: 'images/products/prod_18.png' },
    'prod_19': { id: 'prod_19', name: 'Leopard Tease Stocking Set (4pc)', price: 999.0, image: 'images/products/prod_19.jpg' },
    'prod_20': { id: 'prod_20', name: 'Black flow Long lace lingerie', price: 799.0, image: 'images/products/prod_20.jpg' },
    'prod_21': { id: 'prod_21', name: 'Knotty Night Set', price: 749.0, image: 'images/products/prod_21.png' },
    'prod_22': { id: 'prod_22', name: 'Latex Gold Leash set', price: 899.0, image: 'images/products/prod_22.png' },
    'prod_23': { id: 'prod_23', name: 'The Forbidden Dress', price: 799.0, image: 'images/products/prod_23.jpg' },
    'prod_24': { id: 'prod_24', name: 'Baddie Garter Set & Bodysuit', price: 749.0, image: 'images/products/prod_24.jpg' },
    'prod_25': { id: 'prod_25', name: 'Cheetah Print Garter Set', price: 999.0, image: 'images/products/prod_25.jpg' },
    'prod_26': { id: 'prod_26', name: 'Wifey After Dark Set', price: 799.0, image: 'images/products/prod_26.jpg' },
    'prod_27': { id: 'prod_27', name: 'Good Girl Lace Roleplay', price: 949.0, image: 'images/products/prod_27.png' },
    'prod_28': { id: 'prod_28', name: 'Latex Baddie Nurse Roleplay', price: 1499.0, image: 'images/products/prod_28.png' },
    'prod_29': { id: 'prod_29', name: 'Black rhinestone Lingerie', price: 749.0, image: 'images/products/prod_29.jpg' },
    'prod_30': { id: 'prod_30', name: 'Maid Purple Roleplay Fantasy Full Set', price: 999.0, image: 'images/products/prod_30.png' },
    'prod_31': { id: 'prod_31', name: 'Crystal Mesh Bodysuit', price: 849.0, image: 'images/products/prod_31.png' },
    'prod_32': { id: 'prod_32', name: 'Skin Tease Bodysuit', price: 999.0, image: 'images/products/prod_32.jpg' },
    'prod_33': { id: 'prod_33', name: 'Pink Bunny roleplay full set', price: 1499.0, image: 'images/products/prod_33.jpg' },
    'prod_34': { id: 'prod_34', name: 'Honeybun', price: 999.0, image: 'images/products/prod_34.jpg' },
    'prod_35': { id: 'prod_35', name: 'Latex Curve-Fit Bodysuit', price: 949.0, image: 'images/products/prod_35.jpg' },
    'prod_36': { id: 'prod_36', name: 'High voltage Bodysuit', price: 899.0, image: 'images/products/prod_36.jpg' },
    'prod_37': { id: 'prod_37', name: 'Latex Deep Cut Lingerie+stocking', price: 999.0, image: 'images/products/prod_37.jpg' },
    'prod_38': { id: 'prod_38', name: 'RIPPED Bodystocking', price: 599.0, image: 'images/products/prod_38.png' },
    'prod_39': { id: 'prod_39', name: 'Love Lace Babydoll', price: 599.0, image: 'images/products/prod_39.jpg' },
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
