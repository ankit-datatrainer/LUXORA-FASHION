import os

files = ['index.html', 'shop.html', 'about.html', 'contact.html']

cart_html = '''
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
                <span class="font-body-lg text-lg" id="cart-subtotal">₹0.00</span>
            </div>
            <p class="font-body-md text-sm text-on-surface-variant mb-6 text-center">Shipping & taxes calculated at checkout.</p>
            <button class="w-full py-4 bg-primary text-on-primary font-label-md text-label-md uppercase tracking-[0.2em] transition-all hover:bg-secondary active:scale-95" onclick="alert('Checkout coming soon!')">
                Proceed to Checkout
            </button>
        </div>
    </div>
</div>
'''

desktop_cart = '''<button class="relative material-symbols-outlined hover:text-secondary transition-colors cart-icon-toggle">
    shopping_bag
    <span class="cart-badge absolute -top-1 -right-2 bg-error text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold" style="display:none;">0</span>
</button>'''

mobile_cart = '''<a class="flex flex-col items-center gap-1 text-on-surface-variant cart-icon-toggle relative" href="#">
<span class="material-symbols-outlined">shopping_bag</span>
<span class="font-label-md text-[10px] uppercase">Cart</span>
<span class="cart-badge absolute top-0 right-4 bg-error text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center font-bold" style="display:none;">0</span>
</a>'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Desktop Cart Icon
        content = content.replace('<button class="material-symbols-outlined hover:text-secondary transition-colors">shopping_bag</button>', desktop_cart)
        content = content.replace('<button class="hidden md:block material-symbols-outlined hover:text-secondary transition-colors">shopping_bag</button>', desktop_cart.replace('class="relative', 'class="hidden md:block relative'))
        
        # 2. Mobile Cart Icon
        content = content.replace('<a class="flex flex-col items-center gap-1 text-on-surface-variant" href="#">\n<span class="material-symbols-outlined">shopping_bag</span>\n<span class="font-label-md text-[10px] uppercase">Cart</span>\n</a>', mobile_cart)
        
        # 3. Add JS script
        if 'js/app.js' not in content:
            content = content.replace('js/main.js', 'js/app.js')
            
        # 4. Inject Cart Drawer HTML
        if 'cart-drawer-container' not in content:
            content = content.replace('</body>', f'{cart_html}\n</body>')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("HTML injection complete.")
