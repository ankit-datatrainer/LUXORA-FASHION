import os
import shutil
import re
import glob

# 1. Move images to the images folder
img_dir = 'c:\\Users\\ankit\\OneDrive\\Desktop\\Clothing_brand\\images'
os.makedirs(img_dir, exist_ok=True)

brain_dir = 'C:\\Users\\ankit\\.gemini\\antigravity-ide\\brain\\ff3fc6e0-111b-4be7-aaba-22f06776c1ff'
cat_images = glob.glob(os.path.join(brain_dir, 'cat_*.png'))

for img in cat_images:
    filename = os.path.basename(img)
    match = re.match(r'(cat_[a-z_]+)_\d+\.png', filename)
    if match:
        new_filename = match.group(1) + '.png'
        shutil.copy(img, os.path.join(img_dir, new_filename))

categories = [
    ('Bestsellers', 'cat_bestsellers.png'),
    ('New Arrivals', 'cat_new_arrivals.png'),
    ('Roleplay', 'cat_roleplay.png'),
    ('Latex', 'cat_latex.png'),
    ('Plus Size', 'cat_plus_size.png'),
    ('Babydolls', 'cat_babydolls.png'),
    ('Bridal', 'cat_bridal.png'),
    ('Lingerie Sets', 'cat_lingerie_sets.png'),
    ('Fishnet', 'cat_fishnet.png'),
    ('Bodysuits', 'cat_bodysuits.png')
]

categories_html = '''
<!-- Circular Categories Bar -->
<section class="border-b border-outline-variant bg-surface">
    <div class="px-5 md:px-margin-x py-6">
        <div class="flex gap-6 overflow-x-auto hide-scroll snap-x">
'''

for name, img in categories:
    url_slug = name.lower().replace(' ', '-')
    categories_html += f'''
            <a href="shop.html?category={url_slug}" class="flex flex-col items-center gap-3 min-w-[80px] sm:min-w-[100px] snap-start group">
                <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-full p-[3px] bg-gradient-to-tr from-indigo-200 via-pink-200 to-amber-100 transition-transform duration-300 group-hover:scale-105">
                    <div class="w-full h-full rounded-full overflow-hidden border-[3px] border-surface">
                        <img src="images/{img}" alt="{name}" class="w-full h-full object-cover">
                    </div>
                </div>
                <span class="font-label-md text-on-surface whitespace-nowrap group-hover:text-primary transition-colors">{name}</span>
            </a>
'''

categories_html += '''
        </div>
    </div>
</section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<!-- Quick Categories -->.*?</section>', re.DOTALL)
new_content = pattern.sub(categories_html.strip(), content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully replaced category section and copied images.')
