import urllib.request
from bs4 import BeautifulSoup
import json

urls = {
    'home': 'https://snowra.in/',
    'about': 'https://snowra.in/pages/about-us',
    'contact': 'https://snowra.in/pages/contact',
    'faq': 'https://snowra.in/pages/faqs'
}

data = {}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove scripts and styles
        for script in soup(["script", "style", "noscript", "svg"]):
            script.extract()
            
        text = soup.get_text(separator='\n', strip=True)
        # basic cleanup
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        data[name] = lines
    except Exception as e:
        data[name] = str(e)

with open('snowra_scraped.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
