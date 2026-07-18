import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section = '''<!-- Popular Collection Bento -->
<section class="px-5 md:px-margin-x py-section-gap">
<h2 class="font-headline-lg text-headline-lg uppercase tracking-widest text-center mb-stack-lg">POPULAR COLLECTION</h2>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 lg:grid-rows-2 gap-4 h-auto lg:h-[800px]">
<div class="md:col-span-1 md:row-span-2 relative group cursor-pointer overflow-hidden">
<div class="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-110" data-alt="Bridal theme lingerie" style="background-image: url('images/cat_bridal.png')"></div>
<div class="absolute inset-0 bg-black/30 group-hover:bg-black/40 transition-colors"></div>
<div class="absolute bottom-10 left-10 text-white">
<p class="font-headline-lg text-[24px] uppercase tracking-widest mb-2">BRIDAL LACE</p>
<span class="font-label-md border-b border-white pb-1 uppercase tracking-widest">Shop Now</span>
</div>
</div>
<div class="md:col-span-2 md:row-span-1 relative group cursor-pointer overflow-hidden">
<div class="absolute inset-0 bg-cover bg-[center_top_10%] transition-transform duration-700 group-hover:scale-110" data-alt="Babydolls collection" style="background-image: url('images/cat_babydolls.png')"></div>
<div class="absolute inset-0 bg-black/30 group-hover:bg-black/40 transition-colors"></div>
<div class="absolute bottom-10 left-10 text-white">
<p class="font-headline-lg text-[24px] uppercase tracking-widest mb-2">BABYDOLLS</p>
<span class="font-label-md border-b border-white pb-1 uppercase tracking-widest">Shop Now</span>
</div>
</div>
<div class="md:col-span-1 md:row-span-1 relative group cursor-pointer overflow-hidden">
<div class="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-110" data-alt="Roleplay costumes" style="background-image: url('images/cat_roleplay.png')"></div>
<div class="absolute inset-0 bg-black/30 group-hover:bg-black/40 transition-colors"></div>
<div class="absolute bottom-10 left-10 text-white">
<p class="font-headline-lg text-[20px] uppercase tracking-widest mb-2">ROLEPLAY</p>
<span class="font-label-md border-b border-white pb-1 uppercase tracking-widest">Shop Now</span>
</div>
</div>
<div class="sm:col-span-2 lg:col-span-3 md:row-span-1 relative group cursor-pointer overflow-hidden">
<div class="absolute inset-0 bg-cover bg-[center_top_30%] transition-transform duration-700 group-hover:scale-110" data-alt="Latex Edition" style="background-image: url('images/cat_latex.png')"></div>
<div class="absolute inset-0 bg-black/30 group-hover:bg-black/40 transition-colors"></div>
<div class="absolute bottom-10 left-10 text-white">
<p class="font-headline-lg text-[24px] uppercase tracking-widest mb-2">LATEX EDITION</p>
<span class="font-label-md border-b border-white pb-1 uppercase tracking-widest">Shop Now</span>
</div>
</div>
</div>
</section>'''

# Replace the bento grid section
# It starts at <!-- Popular Collection Bento --> and ends at </section> (which is before </main>)
pattern = re.compile(r'<!-- Popular Collection Bento -->.*?</section>', re.DOTALL)
if pattern.search(content):
    new_content = pattern.sub(new_section, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced the Popular Collection section.")
else:
    print("Could not find Popular Collection section.")
