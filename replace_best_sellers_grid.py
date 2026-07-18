import re
from bs4 import BeautifulSoup

# 1. Read products from js/cart.js
with open('js/cart.js', 'r', encoding='utf-8') as f:
    cart_js = f.read()

products = {}
# Find all lines like: 'prod_0': { id: 'prod_0', name: 'Sugarbaby', price: 899.0, image: 'images/products/prod_0.png' },
for match in re.finditer(r"'(prod_\d+)':\s*\{\s*id:\s*'[^']+',\s*name:\s*'([^']+)',\s*price:\s*([\d.]+),\s*image:\s*'([^']+)'\s*\}", cart_js):
    products[match.group(1)] = {
        'name': match.group(2),
        'price': float(match.group(3)),
        'image': match.group(4)
    }

print(f"Extracted {len(products)} products from cart.js")

# 2. Build 12 products grid HTML
grid_html = ""
for i in range(12):
    pid = f"prod_{i}"
    if pid in products:
        p = products[pid]
        grid_html += f'''
        <div class="group cursor-pointer flex flex-col justify-between h-full" onclick="window.location.href='product.html?id={pid}'">
            <div>
                <div class="relative overflow-hidden bg-gray-100 aspect-[3/4] mb-4">
                    <img src="{p['image']}" alt="{p['name']}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                </div>
                <div class="px-1 mt-2">
                    <h3 class="font-bold text-sm uppercase tracking-widest mb-1 text-black line-clamp-2">{p['name']}</h3>
                    <p class="text-gray-500 text-sm">Rs. {p['price']:.2f}</p>
                </div>
            </div>
            <div class="mt-4 px-1">
                <button onclick="event.stopPropagation(); addToCart('{pid}', 'M', 1);" class="w-full bg-black text-white border border-black py-3 uppercase tracking-widest text-[10px] font-bold hover:bg-transparent hover:text-black transition-colors duration-300 flex justify-center items-center gap-2">
                    <span class="material-symbols-outlined text-[14px]">shopping_bag</span> Add to Cart
                </button>
            </div>
        </div>
        '''

# Create the full section HTML
# Note: The background is light bg-[#FAFAFA] to match the shop page's look & feel
new_section_html = f'''<!-- Best Sellers Section -->
<section class="py-16 bg-[#FAFAFA] border-t border-b border-outline-variant">
    <div class="px-5 md:px-12 lg:px-20 max-w-container-max mx-auto">
        <div class="text-center mb-12">
            <h2 class="font-headline-lg text-[28px] md:text-[36px] tracking-[0.2em] uppercase text-black">Best Sellers</h2>
            <div class="h-[1px] w-12 bg-black mx-auto mt-4"></div>
        </div>
        
        <!-- Product Grid (12 items) -->
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 md:gap-x-12 lg:gap-x-16 gap-y-12 lg:gap-y-20">
            {grid_html}
        </div>
    </div>
</section>'''

# 3. Read index.html and replace the old Best Sellers section
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# We look for <!-- Best Sellers Section --> up to the next section <!-- Service Icons Bar --> or the end of the section
# A regex search to find <!-- Best Sellers Section --> ... </section>
pattern = r'<!-- Best Sellers Section -->\s*<section.*?</section>'
index_html = re.sub(pattern, new_section_html, index_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Successfully replaced Best Sellers section with a 12-product grid in index.html")
