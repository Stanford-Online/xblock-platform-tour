function PlatformTourXBlock(runtime, element) {
    $('button.navmaker', element).click(function(){
        var stepsJson = JSON.parse($('.platformtour-steps', element).text());
        var intro = introJs();
        intro.setOptions({'steps': stepsJson});
        intro.start();
    });
}
