import re
import glob

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

best_sellers_section = re.search(r'<!-- Best Sellers Section -->(.*?)</section>', content, flags=re.DOTALL)
if best_sellers_section:
    section_html = best_sellers_section.group(1)
    
    prods = [glob.glob(f'images/products/prod_{i}.*')[0] for i in range(6)]
    
    img_srcs = re.findall(r'<img[^>]+src="([^"]+)"', section_html)
    for i, old_src in enumerate(img_srcs[:6]):
        section_html = section_html.replace(old_src, prods[i].replace('\\', '/'))
        
    new_content = content[:best_sellers_section.start(1)] + section_html + content[best_sellers_section.end(1):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated index.html best sellers images')
else:
    print('Could not find best sellers section')
