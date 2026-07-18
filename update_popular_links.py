import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'(<div class="md:col-span-1 md:row-span-2 relative group cursor-pointer overflow-hidden")(.*?alt="Bridal theme lingerie")',
     r'\1 onclick="window.location.href=\'product.html?id=bridal\'"\2'),
    (r'(<div class="md:col-span-2 md:row-span-1 relative group cursor-pointer overflow-hidden")(.*?alt="Babydolls collection")',
     r'\1 onclick="window.location.href=\'product.html?id=sugarbaby\'"\2'),
    (r'(<div class="md:col-span-1 md:row-span-1 relative group cursor-pointer overflow-hidden")(.*?alt="Roleplay costumes")',
     r'\1 onclick="window.location.href=\'product.html?id=roleplay\'"\2'),
    (r'(<div class="sm:col-span-2 lg:col-span-3 md:row-span-1 relative group cursor-pointer overflow-hidden")(.*?alt="Latex Edition")',
     r'\1 onclick="window.location.href=\'product.html?id=dominatrix\'"\2')
]

for pattern, repl in replacements:
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html popular collection links")
