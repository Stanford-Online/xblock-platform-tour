"""
This is the core logic for the Platform Tour xblock, which introduces students to
a course through a digital tour.
"""
import json
import pkg_resources
from django.template import Context
from django.template.loader import get_template
from xblock.core import XBlock
from xblock.fields import Dict, Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

def _resource_string(path):
    """Handy helper for getting resources from our kit."""
    data = pkg_resources.resource_string(__name__, path)
    return data.decode("utf8")

class PlatformTourXBlock(XBlock, StudioEditableXBlockMixin):
    """
    Allows students to tour through the course and get familiar with the
    platform.
    """

    display_name = String(
        display_name=('Display Name'),
        help=(
            'This is the title for this component'
        ),
        default='Platform Tour',
        scope=Scope.settings,
    )

    button_label = String(
        display_name=('Button label'),
        help=('This is the text that will appear on the button'),
        default='Begin Platform Tour',
        scope=Scope.settings,
    )

    intro = String(
        display_name=('Introduction text'),
        help=('This is the introduction that will precede the button'
            ' and explain its presence to the user'),
        default='Click the button below to learn how to navigate the platform!',
        scope=Scope.settings,
    )

    steps = Dict(
        display_name=('Steps in the Platform Tour'),
        help=('Data representing the steps that the tour takes through platform courseware'),
        default={
            "steps": [{
                "name": "#navmaker",
                "dataIntro": "Welcome to the Platform Tour! Let's start by exploring the tabs at the top of the page.",
                "dataPosition": "right",
            },
            {
                "name": ".course-tabs",
                "find": "a:contains('Course')",
                "dataIntro": "You are in the Course tab, where all the materials are found.",
                "dataPosition": "right",
            },
            {
                "name": "div#seq_content",
                "dataIntro": "You are looking at content in a page, or unit.",
                "dataPosition": "top",
            },
            {
                "name": ".nav-item.nav-item-sequence",
                "dataIntro": "Notice the trail of breadcrumb links above the content. You are currently on a page, or unit...",
                "dataPosition": "below",
            },
            {
                "name": ".nav-item.nav-item-section",
                "dataIntro": "...in a lesson, or subsection...",
                "dataPosition": "below",
            },
            {
                "name": ".nav-item.nav-item-chapter",
                "dataIntro": "...in a module, or section. Clicking on a breadcrumb will take you to your course's table of contents, and drop you onto the portion related to the section or subsection you clicked on.",
                "dataPosition": "right",
            },
            {
                "name": ".nav-item.nav-item-course",
                "dataIntro": "This 'Course' link will also take you to the table of contents, but to the beginning, as     opposed to a specific section or subsection.",
                "dataPosition": "right",
            },
            {
                "name": "#sequence-list",
                "dataIntro": "Every lesson or subsection is structured as a sequence of pages, or units. Each button on this navigator corresponds to a page of content. You should go through the pages from left to right.",
                "dataPosition": "left",
            },
            {
                "name": "#tab_0",
                "dataIntro": "You are currently viewing the first page of content.",
                "dataPosition": "left",
            },
            {
                "name": "#tab_1",
                "dataIntro": "Move to the next page of content by clicking the icon in the highlighted tab...",
                "dataPosition": "left",
            },
            {
                "name": ".sequence-nav",
                "find": ".sequence-nav-button.button-next",
                "dataIntro": "...or the arrow to the right.",
                "dataPosition": "left",
            },
            {
                "name": ".bookmark-button-wrapper",
                "dataIntro": "If you want to get back later to the content on a particular page, or you want to save it as something important, bookmark it. A Bookmarks folder on your course home page will contain a link to any page you bookmark for easy access later.",
                "dataPosition": "right",
            },
            {
                "name": ".course-tabs",
                "find": "a:contains('Progress')",
                "dataIntro": "Visit the Progress page to check your scores on graded content in the course.",
                "dataPosition": "left",
            },
            {
                "name": ".course-tabs",
                "find": "a:contains('Discussion')",
                "dataIntro": "For course-specific questions, click on the \"Discussion\" tab to post your question to the forum. Peers and course teams may be able to answer your question there.",
                "dataPosition": "left",
            },
            {
                "name": "a.doc-link",
                "dataIntro": "For any technical issues or platform-specific questions, click on the \"Help\" link to access the Help Center or contact support.",
                "dataPosition": "bottom",
            },
            {
                "name": "div.course-wrapper",
                "dataIntro": "That concludes the platform tour. \n\n Click Done to close this tour.",
                "dataPosition": "top",
            },
        ],},
        multiline_editor=True,
        scope=Scope.settings,
    )

    editable_fields = (
        'display_name',
        'button_label',
        'intro',
        'steps',
    )

    def build_fragment(
        self,
        template,
        contect_dict,
    ):
        context = Context(contect_dict)
        fragment = Fragment(template.render(context))
        return fragment

    def student_view(self, context=None):
        """
        The primary view of the PlatformTourXBlock, shown to students
        when viewing courses.
        """
        context = context or {}
        context.update(
            {
                'display_name': self.display_name,
                'button_label': self.button_label,
                'intro': self.intro,
                'steps': json.dumps(self.steps['steps']),
            }
        )
        template = get_template('platformtour.html')
        fragment = self.build_fragment(
            template,
            context
        )
        fragment.add_css(
            _resource_string(
                'static/css/platformtour.css'
            ),
        )
        fragment.add_javascript(_resource_string('static/js/src/platformtour.js'))
        fragment.initialize_js('PlatformTourXBlock')
        return fragment

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PlatformTourXBlock",
             """<platformtour/>
             """),
            ("Multiple PlatformTourXBlock",
             """<vertical_demo>
                <platformtour/>
                <platformtour/>
                <platformtour/>
                </vertical_demo>
             """),
        ]
