import re

with open('shop.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The grid is between <section class="px-5 md:px-12 lg:px-20 py-12 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 md:gap-x-12 lg:gap-x-16 gap-y-12 lg:gap-y-20">
# and </section>

# Inside it, we have:
# <div class="group cursor-pointer flex flex-col" onclick="window.location.href='product.html?id=prod_0'">
#     <div class="relative overflow-hidden bg-gray-100 aspect-[3/4] mb-4">
#         <img src="images/products/prod_0.png" alt="Sugarbaby" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
#     </div>

# Let's use regex to find all <div class="relative overflow-hidden...</div> and inject the button before the closing </div>
# But wait, we need the product ID. The parent div has `product.html?id=prod_0`.

# Regex to match the whole product card and inject the button
pattern = r'(<div class="group cursor-pointer flex flex-col" onclick="window\.location\.href=\'product\.html\?id=(prod_\d+)\'">(.*?<div class="relative overflow-hidden bg-gray-100 aspect-\[3/4\] mb-4">.*?)(</div>)'

def replacer(match):
    prod_id = match.group(2)
    start_html = match.group(1) # The full match string up to the inside of the inner div?
    # Actually, match.group(3) is the inner HTML of the parent up to the inside of the image div
    # Wait, the regex `(.*?)` might match too much.
    pass

# Better approach: parse and replace
cards = re.finditer(r'<div class="group cursor-pointer flex flex-col" onclick="window\.location\.href=\'product\.html\?id=(prod_\d+)\'">\s*<div class="relative overflow-hidden bg-gray-100 aspect-\[3/4\] mb-4">\s*<img[^>]+>\s*</div>', content, flags=re.DOTALL)

new_content = content
# Iterate in reverse to replace safely
for match in reversed(list(cards)):
    prod_id = match.group(1)
    full_card = match.group(0)
    
    # We want to insert the button right before the `</div>` of the image container
    # The image container ends with `</div>` in the matched string.
    # So we can just replace the last `</div>` in full_card
    button_html = f'\n        <button onclick="event.stopPropagation(); addToCart(\'{prod_id}\', \'M\', 1);" class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white/90 backdrop-blur-sm text-black px-6 py-3 uppercase tracking-widest text-[10px] font-bold opacity-0 group-hover:opacity-100 transition-opacity duration-300 hover:bg-black hover:text-white whitespace-nowrap shadow-sm border border-transparent">Add to Cart</button>\n    </div>'
    
    new_card = full_card.rsplit('</div>', 1)[0] + button_html
    
    new_content = new_content[:match.start(0)] + new_card + new_content[match.end(0):]

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Add to Cart buttons to shop.html")
