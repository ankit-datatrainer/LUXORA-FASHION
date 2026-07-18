import re

# Remove from cart.js
with open('js/cart.js', 'r', encoding='utf-8') as f:
    cart_js = f.read()

for prod_id in ['prod_21', 'prod_18', 'prod_12']:
    cart_js = re.sub(rf"    '{prod_id}': {{ id: '{prod_id}'.*?\n", '', cart_js)

with open('js/cart.js', 'w', encoding='utf-8') as f:
    f.write(cart_js)

# Remove from shop.html
with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

for prod_id in ['prod_21', 'prod_18', 'prod_12']:
    # The div spans multiple lines until the next <!-- Product: ... --> or the closing </section>
    # Better: find the start of the card and grab the next 5-6 lines until the closing </div> of the card.
    # Actually, they are wrapped in an HTML comment: <!-- Product: Shadow Queen Set -->
    # We can match from <!-- Product: to the end of the card's outer div
    pattern = rf'\s*<!-- Product: [^-]*?-->\s*<div class="group cursor-pointer flex flex-col" onclick="window\.location\.href=\'product\.html\?id={prod_id}\'">.*?</div>\s*</div>'
    shop_html = re.sub(pattern, '', shop_html, flags=re.DOTALL)
    
    # Also another regex without the comment just in case
    pattern2 = rf'\s*<div class="group cursor-pointer flex flex-col" onclick="window\.location\.href=\'product\.html\?id={prod_id}\'">.*?</div>\s*</div>'
    shop_html = re.sub(pattern2, '', shop_html, flags=re.DOTALL)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(shop_html)

print("Removed products 12, 18, 21")
