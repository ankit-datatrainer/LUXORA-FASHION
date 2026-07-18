import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

best_sellers_section_match = re.search(r'(<!-- Best Sellers Section -->\s*<section class="py-section-gap bg-black text-white">.*?)(</section>)', content, flags=re.DOTALL)
if best_sellers_section_match:
    section_start_to_grid = best_sellers_section_match.group(1)
    
    # We will use regex to find all cards inside the section
    # The cards start with <div class="min-w-[200px]...
    # We can reconstruct the cards from the known prod_ids.
    
    # Wait, the cards have specific titles and emojis. They are already correct because they were scraped.
    # So let's just parse the 6 cards and modify their HTML.
    
    def replacer(match):
        prod_id = match.group(1)
        img_html = match.group(2)
        title_html = match.group(3)
        price_html = match.group(4)
        
        # New Card UI
        # Remove the hover button from inside the image (if it exists)
        img_html = re.sub(r'<button.*?Add to Cart</button>', '', img_html, flags=re.DOTALL)
        
        # Rebuild the card
        return f'''<div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer flex flex-col justify-between" onclick="window.location.href='product.html?id={prod_id}'">
            <div>
                {img_html}
                <div class="mt-4 px-1">
                    {title_html}
                    {price_html}
                </div>
            </div>
            <div class="mt-4 px-1">
                <button onclick="event.stopPropagation(); addToCart('{prod_id}', 'M', 1);" class="w-full bg-white text-black py-3 uppercase tracking-widest text-[11px] font-bold hover:bg-gray-200 transition-colors flex justify-center items-center gap-2">
                    <span class="material-symbols-outlined text-[16px]">shopping_bag</span> Add to Cart
                </button>
            </div>
        </div>'''

    # Pattern to match the old cards
    pattern = r'<div class="min-w-\[200px\].*?onclick="window\.location\.href=\'product\.html\?id=(prod_\d+)\'">\s*(<div class="relative overflow-hidden bg-gray-100 aspect-\[3/4\] mb-4">.*?</div>)\s*(<h3 class="font-bold text-sm.*?>.*?</h3>)\s*(<p class="text-gray-400 text-xs">.*?</p>).*?</div>'
    
    # Actually, the old cards have swatches. The regex `.*?</div>` at the end might match too much.
    # Let's match more carefully:
    # 1. start div
    # 2. img container
    # 3. title
    # 4. price
    # 5. anything else (like swatches) until the closing </div> of the card.
    
    # Better approach: since we know the exact 6 products (0 to 5) and we can pull their data from cart.js
    pass

import json
# Let's just pull from cart.js to rebuild the section perfectly.
with open('js/cart.js', 'r', encoding='utf-8') as f:
    cart_js = f.read()

products = {}
for match in re.finditer(r"'(prod_\d+)': \{ id: '[^']+', name: '([^']+)', price: ([\d.]+), image: '([^']+)' \}", cart_js):
    products[match.group(1)] = {
        'name': match.group(2),
        'price': float(match.group(3)),
        'image': match.group(4)
    }

# Top 6 best sellers are prod_0 to prod_5
cards_html = ""
for i in range(6):
    pid = f"prod_{i}"
    if pid in products:
        p = products[pid]
        cards_html += f'''
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer flex flex-col justify-between" onclick="window.location.href='product.html?id={pid}'">
            <div>
                <div class="relative overflow-hidden bg-gray-100 aspect-[3/4] mb-4">
                    <img src="{p['image']}" alt="{p['name']}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                </div>
                <div class="px-1">
                    <h3 class="font-bold text-sm tracking-wide mb-1 text-white line-clamp-2">{p['name']}</h3>
                    <p class="text-gray-400 text-xs">Rs. {p['price']:.2f}</p>
                </div>
            </div>
            <div class="mt-4 px-1">
                <button onclick="event.stopPropagation(); addToCart('{pid}', 'M', 1);" class="w-full bg-white text-black border border-white py-3 uppercase tracking-widest text-[10px] font-bold hover:bg-transparent hover:text-white transition-colors duration-300 flex justify-center items-center gap-2">
                    <span class="material-symbols-outlined text-[14px]">shopping_bag</span> Add to Cart
                </button>
            </div>
        </div>
        '''

# Now replace the scroll container contents
new_content = re.sub(r'(<div class="flex overflow-x-auto snap-x snap-mandatory gap-5 md:gap-6 hide-scrollbar px-5 md:px-0">).*?(</div>\s*</div>\s*</section>)', 
                     r'\1\n' + cards_html + r'\n\2', 
                     content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html best sellers UI")
