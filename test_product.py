import sys
import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Listen for console messages
        page.on("console", lambda msg: print(f"CONSOLE {msg.type}: {msg.text}"))
        # Listen for unhandled exceptions
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        
        print("Navigating to product.html?id=prod_36")
        page.goto("http://localhost:8000/product.html?id=prod_36")
        time.sleep(2)
        
        print("Page title:", page.title())
        browser.close()

if __name__ == "__main__":
    main()
