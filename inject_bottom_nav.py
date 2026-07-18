import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['generated_shop_grid.html']]

# Read the bottom nav from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

bottom_nav_match = re.search(r'<!-- BottomNavBar for Mobile -->(.*?)<\/nav>', index_content, re.DOTALL)
if not bottom_nav_match:
    print("Could not find bottom nav in index.html")
    exit(1)

# Ensure it has z-[80] so it's above the mobile menu (z-[70])
bottom_nav = '<!-- BottomNavBar for Mobile -->' + bottom_nav_match.group(1) + '</nav>'
bottom_nav = bottom_nav.replace('z-[60]', 'z-[80]')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update or insert bottom nav
    if '<!-- BottomNavBar for Mobile -->' in content:
        # replace existing
        content = re.sub(r'<!-- BottomNavBar for Mobile -->.*?<\/nav>', bottom_nav, content, flags=re.DOTALL)
    else:
        # insert before <script src="js/app.js"> or </body>
        if '<script src="js/app.js">' in content:
            content = content.replace('<script src="js/app.js">', bottom_nav + '\n\n<script src="js/app.js">')
        else:
            content = content.replace('</body>', bottom_nav + '\n</body>')
    
    # Also add padding to the bottom of the mobile menu so it doesn't get obscured
    # Find the mobile menu inner container: <div class="p-6 flex flex-col h-full">
    if '<div class="p-6 flex flex-col h-full">' in content:
        content = content.replace('<div class="p-6 flex flex-col h-full">', '<div class="p-6 pb-24 flex flex-col h-full">')
    
    # Fix the toggleMenu javascript bug if any HTML has translate-x-full while app.js checks for -translate-x-full
    # Wait, the app.js is not modified here. Let's just fix app.js directly later if needed.
    # Actually, let's fix the HTML to use -translate-x-full so it matches app.js
    if 'translate-x-full transition-transform duration-500 md:hidden" id="mobile-menu"' in content and '-translate-x-full' not in content:
        content = content.replace('translate-x-full transition-transform', '-translate-x-full transition-transform')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file}")

