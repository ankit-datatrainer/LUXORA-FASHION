import json
import os
import urllib.request
import re
import uuid

# User's list of products with exact prices
user_list = [
    ("Sugarbaby", 899.00),
    ("Latex Bunny Roleplay Set", 1199.00),
    ("Bridal theme Lace Set", 999.00),
    ("Dominatrix Harness Dress (Stocking incl)", 999.00),
    ("Desert Fantasy Set", 999.00),
    ("Pikachu Cosplay Bodysuit", 749.00),
    ("cat roleplay fantasy Full set with Headgear", 999.00),
    ("Dark Web Cosplay Bodysuit (stockings included)", 999.00),
    ("Hot Muse Lace Fantasy Set", 899.00),
    ("Afterparty Pearl Shirt", 999.00),
    ("Leopard Baddie Bodysuit+Belt", 949.00),
    ("Babygirl Lingerie set with gloves", 899.00),
    ("Date Night Sparkling Bodystocking full", 849.00),
    ("Bunny Velvet Roleplay", 1199.00),
    ("Rainbow Babie", 849.00),
    ("Bubblegum Baddie", 949.00),
    ("Bridal Roleplay Dress", 999.00),
    ("Latex Main Character Jacket", 1199.00),
    ("Shadow Queen Set", 799.00),
    ("Leopard Tease Stocking Set (4pc)", 999.00),
    ("Black flow Long lace lingerie", 799.00),
    ("Knotty Night Set", 749.00),
    ("Latex Gold Leash set", 899.00),
    ("The Forbidden Dress", 799.00),
    ("Baddie Garter Set & Bodysuit", 749.00),
    ("Cheetah Print Garter Set", 999.00),
    ("Wifey After Dark Set", 799.00),
    ("Good Girl Lace Roleplay", 949.00),
    ("Latex Baddie Nurse Roleplay", 1499.00),
    ("Black rhinestone Lingerie", 749.00),
    ("Maid Purple Roleplay Fantasy Full Set", 999.00),
    ("Crystal Mesh Bodysuit", 849.00),
    ("Skin Tease Bodysuit", 999.00),
    ("Pink Bunny roleplay full set", 1499.00),
    ("Honeybun", 999.00),
    ("Latex Curve-Fit Bodysuit", 949.00),
    ("High voltage Bodysuit", 899.00),
    ("Latex Deep Cut Lingerie+stocking", 999.00),
    ("RIPPED Bodystocking", 599.00),
    ("Love Lace Babydoll", 599.00)
]

with open('test_scrape.json', 'r', encoding='utf-8') as f:
    scraped_data = json.load(f)

# Find first matching image for each product
def clean_title(title):
    return re.sub(r'[^\w\s]', '', title).lower().strip()

os.makedirs('images/products', exist_ok=True)

final_products = []
cart_products_js = "const PRODUCTS = {\n"
shop_html_grid = ""

for i, (name, price) in enumerate(user_list):
    c_name = clean_title(name)
    img_url = ""
    # Try finding in scraped
    for item in scraped_data:
        if c_name in clean_title(item['title']) and item['image']:
            img_url = item['image']
            break
            
    # if not found, use a placeholder
    if not img_url:
        img_url = "https://via.placeholder.com/600x800?text=" + urllib.parse.quote(name)

    pid = f"prod_{i}"
    ext = ".jpg" if ".jpg" in img_url.lower() else ".png"
    local_img_path = f"images/products/{pid}{ext}"
    
    # Download image
    if not img_url.startswith("http"):
        # fallback for placeholders
        if not os.path.exists(local_img_path):
            try:
                urllib.request.urlretrieve("https://via.placeholder.com/600x800?text=Image", local_img_path)
            except: pass
    else:
        if not os.path.exists(local_img_path):
            try:
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(local_img_path, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print("Failed to download", img_url, e)
                try:
                    urllib.request.urlretrieve("https://via.placeholder.com/600x800?text=Image", local_img_path)
                except: pass
                
    safe_name = name.replace("'", "")
    cart_products_js += f"    '{pid}': {{ id: '{pid}', name: '{safe_name}', price: {price}, image: '{local_img_path}' }},\n"
    
    # Shop grid HTML
    shop_html_grid += f"""
            <!-- Product: {name} -->
            <div class="group cursor-pointer flex flex-col" onclick="window.location.href='product.html?id={pid}'">
                <div class="relative overflow-hidden bg-gray-100 aspect-[3/4] mb-4">
                    <img src="{local_img_path}" alt="{name}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                </div>
                <h3 class="font-bold text-sm uppercase tracking-widest mb-1">{name}</h3>
                <p class="text-gray-500 text-sm">Rs. {price:.2f}</p>
            </div>"""

cart_products_js += "};\n"

# Output cart products dict to file so we can copy it to cart.js
with open('generated_cart_products.js', 'w', encoding='utf-8') as f:
    f.write(cart_products_js)

# Output shop grid to file so we can inject into shop.html
with open('generated_shop_grid.html', 'w', encoding='utf-8') as f:
    f.write(shop_html_grid)
    
print("Successfully processed all 40 products and downloaded images.")
