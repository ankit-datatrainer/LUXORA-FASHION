import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        # Top banner
        r'FREE SHIPPING ON ORDERS OVER \$99': 'For Urgent Express Shipping - Whatsapp us | Prepaid Orders FREE Blindfold',
        
        # Navigation
        r'>NEW IN<': '>Roleplay & Cosplay<',
        r'>WOMEN<': '>Babydolls<',
        r'>MEN<': '>Gift for Her<',
        r'>ACCESSORIES<': '>LATEX EDITION<',
        r'>SHOES<': '>Plus Size Collection<',
        r'>SALE<': '>New Arrivals<',

        # Footer links
        r'>New Arrivals<': '>Roleplay & Cosplay<',
        r'>Best Sellers<': '>Babydolls<',
        r'>Women\'s Collection<': '>Gift for Her<',
        r'>Men\'s Collection<': '>LATEX EDITION<',
        
        # Hero section (index.html)
        r'NEW SEASON': 'LUXORA FASHION',
        r'SPRING / SUMMER <br/>\s*COLLECTION': 'UNLEASH YOUR<br/>INNER SEDUCTION',
        r'Elevate your style with the latest trends and timeless essentials\.': 'We design lingerie for those who lead with desire, move with intention, and aren\'t afraid to be seen exactly as they are.',
        
        # About Us (about.html)
        r'Founded in a small atelier on the coast of Italy, Luxora Fashion was born from a desire to redefine luxury through simplicity\. We believe that true sophistication doesn\'t shout; it speaks in the quality of the stitch and the drape of the fabric\.': 'LUXORA FASHION exists to break the silence and bring back what routine quietly steals - the spark. We create pieces that don\'t just sit in your wardrobe, they change the mood, shift the energy, and turn ordinary nights into something unforgettable. Because sometimes, it\'s not about doing more - it\'s about feeling differently. Based in Delhi.',
        
        # Contact Us placeholders (contact.html)
        r'We\'re here to assist you with any questions about our collections, sizing, or your recent order\.': 'We would love to hear from you. If you\'ve got great products you\'re making or looking to work with us then drop us a line.',
        r'\+1 \(555\) 123-4567': '+391 (0)35 2568 4593',
        r'clientcare@luxorafashion\.com': 'hello@domain.com',
        r'123 Via della Moda<br/>Milan, Italy 20121': '7895 Piermont Dr NE<br/>Albuquerque, NM 198866',
        r'Monday - Friday: 9am - 6pm CET<br/>Saturday - Sunday: Closed': 'Every day 11am to 7pm',
        r'Client Services': 'Information',
        r'Showroom': 'Address'
    }

    original_content = content
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes made to {filepath}")

if __name__ == "__main__":
    html_files = glob.glob('*.html')
    for f in html_files:
        process_file(f)
