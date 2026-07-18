import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section_html = '''
<!-- Best Sellers Section -->
<section class="py-section-gap bg-black text-white">
<div class="px-5 md:px-margin-x">
    
    <div class="flex justify-center items-center mb-12">
        <h2 class="font-headline-lg text-[24px] md:text-[32px] tracking-wide">
            You are in <span class="border-b-2 border-white/70 pb-1 cursor-pointer flex items-center gap-1 inline-flex">Best sellers <span class="material-symbols-outlined text-[24px]">expand_more</span></span>
        </h2>
    </div>

    <!-- Product Grid (6 columns) -->
    <div class="flex gap-4 md:gap-6 overflow-x-auto hide-scroll snap-x pb-8">
        
        <!-- Product 1 -->
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
            <div class="relative aspect-[3/4] mb-4 overflow-hidden bg-zinc-900">
                <img src="images/cat_babydolls.png" alt="Sugarbaby" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            </div>
            <div>
                <h3 class="font-body-md text-[13px] md:text-sm font-bold tracking-wide mb-1">Sugarbaby 🍓 🎀</h3>
                <p class="font-body-md text-[13px] text-gray-300">Rs. 899.00</p>
            </div>
        </div>

        <!-- Product 2 -->
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
            <div class="relative aspect-[3/4] mb-4 overflow-hidden bg-zinc-900">
                <img src="images/cat_roleplay.png" alt="Latex Bunny Roleplay Set" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            </div>
            <div>
                <h3 class="font-body-md text-[13px] md:text-sm font-bold tracking-wide mb-1">Latex Bunny Roleplay Set 🐰</h3>
                <p class="font-body-md text-[13px] text-gray-300">Rs. 1,199.00</p>
            </div>
        </div>

        <!-- Product 3 -->
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
            <div class="relative aspect-[3/4] mb-4 overflow-hidden bg-zinc-900">
                <img src="images/cat_bridal.png" alt="Bridal theme Lace Set" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            </div>
            <div>
                <h3 class="font-body-md text-[13px] md:text-sm font-bold tracking-wide mb-1">Bridal theme Lace Set 🤍</h3>
                <p class="font-body-md text-[13px] text-gray-300">Rs. 999.00</p>
                <div class="flex gap-2 mt-2">
                    <div class="w-4 h-4 rounded-full bg-white border border-gray-400"></div>
                    <div class="w-4 h-4 rounded-full bg-red-500 border border-transparent"></div>
                </div>
            </div>
        </div>

        <!-- Product 4 -->
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
            <div class="relative aspect-[3/4] mb-4 overflow-hidden bg-zinc-900">
                <img src="images/cat_latex.png" alt="Dominatrix Harness Dress" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            </div>
            <div>
                <h3 class="font-body-md text-[13px] md:text-sm font-bold tracking-wide mb-1">Dominatrix Harness Dress<br>(Stocking incl)</h3>
                <p class="font-body-md text-[13px] text-gray-300 mt-1">Rs. 999.00</p>
                <div class="flex gap-2 mt-2">
                    <div class="w-4 h-4 rounded-full bg-black border border-gray-700"></div>
                </div>
            </div>
        </div>

        <!-- Product 5 -->
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
            <div class="relative aspect-[3/4] mb-4 overflow-hidden bg-zinc-900">
                <img src="images/cat_lingerie_sets.png" alt="Desert Fantasy Set" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            </div>
            <div>
                <h3 class="font-body-md text-[13px] md:text-sm font-bold tracking-wide mb-1">Desert Fantasy Set</h3>
                <p class="font-body-md text-[13px] text-gray-300">Rs. 999.00</p>
                <div class="flex gap-2 mt-2">
                    <div class="w-4 h-4 rounded-full bg-red-500 border border-transparent"></div>
                    <div class="w-4 h-4 rounded-full bg-pink-300 border border-transparent"></div>
                </div>
            </div>
        </div>

        <!-- Product 6 -->
        <div class="min-w-[200px] md:min-w-[calc(16.666%-20px)] snap-start group cursor-pointer">
            <div class="relative aspect-[3/4] mb-4 overflow-hidden bg-zinc-900">
                <img src="images/cat_bodysuits.png" alt="Pikachu Cosplay Bodysuit" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            </div>
            <div>
                <h3 class="font-body-md text-[13px] md:text-sm font-bold tracking-wide mb-1 flex items-center gap-1"><span class="text-yellow-400">⚡</span> Pikachu Cosplay Bodysuit</h3>
                <p class="font-body-md text-[13px] text-gray-300">Rs. 749.00</p>
            </div>
        </div>

    </div>
</div>
</section>
'''

# Find the "New Arrivals Carousel" section and replace it
# The section starts with <!-- New Arrivals Carousel --> and ends before <!-- Footer ... -->
# Using regex to replace it
pattern = re.compile(r'<!-- New Arrivals Carousel -->.*?</section>', re.DOTALL)
if pattern.search(content):
    new_content = pattern.sub(new_section_html.strip(), content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced the New Arrivals section with Best Sellers.")
else:
    print("Could not find New Arrivals section.")
