function PlatformTourStudioUI(runtime, element) {
    'use strict';

    var $ = window.$;
    var $element = $(element);
    var buttonSave = $element.find('.save-button');
    var buttonCancel = $element.find('.cancel-button');
    var url = runtime.handlerUrl(element, 'studio_view_save');

    var customSteps = $element.find('.custom-steps');
    var stepChoices = $element.find('.steps');

    var checkboxIconCheckedClass = 'fa-check-square-o ';
    var checkboxIconUncheckedClass = 'fa-square-o ';

    $('.step input', stepChoices).click(function() {
        var stepSelected = $(this).attr('name');
        $(this).siblings('i').toggleClass(checkboxIconCheckedClass + checkboxIconUncheckedClass);
        if (stepSelected === 'custom') {
            customSteps.toggleClass('enabled');
        }
    });

    buttonCancel.on('click', function () {
        runtime.notify('cancel', {});
        return false;
    });

    buttonSave.on('click', function () {
        var stepChoicesJson = [];
        $('.step', stepChoices).each(function( index ) {
            var stepChoiceKey = $(this).data('key');
            var isStepEnabled = $('input', this).prop('checked');
            if (isStepEnabled) {
                stepChoicesJson.push(stepChoiceKey);
            }
        });
        runtime.notify('save', {
            message: 'Saving...',
            state: 'start',
        });
        $.ajax(url, {
            type: 'POST',
            data: JSON.stringify({
                'display_name': $('.display-name', element).val(),
                'button_label': $('.button-label', element).val(),
                'intro': $('.intro', element).val(),
                'enabled_default_steps': stepChoicesJson,
                'custom_steps': JSON.parse(customSteps.val()),
            }),
            success: function buttonSaveOnSuccess() {
                runtime.notify('save', {
                    state: 'end',
                });
            },
            error: function buttonSaveOnError() {
                runtime.notify('error', {});
            }
        });
        return false;
    });
}
