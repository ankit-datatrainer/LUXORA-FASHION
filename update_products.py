import re
import os

with open('shop.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define a function to process each product card
def process_product(match):
    original_html = match.group(0)
    
    # Extract title and price
    title_match = re.search(r'<h3[^>]*>(.*?)</h3>', original_html)
    title = title_match.group(1).strip() if title_match else "Product"
    
    # Price
    price_match = re.search(r'>₹([0-9\.]+)</p>', original_html)
    if not price_match:
        price_match = re.search(r'>\$([0-9\.]+)\s', original_html)
    price = price_match.group(1) if price_match else "0.00"
    
    # Image
    img_match = re.search(r'src="(.*?)"', original_html)
    img_src = img_match.group(1) if img_match else ""
    
    # ID based on title
    prod_id = re.sub(r'[^a-zA-Z0-9]', '_', title.lower())
    
    # Add data attributes to the outer div
    new_html = original_html.replace('class="group cursor-pointer"', f'class="group cursor-pointer product-card relative" data-id="{prod_id}" data-price="{price}" data-title="{title}"')
    
    # Add "Add to Cart" button inside the image container
    add_btn = f'''
    <button class="add-to-cart-btn absolute bottom-0 left-0 w-full bg-primary text-on-primary font-label-md text-xs py-3 tracking-[0.2em] uppercase translate-y-full group-hover:translate-y-0 transition-transform duration-300 active:bg-secondary z-20" data-id="{prod_id}" data-title="{title}" data-price="{price}" data-image="{img_src}">
        Add to Cart
    </button>
    '''
    
    # Insert button right before the closing div of the image container
    # The image container ends right before the </h3>
    new_html = new_html.replace('</div>\n<h3', f'{add_btn}</div>\n<h3')
    
    return new_html

# Apply replacement to each product card
updated_content = re.sub(r'<div class="group cursor-pointer">.*?</div>\s*</div>', process_product, content, flags=re.DOTALL)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Products updated successfully.")
