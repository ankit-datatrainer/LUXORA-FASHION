import re

# Read index.html to extract the head section (Tailwind config, fonts, etc.)
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract the full <head> content from index.html
head_match = re.search(r'<head>(.*?)</head>', index_html, re.DOTALL)
index_head = head_match.group(1)

# Extract the header (sticky header + mobile menu)
header_match = re.search(r'(<!-- Sticky Header Container -->.*?<!-- Mobile Menu Overlay -->.*?</div>\s*</div>\s*</div>)', index_html, re.DOTALL)
header_html = header_match.group(1)

# Extract the footer
footer_match = re.search(r'(<footer.*?</footer>)', index_html, re.DOTALL)
footer_html = footer_match.group(1)

# Extract the cart drawer
cart_match = re.search(r'(<!-- Cart Drawer.*?</div>\s*</div>\s*</div>)', index_html, re.DOTALL)
cart_drawer_html = cart_match.group(1) if cart_match else ''

# Build the complete product.html
product_html = f'''<!DOCTYPE html>
<html class="light" lang="en">
<head>
{index_head}
</head>
<body class="bg-background text-on-surface font-body-md selection:bg-secondary-fixed selection:text-on-secondary-fixed">

{header_html}

    <main class="max-w-7xl mx-auto px-5 py-12 md:py-24">
        <div class="flex flex-col md:flex-row gap-12 lg:gap-24">
            
            <!-- Product Image -->
            <div class="w-full md:w-1/2">
                <div class="aspect-[3/4] bg-gray-100 overflow-hidden">
                    <img id="product-image" src="" alt="Product Image" class="w-full h-full object-cover">
                </div>
            </div>
            
            <!-- Product Details -->
            <div class="w-full md:w-1/2 flex flex-col justify-center">
                <nav class="text-xs tracking-widest text-gray-500 uppercase mb-8">
                    <a href="index.html" class="hover:text-black">Home</a> / 
                    <a href="shop.html" class="hover:text-black">Shop</a> / 
                    <span id="breadcrumb-name" class="text-black">Product</span>
                </nav>

                <h1 id="product-name" class="font-headline-lg text-4xl md:text-5xl mb-4">Product Name</h1>
                <p id="product-price" class="text-xl mb-8 text-on-surface-variant">Rs. 0.00</p>
                
                <p class="text-on-surface-variant mb-10 leading-relaxed max-w-lg font-body-md">
                    Experience unparalleled luxury with this exquisite piece. Designed with meticulous attention to detail, 
                    it offers a perfect blend of comfort and provocative elegance. A must-have addition to your intimate wardrobe.
                </p>

                <!-- Size Selector -->
                <div class="mb-8">
                    <div class="flex justify-between items-center mb-3">
                        <label class="text-sm uppercase tracking-widest font-bold font-label-md">Size</label>
                        <a href="#" class="text-xs text-on-surface-variant underline font-label-md">Size Guide</a>
                    </div>
                    <div class="flex gap-3" id="size-selector">
                        <button class="size-btn w-12 h-12 border border-outline-variant flex items-center justify-center hover:border-primary transition-colors text-sm font-label-md" data-size="S">S</button>
                        <button class="size-btn w-12 h-12 border border-outline-variant flex items-center justify-center hover:border-primary transition-colors text-sm font-label-md" data-size="M">M</button>
                        <button class="size-btn w-12 h-12 border border-outline-variant flex items-center justify-center hover:border-primary transition-colors text-sm font-label-md" data-size="L">L</button>
                        <button class="size-btn w-12 h-12 border border-outline-variant flex items-center justify-center hover:border-primary transition-colors text-sm font-label-md" data-size="XL">XL</button>
                    </div>
                </div>

                <!-- Quantity Selector -->
                <div class="mb-8">
                    <label class="text-sm uppercase tracking-widest font-bold font-label-md mb-3 block">Quantity</label>
                    <div class="flex items-center border border-outline-variant w-fit">
                        <button id="qty-minus" class="px-4 py-3 hover:bg-surface-container transition-colors font-body-md">-</button>
                        <span id="qty-value" class="px-6 py-3 font-body-md text-sm border-x border-outline-variant">1</span>
                        <button id="qty-plus" class="px-4 py-3 hover:bg-surface-container transition-colors font-body-md">+</button>
                    </div>
                </div>

                <!-- Add to Cart -->
                <button id="add-to-cart-btn" class="w-full bg-primary text-on-primary py-5 uppercase tracking-[0.2em] hover:bg-secondary transition-colors mb-6 font-label-md text-label-md active:scale-95">
                    Add to Cart
                </button>

                <div class="border-t border-outline-variant pt-6 mt-2">
                    <div class="flex items-center gap-3 text-sm text-on-surface-variant mb-3 font-body-md">
                        <span class="material-symbols-outlined text-lg">local_shipping</span> Free shipping on orders over Rs. 3000
                    </div>
                    <div class="flex items-center gap-3 text-sm text-on-surface-variant mb-3 font-body-md">
                        <span class="material-symbols-outlined text-lg">sync</span> 14-day return policy
                    </div>
                    <div class="flex items-center gap-3 text-sm text-on-surface-variant font-body-md">
                        <span class="material-symbols-outlined text-lg">verified_user</span> 100% secure payment
                    </div>
                </div>
            </div>

        </div>
    </main>

    <!-- Footer -->
    {footer_html}

    <!-- Cart Drawer (Overlay) -->
    <div class="fixed inset-0 z-[100] invisible pointer-events-none transition-all duration-300" id="cart-drawer-container">
        <div class="absolute inset-0 bg-black/50 opacity-0 transition-opacity duration-300" id="cart-overlay"></div>
        <div class="absolute right-0 top-0 h-full w-full md:w-[400px] bg-surface-bright shadow-2xl translate-x-full transition-transform duration-300 flex flex-col" id="cart-drawer-panel">
            <div class="p-6 flex justify-between items-center border-b border-outline-variant">
                <h2 class="font-headline-lg text-2xl uppercase tracking-widest">Shopping Bag</h2>
                <button id="close-cart" class="active:scale-90 transition-transform">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <div class="flex-1 overflow-y-auto p-6 space-y-6" id="cart-items-container">
                <!-- Items injected by JS -->
            </div>
            <div class="p-6 border-t border-outline-variant bg-surface-container-low">
                <div class="flex justify-between items-center mb-6">
                    <span class="font-label-md text-sm uppercase tracking-widest">Subtotal</span>
                    <span class="font-body-lg text-lg" id="cart-subtotal">Rs. 0.00</span>
                </div>
                <p class="font-body-md text-sm text-on-surface-variant mb-6 text-center">Shipping & taxes calculated at checkout.</p>
                <button class="w-full py-4 bg-primary text-on-primary font-label-md text-label-md uppercase tracking-[0.2em] transition-all hover:bg-secondary active:scale-95" onclick="alert('Checkout coming soon!')">
                    Proceed to Checkout
                </button>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="js/app.js"></script>
    <script src="js/cart.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            // Parse URL parameters
            const urlParams = new URLSearchParams(window.location.search);
            const productId = urlParams.get('id');

            // Find product or redirect
            const product = PRODUCTS[productId];
            if (!product) {{
                window.location.href = 'index.html';
                return;
            }}

            // Populate Page Content
            document.title = `LUXORA FASHION | ${{product.name}}`;
            document.getElementById('product-image').src = product.image;
            document.getElementById('product-name').innerText = product.name;
            document.getElementById('product-price').innerText = `Rs. ${{product.price.toFixed(2)}}`;
            document.getElementById('breadcrumb-name').innerText = product.name;

            // Handle Size Selection
            let selectedSize = null;
            const sizeBtns = document.querySelectorAll('.size-btn');
            sizeBtns.forEach(btn => {{
                btn.addEventListener('click', (e) => {{
                    sizeBtns.forEach(b => {{
                        b.classList.remove('bg-primary', 'text-on-primary', 'border-primary');
                        b.classList.add('border-outline-variant');
                    }});
                    const target = e.target;
                    target.classList.add('bg-primary', 'text-on-primary', 'border-primary');
                    target.classList.remove('border-outline-variant');
                    selectedSize = target.getAttribute('data-size');
                }});
            }});

            // Handle Quantity
            let quantity = 1;
            const qtyValue = document.getElementById('qty-value');
            document.getElementById('qty-minus').addEventListener('click', () => {{
                if (quantity > 1) {{
                    quantity--;
                    qtyValue.innerText = quantity;
                }}
            }});
            document.getElementById('qty-plus').addEventListener('click', () => {{
                quantity++;
                qtyValue.innerText = quantity;
            }});

            // Handle Add to Cart
            const addBtn = document.getElementById('add-to-cart-btn');
            addBtn.addEventListener('click', () => {{
                if (!selectedSize) {{
                    alert('Please select a size first.');
                    return;
                }}
                addToCart(productId, selectedSize, quantity);
            }});
        }});
    </script>
</body>
</html>
'''

with open('product.html', 'w', encoding='utf-8') as f:
    f.write(product_html)

print("Successfully rebuilt product.html with full Tailwind config and design system")
