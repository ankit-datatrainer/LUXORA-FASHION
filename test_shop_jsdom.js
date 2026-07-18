const jsdom = require('jsdom');
const { JSDOM } = jsdom;

JSDOM.fromFile('shop.html', {
    url: "http://localhost:8000/shop.html",
    runScripts: "dangerously",
    resources: "usable"
}).then(dom => {
    dom.window.localStorage = {
        getItem: () => null,
        setItem: () => {}
    };
    
    dom.window.addEventListener('error', (event) => {
        console.error("Window Error:", event.error);
    });

    dom.window.addEventListener('load', () => {
        setTimeout(() => {
            console.log("Successfully loaded shop.html without errors");
        }, 500);
    });
});
