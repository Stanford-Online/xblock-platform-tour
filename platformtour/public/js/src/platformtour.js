function PlatformTourXBlock(runtime, element) {
    $('button.navmaker', element).click(function(){
        var stepsJson = JSON.parse($('.platformtour-steps', element).text());
        stepsJson = stepsJson.filter(function (obj) {
            // skip step if the element cannot be found on the page
            return $(obj.element).length;
        });
        var intro = introJs();
        intro.setOptions({'steps': stepsJson});
        intro.start();
    });
}
