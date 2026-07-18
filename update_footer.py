import os
import re

files = ['index.html', 'shop.html', 'about.html', 'contact.html']

premium_footer = '''<!-- Footer -->
<footer class="bg-[#0a0a0a] text-white border-t border-white/10">
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-stack-lg px-5 md:px-margin-x py-section-gap max-w-container-max mx-auto">
<div>
<a class="font-headline-lg text-[28px] tracking-[0.2em] text-white uppercase block mb-6" href="index.html">LUXORA</a>
<p class="font-body-md text-gray-400 max-w-xs mb-8 leading-relaxed">
    Redefining intimacy through the lens of luxury, minimalism and timeless elegance.
</p>
<div class="flex gap-5">
<button class="material-symbols-outlined text-gray-400 hover:text-white transition-colors duration-300">public</button>
<button class="material-symbols-outlined text-gray-400 hover:text-white transition-colors duration-300">share</button>
<button class="material-symbols-outlined text-gray-400 hover:text-white transition-colors duration-300">alternate_email</button>
</div>
</div>
<div>
<h5 class="font-label-md text-[13px] tracking-[0.15em] text-gray-300 uppercase mb-8">Shop</h5>
<ul class="flex flex-col gap-4 font-body-md text-gray-400">
<li><a class="hover:text-white transition-colors duration-300" href="shop.html">Roleplay & Cosplay</a></li>
<li><a class="hover:text-white transition-colors duration-300" href="shop.html">Babydolls</a></li>
<li><a class="hover:text-white transition-colors duration-300" href="shop.html">Gift for Her</a></li>
<li><a class="hover:text-white transition-colors duration-300" href="shop.html">Latex Edition</a></li>
</ul>
</div>
<div>
<h5 class="font-label-md text-[13px] tracking-[0.15em] text-gray-300 uppercase mb-8">About</h5>
<ul class="flex flex-col gap-4 font-body-md text-gray-400">
<li><a class="hover:text-white transition-colors duration-300" href="about.html">Our Story</a></li>
<li><a class="hover:text-white transition-colors duration-300" href="about.html">Sustainability</a></li>
<li><a class="hover:text-white transition-colors duration-300" href="contact.html">Store Locator</a></li>
<li><a class="hover:text-white transition-colors duration-300" href="contact.html">Contact Us</a></li>
</ul>
</div>
<div>
<h5 class="font-label-md text-[13px] tracking-[0.15em] text-gray-300 uppercase mb-8">Newsletter</h5>
<p class="font-body-md text-gray-400 mb-6">Subscribe to receive updates and exclusive offers.</p>
<div class="flex border-b border-white/20 pb-2 group">
<input class="bg-transparent border-none outline-none focus:ring-0 w-full placeholder:text-gray-600 text-white" placeholder="Email Address" type="email"/>
<button class="material-symbols-outlined text-gray-400 group-hover:text-white transition-colors duration-300">arrow_forward</button>
</div>
</div>
</div>
<div class="px-5 md:px-margin-x py-8 border-t border-white/10 max-w-container-max mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
<p class="font-label-md text-[10px] tracking-[0.2em] text-gray-500 uppercase">© 2024-2026 LUXORA FASHION. ALL RIGHTS RESERVED.</p>
<div class="flex gap-8">
<a class="font-label-md text-[10px] tracking-[0.2em] text-gray-500 hover:text-white transition-colors duration-300 uppercase" href="#">PRIVACY POLICY</a>
<a class="font-label-md text-[10px] tracking-[0.2em] text-gray-500 hover:text-white transition-colors duration-300 uppercase" href="#">TERMS OF SERVICE</a>
</div>
</div>
</footer>'''

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the footer block
        pattern = re.compile(r'<!-- Footer -->.*?</footer>', re.DOTALL)
        if pattern.search(content):
            new_content = pattern.sub(premium_footer, content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated footer in {file}")
        else:
            print(f"Could not find Footer section in {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
