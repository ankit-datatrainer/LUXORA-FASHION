import re

with open('shop.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the sticky top-[110px] with a transition and class top-0, plus add the ID
# Old line:
# <div class="px-5 md:px-12 lg:px-20 py-5 border-b border-outline-variant flex justify-between items-center bg-surface-bright sticky top-[110px] z-40">
old_line = '<div class="px-5 md:px-12 lg:px-20 py-5 border-b border-outline-variant flex justify-between items-center bg-surface-bright sticky top-[110px] z-40">'
new_line = '<div id="filter-bar-container" class="px-5 md:px-12 lg:px-20 py-5 border-b border-outline-variant flex justify-between items-center bg-surface-bright sticky top-0 transition-all duration-100 z-40">'

content = content.replace(old_line, new_line)

# Add the JS snippet at the bottom to dynamically align the filter bar below the sticky header
js_align_script = '''
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const header = document.querySelector('.sticky.top-0');
            const filterBar = document.getElementById('filter-bar-container');
            
            if (header && filterBar) {
                const updatePosition = () => {
                    filterBar.style.top = `${header.offsetHeight}px`;
                };
                
                // Update position on window resize and scroll
                window.addEventListener('resize', updatePosition);
                updatePosition();
                
                // Add a small observer to watch for header height changes (e.g. mobile menu toggle)
                if (window.ResizeObserver) {
                    const observer = new ResizeObserver(updatePosition);
                    observer.observe(header);
                }
            }
        });
    </script>
</body>'''

# Insert right before </body>
content = content.replace('</body>', js_align_script)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added dynamic sticky positioning to filter-bar-container in shop.html")
