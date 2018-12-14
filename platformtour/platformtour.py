"""
This is the core logic for the Platform Tour xblock, which introduces students to
a course through a digital tour.
"""
import json
import os

from django.template.context import Context
from xblock.core import XBlock
from xblock.fields import List
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader

from . import default_steps


class PlatformTourXBlock(XBlock):
    """
    Allows students to tour through the course and get familiar with the
    platform.
    """

    loader = ResourceLoader(__name__)

    display_name = String(
        display_name=('Display Name'),
        help=(
            'The title for this component'
        ),
        default='Platform Tour',
        scope=Scope.settings,
    )
    button_label = String(
        display_name=('Button label'),
        help=(
            'The text that will appear on the button on which learners click'
            ' to start the Platform Tour.'
        ),
        default='Begin Platform Tour',
        scope=Scope.settings,
    )
    intro = String(
        display_name=('Introduction text'),
        help=(
            'The introduction that will precede the button'
            ' and explain its presence to the user'
        ),
        default='Click the button below to learn how to navigate the platform.',
        scope=Scope.settings,
    )
    enabled_default_steps = List(
        display_name=('Choose the steps for the Platform Tour'),
        help=(
            'List representing steps of the tour'
        ),
        default=[],
        multiline_editor=True,
        scope=Scope.settings,
        resettable_editor=False,
    )
    custom_steps = List(
        display_name=('Custom steps for the platform tour'),
        help=(
            'JSON dictionaries representing additional steps of the tour'
        ),
        default=[],
        multiline_editor=True,
        scope=Scope.settings,
    )

    def get_resource_url(self, path):
        """
        Retrieve a public URL for the file path
        """
        path = os.path.join('public', path)
        resource_url = self.runtime.local_resource_url(self, path)
        return resource_url

    def build_fragment(
            self,
            rendered_template,
            initialize_js_func,
            additional_css=None,
            additional_js=None,
    ):
        """
        Build the HTML fragment, and add required static assets to it.
        """
        additional_css = additional_css or []
        additional_js = additional_js or []
        fragment = Fragment(rendered_template)
        for item in additional_css:
            url = self.get_resource_url(item)
            fragment.add_css_url(url)
        for item in additional_js:
            url = self.get_resource_url(item)
            fragment.add_javascript_url(url)
        fragment.initialize_js(initialize_js_func)
        return fragment

    def student_view(self, context=None):
        """
        The primary view of the PlatformTourXBlock, shown to students
        when viewing courses.
        """
        step_choice_dict = default_steps.get_display_steps(self.enabled_default_steps)
        if 'custom' in self.enabled_default_steps:
            step_choice_dict.extend(self.custom_steps)
        steps = json.dumps(step_choice_dict)

        context = context or {}
        context.update(
            {
                'display_name': self.display_name,
                'button_label': self.button_label,
                'intro': self.intro,
                'steps': steps,
            }
        )
        rendered_template = self.loader.render_django_template(
            'templates/platformtour.html',
            context=Context(context),
        )
        fragment = self.build_fragment(
            rendered_template,
            initialize_js_func='PlatformTourXBlock',
            additional_css=[
                'css/platformtour.css',
            ],
            additional_js=[
                'js/src/intro.js',
                'js/src/platformtour.js',
            ],
        )
        return fragment

    def studio_view(self, context=None):
        """
        Build the fragment for the edit/studio view
        Implementation is optional.
        """
        step_choice_keys = self.enabled_default_steps or default_steps.get_default_keys()
        context = context or {}
        context.update(
            {
                'display_name': self.display_name,
                'button_label': self.button_label,
                'intro': self.intro,
                'enabled_default_steps': default_steps.get_choices(step_choice_keys),
                'custom_steps': json.dumps(self.custom_steps),
            }
        )
        rendered_template = self.loader.render_django_template(
            'templates/platformtour_studio.html',
            context=Context(context),
        )
        fragment = self.build_fragment(
            rendered_template,
            initialize_js_func='PlatformTourStudioUI',
            additional_css=[
                'css/platformtour_studio.css',
            ],
            additional_js=[
                'js/src/platformtour_studio.js',
            ],
        )
        return fragment

    @XBlock.json_handler
    def studio_view_save(self, data, suffix=''):
        """
        Save XBlock fields
        Returns: the new field values
        """

        self.display_name = data['display_name']
        self.button_label = data['button_label']
        self.intro = data['intro']
        self.enabled_default_steps = data['enabled_default_steps']
        self.custom_steps = data['custom_steps']

        return {
            'display_name': self.display_name,
            'button_label': self.button_label,
            'intro': self.intro,
            'enabled_default_steps': self.enabled_default_steps,
            'custom_steps': self.custom_steps,
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """
        A canned scenario for display in the workbench.
        """
        return [
            ("PlatformTourXBlock",
             """<platformtour/>
             """),
            ("Multiple PlatformTourXBlock",
             """<vertical_demo>
                    <platformtour
                        display_name="Platform Tour 1"
                        button_label="Start Tour #1"
                        intro="This is the Platform Tour #1, click the button to start."
                    />
                    <platformtour
                        display_name="Platform Tour 2"
                        button_label="Start Tour #2"
                        intro="This is the Platform Tour #2, click the button to start."
                    />
                    <platformtour
                        display_name="Platform Tour 3"
                        button_label="Start Tour #3"
                        intro="This is the Platform Tour #3, click the button to start."
                    />
                </vertical_demo>
             """),
        ]
