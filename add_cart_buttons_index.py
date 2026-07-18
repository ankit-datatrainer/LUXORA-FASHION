import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

cards = re.finditer(r'<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer" onclick="window\.location\.href=\'product\.html\?id=(prod_\d+)\'">\s*<div class="relative overflow-hidden bg-gray-100 aspect-\[3/4\] mb-4">\s*<img[^>]+>\s*</div>', content, flags=re.DOTALL)

new_content = content
for match in reversed(list(cards)):
    prod_id = match.group(1)
    full_card = match.group(0)
    
    button_html = f'\n        <button onclick="event.stopPropagation(); addToCart(\'{prod_id}\', \'M\', 1);" class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white/90 backdrop-blur-sm text-black px-4 py-2 uppercase tracking-widest text-[10px] font-bold opacity-0 group-hover:opacity-100 transition-opacity duration-300 hover:bg-black hover:text-white whitespace-nowrap shadow-sm border border-transparent">Add to Cart</button>\n    </div>'
    
    new_card = full_card.rsplit('</div>', 1)[0] + button_html
    
    new_content = new_content[:match.start(0)] + new_card + new_content[match.end(0):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Add to Cart buttons to index.html Best Sellers")
