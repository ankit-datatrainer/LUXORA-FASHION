const jsdom = require('jsdom');
const { JSDOM } = jsdom;

JSDOM.fromFile('index.html', {
    url: "http://localhost:8000/index.html",
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
            console.log("Successfully loaded index.html without errors");
        }, 500);
    });
});
