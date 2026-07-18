import re
from bs4 import BeautifulSoup

with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

soup = BeautifulSoup(shop_html, 'html.parser')

# Find the products grid container
# It's <section class="px-5 md:px-12 lg:px-20 py-12 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 md:gap-x-12 lg:gap-x-16 gap-y-12 lg:gap-y-20">
grid = soup.find('section', class_=lambda c: c and 'grid-cols-2' in c and 'gap-y-12' in c)
if grid:
    # Get all product cards (direct divs of the grid)
    cards = grid.find_all('div', recursive=False)
    
    # We also need to extract products database from js/cart.js to get exact details if needed, 
    # but we can just parse the existing text in the card.
    
    for card in cards:
        # Get product ID from onclick
        onclick = card.get('onclick', '')
        match = re.search(r"id=(prod_\d+)", onclick)
        if not match:
            continue
        pid = match.group(1)
        
        # Remove any absolute button from inside image container
        img_container = card.find('div', class_=lambda c: c and 'relative' in c and 'overflow-hidden' in c)
        if img_container:
            btn = img_container.find('button')
            if btn:
                btn.decompose()
        
        # We need to make the card a flex container to align the button to the bottom
        # Let's add classes: flex flex-col justify-between h-full
        # We will wrap the image + info in a div, and the button in another div.
        card['class'] = ['group', 'cursor-pointer', 'flex', 'flex-col', 'justify-between', 'h-full']
        
        # Find h3 and p (title and price)
        h3 = card.find('h3')
        p = card.find('p', class_=lambda c: c and 'text-gray-500' in c)
        
        # Wrap top part
        top_div = soup.new_tag('div')
        # Move image container, h3, p into top_div
        if img_container:
            top_div.append(img_container.extract())
        
        # Create an info wrapper div for padding
        info_div = soup.new_tag('div', attrs={"class": "px-1 mt-2"})
        if h3:
            h3['class'] = ['font-bold', 'text-sm', 'uppercase', 'tracking-widest', 'mb-1', 'line-clamp-2']
            info_div.append(h3.extract())
        if p:
            info_div.append(p.extract())
        top_div.append(info_div)
        
        # Create bottom button div
        btn_div = soup.new_tag('div', attrs={"class": "mt-4 px-1"})
        new_btn = soup.new_tag('button', onclick=f"event.stopPropagation(); addToCart('{pid}', 'M', 1);", 
                               attrs={"class": "w-full bg-black text-white border border-black py-3 uppercase tracking-widest text-[10px] font-bold hover:bg-transparent hover:text-black transition-colors duration-300 flex justify-center items-center gap-2"})
        
        # Add shopping bag icon
        icon = soup.new_tag('span', attrs={"class": "material-symbols-outlined text-[14px]"})
        icon.string = "shopping_bag"
        new_btn.append(icon)
        new_btn.append(" Add to Cart")
        
        btn_div.append(new_btn)
        
        # Clear original card and append new structure
        card.clear()
        card.append(top_div)
        card.append(btn_div)

# Save changes
with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully redesigned shop.html cards")
