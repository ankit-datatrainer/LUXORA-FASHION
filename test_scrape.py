import urllib.request
import re
import json
from bs4 import BeautifulSoup

url = 'https://snowra.in/collections/bestsellers'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')

products = []

# Typical Shopify structure: looking for anything with 'grid__item' or 'product' classes that contain an image
for card in soup.find_all(class_=re.compile(r'card|product-item')):
    title_elem = card.find(class_=re.compile(r'title|heading'))
    if not title_elem:
        continue
    
    title = title_elem.text.strip()
    if not title:
        continue
        
    price_elem = card.find(class_=re.compile(r'price'))
    price = price_elem.text.strip() if price_elem else ''
    
    img = card.find('img')
    img_src = img['src'] if img else ''
    if img_src.startswith('//'):
        img_src = 'https:' + img_src
        
    products.append({'title': title, 'price': price, 'image': img_src})

print(f"Found {len(products)} products via bs4")

# Another approach: find product JSON data in page
json_data = re.findall(r'window\.ShopifyAnalytics\.lib\.page = (\{.*?\});', html)
if json_data:
    print("Found ShopifyAnalytics")

# Alternatively, just look for product schema
schemas = soup.find_all('script', type='application/ld+json')
found_schema = False
for s in schemas:
    try:
        data = json.loads(s.string)
        if isinstance(data, list):
            data = data[0]
        if data.get('@type') in ['ItemList', 'Product']:
            print("Found schema:", data.get('@type'))
            found_schema = True
    except:
        pass
        
with open('test_scrape.json', 'w') as f:
    json.dump(products, f, indent=2)
