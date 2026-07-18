import re

# Read index.html to extract the correct header and mobile menu
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the sticky header container
header_match = re.search(r'(<!-- Sticky Header Container -->.*?)</nav>\s*</div>', index_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)
header_html = header_match.group(1) + '</nav>\n</div>'

# Extract the mobile menu overlay
mobile_menu_match = re.search(r'(<!-- Mobile Menu Overlay -->.*?</div>\s*</div>)', index_content, re.DOTALL)
if not mobile_menu_match:
    print("Could not find mobile menu in index.html")
    exit(1)
mobile_menu_html = mobile_menu_match.group(1)

combined_header_and_menu = header_html + '\n' + mobile_menu_html

# Update shop.html, about.html, contact.html
files_to_update = ['shop.html', 'about.html', 'contact.html']

for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove existing sticky header / utility bars
        # This regex looks for <!-- Sticky Header Container --> or <!-- Utility Bar --> up to <main
        new_content = re.sub(r'<!-- (Sticky Header Container|Utility Bar|Small TopAppBar).*?<main', 
                             combined_header_and_menu + '\n<main', 
                             content, 
                             flags=re.DOTALL)
                             
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

# Now update the slider images in index.html
# The current slider images are shopify CDN links
slider_images = [
    'images/luxora_babydoll.png',
    'images/luxora_seduction.png',
    'images/luxora_essentials.png'
]

# Replace first 3 img src in the hero-slider section
slider_match = re.search(r'<section[^>]*id="hero-slider".*?</section>', index_content, re.DOTALL)
if slider_match:
    slider_content = slider_match.group(0)
    # Replace the src attributes of images inside slider_content
    # Find all <img src="..."> in the slider
    img_tags = re.findall(r'<img[^>]*src="([^"]+)"', slider_content)
    new_slider_content = slider_content
    for i, old_src in enumerate(img_tags):
        if i < 3:
            new_slider_content = new_slider_content.replace(f'src="{old_src}"', f'src="{slider_images[i]}"')
    
    index_content = index_content.replace(slider_content, new_slider_content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Successfully updated slider images in index.html")
else:
    print("Could not find hero-slider in index.html")
