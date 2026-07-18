import os
import re

files = ['shop.html', 'about.html', 'contact.html']

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The mobile menu is missing a closing </div> right before <main
        # Let's fix this reliably.
        if '</div>\n<main' in content:
            content = content.replace('</div>\n<main', '</div>\n</div>\n<main')
        elif '</div><main' in content:
            content = content.replace('</div><main', '</div></div><main')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {file}')
    except Exception as e:
        print(e)
