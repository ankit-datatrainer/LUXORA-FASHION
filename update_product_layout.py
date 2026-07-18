import re

# Read index.html to extract the correct header and mobile menu
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the sticky header container
header_match = re.search(r'(<!-- Sticky Header Container -->.*?)</nav>\s*</div>', index_content, re.DOTALL)
header_html = header_match.group(1) + '</nav>\n</div>'

# Extract the mobile menu overlay
mobile_menu_match = re.search(r'(<!-- Mobile Menu Overlay -->.*?</div>\s*</div>)', index_content, re.DOTALL)
mobile_menu_html = mobile_menu_match.group(1)

combined_header = header_html + '\n' + mobile_menu_html

# Extract the footer
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
footer_html = footer_match.group(1)

# Now update product.html
with open('product.html', 'r', encoding='utf-8') as f:
    product_content = f.read()

# Replace Header (everything from <header ...> to </header>)
product_content = re.sub(r'<header id="main-header".*?</header>', combined_header, product_content, flags=re.DOTALL)

# Replace Footer
product_content = re.sub(r'<footer.*?</footer>', footer_html, product_content, flags=re.DOTALL)

with open('product.html', 'w', encoding='utf-8') as f:
    f.write(product_content)

print("Updated product.html with global header and footer")
