
var greetings = ['Hello!', 'What\'s up!', 'Welcome!'];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function autoType(e, word) {
    var buffer = e.html();
    for(var i = 0; i < word.length; i++) {
        await sleep(125);
        buffer += word.charAt(i);
        e.html(buffer);
    }

    // Blink cursor after done typing
    cursorBlink($("#cursor"));
}

async function cursorBlink(e) {
    while (true){
        await sleep(750);
        e.fadeOut(100);
        await sleep(750);
        e.fadeIn(100);
    }
}

$(document).ready(async function () {
    // await sleep(250);
    // setTimeout(function() {autoType($("#js-auto-type"), greetings[Math.floor(Math.random() * greetings.length)])}, 0);

    posts_shown = false;
    $("#show_more_posts").click(function(){
        if (posts_shown) {
            $("#show_more_posts").html(" Show All Posts");
            $(".post_extra").fadeOut();
            posts_shown = false;
        } else {
            $("#show_more_posts").html(" Show Only Recent");
            $(".post_extra").fadeIn();
            posts_shown = true;
        }
    });

    $("#back_to_top").click(function(){
        $("html, body").animate({scrollTop: 0}, 200);
    })
});
