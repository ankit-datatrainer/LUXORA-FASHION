import re

# 1. Update js/cart.js to support both selectors and classes from app.js
with open('js/cart.js', 'r', encoding='utf-8') as f:
    cart_content = f.read()

# Update updateCartUI to find both .cart-count and .cart-badge
cart_content = cart_content.replace(
    "const cartCountElements = document.querySelectorAll('.cart-count');",
    "const cartCountElements = document.querySelectorAll('.cart-count, .cart-badge');"
)

# Update DOMContentLoaded to attach listeners to both .shopping-bag-icon and .cart-icon-toggle
cart_content = cart_content.replace(
    "const bagIcons = document.querySelectorAll('.shopping-bag-icon');",
    "const bagIcons = document.querySelectorAll('.shopping-bag-icon, .cart-icon-toggle');"
)

with open('js/cart.js', 'w', encoding='utf-8') as f:
    f.write(cart_content)
print("Updated js/cart.js with unified selectors")


# 2. Remove cart logic from js/app.js
with open('js/app.js', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Remove the line `initCart();` from DOMContentLoaded
app_content = app_content.replace("    initCart();\n", "")

# Remove the section 2: SHOPPING CART LOGIC
# The section starts with /* ==============================\n   2. SHOPPING CART LOGIC
# and ends before /* ==============================\n   3. SHOP FILTER
pattern = r'/\* =+ \s*2\. SHOPPING CART LOGIC.*?(?=/\* =+ \s*3\. SHOP FILTER)'
app_content = re.sub(pattern, '', app_content, flags=re.DOTALL)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_content)
print("Removed cart logic from js/app.js to prevent conflicts")
