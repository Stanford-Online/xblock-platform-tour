"""
This is the default steps for Platform Tour xblock, which introduces students to
a course through a digital tour.

'key' and 'title' are only used by edX Studio
'element', 'intro', and 'position' are used by intro.js in LMS tours

The functions are used to pull the required keys out of the list.
"""
DEFAULT_STEPS = [
    {
        'key': 'intro',
        'title': 'Welcome / Intro',
        'element': 'button.navmaker',
        'intro': (
            'Welcome to the platform walkthrough tour! '
            'Let\'s start by exploring the tabs at the top of the page.'
        ),
        'position': 'right',
    },
    {
        'key': 'course_tab',
        'title': 'Course Tab',
        'element': '.course-tabs a[href*="/courseware"]',
        'intro': 'You are in the Course tab, where all the materials are found.',
        'position': 'right',
    },
    {
        'key': 'course_content',
        'title': 'Course Content',
        'element': 'div#seq_content',
        'intro': 'You are looking at content in a page, or unit.',
        'position': 'top',
    },
    {
        'key': 'unit_breadcrumb',
        'title': 'Unit Breadcrumb',
        'element': '.nav-item.nav-item-sequence',
        'intro': (
            'Notice the trail of breadcrumb links above the content. '
            'You are currently on a page, or unit...'
        ),
        'position': 'below',
    },
    {
        'key': 'subsection_breadcrumb',
        'title': 'Subsection Breadcrumb',
        'element': '.nav-item.nav-item-section',
        'intro': '...in a lesson, or subsection...',
        'position': 'below',
    },
    {
        'key': 'section_breadcrumb',
        'title': 'Section Breadcrumb',
        'element': '.nav-item.nav-item-chapter',
        'intro': (
            '...in a module, or section. Clicking on a breadcrumb will take you to your '
            'course\'s table of contents, and drop you onto the portion related to the '
            'section or subsection you clicked on.'
        ),
        'position': 'right',
    },
    {
        'key': 'course_breadcrumb',
        'title': 'Course Breadcrumb',
        'element': '.nav-item.nav-item-course',
        'intro': (
            'This \'Course\' link will also take you to the table of contents, '
            'but to the beginning, as opposed to a specific section or subsection.'
        ),
        'position': 'right',
    },
    {
        'key': 'filmstrip',
        'title': 'Film Strip Navigator',
        'element': '#sequence-list',
        'intro': (
            'Every lesson or subsection is structured as a sequence of pages, or units. '
            'Each button on this navigator corresponds to a page of content. '
            'You should go through the pages from left to right.'
        ),
        'position': 'left',
    },
    {
        'key': 'filmstrip_first_tab',
        'title': 'First Page Tab',
        'element': '#tab_0',
        'intro': 'You are currently viewing the first page of content.',
        'position': 'left',
    },
    {
        'key': 'filmstrip_second_tab',
        'title': 'Second Page Tab',
        'element': '#tab_1',
        'intro': 'Move to the next page of content by clicking the icon in the highlighted tab...',
        'position': 'left',
    },
    {
        'key': 'filmstrip_next_arrow',
        'title': 'Next Arrow',
        'element': '.sequence-nav .sequence-nav-button.button-next',
        'intro': '...or the arrow to the right.',
        'position': 'left',
    },
    {
        'key': 'bookmarking',
        'title': 'Bookmarking',
        'element': '.bookmark-button-wrapper',
        'intro': (
            'If you want to get back later to the content on a particular page, '
            'or you want to save it as something important, bookmark it. '
            'A Bookmarks folder on your course home page will contain a link to '
            'any page you bookmark for easy access later.'
        ),
        'position': 'right',
    },
    {
        'key': 'course_progress',
        'title': 'Course Progress',
        'element': '.course-tabs a[href*="/progress"]',
        'intro': 'Visit the Progress page to check your scores on graded content in the course.',
        'position': 'left',
    },
    {
        'key': 'discussion_forum',
        'title': 'Discussion Forum',
        'element': '.course-tabs a[href*="/discussion"]',
        'intro': (
            'For course-specific questions, click on the \'Discussion\' tab to post your '
            'question to the forum. Peers and course teams may be able to answer your '
            'question there.'
        ),
        'position': 'left',
    },
    {
        'key': 'help_link',
        'title': 'Help Link',
        'element': 'a.doc-link',
        'intro': (
            'For any technical issues or platform-specific questions, '
            'click on the \'Help\' link to access the Help Center or contact support.'
        ),
        'position': 'bottom',
    },
    {
        'key': 'tour_done',
        'title': 'End of Platform Tour',
        'element': 'div.course-wrapper',
        'intro': 'That concludes the platform tour. \n\n Click Done to close this walkthrough.',
        'position': 'top',
    },
]

def get_choices(keys):
    """
    Build list of choices and whether the user has them enabled.
    """
    choices_list = []
    for step in DEFAULT_STEPS:
        key = step.get('key')
        title = step.get('title')
        if key and title:
            _append_choice(key, title, keys, choices_list)
    _append_choice('custom', 'Custom (Advanced Users)', keys, choices_list)
    return choices_list

def _append_choice(key, title, keys, choices_list):
    is_choice_enabled = key in keys
    choice = {
        'key': key,
        'title': title,
        'enabled': is_choice_enabled
    }
    choices_list.append(choice)

def get_default_keys():
    """
    Get all the keys in DEFAULT_STEPS.
    """
    keys = [
        step.get('key')
        for step in DEFAULT_STEPS
    ]
    return keys

def get_display_steps(keys):
    """
    Collect all the enabled steps for display.
    """
    steps = [
        step
        for step in DEFAULT_STEPS
        if step.get('key') in keys
    ]
    return steps
