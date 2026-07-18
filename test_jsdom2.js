const jsdom = require('jsdom');
const { JSDOM } = jsdom;

JSDOM.fromFile('product.html', {
    url: "http://localhost:8000/product.html?id=prod_36",
    runScripts: "dangerously",
    resources: "usable"
}).then(dom => {
    dom.window.localStorage = {
        getItem: () => null,
        setItem: () => {}
    };
    
    dom.window.addEventListener('load', () => {
        setTimeout(() => {
            console.log("Product Name:", dom.window.document.getElementById('product-name').textContent);
            console.log("Image SRC:", dom.window.document.getElementById('product-image').src);
            console.log("Price:", dom.window.document.getElementById('product-price').textContent);
        }, 500);
    });
});
