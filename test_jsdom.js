const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('product.html', 'utf-8');
const cartJs = fs.readFileSync('js/cart.js', 'utf-8');

const dom = new JSDOM(html, {
    url: "http://localhost:8000/product.html?id=prod_36",
    runScripts: "dangerously",
    resources: "usable"
});

// Mock localStorage
dom.window.localStorage = {
    getItem: () => null,
    setItem: () => {}
};

// Manually run cart.js and then the inline script
const script1 = dom.window.document.createElement("script");
script1.textContent = cartJs;
dom.window.document.body.appendChild(script1);

dom.window.addEventListener('load', () => {
    // Manually trigger DOMContentLoaded
    const event = dom.window.document.createEvent('Event');
    event.initEvent('DOMContentLoaded', true, true);
    dom.window.document.dispatchEvent(event);
    
    setTimeout(() => {
        console.log("Product Name:", dom.window.document.getElementById('product-name').textContent);
        console.log("Image SRC:", dom.window.document.getElementById('product-image').src);
        console.log("Price:", dom.window.document.getElementById('product-price').textContent);
    }, 100);
});
