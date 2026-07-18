import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add <script src="js/cart.js"></script> before </body>
if '<script src="js/cart.js"></script>' not in content:
    content = content.replace('</body>', '<script src="js/cart.js"></script>\n</body>')

# In the Best Sellers section, we have these divs:
# <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
# Let's change them to links or add onclick
# But earlier we added them in update_bestsellers.py without explicit links.
# We will use re.sub to inject onclick handlers for the specific products based on the alt tags.

replacements = [
    (r'(<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer")(.*?alt="Sugarbaby")',
     r'\1 onclick="window.location.href=\'product.html?id=sugarbaby\'"\2'),
    (r'(<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer")(.*?alt="Latex Bunny Roleplay Set")',
     r'\1 onclick="window.location.href=\'product.html?id=roleplay\'"\2'),
    (r'(<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer")(.*?alt="Bridal theme Lace Set")',
     r'\1 onclick="window.location.href=\'product.html?id=bridal\'"\2'),
    (r'(<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer")(.*?alt="Dominatrix Harness Dress")',
     r'\1 onclick="window.location.href=\'product.html?id=dominatrix\'"\2'),
    (r'(<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer")(.*?alt="Desert Fantasy Set")',
     r'\1 onclick="window.location.href=\'product.html?id=desert\'"\2'),
    (r'(<div class="min-w-\[200px\] md:min-w-\[calc\(16\.666%-20px\)\] snap-start group cursor-pointer")(.*?alt="Pikachu Cosplay Bodysuit")',
     r'\1 onclick="window.location.href=\'product.html?id=pikachu\'"\2')
]

for pattern, repl in replacements:
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html best sellers links and injected cart.js")

# Now inject cart.js into shop.html, about.html, contact.html
for page in ['shop.html', 'about.html', 'contact.html']:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            pcontent = f.read()
        if '<script src="js/cart.js"></script>' not in pcontent:
            pcontent = pcontent.replace('</body>', '<script src="js/cart.js"></script>\n</body>')
            with open(page, 'w', encoding='utf-8') as f:
                f.write(pcontent)
            print(f"Injected cart.js into {page}")
    except:
        pass
