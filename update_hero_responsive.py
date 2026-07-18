import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new responsive slides HTML
# Slide 1: Unleash Your Inner Seduction
# Slide 2: Luxury Babydolls
# Slide 3: Bold & Unapologetic

new_slides_html = '''
        <!-- Slide 1 -->
        <div class="w-full h-full flex-shrink-0 relative flex flex-col md:flex-row">
            <!-- Content Column -->
            <div class="absolute inset-0 md:relative md:w-1/2 h-full bg-black/50 md:bg-black flex flex-col items-center justify-center text-center px-6 md:px-12 lg:px-20 z-10 py-12">
                <p class="font-label-md text-label-md uppercase tracking-[0.3em] mb-4 text-white/90">LUXORA FASHION</p>
                <h1 class="font-display-lg text-[36px] md:text-headline-lg lg:text-[56px] uppercase leading-tight mb-6 text-white">
                    UNLEASH YOUR<br class="hidden md:block"/>INNER SEDUCTION
                </h1>
                <div class="h-[1px] w-16 bg-white/70 mb-6"></div>
                <p class="font-body-lg text-sm md:text-body-lg text-white/80 max-w-md mb-10">
                    We design lingerie for those who lead with desire, move with intention, and aren't afraid to be seen exactly as they are.
                </p>
                <a href="shop.html" class="inline-block bg-white text-black font-label-md text-label-md uppercase tracking-widest px-10 py-4 hover:bg-gray-200 transition-colors duration-300 active:scale-95 shadow-lg">
                    SHOP NOW
                </a>
            </div>
            <!-- Image Column -->
            <div class="absolute inset-0 md:relative md:w-1/2 h-full z-0">
                <div class="w-full h-full bg-cover bg-center md:bg-[center_top_10%]" style="background-image: url('https://cdn.shopify.com/s/files/1/0918/2619/2702/files/81A3EB64-59FF-473D-910F-2577A2B46F4B.jpg?v=1783893989')"></div>
            </div>
        </div>

        <!-- Slide 2 -->
        <div class="w-full h-full flex-shrink-0 relative flex flex-col md:flex-row">
            <!-- Content Column -->
            <div class="absolute inset-0 md:relative md:w-1/2 h-full bg-black/50 md:bg-black flex flex-col items-center justify-center text-center px-6 md:px-12 lg:px-20 z-10 py-12">
                <p class="font-label-md text-label-md uppercase tracking-[0.3em] mb-4 text-white/90">NEW ARRIVALS</p>
                <h1 class="font-display-lg text-[36px] md:text-headline-lg lg:text-[56px] uppercase leading-tight mb-6 text-white">
                    LUXURY<br class="hidden md:block"/>BABYDOLLS
                </h1>
                <div class="h-[1px] w-16 bg-white/70 mb-6"></div>
                <p class="font-body-lg text-sm md:text-body-lg text-white/80 max-w-md mb-10">
                    Elegance meets temptation in our newest collection of delicate lace and sheer chiffon babydolls.
                </p>
                <a href="shop.html" class="inline-block bg-white text-black font-label-md text-label-md uppercase tracking-widest px-10 py-4 hover:bg-gray-200 transition-colors duration-300 active:scale-95 shadow-lg">
                    EXPLORE NOW
                </a>
            </div>
            <!-- Image Column -->
            <div class="absolute inset-0 md:relative md:w-1/2 h-full z-0">
                <div class="w-full h-full bg-cover bg-center md:bg-[center_top_10%]" style="background-image: url('https://cdn.shopify.com/s/files/1/0918/2619/2702/files/CD7BF4CA-0D51-498C-8DD0-BCA519951175.jpg?v=1783110627')"></div>
            </div>
        </div>

        <!-- Slide 3 -->
        <div class="w-full h-full flex-shrink-0 relative flex flex-col md:flex-row">
            <!-- Content Column -->
            <div class="absolute inset-0 md:relative md:w-1/2 h-full bg-black/50 md:bg-black flex flex-col items-center justify-center text-center px-6 md:px-12 lg:px-20 z-10 py-12">
                <p class="font-label-md text-label-md uppercase tracking-[0.3em] mb-4 text-white/90">THE ESSENTIALS</p>
                <h1 class="font-display-lg text-[36px] md:text-headline-lg lg:text-[56px] uppercase leading-tight mb-6 text-white">
                    BOLD &<br class="hidden md:block"/>UNAPOLOGETIC
                </h1>
                <div class="h-[1px] w-16 bg-white/70 mb-6"></div>
                <p class="font-body-lg text-sm md:text-body-lg text-white/80 max-w-md mb-10">
                    Make a statement that cannot be ignored. Premium designs for those who demand attention.
                </p>
                <a href="shop.html" class="inline-block bg-white text-black font-label-md text-label-md uppercase tracking-widest px-10 py-4 hover:bg-gray-200 transition-colors duration-300 active:scale-95 shadow-lg">
                    SHOP COLLECTION
                </a>
            </div>
            <!-- Image Column -->
            <div class="absolute inset-0 md:relative md:w-1/2 h-full z-0">
                <div class="w-full h-full bg-cover bg-center md:bg-[center_top_10%]" style="background-image: url('https://cdn.shopify.com/s/files/1/0918/2619/2702/files/061177E0-7892-489F-B4CB-3086367434F3.jpg?v=1781677325')"></div>
            </div>
        </div>
'''

# Find the slides container and replace the contents
# Container starts with <div class="absolute inset-0 w-full h-full flex transition-transform duration-700 ease-out" id="hero-slides" style="transform: translateX(0%);">
pattern = r'(<div class="absolute inset-0 w-full h-full flex transition-transform duration-700 ease-out" id="hero-slides"[^>]*>).*?(</div>\s*<!-- Navigation Arrows -->)'
new_content = re.sub(pattern, r'\1' + new_slides_html + r'\n    \2', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully redesigned index.html hero slides for responsive desktop display")
