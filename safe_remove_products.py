import re
from bs4 import BeautifulSoup

# 1. Update js/cart.js safely
with open('js/cart.js', 'r', encoding='utf-8') as f:
    cart_js = f.read()

for prod_id in ['prod_21', 'prod_18', 'prod_12']:
    # Match the line starting with 'prod_X': and ending with },
    cart_js = re.sub(rf"\s*'{prod_id}':\s*{{.*?}},\n", '', cart_js)

with open('js/cart.js', 'w', encoding='utf-8') as f:
    f.write(cart_js)
print("Updated js/cart.js safely")

# 2. Update shop.html safely using BeautifulSoup
with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

soup = BeautifulSoup(shop_html, 'html.parser')

for prod_id in ['prod_21', 'prod_18', 'prod_12']:
    # Find the div with the specific onclick attribute
    target_attr = f"window.location.href='product.html?id={prod_id}'"
    target_div = soup.find('div', onclick=target_attr)
    if target_div:
        # Also remove the comment before it if it exists
        # BeautifulSoup doesn't easily let us delete preceding comments unless we navigate the tree,
        # but decompose() on the div is enough to remove it from the page layout.
        target_div.decompose()
        print(f"Removed {prod_id} from shop.html")
    else:
        print(f"Could not find {prod_id} in shop.html")

# Write the prettified HTML back
# BeautifulSoup's prettify() might change the formatting too much. Let's just write str(soup)
with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Updated shop.html safely")
