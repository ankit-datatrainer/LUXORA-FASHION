import re
with open('shop.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
with open('generated_shop_grid.html', 'r', encoding='utf-8') as f:
    grid_html = f.read()

grid_start = '<section class="px-5 md:px-12 lg:px-20 py-12 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-6 md:gap-x-12 lg:gap-x-16 gap-y-12 lg:gap-y-20">'
grid_end = '</section>'

match = re.search(re.escape(grid_start) + r'(.*?)' + re.escape(grid_end), content, flags=re.DOTALL)
if match:
    new_content = content[:match.start(1)] + '\n' + grid_html + '\n' + content[match.end(1):]
    with open('shop.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated shop.html')
else:
    print('Could not find grid container')
