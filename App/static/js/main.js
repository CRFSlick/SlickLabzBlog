
var greetings = ['Hello!', 'What\'s up!', 'Welcome!'];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function autoType(e, word) {
    var buffer = e.html();
    for(var i = 0; i < word.length; i++) {
        await sleep(125);
        console.log(word.charAt(i));
        buffer += word.charAt(i);
        e.html(buffer);
    }

    // Blink cursor after done typing
    cursorBlink($("#cursor"));
}

async function cursorBlink(e) {
    while (true){
        console.log("test")
        await sleep(750);
        e.fadeOut(100);
        await sleep(750);
        e.fadeIn(100);
    }
}

$(document).ready(async function () {
    await sleep(250);
    setTimeout(function() {autoType($("#js-auto-type"), greetings[Math.floor(Math.random() * greetings.length)])}, 0);
});